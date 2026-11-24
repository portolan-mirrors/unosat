#!/usr/bin/env python3
"""Every relative link and asset href resolves to a file that exists.

This catches the most common hand-edit mistake: adding a child link before the
directory it points at exists. Dependency-free and offline, so it runs in
milliseconds on a clean checkout.

CI clones the metadata and not the bytes, because .gitignore keeps data out of
git. Set CI_LIGHT=1 there. It exempts hrefs with a data suffix, and nothing
else. The rule is the same for an asset href and a link href, for example
rel:pmtiles. Every structural link still resolves. Leave CI_LIGHT unset
locally, where the bytes are on disk, and the gate checks every href.

Before it walks the catalog, the gate runs two self-checks. Every data suffix
must be ignored by .gitignore, so CI_LIGHT never exempts a file that git
holds. A fixture catalog proves the exemption in both modes.

Run: python3 tests/test_links.py
"""
import json
import os
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

from publish import load_config  # noqa: E402

config = load_config()
BASE = ROOT / config["publish_dir"]

CI_LIGHT = os.environ.get("CI_LIGHT") == "1"
# The exemption reads the suffix and nothing else. A directory rule or a path
# prefix rule widens on its own as the catalog grows. This tuple does not.
DATA_SUFFIXES = (
    ".parquet", ".pmtiles", ".tif", ".tiff", ".copc.laz", ".laz", ".gpkg",
    ".zarr", ".geojsonl", ".shp", ".zip",
)


def is_remote(href: str) -> bool:
    return "://" in href or href.startswith(("#", "mailto:"))


def is_unpublished_data(href: str, ci_light: bool) -> bool:
    """True when href points at a file kept out of git on purpose."""
    return ci_light and href.lower().endswith(DATA_SUFFIXES)


def unignored_suffixes(gitignore: Path) -> list[str]:
    """The data suffixes that no `*<suffix>` line in .gitignore ignores.

    The match is literal. A pattern in another form, for example
    `**/*.parquet`, reports the suffix as not ignored. That error is loud and
    safe. The other error, an exemption for a file that git holds, is silent.
    """
    patterns = {
        line.strip() for line in gitignore.read_text().splitlines()
        if line.strip() and not line.lstrip().startswith(("#", "!"))
    }
    return [
        suffix for suffix in DATA_SUFFIXES
        if f"*{suffix}" not in patterns and f"*{suffix}/" not in patterns
    ]


def stac_documents(base: Path, report_root: Path, errors: list[str]):
    """Every STAC object under base."""
    out = []
    for path in sorted(base.rglob("*.json")):
        if any(part.startswith(".") for part in path.relative_to(base).parts):
            continue
        if path.name.endswith(".style.json") or "styles" in path.parts:
            continue
        try:
            doc = json.loads(path.read_text())
        except json.JSONDecodeError as exc:
            errors.append(
                f"{path.relative_to(report_root)}: invalid JSON ({exc})"
            )
            continue
        if isinstance(doc, dict) and doc.get("type") in {
            "Catalog", "Collection", "Feature"
        }:
            out.append(path)
    return out


def check_catalog(base: Path, report_root: Path, ci_light: bool):
    """Resolve every relative href under base.

    Returns (errors, checked, skipped, number of STAC objects).
    """
    errors: list[str] = []
    checked = 0
    skipped = 0
    documents = stac_documents(base, report_root, errors)

    for path in documents:
        doc = json.loads(path.read_text())
        rel_path = path.relative_to(report_root)
        hrefs = [
            (f"rel:{link.get('rel')}", link.get("href", ""))
            for link in doc.get("links", [])
        ] + [
            (f"asset {key}", asset.get("href", ""))
            for key, asset in (doc.get("assets") or {}).items()
        ]
        for label, href in hrefs:
            if not href or is_remote(href):
                continue
            if is_unpublished_data(href, ci_light):
                skipped += 1
                continue
            checked += 1
            if not (path.parent / href).resolve().exists():
                errors.append(f"{rel_path}: {label} -> {href} does not exist")

    return errors, checked, skipped, len(documents)


def write_json(path: Path, doc: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(doc))


def self_check() -> list[str]:
    """Prove the exemption on a fixture catalog, in both modes."""
    failures = []
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        base = root / "catalog"
        write_json(base / "catalog.json", {
            "type": "Catalog",
            "links": [
                {"rel": "child", "href": "./roads/collection.json"},
                {"rel": "child", "href": "./gone/collection.json"},
            ],
        })
        # The bytes of roads.pmtiles and roads.parquet are not on disk, as
        # in a CI checkout. README.md and the thumbnail belong in git, and
        # they are also absent.
        write_json(base / "roads/collection.json", {
            "type": "Collection",
            "links": [
                {"rel": "parent", "href": "../catalog.json"},
                {"rel": "pmtiles", "href": "./roads.pmtiles"},
                {"rel": "describedby", "href": "./README.md"},
            ],
            "assets": {
                "data": {"href": "./roads.parquet"},
                "thumbnail": {"href": "./roads.thumb.jpg"},
            },
        })
        in_git = {
            "catalog/catalog.json: rel:child -> ./gone/collection.json "
            "does not exist",
            "catalog/roads/collection.json: rel:describedby -> ./README.md "
            "does not exist",
            "catalog/roads/collection.json: asset thumbnail -> "
            "./roads.thumb.jpg does not exist",
        }
        data = {
            "catalog/roads/collection.json: rel:pmtiles -> ./roads.pmtiles "
            "does not exist",
            "catalog/roads/collection.json: asset data -> ./roads.parquet "
            "does not exist",
        }

        errors, _, skipped, _ = check_catalog(base, root, ci_light=True)
        if set(errors) != in_git:
            failures.append(
                f"CI_LIGHT: expected errors {sorted(in_git)}, "
                f"got {sorted(errors)}"
            )
        if skipped != 2:
            failures.append(
                f"CI_LIGHT: expected 2 skipped data hrefs, got {skipped}"
            )

        errors, _, skipped, _ = check_catalog(base, root, ci_light=False)
        if set(errors) != in_git | data:
            failures.append(
                f"full mode: expected errors {sorted(in_git | data)}, "
                f"got {sorted(errors)}"
            )
        if skipped != 0:
            failures.append(
                f"full mode: expected 0 skipped hrefs, got {skipped}"
            )
    return failures


failures = [
    f".gitignore: {suffix} is in DATA_SUFFIXES, but no '*{suffix}' line "
    "ignores it. CI_LIGHT must not exempt a file that git can hold."
    for suffix in unignored_suffixes(ROOT / ".gitignore")
] + [f"self-check: {failure}" for failure in self_check()]
if failures:
    print("\n".join(f"error  {f}" for f in failures))
    raise SystemExit(1)

errors, checked, skipped, count = check_catalog(BASE, ROOT, CI_LIGHT)

if skipped:
    print(
        f"note   {skipped} data href(s) not checked: CI_LIGHT is set and the "
        "bytes live in\n       object storage, not git. Run without CI_LIGHT "
        "locally to check them."
    )

if errors:
    print("\n".join(f"error  {e}" for e in errors))
    raise SystemExit(1)

print(f"OK: {checked} relative href(s) across {count} object(s)")

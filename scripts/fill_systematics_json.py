#!/usr/bin/env python3
"""
Delete all Ztautau_phi_* files that are not Ztautau_phi_0 from the systematics
directories, then regenerate systematics.json.
"""

import os
import json
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SYST_DIR = os.path.join(SCRIPT_DIR, "../public/plots/ztautau/systematics")
PUBLIC_DIR = os.path.realpath(os.path.join(SCRIPT_DIR, "../public"))
JSON_OUT = os.path.join(os.path.dirname(__file__), "../src/data/ztautau/systematics.json")

# Matches Ztautau_phi_* but NOT Ztautau_phi_0 (the zero sample has no suffix after 0)
UNWANTED = re.compile(r"Ztautau_phi_(?!0[^0-9p])(?!0\.png)(?!0_)")

deleted = 0
for root, dirs, files in os.walk(SYST_DIR):
    for fname in files:
        if "Ztautau_phi_" in fname and not re.search(r"Ztautau_phi_0[_.]", fname):
            path = os.path.join(root, fname)
            os.remove(path)
            print(f"deleted: {path}")
            deleted += 1

print(f"\nDeleted {deleted} files.")

# Rebuild systematics.json
result = {
    "id": "systematics",
    "name": "Systematic Uncertainties",
    "description": "",
    "defaultGridCols": 4,
    "plots": [],
}

for syst in sorted(os.listdir(SYST_DIR)):
    syst_dir = os.path.join(SYST_DIR, syst)
    if not os.path.isdir(syst_dir):
        continue

    files = []
    for subdir, _, fnames in os.walk(syst_dir):
        for fname in sorted(fnames):
            if fname.endswith(".png"):
                full = os.path.join(subdir, fname)
                rel = os.path.realpath(full)[len(PUBLIC_DIR):]
                files.append(rel)

    files.sort()

    result["plots"].append(
        {
            "id": syst.lower().replace("_", "-"),
            "title": syst,
            "files": files,
        }
    )

with open(JSON_OUT, "w") as f:
    json.dump(result, f, indent=2)
    f.write("\n")

print(f"\nWrote {JSON_OUT}")
for p in result["plots"]:
    print(f"  {p['title']}: {len(p['files'])} files")

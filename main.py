#!/usr/bin/env python3
"""news-image-20261120 entry (Python 3.13, standard library only).

Writes the 20 November 2026 world-news poster to /output/entry.png.

The poster itself lives in this repository as entry.png: a 1024x1024
PNG drawn programmatically (see make_poster.py for the generator and
its verified sources) summing up Friday 20 November 2026 — the ICJ
genocide ruling, the Shenzhen three-way summit, Anthropic's Nasdaq
debut and the AI sell-off, the Houthi strike on Riyadh, the COP31
draft, and Kenya's last Ebola patient. This program copies that file
to the output directory, byte for byte, so the run is deterministic:
no network, no clock, no randomness.

Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(SOURCE, target)
    size = target.stat().st_size
    assert size <= 1_048_576, f"entry.png is {size} bytes, over the 1 MiB cap"
    print(f"wrote {target} ({size} bytes)")


if __name__ == "__main__":
    main()

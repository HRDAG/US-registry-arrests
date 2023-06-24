"""Import File"""
# !/usr/bin/env python3
# vim: set expandtab ts=4 sw=4 ft=python ai fileencoding=utf-8
#
# Author: LB
# Maintainer(s): BP LB
# License: (c) HRDAG 2023, GPL v2 or newer
#
# US-registry-arrests/individual/chi_daycares/import/src
# -----------------------------------------------------------
#
import argparse
from pathlib import Path
import re
import pandas as pd


def getargs():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default=None)
    parser.add_argument("--output", default=None)
    args = parser.parse_args()
    assert Path(args.input).exists()
    assert args.output.endswith(".parquet")
    return args


if __name__ == "__main__":
    args = getargs()
    chi_daycares = pd.read_csv(args.input)
    print(chi_daycares.info())
    chi_daycares.to_parquet(args.output)
    print(f"Wrote {len(chi_daycares)} records to {args.output},done.")
# done

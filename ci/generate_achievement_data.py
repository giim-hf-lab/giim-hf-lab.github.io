#!/usr/bin/env python3
import sys

import pandas as pd


def _main() -> int:
    raw = pd.read_excel(
        "achievements.raw.xlsx",
        sheet_name=["awards", "copyrights", "patents", "projects"],
        header=0,
        dtype=str
    )

    raw_awards = raw["awards"]
    raw_awards.sort_values(by="year", axis=0, ascending=False, inplace=True, ignore_index=True)
    raw_awards.to_csv("docs/_data/achievements/awards.csv", index=False, encoding="utf-8")

    raw_patents = raw["patents"]
    raw_patents["applied"] = pd.to_datetime(raw_patents["applied"])
    raw_patents["authorised"] = pd.to_datetime(raw_patents["authorised"])
    raw_patents.sort_values(by=["applied", "authorised"], axis=0, ascending=False, inplace=True, ignore_index=True)
    raw_patents.to_csv("docs/_data/achievements/patents.csv", index=False, encoding="utf-8")

    raw_copyrights = raw["copyrights"]
    raw_copyrights["registered"] = pd.to_datetime(raw_copyrights["registered"])
    raw_copyrights.sort_values(by="registered", axis=0, ascending=False, inplace=True, ignore_index=True)
    raw_copyrights.to_csv("docs/_data/achievements/copyrights.csv", index=False, encoding="utf-8")

    raw_projects = raw["projects"]
    raw_projects.sort_values(by="year", axis=0, ascending=False, inplace=True, ignore_index=True)
    raw_projects.to_csv("docs/_data/achievements/projects.csv", index=False, encoding="utf-8")

    return 0


if __name__ == "__main__":
    sys.exit(_main())

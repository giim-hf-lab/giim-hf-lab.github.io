#!/usr/bin/env python3
import hashlib
import math
import re
import sys

import pandas as pd
import yaml


def _main() -> int:
    raw = pd.read_excel(
        "achievements.raw.xlsx",
        sheet_name=["awards", "copyrights", "patents", "projects", "publications"],
        header=0,
        dtype=str
    )

    raw_awards = raw["awards"]
    raw_awards.sort_values(by="year", axis=0, ascending=False, inplace=True, ignore_index=True)
    raw_awards.to_csv("docs/_data/achievements/awards.csv", index=False, encoding="utf-8", line_terminator="\n")

    raw_patents = raw["patents"]
    raw_patents["applied"] = pd.to_datetime(raw_patents["applied"])
    raw_patents["authorised"] = pd.to_datetime(raw_patents["authorised"])
    raw_patents.sort_values(by=["applied", "authorised"], axis=0, ascending=False, inplace=True, ignore_index=True)
    raw_patents.to_csv("docs/_data/achievements/patents.csv", index=False, encoding="utf-8", line_terminator="\n")

    raw_copyrights = raw["copyrights"]
    raw_copyrights["registered"] = pd.to_datetime(raw_copyrights["registered"])
    raw_copyrights.sort_values(by="registered", axis=0, ascending=False, inplace=True, ignore_index=True)
    raw_copyrights.to_csv("docs/_data/achievements/copyrights.csv", index=False, encoding="utf-8", line_terminator="\n")

    raw_projects = raw["projects"]
    raw_projects.sort_values(by="year", axis=0, ascending=False, inplace=True, ignore_index=True)
    raw_projects.to_csv("docs/_data/achievements/projects.csv", index=False, encoding="utf-8", line_terminator="\n")

    yaml_dumper = getattr(yaml, "CDumper", None) or getattr(yaml, "Dumper")

    authors_split = re.compile(r"[^\w\s]+")

    raw_publications = raw["publications"]
    raw_publications["accepted"] = pd.to_datetime(raw_publications["accepted"])
    for index, row in raw_publications.iterrows():
        title = row["title"].strip()
        filename = hashlib.sha3_512(title.encode("utf-8")).hexdigest()
        data = {
            "title": title,
            "authors": [
                author.title()
                for author in (
                    author.strip()
                    for author in authors_split.split(row["authors"])
                    if author
                )
                if author
            ],
            "by": row["by"],
            "tags": [row["category"]]
        }
        doi = row["doi"]
        if isinstance(doi, str) and doi:
            data["doi"] = doi
        accepted = row["accepted"]
        with open(f"docs/publications/archives/_posts/{accepted:%Y-%m-%d}-{filename}.md", "wb") as f:
            f.write(b"---\n")
            yaml.dump(data, f, yaml_dumper, indent=2, allow_unicode=True, encoding="utf-8")
            f.write(b"---\n")

    return 0


if __name__ == "__main__":
    sys.exit(_main())

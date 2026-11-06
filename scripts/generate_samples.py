"""Rebuild the dataset files from scripts/facts_source.py.

    python3 scripts/generate_samples.py

Writes data/facts.csv (one row per fact), data/facts.json, data/matrix.csv
(one row per tool, one column per field, blank where the vendor's page
doesn't say) and docs/comparison.md.
"""
import csv
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from facts_source import FACTS  # noqa: E402


def main():
    fields = list(csv.DictReader(open(os.path.join(ROOT, "data", "fields.csv"), encoding="utf-8")))
    tools = list(csv.DictReader(open(os.path.join(ROOT, "data", "tools.csv"), encoding="utf-8")))
    rows = [{"tool_id": t, "field": f, "value": v, "source_url": u, "checked": c, "note": n} for t, f, v, u, c, n in FACTS]
    with open(os.path.join(ROOT, "data", "facts.csv"), "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["tool_id", "field", "value", "source_url", "checked", "note"], lineterminator="\r\n")
        w.writeheader()
        w.writerows(rows)
    with open(os.path.join(ROOT, "data", "facts.json"), "w", encoding="utf-8") as fh:
        json.dump({"dataset": "AI accounting software feature dataset", "publisher": "ZeraBooks (Zera Books Inc.)",
                   "note": "ZeraBooks makes one of the tools listed. Every fact was read on the vendor's own page on its checked date.",
                   "tools": tools, "fields": fields, "facts": rows}, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    by = {(r["tool_id"], r["field"]): r for r in rows}
    with open(os.path.join(ROOT, "data", "matrix.csv"), "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, lineterminator="\r\n")
        w.writerow(["tool"] + [f["field"] for f in fields])
        for t in tools:
            w.writerow([t["tool"]] + [by.get((t["tool_id"], f["field"]), {}).get("value", "") for f in fields])
    md = ["# AI accounting software comparison", "",
          "Generated from `data/facts.csv`. Every cell links to the vendor page it was read on, with the date. A blank cell means the vendor's page didn't say. ZeraBooks makes one of these tools.", ""]
    for f in fields:
        md += [f"## {f['label']}", "", f"_{f['what_it_records']}_", "", "| Tool | Value | Source |", "|---|---|---|"]
        for t in tools:
            r = by.get((t["tool_id"], f["field"]))
            if r:
                val = r["value"].replace("|", "/") + (f" ({r['note']})" if r["note"] else "")
                md.append(f"| {t['tool']} | {val} | [{r['checked']}]({r['source_url']}) |")
            else:
                md.append(f"| {t['tool']} | | |")
        md.append("")
    open(os.path.join(ROOT, "docs", "comparison.md"), "w", encoding="utf-8").write("\n".join(md))
    print(f"{len(rows)} facts, {len(tools)} tools, {len(fields)} fields")


if __name__ == "__main__":
    main()

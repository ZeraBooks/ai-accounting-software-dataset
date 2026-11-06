import contextlib
import csv
import datetime as dt
import io
import os
import shutil
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "cli"))
import check_dataset as cd  # noqa: E402

AS_OF = dt.date(2026, 11, 5)


class Dataset(unittest.TestCase):
    def test_clean_on_release_date(self):
        issues, s = cd.check(AS_OF)
        self.assertEqual([i for i in issues if i[1] == "error"], [])
        self.assertEqual(s["tools"], 8)
        self.assertGreaterEqual(s["facts"], 70)

    def test_old_facts_go_stale(self):
        issues, _ = cd.check(dt.date(2027, 3, 1))
        self.assertTrue(any(i[0] == "DS-006" for i in issues))

    def test_every_tool_has_price_and_ai_rows_or_says_why(self):
        facts = list(csv.DictReader(open(os.path.join(ROOT, "data", "facts.csv"))))
        tools = {r["tool_id"] for r in csv.DictReader(open(os.path.join(ROOT, "data", "tools.csv")))}
        for t in tools:
            have = {f["field"] for f in facts if f["tool_id"] == t}
            self.assertIn("plans_and_list_prices", have, t)
            self.assertIn("ai_features", have, t)

    def test_zerabooks_facts_stay_true(self):
        z = {f["field"]: f["value"] for f in csv.DictReader(open(os.path.join(ROOT, "data", "facts.csv"))) if f["tool_id"] == "zerabooks"}
        self.assertEqual(z["starting_price_monthly_usd"], "79")
        self.assertIn("No live bank feeds", z["bank_connections"])
        self.assertIn("card at checkout", z["free_trial"])
        text = " ".join(z.values()).lower()
        for banned in ("unlimited", "soc 2", "sync", "free plan", ".qbo", "iif"):
            self.assertNotIn(banned, text)

    def test_foreign_source_is_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            shutil.copytree(os.path.join(ROOT, "data"), os.path.join(d, "data"))
            p = os.path.join(d, "data", "facts.csv")
            rows = list(csv.DictReader(open(p)))
            rows[0]["source_url"] = "https://www.g2.com/products/x"
            with open(p, "w", newline="") as fh:
                w = csv.DictWriter(fh, fieldnames=list(rows[0]), lineterminator="\r\n")
                w.writeheader()
                w.writerows(rows)
            old = cd.ROOT
            cd.ROOT = d
            try:
                issues, _ = cd.check(AS_OF)
            finally:
                cd.ROOT = old
            self.assertIn("DS-002", {i[0] for i in issues})

    def test_cli(self):
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(cd.main(["--as-of", "2026-11-05"]), 0)


if __name__ == "__main__":
    unittest.main()

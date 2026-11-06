# AI accounting software feature dataset

Which AI accounting software does what, and for how much? This dataset answers it for eight tools (ZeraBooks, QuickBooks Online, Xero, Digits, Puzzle, Booke AI, Zeni and Rillet) with one rule: every cell was read on the vendor's own page, and carries that page's URL and the date it was read. Where a vendor's page doesn't say, the cell is blank. It's published by [ZeraBooks](https://www.zerabooks.com/best-ai-accounting-software), which makes one of the tools, so you can check every one of our claims the same way you check everyone else's.

- One row per fact: [`data/facts.csv`](data/facts.csv) and [`data/facts.json`](data/facts.json)
- One row per tool: [`data/matrix.csv`](data/matrix.csv)
- Readable tables with a source link in every cell: [`docs/comparison.md`](docs/comparison.md)
- Field definitions: [`data/fields.csv`](data/fields.csv)
- Checker: [`cli/check_dataset.py`](cli/check_dataset.py)
- Release zip: [latest](https://github.com/ZeraBooks/ai-accounting-software-dataset/releases/latest)

## At a glance

Regular monthly list prices in USD as shown on each pricing page. Full wording, promotions and notes are in the data.

| Tool | Starting price a month | Free trial | How transactions get in | Ledger | Human service |
|---|---|---|---|---|---|
| ZeraBooks | $79 billed annually ($149 monthly) | 7 days, card at checkout | Uploaded bank and card statements, proven against printed balances | Its own | From $150 a month |
| QuickBooks Online | $38 (Simple Start); Free plan listed | 30-day option shown | Bank connections | Its own | |
| Xero | $27 | "Get one month free" shown, no terms | Bank reconciliation | Its own | |
| Digits | $65 | 30 days | 12,000+ banks, cards and payroll providers | Its own | |
| Puzzle | $30 | "Try for free", no terms | Connections and integrations | Its own | From $171 a month |
| Booke AI | $129 per business, plus QuickBooks or Xero | | QuickBooks Online or Xero bank feed | Inside QuickBooks Online or Xero | |
| Zeni | $549 ($494 billed annually) | Demo | | | Finance team in every plan |
| Rillet | Not published | Demo | | Its own | |

Checked November 5, 2026, except a few product descriptions carried from October 1, 2026 (each row says which). A blank cell means the vendor's page didn't say on the check date, not that the tool can't.

## Which one to pick

That depends on the job, and the fields are there so you can sort by yours:

- **You want the books done from bank statements, with proof.** ZeraBooks works from your statements instead of a bank feed, proves every month against the printed balances, categorizes from each client's reviewed history, and includes a statement converter in the same plan. It asks when it isn't sure, and anything it did can be undone. This is the case [our comparison page](https://www.zerabooks.com/best-ai-accounting-software) makes, with the reasons.
- **You want live bank feeds in a mainstream ledger.** QuickBooks Online and Xero, both with AI features by plan. Digits and Puzzle if you're a U.S. startup (Digits serves U.S.-based entities only).
- **You're staying on QuickBooks Online or Xero and want AI on top.** Booke AI, per business.
- **You want a finance team, not software.** Zeni, or a service such as [ZeraBooks bookkeeping](https://www.zerabooks.com/bookkeeping-services).
- **You're a finance team replacing an ERP.** Rillet.

## The fields

| Field | What it records |
|---|---|
| `what_it_is` | The vendor's one-line description |
| `plans_and_list_prices` | Every plan and its regular monthly price |
| `starting_price_monthly_usd` | Lowest paid plan, as a number |
| `billing_note` | Annual vs monthly, per-business pricing, what drives the price |
| `promotion` | An introductory discount shown on the check date |
| `free_trial`, `free_plan` | As stated |
| `bank_connections` | Live feeds, or how transactions get in |
| `works_with` | Its own ledger, or inside another system |
| `ai_features`, `ai_assistant` | In the vendor's own terms |
| `auto_categorization_claim` | A published categorization rate (only Puzzle publishes one) |
| `human_service` | Bookkeeping or finance staff, and price if published |
| `multi_entity` | How extra companies or clients are priced |
| `statement_documents` | Reading PDF statements and documents |
| `availability` | Country or entity limits |

## Rules the data follows

1. **The vendor's own page only.** No review sites, no press, no inference. `cli/check_dataset.py` fails any source that isn't on the vendor's domain (DS-002).
2. **Blank beats a guess.** A fact the page doesn't state is left out. There are 53 blank cells out of 128.
3. **Dated.** Every fact has the day it was read. The checker warns on anything older than 90 days (DS-006), because prices change.
4. **Quoted where it matters.** Vendor phrases are in quotation marks.
5. **ZeraBooks gets no special treatment.** Our facts are sourced to our public pages like everyone else's, and the tests fail if our rows ever claim bank feeds, a free plan or anything unlimited.

```bash
python3 cli/check_dataset.py                    # checks every rule as of today
python3 cli/check_dataset.py --as-of 2027-02-01 # what will need re-checking by then
```

## Corrections

Prices and plans change. If a cell is out of date, open an issue or a pull request with the vendor page URL. Edit `scripts/facts_source.py`, then run `python3 scripts/generate_samples.py` to rebuild every file. Vendors are welcome to send corrections about their own products.

## Tests

```bash
python3 scripts/generate_samples.py
python3 -m unittest discover -s tests -v
```

## License and citation

Code MIT ([`LICENSE`](LICENSE)). Data and docs CC BY 4.0 ([`LICENSE-SAMPLES`](LICENSE-SAMPLES)): use it in your own comparisons with credit. Cite with [`CITATION.cff`](CITATION.cff). `MANIFEST.json` and `checksums.txt` list every file with its SHA-256.

Product names are trademarks of their owners. Short quotations from vendor pages are used for comparison. Not financial advice.

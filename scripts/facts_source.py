"""The facts, as read on each vendor's own pages. Edit here, then run
scripts/generate_samples.py to rebuild data/facts.csv, data/facts.json,
data/matrix.csv and docs/comparison.md.

Rules: only what the vendor's own page says on the check date. No third-party
sources, no inference. If a page doesn't say, the fact is left out and the
cell stays blank. Quotes are short and marked with quotation marks.
"""

ZB = "https://www.zerabooks.com/pricing"
ZB_AI = "https://www.zerabooks.com/ai-bookkeeping"
ZB_BK = "https://www.zerabooks.com/bookkeeping-services"
ZB_CONV = "https://www.zerabooks.com/bank-statement-converter"
QBO = "https://quickbooks.intuit.com/pricing/"
XERO = "https://www.xero.com/us/pricing-plans/"
DIG = "https://digits.com/pricing/"
PUZ = "https://puzzle.io/pricing"
BOOKE = "https://booke.ai/pricing"
ZENI = "https://www.zeni.ai/pricing"
RIL = "https://www.rillet.com/pricing"
RIL_HOME = "https://www.rillet.com/"
D = "2026-11-05"
OCT = "2026-10-01"

FACTS = [
    # ZeraBooks (we make it; facts from our own pages and product docs)
    ("zerabooks", "what_it_is", "AI-native accounting software: AI does the bookkeeping from bank and credit card statements inside a double-entry general ledger. A financial document converter is included.", ZB_AI, D, ""),
    ("zerabooks", "plans_and_list_prices", "One plan with General Ledger and Converter: $149 a month billed monthly, or $79 a month billed annually ($948 a year), with 1,000 Converter pages a month. Larger page plans: 2,500 pages $249 monthly or $179 billed annually; 5,000 pages $599 monthly or $449 billed annually.", ZB, D, ""),
    ("zerabooks", "starting_price_monthly_usd", "79", ZB, D, "Billed annually; $149 billed monthly."),
    ("zerabooks", "billing_note", "Monthly or annual billing. Annual billing gives the year's 12,000 pages upfront.", ZB, D, ""),
    ("zerabooks", "free_trial", "7 days; a card at checkout, nothing charged for 7 days.", ZB, D, ""),
    ("zerabooks", "free_plan", "No", ZB, D, ""),
    ("zerabooks", "bank_connections", "No live bank feeds. Transactions come from uploaded bank and credit card statements, each proven against its printed balances.", ZB_AI, D, ""),
    ("zerabooks", "works_with", "Its own double-entry general ledger.", ZB_AI, D, ""),
    ("zerabooks", "ai_features", "Categorizes from each client's reviewed history, matches bills and invoices to payments, reconciles each month, drafts month-end entries for review, asks when it isn't sure, and anything it did can be undone.", ZB_AI, D, ""),
    ("zerabooks", "ai_assistant", "Ask Zera", ZB_AI, D, ""),
    ("zerabooks", "human_service", "Done-for-you bookkeeping by the ZeraBooks team, from $150 a month (USD), priced after a free call.", ZB_BK, D, ""),
    ("zerabooks", "multi_entity", "3 active client companies included; each additional active client $29 a month, or $290 a year on annual billing.", ZB, D, ""),
    ("zerabooks", "statement_documents", "Reads PDF bank, card, check and brokerage statements (up to 500 pages a file) and proves each account against its printed balances. Excel and CSV downloads, including QuickBooks-, Xero- and Sage-ready CSV layouts.", ZB_CONV, D, ""),
    # QuickBooks Online
    ("quickbooks-online", "what_it_is", "Intuit's cloud accounting software for small businesses.", QBO, D, ""),
    ("quickbooks-online", "plans_and_list_prices", "Free $0; Simple Start $38; Essentials $85; Plus $140; Advanced $340 a month (struck-through list prices).", QBO, D, ""),
    ("quickbooks-online", "starting_price_monthly_usd", "38", QBO, D, "Simple Start list price. A Free plan is also listed."),
    ("quickbooks-online", "promotion", "50% off for 3 months on paid plans (Simple Start $19, Essentials $42.50, Plus $70, Advanced $170).", QBO, D, ""),
    ("quickbooks-online", "free_trial", "\"Free trial for 30 days\" option shown; the page doesn't say which plan it applies to.", QBO, D, ""),
    ("quickbooks-online", "free_plan", "Yes: Free, $0 a month, 1 bank account, no credit card required.", QBO, D, ""),
    ("quickbooks-online", "bank_connections", "Bank connections; the Free plan connects 1 bank account.", QBO, D, ""),
    ("quickbooks-online", "works_with", "Its own ledger.", QBO, D, ""),
    ("quickbooks-online", "ai_features", "Listed under Intuit Intelligence: AI Chat (beta), expense categorization, book cleanup, reconciliation, auto-categorized and verified transactions (Plus), anomaly detection, and more by plan.", QBO, D, "The page says automatic categorization is available in Plus and Advanced while also listing categorization on lower plans."),
    ("quickbooks-online", "ai_assistant", "Intuit Intelligence", QBO, D, ""),
    # Xero
    ("xero", "what_it_is", "Cloud accounting software for small businesses.", XERO, D, ""),
    ("xero", "plans_and_list_prices", "Early $27; Growing $59; Established $97 a month.", XERO, D, ""),
    ("xero", "starting_price_monthly_usd", "27", XERO, D, ""),
    ("xero", "promotion", "80% off the base plan for the first 3 months for new U.S. customers (Early $5.40, Growing $11.80, Established $19.40).", XERO, D, ""),
    ("xero", "free_trial", "A \"Get one month free\" button is shown without terms.", XERO, D, ""),
    ("xero", "free_plan", "No", XERO, D, ""),
    ("xero", "bank_connections", "Bank transaction reconciliation on all plans; auto-reconcile $5 a month on Early, included on Growing and Established.", XERO, D, ""),
    ("xero", "works_with", "Its own ledger.", XERO, D, ""),
    ("xero", "ai_features", "Smart Document Capture and auto-reconcile in the plan tables.", XERO, D, ""),
    ("xero", "ai_assistant", "JAX, \"your AI finance partner\"", XERO, D, ""),
    # Digits
    ("digits", "what_it_is", "AI-native accounting software with an automated ledger.", DIG, OCT, ""),
    ("digits", "plans_and_list_prices", "Essentials $65; Core $100; Pro $250 a month (Pro \"coming soon\").", DIG, D, ""),
    ("digits", "starting_price_monthly_usd", "65", DIG, D, ""),
    ("digits", "free_trial", "30 days.", DIG, D, ""),
    ("digits", "free_plan", "No; free firm books for partner accounting firms' own books.", DIG, D, ""),
    ("digits", "bank_connections", "Bank and payroll connections: 12,000+ banks, cards and payroll providers.", DIG, D, ""),
    ("digits", "works_with", "Its own ledger.", DIG, OCT, ""),
    ("digits", "ai_features", "24/7 AI bookkeeping and reconciliation, quality checks, automated schedules (Core and Pro).", DIG, D, ""),
    ("digits", "ai_assistant", "Ask Digits", DIG, D, ""),
    ("digits", "multi_entity", "Multi-entity on all plans; additional entities free up to 250 transactions a year, then from $35 a month.", DIG, D, ""),
    ("digits", "availability", "U.S.-based entities only.", DIG, D, ""),
    # Puzzle
    ("puzzle", "what_it_is", "Accounting software and services for startups.", PUZ, OCT, ""),
    ("puzzle", "plans_and_list_prices", "Starter $30; Core $72; Complete $120; Scale $360 a month. Core + Expert Reviewed $171 a month.", PUZ, D, ""),
    ("puzzle", "starting_price_monthly_usd", "30", PUZ, D, ""),
    ("puzzle", "free_trial", "\"Try for free\" on each plan; length and terms not stated.", PUZ, D, ""),
    ("puzzle", "bank_connections", "Unlimited connections on Starter; integrations listed with Stripe, Ramp, Mercury, Brex and more.", PUZ, D, ""),
    ("puzzle", "works_with", "Its own ledger.", PUZ, OCT, ""),
    ("puzzle", "ai_features", "AI Suite (Chat, Cowork, Close) on all plans; AI-powered accuracy review, reconciliations and insights on Complete and Scale. AI credits by plan.", PUZ, D, ""),
    ("puzzle", "auto_categorization_claim", "85-90% of transactions categorized automatically (Starter).", PUZ, D, ""),
    ("puzzle", "human_service", "Core + Expert Reviewed $171 a month up to $10K monthly expenses; Full Service priced by monthly expenses.", PUZ, D, ""),
    # Booke AI
    ("booke-ai", "what_it_is", "An AI bookkeeper that works inside QuickBooks Online and Xero.", BOOKE, D, ""),
    ("booke-ai", "plans_and_list_prices", "AI Bookkeeper (Business) $129 per business a month; Accounting Firms pricing by request.", BOOKE, D, ""),
    ("booke-ai", "starting_price_monthly_usd", "129", BOOKE, D, "Plus the QuickBooks Online or Xero subscription."),
    ("booke-ai", "billing_note", "Per business. A business added mid-period is prorated.", BOOKE, D, ""),
    ("booke-ai", "bank_connections", "Works from the QuickBooks Online or Xero bank feed.", BOOKE, D, ""),
    ("booke-ai", "works_with", "QuickBooks Online and Xero.", BOOKE, D, ""),
    ("booke-ai", "ai_features", "Daily bank-feed categorization, document matching, missing-document requests, rules and thresholds, exception review with an audit trail, OCR for bills, invoices and receipts.", BOOKE, D, ""),
    ("booke-ai", "multi_entity", "Multi-client management on the Accounting Firms plan.", BOOKE, D, ""),
    # Zeni
    ("zeni", "what_it_is", "AI bookkeeping with a dedicated finance team, for startups.", ZENI, D, ""),
    ("zeni", "plans_and_list_prices", "AI Bookkeeping: Starter $549, Growth $799 a month; $494 and $719 a month billed annually; Enterprise custom.", ZENI, D, ""),
    ("zeni", "starting_price_monthly_usd", "549", ZENI, D, "$494 a month billed annually."),
    ("zeni", "billing_note", "\"Pricing based on bookkeeping complexity, monthly expenses, and annual revenue.\"", ZENI, D, ""),
    ("zeni", "free_trial", "No trial listed; demo.", ZENI, D, ""),
    ("zeni", "ai_features", "AI bookkeeping dashboard, AI bill payments, AI reimbursements, AI business checking.", ZENI, D, ""),
    ("zeni", "human_service", "Every AI Bookkeeping plan includes a dedicated finance team (controller, bookkeeping manager, analyst). Fractional CFO from $1,599 a month.", ZENI, D, ""),
    # Rillet
    ("rillet", "what_it_is", "An AI-native ERP for finance teams aiming at a zero-day close.", RIL_HOME, OCT, ""),
    ("rillet", "plans_and_list_prices", "No subscription price published; demo.", RIL, D, ""),
    ("rillet", "billing_note", "Implementation listed at $10K to $30K.", RIL, D, ""),
    ("rillet", "free_trial", "Not mentioned; \"Book a 30-minute demo.\"", RIL, D, ""),
    ("rillet", "works_with", "Its own general ledger.", RIL, D, ""),
    ("rillet", "ai_features", "Aura AI agents in the general ledger, AI flux analysis, AI accrual module, custom agents.", RIL, D, ""),
    ("rillet", "ai_assistant", "Aura AI", RIL, D, ""),
]

# BreastScreening-AI IR and Financial PDF, PPTX, and Word Templates

This file defines the layout, structure, and content rules for public-facing PDF, PPTX, and Word assets linked from `reports.html`.

Future prompts should instruct the assistant to read and follow this file before creating or updating report assets:

```text
Before creating or updating report PDFs, PPTX files, or Word files, read and follow media/reports/governance/REPORT_PDF_TEMPLATES.md and PROMPT_RULES.md. Use the latest rule version as authoritative.
```

## Generated Template Assets

Use these files as the baseline visual templates for future `reports.html` assets:

```text
media/reports/templates/breastscreeningai_template_annual_financial_statements.pdf
media/reports/templates/breastscreeningai_template_annual_financial_statements.pptx
media/reports/templates/breastscreeningai_template_annual_financial_statements.docx

media/reports/templates/breastscreeningai_template_ir_presentation.pdf
media/reports/templates/breastscreeningai_template_ir_presentation.pptx

media/reports/templates/breastscreeningai_template_ir_letter.pdf
media/reports/templates/breastscreeningai_template_ir_letter.pptx
media/reports/templates/breastscreeningai_template_ir_letter.docx

media/reports/templates/breastscreeningai_template_ir_news_notice.pdf
media/reports/templates/breastscreeningai_template_ir_news_notice.pptx
media/reports/templates/breastscreeningai_template_ir_news_notice.docx
```

## Shared Template Rules

All report PDFs, PPTX files, and Word files must use source-backed information only. Do not invent revenue, customers, contracts, valuation, partnerships, funding rounds, regulatory status, clinical deployment, or forecasts.

All report assets must use a clean BreastScreening-AI visual style:

- Page size: A4 for document reports and letters, 16:9 landscape for presentation companion PDFs.
- Primary color: navy.
- Accent color: BreastScreening-AI blue.
- Supporting colors: soft blue, teal for positive signals, amber for caution or unresolved items.
- Typography: clear sans-serif headings, readable body copy, strong hierarchy.
- Header: BreastScreening-AI name, short blue accent bar, document type, and publication date where relevant.
- Footer: company communication asset label, page number, and optional short source note.
- Visual elements: cards, compact tables, charts, and callouts only when they improve readability.
- Evidence boundary: clearly identify missing information when a claim is not established by the source set.
- File naming: use stable descriptive lowercase filenames under `media/reports/generated` or `media/reports/templates`.
- Public wording: never state or imply that the asset was AI-generated.
- Avoid rejected wording, including `without investor-sensitive detail`.
- Paired template rule: every public PDF should have an editable source template when practical. Use PPTX for presentation-style assets and Word for narrative or report-style assets.
- Design propagation rule: when the report design system changes, update the template files and any active report assets that use the old design, unless the user explicitly asks for a narrower update.

## Format Selection Rules

Use PDF for public access, website downloads, archive copies, and investor-facing documents that should not be casually edited.

Use PPTX when the asset is a slide deck, pitch deck, IR presentation, board-style visual narrative, or chart-heavy document where layout, slide rhythm, and presentation flow matter.

Use Word when the asset is a narrative document, letter, report, announcement, notice, financial statement access copy, or review draft where prose editing, tracked changes, comments, and longer-form paragraphs matter.

Use both PDF and PPTX for IR Presentations.

Use both PDF and Word for Annual Financial Statements, IR Letters, and IR News and Notice documents.

Use all three formats only when a document must exist as a public PDF, an editable narrative document, and a slide-based communication. This should be exceptional rather than the default.

Existing PPTX templates for non-presentation report families may remain as visual design references, but Word is the preferred editable source for narrative and statement-style report assets.

## Audit and Improvement Rules

Before treating report PDFs as ready, render the pages to images and inspect the visual output. The audit must check readability, spacing, hierarchy, clipped text, overlapping tables, broken charts, poor contrast, page size, page count, and metadata.

When a template PDF is improved, update the matching editable source template in the same pass. Use PPTX as the editable source for presentations and Word as the editable source for narrative or report-style documents.

Use card-based financial and disclosure blocks when exact values are placeholders or when a table would become too dense. Dense statement tables should only be used when the source data is complete and the text remains legible at the final PDF size.

Remove temporary inspect files, Office lock files, and other sidecar artifacts from public report asset folders before delivery.

Audit outcome on 2026-06-15: the template set was visually reviewed and improved. The Annual Financial Statements template was changed from dense table placeholders to larger readable financial cards, the document templates received stronger cover hierarchy, all template PDFs received BreastScreening-AI metadata, and page sizes were verified as A4 for document templates and 16:9 landscape for the presentation companion PDF.

Word template outcome on 2026-06-15: Word templates were added for Annual Financial Statements, IR Letters, and IR News and Notice. These files are the preferred editable sources for narrative and statement-style report assets. The rendered Word templates were visually reviewed for page breaks, table readability, spacing, and clipping.

## Template 1 - Annual Financial Statements

Use this template for annual or interim financial statement access copies based on signed accounting records.

Recommended filename pattern:

```text
breastscreeningai_annual_financial_statements_[year].pdf
breastscreeningai_interim_financial_statements_[year].pdf
```

Recommended structure:

```markdown
Document type:
Annual Financial Statements or Interim Financial Statements

Cover / Executive Summary:
- Reporting period
- Publication date
- Source basis
- Currency
- Short management-level summary

Company Overview:
- Company name
- Reporting context
- Scope of the document

Year or Period in Review:
- Supported operating context
- Financial movement compared with prior period, when supported
- Relevant subsequent events, if applicable and clearly dated

Financial Performance:
- Revenue or sales and services, if supported
- Subsidies, grants, or other income, if supported
- External services
- Personnel expenses
- Other expenses
- Net result

Statement of Financial Position:
- Total assets
- Cash and deposits
- Equity
- Liabilities
- Supplier liabilities, when material
- State and other public entity balances, when relevant

Key Metrics:
- Compact cards for the most important figures
- Optional comparison table against previous year or interim period

Risks and Uncertainties:
- Working-capital exposure
- Cash visibility
- Reliance on grants or subsidies
- Missing audit, cash-flow, filing, or note disclosures

Outlook:
- Only source-backed priorities
- No unsupported forecasts

Source Basis and Missing Information:
- List exact source documents or source categories
- List unavailable items, such as audit opinion, cash-flow statement, statutory filing metadata, payment schedule, or board-approved KPIs
```

Layout notes:

- Use metric cards for core financial figures.
- Use tables for statements and period comparisons.
- Avoid dense statutory formatting unless source data supports it.
- If the document is not a statutory filing, describe it as an access copy or company communication asset based on accounting records.

## Template 2 - IR Presentations

Use this template for investor-facing presentation PDFs and editable PPTX decks.

Recommended filename pattern:

```text
breastscreeningai_ir_presentation_[year].pdf
breastscreeningai_ir_presentation_[year].pptx
```

Recommended structure:

```markdown
Slide 1 - Cover:
- Company name
- Reporting period
- Publication date
- Source-backed positioning statement
- Key supported figures

Slide 2 - Executive Snapshot:
- Most important financial and strategic signals
- Current evidence boundary
- Main diligence takeaway

Slide 3 - Vision and Mission:
- Project purpose
- Clinical or hospital-facing value logic
- Evidence boundary

Slide 4 - Problem:
- Clinical complexity
- Workflow pressure
- Economic pressure
- Trust and governance gap

Slide 5 - Solution:
- Platform thesis
- Workflow thesis
- Evidence thesis

Slide 6 - Product Overview:
- Platform
- Workflow
- Evidence
- Reports or analytics surface

Slide 7 - Technology:
- Multimodality rationale
- Human-centered AI positioning
- Model and workflow evidence boundary

Slide 8 - Evidence Foundation:
- Supported research and documentation
- Not established claims
- Investor implication

Slide 9 - Market Opportunity:
- Qualitative opportunity framing
- No unsupported TAM, pricing, customer, or valuation claim

Slide 10 - Business Model:
- Current evidence status
- Plausible future categories clearly marked as strategy
- No unsupported revenue forecast

Slide 11 - Partnerships and Ecosystem:
- Only confirmed partnerships or funding ecosystem signals
- Do not imply unconfirmed partner commitments

Slide 12 - Financial Highlights:
- FY2024, FY2025, and interim FY2026 figures when relevant
- Charts and metric cards
- Cash and working-capital context

Slide 13 - Risks:
- Financial risks
- Funding timing risks
- Commercial proof risks
- Clinical or regulatory evidence gaps

Slide 14 - Growth Strategy and Outlook:
- Next supported priorities
- Evidence needed next
- Diligence roadmap
```

Layout notes:

- Use 16:9 landscape format.
- Keep slides editable in PPTX when a deck is requested.
- Use large titles, clear cards, and limited text.
- Use charts only when labels remain readable.
- Include a companion PDF for `reports.html` access when appropriate.
- Keep the editable PPTX as the source design asset when a presentation is created.

## Template 3 - IR Letters

Use this template for founder-style investor communications explaining a reporting period.

Recommended filename pattern:

```text
breastscreeningai_ir_letter_[year].pdf
```

Recommended structure:

```markdown
Document type:
Investor Relations Letter

Opening:
- Address investors and stakeholders
- State the reporting period
- Summarize the period in one clear paragraph

Core Figures:
- Metric cards for the most important supported financial figures

What Occurred During the Period:
- Supported financial events
- Supported operational context
- Comparison with prior period when supported

Why It Matters:
- Investor relevance
- Strategic meaning
- Evidence boundary

Challenges and Management Response:
- Working-capital issues
- Revenue maturity
- Funding dependency
- Management response based on actual decisions or conservative interpretation

Subsequent Events:
- Include only dated, supported subsequent events
- EIC Pre-Accelerator status may be included only with unresolved payment details clearly marked

Priorities Ahead:
- Source-backed or clearly stated execution priorities
- No unsupported forecasts

Evidence Gaps:
- Audit status
- Cash-flow statement availability
- Commercial proof
- Regulatory status
- Payment schedule

Closing:
- Management signature line
```

Layout notes:

- Use A4 portrait.
- Keep a polished letter feel, not a dense report.
- Use paragraphs supported by a small number of cards or tables.
- Use transparent language for gaps and risks.

## Template 4 - IR News and Notice

Use this template for investor-facing announcements, financial notices, and material source-backed updates.

Recommended filename patterns:

```text
breastscreeningai_ir_news_[event]_[year].pdf
breastscreeningai_ir_notice_[event]_[year].pdf
```

Recommended structure:

```markdown
Document type:
IR News Release or Investor Notice

Headline:
- Clear event title
- Avoid promotional exaggeration

Summary:
- One short paragraph describing the event
- Include date, period, or reporting basis

Event Details:
- Reporting period or event date
- Related document or source
- Currency, if financial
- Program, proposal, or grant identifier, if funding-related

Key Figures:
- Metric cards only when source-backed
- Avoid estimates unless clearly labeled as estimates

Detailed Announcement:
- What happened
- Why it matters
- What remains pending

Investor Relevance:
- Diligence importance
- Strategic or financial implication
- No unsupported forward-looking claims

Source Basis:
- Human-readable source description
- Do not expose private local file paths

Information Not Established:
- Missing payment schedule
- Missing audit or statutory filing details
- Missing customer or regulatory confirmation
- Any other material limitation
```

Layout notes:

- Use A4 portrait.
- Keep the document concise, usually one to two pages.
- Use metric cards near the top for clarity.
- For notices, keep tone factual and restrained.
- For news releases, use stronger narrative but remain source-backed.

## Template Maintenance Rules

- Update this file when a recurring report layout decision changes.
- Do not remove older template logic unless the user explicitly requests it.
- If a new template category is needed, append it as a new section.
- If a template changes materially, update `PROMPT_RULES.md` with a new version.
- If a design update is requested for one report family, check whether the same design change should be applied to all report templates and active report assets.
- Future report assets should follow the latest rules in both this file and `PROMPT_RULES.md`.

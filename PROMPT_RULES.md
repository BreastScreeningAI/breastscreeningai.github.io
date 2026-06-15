# BreastScreening-AI Prompt Rules and Templates

This file defines the working rules, evidence standards, and reusable prompt templates for BreastScreening-AI website, documentation, evidence, financial reporting, investor relations, and communications work.

Future prompts should explicitly instruct the assistant to read and follow this file before making changes:

```text
Before answering or editing files, read and follow PROMPT_RULES.md. Use the latest rule version as authoritative. Preserve older rule versions and append any new rules under a new version header.
```

## Rule Precedence

1. The most recent version section in **Versioned Rules** is authoritative.
2. Older versions must remain in the file for traceability.
3. When adding new rules, do not rewrite or delete older version sections.
4. Add a new version header with the date, reason for change, and updated rules.
5. If rules conflict, follow the newest dated rule unless the user gives a direct instruction in the current prompt.
6. Current prompt instructions override this file only for the current task, unless the user explicitly asks to update this file.

## Update Protocol

When updating this file:

1. Add a new section under **Versioned Rules**.
2. Use this header format:

```markdown
### vYYYY.MM.DD.N - Short Title
Timestamp: YYYY-MM-DD HH:MM:SS TZ (UTC offset)
Reason: Brief reason for the update.
Status: [Current or Superseded]
```

3. Change the previous latest section status from `Current` to `Superseded`.
4. Do not remove prior versions.
5. Update only the new version header and the new rules being added.
6. Keep templates stable unless the user specifically asks to update them.

## Versioned Rules

### v2026.06.15.1 - Initial Project Rules
Date: 2026-06-15
Reason: Establish durable project instructions, evidence standards, and reusable templates.
Status: Superseded

#### Core Working Rules

- Act as a proactive project collaborator: diagnose, implement, verify, and summarize.
- Before making website or document changes, inspect the relevant files and reuse existing structure, naming, style, and footer/header conventions.
- Keep edits scoped to the requested pages or assets.
- Do not revert unrelated user changes.
- Use concise, professional public-facing language.
- Avoid unsupported claims, especially in medical, clinical, regulatory, financial, investor, commercial, and partnership contexts.
- Clearly distinguish confirmed facts, reasonable interpretations, assumptions, and missing information.
- Prefer source-backed wording over promotional wording.
- Do not say or imply that reports, letters, notices, financial statements, presentations, or public communication assets were AI-generated.
- Avoid phrases the user has rejected, including `without investor-sensitive detail`.

#### Website Information Architecture

- `index.html` is the main site entry page.
- `platform.html` should be business-oriented: platform value, market logic, multimodality rationale, operational/economic relevance.
- `workflow.html` should be clinical workflow-oriented: process impact, modality roles, clinical operations, adoption, governance.
- `evidence.html` should represent overall evidence across research, validation, and future clinical pilots.
- `voucher.html` should preserve Startup Voucher material and link from evidence where relevant.
- `reports.html` should be `IR & Financials`, focused on Annual Financial Statements, IR Presentations, IR Letters, and IR News & Notice.
- `publications.html` should be curated to project-relevant publications, theses, patents, and related scientific assets.
- `news.html` should use low-maintenance sources only with editorial control.
- `media.html` should hold brand/media assets.
- `faq.html` should answer common stakeholder, support, clinical, company, and investor questions.

#### Footer Rules

Use the product-journey footer logic unless the user asks otherwise:

- Business: Platform, Workflow, Analytics, Insights
- Support: Documentation, Live, Contact, FAQs
- Company: About, Story, Careers, Reports
- Legal: Terms, Privacy, Cookies, Disclaimer
- Explore: Evidence, Publications, News, Media

Secondary pages should share the same footer/header behavior where practical:

- `evidence.html`
- `faq.html`
- `media.html`
- `news.html`
- `platform.html`
- `publications.html`
- `reports.html`
- `story.html`
- `voucher.html`
- `workflow.html`

#### Claims and Evidence Rules

- Use `CLAIMS_REGISTER.md` as the evidence and claims control reference when public pages include quantified or sensitive claims.
- Do not invent clinical performance, customers, pilots, regulatory status, partnerships, commercial revenue, valuation, or market metrics.
- For clinical and economic claims, state whether the claim is directly supported, inferred, assumed, or missing evidence.
- For investor materials, use only supported financial figures and dated events.
- When evidence is incomplete, present the gap as a next diligence or execution item.

#### Financial and Investor Relations Rules

- `reports.html` assets should be realistic, professional, investor-facing, and source-backed.
- Annual Financial Statements should summarize financial position and performance for a fiscal period.
- IR Presentations should present investor narrative, business context, evidence, financial highlights, risks, and outlook.
- IR Letters should be founder-style communications explaining what happened, why it matters, challenges, management response, and priorities ahead.
- IR News & Notice should cover material source-backed reporting, funding, or company communication events.
- Use real dates and data from uploaded/source files.
- Do not invent revenues, customers, signed contracts, valuations, funding rounds, regulatory clearances, or partnerships.
- If final payment schedules, audit reports, cash-flow statements, or statutory filings are unavailable, say so clearly.
- EIC Pre-Accelerator source-backed facts currently established:
  - Expected amount: up to EUR 500,000.
  - Proposal: Horizon Europe Lump Sum Grant proposal 101310071.
  - Duration: 18 months.
  - Grant Agreement ready for signature: 10 June 2026.
  - Coordinator signature: 12 June 2026.
  - EU services signature, final payment schedule, pre-financing percentage, and exact payment date were not confirmed in the available source set.

#### Current Supported Financial Figures

FY2024:

- Total assets: EUR 1,123.38.
- Cash and deposits: EUR 721.34.
- Equity: EUR -611.69.
- Liabilities: EUR 1,735.07.
- Subsidies: EUR 1,796.63.
- Net result: EUR -711.69.

FY2025:

- Total assets: EUR 12,458.22.
- Equity: EUR 3,510.80.
- Liabilities: EUR 8,947.42.
- Cash and deposits: EUR 3,856.90.
- Subsidies: EUR 24,500.00.
- Sales and services: EUR 100.00.
- Other income: EUR 3,000.00.
- External services: EUR 17,760.11.
- Personnel expenses: EUR 5,852.31.
- Supplier liabilities: EUR 7,227.74.
- Net result: EUR 1,122.49.

Interim FY2026, dated 28 February 2026:

- Total assets: EUR 7,476.39.
- Cash and deposits: EUR 258.30.
- Equity: EUR -1,064.88.
- Liabilities: EUR 8,541.27.
- Supplier liabilities: EUR 7,866.32.
- Net result: EUR -4,575.68.

#### Canonical and URL Rules

- Avoid canonical URLs when possible.
- When canonical URLs are needed, prefer `breastscreeningai.github.io`.
- Avoid unnecessary date-stamp copy such as `Updated 15 June 2026` unless the user specifically requests it or the page needs a formal publication date.

#### Asset Generation Rules

- PDFs should be visually checked when layout matters.
- Presentations should be editable PPTX when requested as decks; companion PDFs may be generated for website access.
- Keep public filenames descriptive and stable.
- Do not leave temporary build artifacts in public folders.
- Do not expose private local source paths in public-facing assets.

### v2026.06.15.2 - Interaction and Writing Style Rules
Date: 2026-06-15
Reason: Add durable instructions for interactive Agentic AI behavior and user-preferred writing style.
Status: Superseded

#### Inherited Rules

- Follow all rules from `v2026.06.15.1` unless a newer rule in this section supersedes them.
- When new recurring rules appear in the conversation, append them as a new version section in this file.
- Preserve older rules for traceability.
- Treat the most recent version section as authoritative for future work.

#### Agentic Interaction Rules

- Act as an interactive Agentic AI assistant throughout this project.
- Deliver thorough, rigorous, and context-aware responses.
- Avoid generic, superficial, or template-like replies.
- Ground answers in the current project context, uploaded/source files, prior decisions, and user objectives.
- Provide precise, high-quality insights that demonstrate careful reasoning and intellectual depth.
- Anticipate likely follow-up needs, risks, missing information, and dependencies.
- Ask clarifying questions when necessary, especially when the missing information cannot be discovered from the workspace and a reasonable assumption would risk an incorrect or unsupported result.
- Propose refinements proactively when they improve quality, consistency, evidence strength, usability, investor readiness, clinical credibility, or public communication.
- Maintain internal consistency across pages, reports, assets, claims, and prior decisions.
- When the user asks for execution and implementation is feasible, proceed through inspection, implementation, verification, and concise handoff.

#### Writing Style Rules

- Tailor the writing style to the specific context and intended audience.
- Maintain a human tone that is clear, coherent, constructive, and professional.
- Avoid overly formal, robotic, generic, or formulaic language.
- Use complete, uncontracted forms of expressions. Do not use contractions.
- Use straight quotation marks (`"`) instead of curly quotation marks.
- Use straight apostrophes (`'`) instead of curly apostrophes.
- Disable smart punctuation for compatibility with plain text, code, and technical systems.
- Do not use the em dash character.
- Do not start a sentence with the word `By`.
- Try not to start sentences with the words `This` or `These`.
- Avoid formulaic transitions such as `Moreover` and `In conclusion`.
- Prefer several well-developed paragraphs for prose-oriented answers.
- Avoid bullet points or numbering unless structure is necessary for clarity, implementation summaries, verification reports, or technical instructions.
- Vary sentence length and structure to make the prose feel natural.
- Use context-specific phrasing where appropriate.
- Keep responses professional, focused, and useful.

### v2026.06.15.3 - Language and Markdown Delivery Rules
Date: 2026-06-15
Reason: Add durable language-selection and Markdown packaging rules for reusable materials.
Status: Superseded

#### Inherited Rules

- Follow all rules from `v2026.06.15.1` and `v2026.06.15.2` unless a newer rule in this section supersedes them.
- When new recurring rules appear in the conversation, append them as a new version section in this file.
- Preserve older rules for traceability.
- Treat the most recent version section as authoritative for future work.

#### Language Rules

- Always write in English unless the user explicitly asks for another language.
- When the user asks for Portuguese, always write in Portuguese from Portugal.
- Keep explanatory surrounding text in English unless the user explicitly requests otherwise.
- If a deliverable itself must be in another language, keep any brief implementation notes or handoff explanation in English unless instructed otherwise.

#### Markdown Delivery Rules

- Encapsulate reusable materials in Markdown when they are intended to be copied, reused, sent as messages, included in documents, or transferred elsewhere.
- Use plain-text Markdown notation.
- Keep Markdown clean, portable, and compatible with technical systems.
- Do not over-format ordinary explanations that are not intended as reusable material.
- Continue to follow the writing-style rules from `v2026.06.15.2` inside Markdown deliverables.

### v2026.06.15.4 - Reports PDF Template Rules
Date: 2026-06-15
Reason: Add durable layout and content rules for `reports.html` PDF assets.
Status: Superseded

#### Inherited Rules

- Follow all rules from `v2026.06.15.1`, `v2026.06.15.2`, and `v2026.06.15.3` unless a newer rule in this section supersedes them.
- When new recurring rules appear in the conversation, append them as a new version section in this file.
- Preserve older rules for traceability.
- Treat the most recent version section as authoritative for future work.

#### Reports PDF Template Rules

- Before creating or updating any PDF asset linked from `reports.html`, read and follow `media/reports/governance/REPORT_PDF_TEMPLATES.md`.
- Apply the appropriate template category: Annual Financial Statements, IR Presentations, IR Letters, or IR News and Notice.
- Keep all report assets source-backed and investor-appropriate.
- Use stable descriptive filenames under `media/reports`.
- If a report layout decision changes materially, update `media/reports/governance/REPORT_PDF_TEMPLATES.md`.
- If the new layout decision is recurring, append a new version section to this file.
- Do not remove older rules or template logic unless the user explicitly requests it.
- Continue to verify report PDFs visually and technically before delivery.

### v2026.06.15.5 - Reports PDF and PPTX Template Asset Rules
Date: 2026-06-15
Reason: Add durable paired PDF and PPTX template asset rules for all `reports.html` report families.
Status: Superseded

#### Inherited Rules

- Follow all rules from `v2026.06.15.1`, `v2026.06.15.2`, `v2026.06.15.3`, and `v2026.06.15.4` unless a newer rule in this section supersedes them.
- When new recurring rules appear in the conversation, append them as a new version section in this file.
- Preserve older rules for traceability.
- Treat the most recent version section as authoritative for future work.

#### Reports Template Asset Rules

- Before creating or updating any PDF or PPTX asset linked from `reports.html`, read and follow `media/reports/governance/REPORT_PDF_TEMPLATES.md`.
- Maintain paired template assets for the four report families whenever practical: Annual Financial Statements, IR Presentations, IR Letters, and IR News and Notice.
- Store reusable report templates under `media/reports/templates`.
- Keep template designs visually aligned across report families, using the shared BreastScreening-AI navy, blue, soft blue, teal, and amber design system.
- When a report design system update is requested, update both the template files and the active non-template report assets that use the older design, unless the user explicitly asks for a narrower update.
- If a template design decision changes materially, update `media/reports/governance/REPORT_PDF_TEMPLATES.md`.
- If the design decision is recurring, append a new version section to this file.
- Verify generated PDFs and PPTX files technically, and visually inspect rendered previews before delivery.

### v2026.06.15.6 - Report Asset Audit and Improvement Rules
Date: 2026-06-15
Reason: Make visual audit, page-size verification, metadata checks, and paired PDF/PPTX improvement mandatory for generated report assets.
Status: Superseded

#### Inherited Rules

- Follow all rules from `v2026.06.15.1`, `v2026.06.15.2`, `v2026.06.15.3`, `v2026.06.15.4`, and `v2026.06.15.5` unless a newer rule in this section supersedes them.
- When new recurring rules appear in the conversation, append them as a new version section in this file.
- Preserve older rules for traceability.
- Treat the most recent version section as authoritative for future work.

#### Report Asset Audit Rules

- Before accepting generated report PDFs as final, render the pages to images and inspect a contact sheet or representative full-size pages for readability, spacing, hierarchy, clipped text, overlapping tables, broken charts, and poor contrast.
- Verify PDF metadata, page count, and page size. Use A4 for document reports and letters, and 16:9 landscape for presentation companion PDFs unless a source file requires another format.
- When improving template PDFs, update the matching editable PPTX templates at the same time so the PDF preview and editable source remain aligned.
- Remove temporary inspect files, Office lock files, and other sidecar artifacts from public report asset folders before delivery.
- Prefer readable card-based financial and disclosure blocks over dense tables when the available figures are placeholders or when table text would become too small.
- Treat report template PDFs as visual preview companions when they are rendered from PPTX files. Use the PPTX as the editable source unless the user requests a text-searchable PDF template.
- Keep public wording conservative and source-backed. Do not include process language such as "generated", and do not include rejected phrasing such as `without investor-sensitive detail`.

### v2026.06.15.7 - Report Format Selection and Word Template Rules
Date: 2026-06-15
Reason: Add durable rules for choosing PDF, PPTX, Word, or combinations for `reports.html` assets.
Status: Superseded

#### Inherited Rules

- Follow all rules from `v2026.06.15.1`, `v2026.06.15.2`, `v2026.06.15.3`, `v2026.06.15.4`, `v2026.06.15.5`, and `v2026.06.15.6` unless a newer rule in this section supersedes them.
- When new recurring rules appear in the conversation, append them as a new version section in this file.
- Preserve older rules for traceability.
- Treat the most recent version section as authoritative for future work.

#### Report Format Selection Rules

- Before creating or updating report PDFs, PPTX files, or Word files linked from `reports.html`, read and follow `media/reports/governance/REPORT_PDF_TEMPLATES.md`.
- Use PDF for public access, website downloads, archive copies, and investor-facing documents that should not be casually edited.
- Use PPTX when the asset is a slide deck, pitch deck, IR presentation, board-style visual narrative, or chart-heavy document where layout, slide rhythm, and presentation flow matter.
- Use Word when the asset is a narrative document, letter, report, announcement, notice, financial statement access copy, or review draft where prose editing, tracked changes, comments, and longer-form paragraphs matter.
- Use PDF and PPTX for IR Presentations.
- Use PDF and Word for Annual Financial Statements, IR Letters, and IR News and Notice documents.
- Use PDF, PPTX, and Word together only when a document must function as a public access copy, an editable narrative document, and a slide-based communication.
- Keep template designs visually aligned across PDF, PPTX, and Word assets by using the same BreastScreening-AI navy, blue, soft blue, teal, amber, spacing, and evidence-boundary logic.
- When the report design system changes, update template files and active non-template report assets that use the old design, unless the user explicitly asks for a narrower update.
- Render and visually inspect Word templates before delivery when document rendering is available.

### v2026.06.15.8 - Full-Thread Rule Continuity
Date: 2026-06-15
Reason: Confirm that future interactions must consistently follow the latest rules together with all compatible prior rules established throughout the chat thread.
Status: Superseded

#### Inherited Rules

- Follow all rules from `v2026.06.15.1` through `v2026.06.15.7` unless a newer rule in this section explicitly supersedes a specific instruction.
- Preserve every older version for traceability and never silently remove established rules, decisions, terminology, evidence boundaries, or stylistic preferences.
- Treat the most recent version section as authoritative while retaining all compatible requirements from previous versions.

#### Continuity and Update Rules

- Before answering, analyzing, editing files, or creating assets, review the relevant full-thread context and the latest version of this file.
- Apply earlier decisions, source hierarchies, claim restrictions, naming conventions, design systems, templates, and verification requirements whenever they affect the current task.
- Do not treat prompts as isolated requests when prior context materially changes their interpretation or implementation.
- When a new recurring instruction appears, append a new version section, mark the previous current version as `Superseded`, and preserve all older content.
- When instructions conflict, follow the newest applicable user instruction unless it conflicts with a higher-priority system or developer instruction. Explicitly identify material ambiguities or unresolved conflicts.
- Maintain source-backed distinctions between confirmed facts, interpretations, assumptions, projections, and missing information.
- Continue following the established English-language, punctuation, professional-tone, evidence, website, document, financial-reporting, investor-relations, and visual-quality rules throughout this thread.
- Verify that each final response and completed artifact reflects the newest request without losing relevant earlier requirements.

### v2026.06.15.9 - Precise Rule Timestamps
Timestamp: 2026-06-15 13:59:50 WEST (+0100)
Reason: Require hours, minutes, seconds, timezone, and UTC offset in all future rule-version timestamps.
Status: Superseded by v2026.06.15.10

#### Inherited Rules

- Follow all rules from `v2026.06.15.1` through `v2026.06.15.8` unless a newer rule explicitly supersedes a specific instruction.
- Preserve older rule entries and their original date fields without retroactively inventing times that were not recorded.
- Treat the most recent version section as authoritative while retaining all compatible previous requirements.

#### Timestamp Rules

- Every new version entry must include a `Timestamp` field containing the full local date and time with hours, minutes, seconds, timezone abbreviation, and numeric UTC offset.
- Use the format `YYYY-MM-DD HH:MM:SS TZ (+HHMM)` or `YYYY-MM-DD HH:MM:SS TZ (-HHMM)`.
- Obtain the timestamp from the current execution environment when updating this file rather than estimating it.
- Apply the same full timestamp precision to future project logs, audit records, source-register reviews, and generated asset metadata when a timestamp is required.
- When only a historical date is known, preserve the date and explicitly state that the time is unknown rather than assigning an unsupported time.
- Continue following the full-thread continuity requirements and all compatible previous rules.

### v2026.06.15.10 - Publication Governance and Quality Gates
Timestamp: 2026-06-15 14:01:15 WEST (+0100)
Reason: Add consistent provenance, approval, confidentiality, freshness, accessibility, and publication controls across the website, evidence materials, news, and investor communications.
Status: Superseded by v2026.06.15.11

#### Inherited Rules

- Follow every compatible rule from `v2026.06.15.1` through `v2026.06.15.9`.
- Treat this version as authoritative where an earlier rule conflicts with it.
- Preserve previous versions and append future changes with a complete timestamp, including timezone and UTC offset.

#### Source and Document Control

- Trace every material public claim to a primary source, `CLAIMS_REGISTER.md`, or `media/reports/governance/REPORT_SOURCE_REGISTER.md`.
- Record the source, evidence status, owner, approval status, review timestamp, visibility classification, and supersession status when maintaining governed claims or documents.
- Prefer signed financial records, executed agreements, final publications, and official institutional notices over proposals, pitch decks, drafts, or secondary summaries.
- Preserve qualifiers, denominators, study populations, dates, and uncertainty. Never combine figures from different studies as if they described one cohort.
- Label assets as `Public`, `Internal`, `Controlled`, `Draft`, or `Superseded`. Editable DOCX and PPTX files remain internal unless explicitly approved for publication.

#### Publication and Approval Gates

- Require responsible-owner approval before publishing material financial, clinical, regulatory, funding, partnership, or leadership claims.
- Never silently promote a `Conditional`, `Hold`, `Draft`, or unsupported claim to confirmed status.
- Separate verified facts from interpretations, scenarios, assumptions, estimates, and missing information in narrative and visual content.
- Never expose patient data, personal identifiers, private correspondence, bank or tax identifiers, confidential partner information, private filesystem paths, or document metadata in public assets.
- Maintain one clearly identified public asset for each purpose and reporting period. Label or archive obsolete, duplicate, placeholder, and superseded assets rather than reusing them without explanation.

#### Timeliness and Review

- Verify time-sensitive claims before publication, especially funding, payment timing, leadership, partnerships, regulation, financial position, news, contact details, and external links.
- Use a full timestamp for reviews and approvals. Never invent hours, minutes, or seconds for historical events when the source provides only a date.
- Avoid words such as `latest`, `current`, `today`, or `recent` unless the information has been checked against an authoritative source at the time of writing.
- Assign a future review date to time-sensitive public content and reassess it when new evidence supersedes the existing record.

#### Accessibility and Verification

- Use semantic HTML, keyboard-accessible controls, descriptive link text, sufficient contrast, meaningful alternative text, and correctly marked table headers.
- Give every material chart or diagram a readable title, units, source, assumptions, and a text or table alternative where practical.
- Verify active links, responsive layouts, headings, downloads, document readability, and consistency across shared headers, footers, templates, and published assets after changes.
- Audit PDFs, DOCX files, and PPTX files visually and structurally before publication. Correct clipping, overflow, low contrast, unreadable tables, inconsistent pagination, and missing source notes.

#### News and External Coverage

- Distinguish company announcements, institutional coverage, independent media, research updates, and discovery-feed candidates.
- Record the event date, publication date, publisher, original source, relevance, duplicate status, and editorial approval for each news item.
- Treat RSS feeds and Google News as discovery mechanisms, not automatic publication authorities. Publish only after relevance, source quality, duplication, and factual accuracy have been reviewed.

#### Change Management

- Inventory every affected template, active asset, page, navigation element, and cross-reference before applying a shared design or information-architecture change.
- Apply approved design-system changes consistently to templates and active non-template assets, then verify all affected outputs.
- Update the rules when a new durable requirement emerges. Do not add one-off task details unless they establish a reusable standard.

### v2026.06.15.11 - Primary Source Citation Only
Timestamp: 2026-06-15 14:37:09 WEST (+0100)
Reason: Prohibit circular, self-referential, and distribution-page citations in investor and public communication assets.
Status: Superseded by v2026.06.15.12

#### Inherited Rules

- Follow every compatible rule from `v2026.06.15.1` through `v2026.06.15.10`.
- Treat this version as authoritative where an earlier rule conflicts with it.

#### Source Citation Rules

- Cite the underlying primary or controlling evidence in every source-basis section.
- Never cite `reports.html`, another website listing page, the asset itself, or an access copy as evidence supporting the asset's claims.
- Avoid circular wording such as `annual financial statement access copy listed on reports.html` and equivalent formulations.
- Use signed accounting records, executed agreements, official notices, final publications, approved corporate records, or clearly identified source documents instead.
- A website page may be mentioned only as a distribution location outside the source-basis section when that information is operationally necessary.

### v2026.06.15.12 - Public Source Description Rules
Timestamp: 2026-06-15 14:39:11 WEST (+0100)
Reason: Prevent internal filenames, extensions, paths, and repository-oriented identifiers from appearing in public source descriptions.
Status: Superseded by v2026.06.15.13

#### Inherited Rules

- Follow every compatible rule from `v2026.06.15.1` through `v2026.06.15.11`.
- Treat this version as authoritative where an earlier rule conflicts with it.

#### Public Source Wording

- Use natural, reader-facing descriptions in public source-basis sections.
- Never expose internal filenames, file extensions, folder structures, local paths, repository paths, version suffixes, or working-document identifiers in public assets.
- Avoid wording such as `BreastScreeningAI_Press_Release_PR0001.docx` and equivalent internal document references.
- Refer to evidence by its public meaning, issuer, document type, reporting period, and date where relevant, for example `Company announcement dated 27 April 2026`.
- Internal registers may retain exact filenames and paths when required for controlled audit traceability, but that wording must not be copied into public communications.


### v2026.06.15.13 - Reports Asset Retention and Cleanup Rules
Timestamp: 2026-06-15 16:34:58 WEST (+0100)
Reason: Add durable guidance for deciding whether files associated with `reports.html` should be kept, moved, archived, or removed.
Status: Superseded by v2026.06.15.14

#### Inherited Rules

- Follow every compatible rule from `v2026.06.15.1` through `v2026.06.15.12`.
- Treat this version as authoritative where an earlier rule conflicts with it.

#### Reports Asset Retention Rules

- Never remove files linked from `reports.html` unless the page is updated in the same change and all replacement links are verified.
- Keep public `media/reports` assets limited to files intended for website access, preferably final public PDFs with stable descriptive filenames.
- Keep `REPORT_SOURCE_REGISTER.md`, `REPORT_PDF_TEMPLATES.md`, and approved template files because they support provenance, repeatability, review, and future asset generation.
- Keep editable DOCX, PPTX, and source files when they are needed for future revisions, but prefer moving them to a clearly marked internal or template folder rather than exposing them as public-facing archive clutter.
- Remove or archive `.DS_Store`, temporary build outputs, stale placeholders, superseded drafts, duplicate access copies, and older summary files when they are not linked, not part of the source register, and not needed for audit traceability.
- Before deleting any report-related asset, inventory all references from `reports.html`, source registers, templates, scripts, and related documentation.
- Prefer archiving over deletion when a file may contain source-backed financial, investor, legal, grant, or governance context.
- After cleanup, verify that all `reports.html` links resolve and that no public page references removed files.

### v2026.06.15.14 - Reports Folder Structure Rules
Timestamp: 2026-06-15 19:52:17 WEST (+0100)
Reason: Move report Markdown governance files into a dedicated folder and require future generated report assets to be placed under a generated-assets folder.
Status: Superseded by v2026.06.15.15

#### Inherited Rules

- Follow every compatible rule from `v2026.06.15.1` through `v2026.06.15.13`.
- Treat this version as authoritative where an earlier rule conflicts with it.

#### Reports Folder Structure

- Store report governance Markdown files under `media/reports/governance/`.
- Store public generated report assets under `media/reports/generated/`.
- Keep reusable report templates under `media/reports/templates/`.
- Future generated PDFs, DOCX files, PPTX files, and related public report assets for `reports.html` should be written to `media/reports/generated/` unless the user explicitly asks for a different folder.
- Update `reports.html` links whenever generated report assets move folder.
- Update scripts and registers so they reference the folder structure actually used.
- Before generating or relinking report assets, inventory `media/reports`, identify missing files, and avoid assuming deleted files still exist.
- After generation, verify that every `reports.html` link resolves against the new generated-assets folder.

### v2026.06.15.15 - Media Folder Organization and System Ignore Rules
Timestamp: 2026-06-15 19:57:35 WEST (+0100)
Reason: Require root-level `media` PDFs to be organized by purpose and keep operating-system/editor artifacts out of version control.
Status: Superseded by v2026.06.15.16

#### Inherited Rules

- Follow every compatible rule from `v2026.06.15.1` through `v2026.06.15.14`.
- Treat this version as authoritative where an earlier rule conflicts with it.

#### Media Folder Organization

- Do not keep public PDF assets directly under `media/` unless there is a specific reason approved by the user.
- Store legal PDFs under `media/legal/`.
- Store investor-facing pitch or fundraising PDFs under `media/investor/`.
- Store scientific, research, publication, evidence-summary, and award/research-background PDFs under `media/research/`, unless they belong to a more specific page folder.
- Store report assets under the report structure defined in `v2026.06.15.14`: `media/reports/generated/`, `media/reports/governance/`, and `media/reports/templates/`.
- When moving media files, update every site, wiki, README, claims, rules, and data reference in the same change.
- After moving media files, verify that all internal PDF links resolve and that no public page references a deleted or old root-level path.

#### Ignore Rules

- Keep macOS, Windows, Linux, editor, temporary, and Office lock artifacts out of version control.
- Update `.gitignore` whenever a recurring local artifact appears, especially `.DS_Store`, AppleDouble files, Spotlight metadata, thumbnail databases, Office lock files, swap files, and local IDE metadata.

### v2026.06.15.16 - Media Text and Markdown Folder Rules
Timestamp: 2026-06-15 20:00:37 WEST (+0100)
Reason: Extend media organization rules to root-level Markdown and text files and require full path audits after file moves.
Status: Current

#### Inherited Rules

- Follow every compatible rule from `v2026.06.15.1` through `v2026.06.15.15`.
- Treat this version as authoritative where an earlier rule conflicts with it.

#### Media Text and Markdown Organization

- Do not keep public Markdown or text assets directly under `media/` unless the user explicitly approves an exception.
- Store public brand Markdown assets under `media/brand/`.
- Store press boilerplates, press copy, and media text snippets under `media/press/`.
- Store report governance Markdown under `media/reports/governance/`.
- Store future public text or Markdown assets in a purpose-specific folder that matches the audience and use case, such as `media/brand/`, `media/press/`, `media/legal/`, `media/investor/`, `media/research/`, or a page-specific folder.
- When moving Markdown, text, PDF, DOCX, PPTX, image, or data assets, update all references across HTML, Markdown, JSON, JavaScript, CSS, scripts, claims registers, source registers, prompt rules, and documentation.
- After moving assets, run a path audit that checks local `href`, `src`, `download`, Markdown links, JSON references, and script references for missing files or stale root-level paths.

## Prompt Templates

Use these templates as starting points. Each template assumes the assistant must follow the latest versioned rules in this file.

### Template 1 - Website Page Update

```text
Before answering or editing files, read and follow PROMPT_RULES.md. Use the latest rule version as authoritative.

Task:
Update [PAGE.html] to [GOAL].

Requirements:
- Reuse existing site style, header, footer, and naming conventions.
- Keep claims source-backed and aligned with CLAIMS_REGISTER.md.
- Do not invent clinical, financial, regulatory, customer, or partnership claims.
- Verify the page after editing.
- Summarize changed files and any remaining gaps.
```

### Template 2 - Investor Relations Asset

```text
Before answering or editing files, read and follow PROMPT_RULES.md. Use the latest rule version as authoritative.

Task:
Create a [Annual Financial Statement / IR Presentation / IR Letter / IR News Release / Investor Notice] for [REPORTING PERIOD].

Requirements:
- Use only facts, dates, and figures supported by uploaded/source files.
- Do not invent revenue, customers, partnerships, investments, valuation, regulatory status, or forecasts.
- Distinguish confirmed facts from assumptions and missing information.
- Use professional investor-facing language.
- Create the asset under media/reports with a stable descriptive filename.
- If relevant, update reports.html.
- Verify the asset visually and technically.
```

### Template 3 - Clinical Evidence Synthesis

```text
Before answering or editing files, read and follow PROMPT_RULES.md. Use the latest rule version as authoritative.

Task:
Analyze the uploaded/source materials for clinical evidence and summarize implications for [PAGE / REPORT / STUDY / PRESENTATION].

Requirements:
- Extract supported clinical findings, metrics, methods, populations, limitations, and risks.
- Separate direct evidence, interpretation, assumptions, and missing information.
- Do not overstate patient impact, diagnostic performance, workflow impact, regulatory readiness, or clinical adoption.
- Recommend next evidence, validation, and reporting steps.
```

### Template 4 - Financial Analysis

```text
Before answering or editing files, read and follow PROMPT_RULES.md. Use the latest rule version as authoritative.

Task:
Analyze the uploaded/source financial files for [YEAR / PERIOD / REPORT].

Requirements:
- Extract exact financial figures, dates, and source documents.
- Explain financial meaning, risks, dependencies, and investor implications.
- Do not invent forecasts, valuation, funding rounds, contracts, or revenues.
- Identify missing information such as cash-flow statements, audit opinions, statutory filings, payment schedules, or board-approved KPIs.
- Provide recommendations for investor readiness.
```

### Template 5 - Claims Register Update

```text
Before answering or editing files, read and follow PROMPT_RULES.md. Use the latest rule version as authoritative.

Task:
Update CLAIMS_REGISTER.md for [NEW PAGE / ASSET / CLAIM SET].

Requirements:
- Add only claims that appear in public-facing materials.
- For each claim, include source basis, evidence status, risk level, and recommended wording.
- Mark unsupported or partially supported claims clearly.
- Do not remove old claims unless explicitly requested.
```

### Template 6 - Rules Update

```text
Before answering or editing files, read and follow PROMPT_RULES.md. Use the latest rule version as authoritative.

Task:
Update PROMPT_RULES.md with the following new rules:
[RULES]

Requirements:
- Add a new version section under Versioned Rules.
- Mark the previous current version as Superseded.
- Do not delete older versions.
- Update only the new version header and newly added rules.
- Ensure future prompts follow the most recent rules.
```

## Suggested Prompt Prefix

For future work, paste this at the top of prompts when consistency matters:

```text
Before answering or editing files, read and follow PROMPT_RULES.md. Use the latest rule version as authoritative. If new rules are needed, append a new version section without deleting older versions.
```

# Public Claims Register

Last reviewed: 14 June 2026

This register controls quantitative, clinical, maturity, funding, and relationship claims published by BreastScreening-AI. It covers the discoverable website pages and the downloadable Startup Voucher poster in this repository. Public wording must strengthen, not replace, clinical judgement and must not imply regulatory authorization, clinical efficacy, endorsement, or medical advice.

## Status keys

- **Approved**: supported by an identified public or project source and suitable for the wording below.
- **Conditional**: may be published only with the stated limitations and after the evidence owner confirms the underlying analysis package.
- **Hold**: do not publish until the missing evidence or approval is resolved.
- **Objective**: an intended outcome, not an achieved result.

Named individuals remain to be assigned. Until then, the role in the **Owner** column is accountable for confirmation and approval.

## Quantitative and maturity claims

| ID | Public claim | Public location | Dataset or evidence | Sample and analysis | Owner | Status | Approved public wording / action |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CLM-001 | 45 clinicians from nine institutions | `platform.html`, `voucher.html` | 2022 peer-reviewed study, DOI `10.1016/j.artmed.2022.102285` | Controlled clinician-only versus clinician-AI study; verify the archived analysis and participant-accounting package against the paper | Scientific evidence owner | Approved | "A 2022 peer-reviewed study compared clinician-only and clinician-AI scenarios with 45 clinicians from nine institutions." |
| CLM-002 | 27% fewer false positives | `platform.html`, `voucher.html` | Same study as CLM-001 | Same study; do not combine with Hospital da Luz results | Scientific evidence owner | Approved | "The 2022 study reported a 27% decrease in false positives." |
| CLM-003 | 4% fewer false negatives | `platform.html`, `voucher.html` | Same study as CLM-001 | Same study; do not combine with Hospital da Luz results | Scientific evidence owner | Approved | "The 2022 study reported a 4% decrease in false negatives." |
| CLM-004 | Three minutes shorter diagnosis time | `voucher.html` | Same study as CLM-001 | Same study; confirm the exact endpoint label and unit in the paper and analysis archive | Scientific evidence owner | Approved | "The 2022 study reported a three-minute reduction in time to diagnosis per patient." |
| CLM-005 | 91% positive expectations and satisfaction | `platform.html`, `voucher.html` | Same study as CLM-001 | Same study; preserve the publication's construct and denominator | Scientific evidence owner | Approved | "In the 2022 study, 91% of clinicians reported positive expectations and perceptive satisfaction." |
| CLM-006 | Seven physicians | `voucher.html` | Hospital da Luz pilot records and final April-June 2026 report package | Exploratory integration and usability study | Hospital da Luz study owner | Conditional | "The exploratory Hospital da Luz pilot involved seven physicians." Confirm participant accounting in the final report before the next publication update. |
| CLM-007 | Approximately 11 patients, 23 images, and 110 paired observations | `voucher.html` | Hospital da Luz pilot dataset manifest and analysis notebook | Small exploratory subset; patient count is approximate | Hospital da Luz study owner | Conditional | "The exploratory analysis used approximately 11 patients, 23 images, and 110 paired observations." Archive the de-identified manifest and observation derivation. |
| CLM-008 | +11.82 percentage points in triage-level decision accuracy | `voucher.html` | Hospital da Luz final analysis package | Complementary exploratory triage analysis; BI-RADS remained the primary clinical reference | Hospital da Luz study owner | Conditional | "The exploratory complementary triage analysis observed an 11.82 percentage-point increase in decision accuracy." Always state the small sample and do not present this as clinical efficacy. |
| CLM-009 | 81.82% decision stability | `voucher.html` | Hospital da Luz final analysis package | Descriptive proportion of decisions unchanged with AI assistance | Hospital da Luz study owner | Conditional | "Decision stability was 81.82% in this exploratory sample." Define the numerator and denominator in the final report. |
| CLM-010 | `p = 0.0036` | `voucher.html` | Hospital da Luz statistical output and analysis code | Exploratory complementary triage analysis | Hospital da Luz study owner | Conditional | "The complementary exploratory triage analysis reported p = 0.0036." Publish the test, hypothesis, sidedness, assumptions, and multiplicity treatment with the final report. |
| CLM-011 | Project-level TRL 5 progressing toward TRL 6 | `evidence.html`, `voucher.html` | Internal maturity assessment supported by Hospital da Luz integration/usability evidence | Project interpretation; not external certification, regulatory authorization, or clinical deployment approval | Technology and regulatory evidence owner | Approved | "BreastScreening-AI is at project-level TRL 5 and is progressing toward TRL 6." |
| CLM-012 | Three CHTMAD/ULSTMAD fieldwork periods: 17-21 Nov 2025, 5-9 Jan 2026, and 26-30 Jan 2026 | `voucher.html`, `assets/js/voucher.js` | Fieldwork records, ethics documentation, and visit materials | Activity dates only; quantitative outcomes are not consolidated | CHTMAD study owner | Approved | Publish the dates and research focus. Do not publish quantitative outcomes until the analysis is consolidated and approved. |
| CLM-013 | Startup Voucher investment of EUR 30,000 | Downloadable poster | Approved Startup Voucher operation documentation and poster | Funding amount, not revenue, valuation, or clinical investment | Funding compliance owner | Conditional | Use the approved Portuguese poster wording. Reconcile the amount, operation code, beneficiary, implementation period, and eligible expenditure file with Leyton. |
| CLM-014 | "Top 12 AI Startup" | `index.html` image alternative text | F6S recognition page or dated award evidence | Recognition claim; date and programme are not stated on the website | Communications owner | Hold | Replace or expand only after archiving the dated F6S source and exact award/programme wording. Current image alt text should be treated as unverified public copy. |
| CLM-015 | "100 exams" increases exhaustion and error likelihood | Quoted testimonial in `index.html` | Attributed clinician testimonial | Personal qualitative statement, not a measured project result | Clinical communications owner | Conditional | Keep only as a clearly attributed quotation with documented consent. Do not restate as a general clinical fact without independent evidence. |
| CLM-016 | 14 curated outputs: 12 scholarly outputs and two patent families | `evidence.html` | `assets/data/publications.json`, reviewed 14 June 2026 | Catalogue count; inclusion is based on project relevance | Scientific evidence owner | Approved | State the catalogue date and keep scholarly outputs separate from patent families. |
| CLM-017 | 135 reported study participations | `evidence.html` | Reported cohorts of 31, 45, 52 and seven | Arithmetic sum; cohorts may overlap and are not deduplicated unique clinicians | Scientific evidence owner | Conditional | Use "study participations," never "135 unique clinicians." |
| CLM-018 | 25+ hospitals engaged | `evidence.html` | Internal business-development and engagement register; Winter 2026 business presentation | Traction figure spanning conversations, research engagement and collaboration activity; not 25 clinical validation sites or customers | Business development owner | Conditional | Use "25+ hospitals engaged" and state that the figure does not represent completed clinical validations, customers or endorsements. Reconcile against a deduplicated engagement register before the next review. |

## Funding, activity, and relationship claims

| ID | Public claim | Public location | Required source | Owner | Status | Approved public wording / action |
| --- | --- | --- | --- | --- | --- | --- |
| REL-001 | Startup Voucher / PRR / EU financial support | `index.html`, `evidence.html`, `wiki-home.md`, poster | Grant/operation documentation and communication rules | Funding compliance owner | Conditional | State that the operation benefits from PRR and EU financial support through Startup Voucher. Add the formal beneficiary, operation title/code, period, support amount, objectives, results, and indicators once confirmed. |
| REL-002 | Hospital da Luz workflow integration through Siemens syngo.via Frontier/OpenApps | `evidence.html` | Pilot protocol, access/integration records, and final report | Hospital da Luz study owner | Conditional | Describe the environment and integration activity without implying endorsement by Hospital da Luz or Siemens. |
| REL-003 | CHTMAD/ULSTMAD anonymized, ethics-approved research | `evidence.html` | Ethics approval, data-handling protocol, and fieldwork records | CHTMAD study owner | Conditional | "Research activities used anonymized cases under an ethics-approved protocol." Confirm the exact institution name and approval reference before adding them publicly. |
| REL-004 | Collaborator and provider roles | `evidence.html` | Executed engagement records, proposals, invoices, or written confirmations | Corporate/legal owner | Conditional | Use only the scoped role descriptions approved for SNAP, Leyton, SAVEAS, KGSA, Complear, and AAVANZ. Do not imply clinical endorsement or a broader contractual relationship. |
| REL-005 | Logos presented as partnerships or collaborations | `index.html` | Contract, memorandum, grant record, or written publication approval for each logo | Corporate/legal owner | Hold | Audit UPMC, Siemens, AWS, HFF, IPO Lisboa, CHTMAD, and Amigas do Peito individually. Rename headings or remove logos where the documented relationship does not support "partner" or "collaboration." |

## Claims not approved for public reuse

The following claims require reconciliation against source datasets and written approval before publication:

- More than 15,000 cases or any other dataset-size claim taken from an EIC proposal.
- Major performance improvements stated in proposals but not supported by the approved evidence packages above.
- Quantitative CHTMAD/ULSTMAD outcomes before consolidated analysis.
- Statements that the software diagnoses cancer, eradicates medical errors, replaces clinicians, is clinically authorized, is regulatory certified, or provides medical advice.
- A completed TRL 6 claim. The approved maturity statement is project-level TRL 5 progressing toward TRL 6.

## Evidence package checklist

Each quantitative claim should have one archived package containing:

1. A frozen, de-identified dataset manifest and version or checksum.
2. The protocol, endpoint definitions, inclusion/exclusion rules, and denominator derivation.
3. Reproducible analysis code or notebook and exported statistical output.
4. Study limitations, missing-data handling, and any exploratory or multiplicity qualification.
5. Scientific, clinical, regulatory, legal, and communications approvals as applicable.
6. The approved wording, approval date, expiry/review date, owner, and every public location using the claim.

## Immediate evidence gaps

- Assign named owners to each accountable role.
- Complete and archive the Hospital da Luz final report and analysis package by 30 June 2026.
- Resolve the report page's former completed-TRL-6 wording everywhere it may have been copied.
- Confirm and archive the exact Startup Voucher operation metadata and poster photograph.
- Audit all partnership/collaboration logos and testimonial consent records.
- Reconcile proposal claims, legal status, dataset sizes, and performance metrics before reusing proposal text publicly.

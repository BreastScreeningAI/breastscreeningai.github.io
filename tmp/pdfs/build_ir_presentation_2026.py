from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "media" / "reports" / "generated"

NAVY = "102A43"
BLUE = "1479D1"
TEAL = "0C8A7B"
AMBER = "F5A623"
INK = "243B53"
MUTED = "627D98"
LIGHT = "F5F8FB"
PALE = "EAF4FB"
LINE = "D9E2EC"
WHITE = "FFFFFF"

TITLE = "IR Presentation 2026"
PERIOD = "Interim period ended 28 February 2026"
PUBLICATION_DATE = "15 June 2026"


SLIDES = [
    {
        "title": "BreastScreening-AI IR Presentation 2026",
        "subtitle": PERIOD,
        "bullets": [
            "Human-centered, multimodal AI for breast-imaging decision support.",
            "Developed from a long-running research and clinical workflow programme.",
            "Prepared from reviewed financial, research, grant, and project records.",
            "No unsupported customer, revenue, valuation, regulatory authorization, or deployment claims are included.",
        ],
        "cards": [("Publication date", PUBLICATION_DATE), ("Category", "IR Presentation"), ("Evidence standard", "Source-backed only")],
    },
    {
        "title": "Executive Snapshot",
        "bullets": [
            "Early-stage, research-intensive medical AI company.",
            "Translating multimodal breast-imaging research into a structured platform and workflow proposition.",
            "Investor diligence should focus on funding timing, working-capital discipline, clinical validation progress, and evidence-governed claims.",
        ],
        "cards": [
            ("Total assets", "EUR 7,476.39"),
            ("Cash", "EUR 258.30"),
            ("Equity", "EUR -1,064.88"),
            ("Interim net result", "EUR -4,575.68"),
        ],
    },
    {
        "title": "Company Purpose",
        "bullets": [
            "BreastScreening-AI studies and develops multimodal breast-imaging decision support across mammography, ultrasound, and MRI.",
            "The project is positioned to strengthen clinical judgment rather than replace clinicians.",
            "Research software and information must not be presented as medical advice, diagnosis, emergency support, regulatory authorization, or clinical deployment unless directly supported.",
        ],
        "cards": [("Modality scope", "MG, US, MRI"), ("Clinical position", "Decision support"), ("Public language", "Conservative")],
    },
    {
        "title": "Research Lineage",
        "bullets": [
            "Documented lineage: MIMBCD-UI to MIDA and BreastScreening to MIA-BREAST to BreastScreening-AI and AI-Radiologist.",
            "Earliest documented fieldwork began on 20 November 2015 at Hospital Amadora-Sintra with radiologist Clara Aleluia.",
            "The work evolved from clinical requirements and multimodal imaging into explainability, trust, workload, adoption, structured reporting, and responsible AI.",
        ],
        "cards": [("Start", "20 Nov 2015"), ("Lineage", "2015 to 2026"), ("Core method", "Human-centered")],
    },
    {
        "title": "Product Thesis",
        "bullets": [
            "Support breast-imaging work through a human-centered, multimodal AI platform.",
            "Mammography supports screening-scale detection and population workflow context.",
            "Ultrasound supports lesion characterization and adjunct diagnostic interpretation.",
            "MRI supports higher-complexity assessment and multimodal completeness.",
        ],
        "cards": [("Platform", "Multimodal"), ("Workflow", "Clinician-centered"), ("Evidence", "Governed")],
    },
    {
        "title": "Evidence Foundation",
        "bullets": [
            "A historical controlled study included 45 clinicians from nine institutions.",
            "Reported outcomes included 27% fewer false positives, 4% fewer false negatives, three minutes shorter diagnosis time, and 91% positive expectations and satisfaction.",
            "Figures belong to the documented controlled study and must not be generalized as current product-wide performance or real-world deployment impact without further validation.",
        ],
        "cards": [("Clinicians", "45"), ("Institutions", "9"), ("False positives", "27% fewer"), ("Diagnosis time", "3 min shorter")],
    },
    {
        "title": "Exploratory Clinical Work",
        "bullets": [
            "Hospital da Luz exploratory study involved seven physicians, approximately 11 patients, 23 images, and 110 paired observations.",
            "Exploratory triage-level decision accuracy increased by 11.82 percentage points, with 81.82% decision stability and p = 0.0036.",
            "The study is exploratory and limited by sample size. BI-RADS remains the primary clinical reference.",
        ],
        "cards": [("Physicians", "7"), ("Images", "23"), ("Paired observations", "110"), ("Decision stability", "81.82%")],
    },
    {
        "title": "Clinical Workflow Development",
        "bullets": [
            "CHTMAD/ULSTMAD fieldwork was documented from 17 to 21 November 2025, 5 to 9 January 2026, and 26 to 30 January 2026.",
            "Focus areas included structured reporting, human-machine readability, and ethics-approved anonymized research.",
            "No consolidated quantitative results should be claimed until analysis is complete. Infrastructure access remains a dependency.",
        ],
        "cards": [("Fieldwork windows", "3"), ("Latest window", "26 to 30 Jan 2026"), ("Result status", "Pending consolidation")],
    },
    {
        "title": "Funding Context",
        "bullets": [
            "EIC Pre-Accelerator proposal 101310071 is documented as a Horizon Europe Lump Sum Grant proposal.",
            "Expected support is up to EUR 500,000 over an 18-month duration.",
            "Grant Agreement was ready for signature on 10 June 2026 and signed by the coordinator on 12 June 2026.",
            "EU services signature, final payment schedule, pre-financing percentage, first-tranche amount, and exact payment date were not confirmed in the reviewed source set.",
        ],
        "cards": [("Proposal", "101310071"), ("Potential support", "Up to EUR 500,000"), ("Duration", "18 months")],
    },
    {
        "title": "Financial Position",
        "bullets": [
            "Interim FY2026 figures cover the period ended 28 February 2026.",
            "Total assets were EUR 7,476.39 and cash and deposits were EUR 258.30.",
            "Equity was EUR -1,064.88, liabilities were EUR 8,541.27, and supplier liabilities were EUR 7,866.32.",
            "The interim net result was EUR -4,575.68 and should not be annualized.",
        ],
        "cards": [("Assets", "EUR 7,476.39"), ("Cash", "EUR 258.30"), ("Liabilities", "EUR 8,541.27"), ("Supplier liabilities", "EUR 7,866.32")],
    },
    {
        "title": "Historical Financial Context",
        "bullets": [
            "FY2024: total assets of EUR 1,123.38, cash and deposits of EUR 721.34, equity of EUR -611.69, liabilities of EUR 1,735.07, subsidies of EUR 1,796.63, and net result of EUR -711.69.",
            "FY2025: total assets of EUR 12,458.22, cash and deposits of EUR 3,856.90, equity of EUR 3,510.80, liabilities of EUR 8,947.42, subsidies of EUR 24,500.00, sales and services of EUR 100.00, other income of EUR 3,000.00, and net result of EUR 1,122.49.",
            "FY2025 shows a larger operating base and positive result, but sales and services remained limited.",
        ],
        "cards": [("FY2024 result", "EUR -711.69"), ("FY2025 result", "EUR 1,122.49"), ("FY2025 sales", "EUR 100.00")],
    },
    {
        "title": "Recognition and Venture Development",
        "bullets": [
            "European Innovation Academy Porto 2023: named among the top ten teams from 100 international startup teams.",
            "WIPO Global Awards 2024: recognized as one of 25 finalists selected from 667 applications across 107 countries.",
            "S3E Start 2024: selected as one of 14 teams in the programme.",
            "Recognitions support external visibility and venture-development credibility, not customers, investment proceeds, clinical deployment, regulatory authorization, or recurring revenue.",
        ],
        "cards": [("EIA teams", "100"), ("WIPO finalists", "25"), ("WIPO applications", "667"), ("S3E cohort", "14")],
    },
    {
        "title": "Commercial Progress",
        "bullets": [
            "Confirmed commercial revenue in the reviewed financial source set is limited.",
            "FY2025 sales and services were EUR 100.00.",
            "No source-backed evidence in the reviewed set establishes recurring revenue, signed customer contracts, paid deployments, valuation, or a repeatable sales model.",
            "Commercial development should be presented as an execution priority rather than proven traction.",
        ],
        "cards": [("FY2025 sales and services", "EUR 100.00"), ("Recurring revenue", "Not established"), ("Paid deployments", "Not established")],
    },
    {
        "title": "Partnerships and Ecosystem",
        "bullets": [
            "SNAP: European proposal development, EIC project management, and Grant Agreement Preparation.",
            "Leyton: Startup Voucher and PRR reporting, cost eligibility, and communication compliance.",
            "SAVEAS: intellectual-property strategy, freedom-to-operate, and related consultancy.",
            "KGSA: corporate, contractual, and broader legal matters.",
            "Complear: regulatory-strategy and independent-validation discussions.",
            "AAVANZ: EIC Pathfinder and Horizon Europe proposal preparation.",
        ],
        "cards": [("Evidence rule", "Precise roles only"), ("No implication", "Clinical endorsement"), ("No implication", "Broader contracts")],
    },
    {
        "title": "Risk Factors",
        "bullets": [
            "Grant payment timing remains unresolved until final grant documentation confirms payment terms.",
            "Interim FY2026 cash position was low at 28 February 2026.",
            "Equity was negative at the interim reporting date.",
            "Supplier liabilities were material relative to assets.",
            "Commercial revenue remains limited in the reviewed records.",
            "Clinical evidence includes promising but bounded studies, including exploratory work with small samples.",
            "Regulatory authorization and clinical deployment are not established in the reviewed source set.",
        ],
        "cards": [("Liquidity", "Priority risk"), ("Commercial proof", "Pending"), ("Regulatory status", "Not authorized")],
    },
    {
        "title": "Management Priorities",
        "bullets": [
            "Confirm EIC Pre-Accelerator payment schedule, pre-financing percentage, and first cash receipt.",
            "Maintain working-capital discipline and supplier-liability control.",
            "Complete Hospital da Luz final reporting.",
            "Resolve ULSTMAD infrastructure dependencies.",
            "Reconcile public claims with source-backed evidence.",
            "Preserve conservative medical, financial, regulatory, and partnership language.",
        ],
        "cards": [("Funding", "Confirm terms"), ("Evidence", "Complete reporting"), ("Governance", "Control claims")],
    },
    {
        "title": "Investor Diligence Questions",
        "bullets": [
            "When will EIC Pre-Accelerator funds be received, and in what tranches?",
            "What is the current runway after February 2026?",
            "Which clinical studies are complete, exploratory, or pending analysis?",
            "Which claims are validated, and which remain assumptions?",
            "What is the commercial route from research evidence to hospital adoption?",
            "Which regulatory pathway is intended, and what evidence is missing?",
        ],
        "cards": [("Funding", "Timing"), ("Evidence", "Validation status"), ("Commercial", "Route to adoption")],
    },
    {
        "title": "Closing Message",
        "bullets": [
            "BreastScreening-AI has a long research lineage, documented clinical workflow work, recognized venture-development milestones, and a non-dilutive funding pathway in progress.",
            "The investment case should be presented as an evidence-governed, early-stage medical AI opportunity that still requires disciplined execution across validation, regulation, funding, commercialization, and working-capital management.",
            "The strongest current narrative is deep research foundation, credible programme momentum, early financial reporting discipline, and a clear path toward stronger clinical and investor readiness.",
        ],
        "cards": [("Narrative", "Evidence governed"), ("Stage", "Early-stage"), ("Next proof", "Execution")],
    },
]


def hex_color(value):
    return colors.HexColor(f"#{value}")


def pdf_styles():
    styles = getSampleStyleSheet()
    return {
        "kicker": ParagraphStyle("kicker", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=8.5, leading=10, textColor=hex_color(BLUE), spaceAfter=6),
        "title": ParagraphStyle("title", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=23, leading=27, textColor=hex_color(NAVY), alignment=TA_LEFT, spaceAfter=8),
        "subtitle": ParagraphStyle("subtitle", parent=styles["Normal"], fontName="Helvetica", fontSize=11, leading=14, textColor=hex_color(MUTED), spaceAfter=14),
        "body": ParagraphStyle("body", parent=styles["Normal"], fontName="Helvetica", fontSize=10.4, leading=14.2, textColor=hex_color(INK), spaceAfter=7),
        "bullet": ParagraphStyle("bullet", parent=styles["Normal"], fontName="Helvetica", fontSize=10.2, leading=13.8, textColor=hex_color(INK), leftIndent=12, firstLineIndent=-7, spaceAfter=5),
        "card_label": ParagraphStyle("card_label", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=7.5, leading=9, textColor=hex_color(MUTED), alignment=TA_LEFT),
        "card_value": ParagraphStyle("card_value", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=11.8, leading=14, textColor=hex_color(NAVY), alignment=TA_LEFT),
    }


def page_header(canvas, doc):
    width, height = landscape((13.333 * inch, 7.5 * inch))
    canvas.saveState()
    canvas.setFillColor(hex_color(NAVY))
    canvas.rect(0, height - 0.34 * inch, width, 0.34 * inch, stroke=0, fill=1)
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica-Bold", 8)
    canvas.drawString(0.42 * inch, height - 0.22 * inch, "BreastScreening-AI")
    canvas.setFont("Helvetica", 7.5)
    canvas.drawRightString(width - 0.42 * inch, height - 0.22 * inch, f"{TITLE} | {PUBLICATION_DATE}")
    canvas.setFillColor(hex_color(MUTED))
    canvas.setFont("Helvetica", 7.3)
    canvas.drawString(0.42 * inch, 0.22 * inch, "Company communication asset. Source-backed investor relations presentation.")
    canvas.drawRightString(width - 0.42 * inch, 0.22 * inch, f"Slide {doc.page}")
    canvas.restoreState()


def build_pdf():
    path = OUTPUT / "breastscreeningai_ir_presentation_2026.pdf"
    doc = SimpleDocTemplate(
        str(path),
        pagesize=landscape((13.333 * inch, 7.5 * inch)),
        leftMargin=0.55 * inch,
        rightMargin=0.55 * inch,
        topMargin=0.65 * inch,
        bottomMargin=0.5 * inch,
        title=TITLE,
        author="BreastScreening-AI",
        subject=PERIOD,
    )
    s = pdf_styles()
    story = []
    for idx, slide in enumerate(SLIDES, 1):
        story.append(Paragraph(f"{idx:02d} | {TITLE}", s["kicker"]))
        story.append(Paragraph(slide["title"], s["title"]))
        if slide.get("subtitle"):
            story.append(Paragraph(slide["subtitle"], s["subtitle"]))
        story.extend(Paragraph(f"- {bullet}", s["bullet"]) for bullet in slide["bullets"])
        if slide.get("cards"):
            rows = []
            cards = []
            for label, value in slide["cards"]:
                cards.append([Paragraph(label.upper(), s["card_label"]), Paragraph(value, s["card_value"])])
            for start in range(0, len(cards), 4):
                rows.append(cards[start:start + 4])
            table = Table(rows, colWidths=[2.85 * inch] * min(4, max(1, len(cards))), hAlign="LEFT")
            table.setStyle(
                TableStyle(
                    [
                        ("BACKGROUND", (0, 0), (-1, -1), hex_color(PALE)),
                        ("BOX", (0, 0), (-1, -1), 0.7, hex_color(LINE)),
                        ("INNERGRID", (0, 0), (-1, -1), 0.4, colors.white),
                        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                        ("LEFTPADDING", (0, 0), (-1, -1), 8),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                        ("TOPPADDING", (0, 0), (-1, -1), 8),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                    ]
                )
            )
            story.extend([Spacer(1, 0.08 * inch), table])
        if idx < len(SLIDES):
            story.append(PageBreak())
    doc.build(story, onFirstPage=page_header, onLaterPages=page_header)
    return path


def slide_xml(title, bullets, cards, slide_no, subtitle=None):
    bullet_xml = "".join(
        f"""
        <a:p><a:pPr marL="285750" indent="-142875"><a:buChar char="•"/><a:defRPr sz="1600"/></a:pPr><a:r><a:rPr lang="en-US" sz="1600"><a:solidFill><a:srgbClr val="{INK}"/></a:solidFill></a:rPr><a:t>{escape(line)}</a:t></a:r></a:p>
        """
        for line in bullets
    )
    card_text = " | ".join(f"{label}: {value}" for label, value in cards)
    subtitle_xml = ""
    if subtitle:
        subtitle_xml = f'<a:p><a:r><a:rPr lang="en-US" sz="1250"><a:solidFill><a:srgbClr val="{MUTED}"/></a:solidFill></a:rPr><a:t>{escape(subtitle)}</a:t></a:r></a:p>'
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:cSld>
    <p:bg><p:bgPr><a:solidFill><a:srgbClr val="{LIGHT}"/></a:solidFill><a:effectLst/></p:bgPr></p:bg>
    <p:spTree>
      <p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>
      <p:sp><p:nvSpPr><p:cNvPr id="2" name="Accent"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr><p:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="9144000" cy="228600"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom><a:solidFill><a:srgbClr val="{NAVY}"/></a:solidFill></p:spPr><p:txBody><a:bodyPr/><a:lstStyle/><a:p/></p:txBody></p:sp>
      <p:sp>
        <p:nvSpPr><p:cNvPr id="3" name="Title"/><p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr><p:nvPr/></p:nvSpPr>
        <p:spPr><a:xfrm><a:off x="457200" y="457200"/><a:ext cx="8229600" cy="900000"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom><a:noFill/></p:spPr>
        <p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:r><a:rPr lang="en-US" sz="2700" b="1"><a:solidFill><a:srgbClr val="{NAVY}"/></a:solidFill></a:rPr><a:t>{escape(title)}</a:t></a:r></a:p>{subtitle_xml}</p:txBody>
      </p:sp>
      <p:sp>
        <p:nvSpPr><p:cNvPr id="4" name="Body"/><p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr><p:nvPr/></p:nvSpPr>
        <p:spPr><a:xfrm><a:off x="548640" y="1450000"/><a:ext cx="8046720" cy="2920000"/></a:xfrm><a:prstGeom prst="roundRect"><a:avLst/></a:prstGeom><a:solidFill><a:srgbClr val="{WHITE}"/></a:solidFill><a:ln w="12700"><a:solidFill><a:srgbClr val="{LINE}"/></a:solidFill></a:ln></p:spPr>
        <p:txBody><a:bodyPr lIns="220000" tIns="180000" rIns="220000" bIns="160000"/><a:lstStyle/>{bullet_xml}</p:txBody>
      </p:sp>
      <p:sp>
        <p:nvSpPr><p:cNvPr id="5" name="Cards"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
        <p:spPr><a:xfrm><a:off x="548640" y="4560000"/><a:ext cx="8046720" cy="620000"/></a:xfrm><a:prstGeom prst="roundRect"><a:avLst/></a:prstGeom><a:solidFill><a:srgbClr val="{PALE}"/></a:solidFill><a:ln w="12700"><a:solidFill><a:srgbClr val="{BLUE}"/></a:solidFill></a:ln></p:spPr>
        <p:txBody><a:bodyPr lIns="180000" tIns="110000" rIns="180000" bIns="90000"/><a:lstStyle/><a:p><a:r><a:rPr lang="en-US" sz="1150" b="1"><a:solidFill><a:srgbClr val="{NAVY}"/></a:solidFill></a:rPr><a:t>{escape(card_text)}</a:t></a:r></a:p></p:txBody>
      </p:sp>
      <p:sp><p:nvSpPr><p:cNvPr id="6" name="Footer"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr><p:spPr><a:xfrm><a:off x="457200" y="4877000"/><a:ext cx="8229600" cy="300000"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom><a:noFill/></p:spPr><p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:r><a:rPr lang="en-US" sz="850"><a:solidFill><a:srgbClr val="{MUTED}"/></a:solidFill></a:rPr><a:t>BreastScreening-AI | Company communication asset | Slide {slide_no}</a:t></a:r></a:p></p:txBody></p:sp>
    </p:spTree>
  </p:cSld>
  <p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>
</p:sld>"""


def content_types(n):
    overrides = "\n".join(f'<Override PartName="/ppt/slides/slide{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>' for i in range(1, n + 1))
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/>
<Override PartName="/ppt/slideMasters/slideMaster1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml"/>
<Override PartName="/ppt/slideLayouts/slideLayout1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml"/>
<Override PartName="/ppt/theme/theme1.xml" ContentType="application/vnd.openxmlformats-officedocument.theme+xml"/>
<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
{overrides}
</Types>"""


def root_rels():
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="ppt/presentation.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>"""


def presentation_xml(n):
    sld_ids = "\n".join(f'<p:sldId id="{255+i}" r:id="rId{i}"/>' for i in range(1, n + 1))
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:presentation xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
<p:sldMasterIdLst><p:sldMasterId id="2147483648" r:id="rId{n+1}"/></p:sldMasterIdLst>
<p:sldIdLst>{sld_ids}</p:sldIdLst>
<p:sldSz cx="9144000" cy="5143500" type="screen16x9"/>
<p:notesSz cx="6858000" cy="9144000"/>
</p:presentation>"""


def presentation_rels(n):
    rels = "\n".join(f'<Relationship Id="rId{i}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide{i}.xml"/>' for i in range(1, n + 1))
    rels += f'\n<Relationship Id="rId{n+1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="slideMasters/slideMaster1.xml"/>'
    rels += f'\n<Relationship Id="rId{n+2}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme" Target="theme/theme1.xml"/>'
    return f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">{rels}</Relationships>'


def theme_xml():
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" name="BreastScreening-AI"><a:themeElements><a:clrScheme name="BreastScreening-AI"><a:dk1><a:srgbClr val="{NAVY}"/></a:dk1><a:lt1><a:srgbClr val="{WHITE}"/></a:lt1><a:dk2><a:srgbClr val="{INK}"/></a:dk2><a:lt2><a:srgbClr val="{LIGHT}"/></a:lt2><a:accent1><a:srgbClr val="{BLUE}"/></a:accent1><a:accent2><a:srgbClr val="{TEAL}"/></a:accent2><a:accent3><a:srgbClr val="{AMBER}"/></a:accent3><a:accent4><a:srgbClr val="{MUTED}"/></a:accent4><a:accent5><a:srgbClr val="{LINE}"/></a:accent5><a:accent6><a:srgbClr val="{PALE}"/></a:accent6><a:hlink><a:srgbClr val="{BLUE}"/></a:hlink><a:folHlink><a:srgbClr val="{TEAL}"/></a:folHlink></a:clrScheme><a:fontScheme name="Arial"><a:majorFont><a:latin typeface="Arial"/></a:majorFont><a:minorFont><a:latin typeface="Arial"/></a:minorFont></a:fontScheme><a:fmtScheme name="Office"><a:fillStyleLst><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:fillStyleLst><a:lnStyleLst><a:ln w="9525"><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:ln></a:lnStyleLst><a:effectStyleLst><a:effectStyle><a:effectLst/></a:effectStyle></a:effectStyleLst><a:bgFillStyleLst><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:bgFillStyleLst></a:fmtScheme></a:themeElements></a:theme>"""


def slide_master_xml():
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?><p:sldMaster xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"><p:cSld><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr></p:spTree></p:cSld><p:clrMap bg1="lt1" tx1="dk1" bg2="lt2" tx2="dk2" accent1="accent1" accent2="accent2" accent3="accent3" accent4="accent4" accent5="accent5" accent6="accent6" hlink="hlink" folHlink="folHlink"/><p:sldLayoutIdLst><p:sldLayoutId id="2147483649" r:id="rId1"/></p:sldLayoutIdLst><p:txStyles><p:titleStyle/><p:bodyStyle/><p:otherStyle/></p:txStyles></p:sldMaster>"""


def slide_master_rels():
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/><Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme" Target="../theme/theme1.xml"/></Relationships>"""


def slide_layout_xml():
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?><p:sldLayout xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" type="blank" preserve="1"><p:cSld name="Blank"><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr></p:spTree></p:cSld><p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr></p:sldLayout>"""


def slide_layout_rels():
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="../slideMasters/slideMaster1.xml"/></Relationships>"""


def slide_rels():
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/></Relationships>"""


def core_xml():
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?><cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><dc:title>{escape(TITLE)}</dc:title><dc:creator>BreastScreening-AI</dc:creator><cp:lastModifiedBy>BreastScreening-AI</cp:lastModifiedBy></cp:coreProperties>"""


def app_xml(n):
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes"><Application>BreastScreening-AI</Application><PresentationFormat>On-screen Show (16:9)</PresentationFormat><Slides>{n}</Slides></Properties>"""


def build_pptx():
    n = len(SLIDES)
    path = OUTPUT / "breastscreeningai_ir_presentation_2026.pptx"
    with ZipFile(path, "w", ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", content_types(n))
        z.writestr("_rels/.rels", root_rels())
        z.writestr("ppt/presentation.xml", presentation_xml(n))
        z.writestr("ppt/_rels/presentation.xml.rels", presentation_rels(n))
        z.writestr("ppt/theme/theme1.xml", theme_xml())
        z.writestr("ppt/slideMasters/slideMaster1.xml", slide_master_xml())
        z.writestr("ppt/slideMasters/_rels/slideMaster1.xml.rels", slide_master_rels())
        z.writestr("ppt/slideLayouts/slideLayout1.xml", slide_layout_xml())
        z.writestr("ppt/slideLayouts/_rels/slideLayout1.xml.rels", slide_layout_rels())
        z.writestr("docProps/core.xml", core_xml())
        z.writestr("docProps/app.xml", app_xml(n))
        for index, slide in enumerate(SLIDES, 1):
            z.writestr(f"ppt/slides/slide{index}.xml", slide_xml(slide["title"], slide["bullets"], slide["cards"], index, slide.get("subtitle")))
            z.writestr(f"ppt/slides/_rels/slide{index}.xml.rels", slide_rels())
    return path


def main():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    pdf = build_pdf()
    pptx = build_pptx()
    print(pdf.relative_to(ROOT))
    print(pptx.relative_to(ROOT))


if __name__ == "__main__":
    main()

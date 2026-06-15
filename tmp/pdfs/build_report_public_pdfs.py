from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch, mm
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "media" / "reports" / "generated"

NAVY = "102A43"
BLUE = "1479D1"
INK = "243B53"
MUTED = "627D98"
PALE = "EAF4FB"
LINE = "D9E2EC"


DOCUMENTS = [
    {
        "filename": "breastscreeningai_annual_financial_statements_2024.pdf",
        "type": "Annual Financial Statements",
        "title": "Annual Financial Statements 2024",
        "period": "Year ended 31 December 2024",
        "summary": "FY2024 establishes the historical financial baseline for the company report archive.",
        "metrics": [
            ("Total assets", "EUR 1,123.38"),
            ("Cash and deposits", "EUR 721.34"),
            ("Equity", "EUR -611.69"),
            ("Liabilities", "EUR 1,735.07"),
            ("Subsidies", "EUR 1,796.63"),
            ("Net result", "EUR -711.69"),
        ],
        "body": [
            "The period reflects an early operating baseline, with limited asset scale and negative equity.",
            "The source set does not establish an auditor opinion, cash-flow statement, statutory filing confirmation, signed customer contracts, valuation, or commercial forecast for FY2024.",
        ],
    },
    {
        "filename": "breastscreeningai_interim_financial_statements_2026.pdf",
        "type": "Interim Financial Statements",
        "title": "Interim Financial Statements 2026",
        "period": "Interim period ended 28 February 2026",
        "summary": "The interim FY2026 view highlights liquidity and working-capital discipline before later funding events were confirmed.",
        "metrics": [
            ("Total assets", "EUR 7,476.39"),
            ("Cash and deposits", "EUR 258.30"),
            ("Equity", "EUR -1,064.88"),
            ("Liabilities", "EUR 8,541.27"),
            ("Supplier liabilities", "EUR 7,866.32"),
            ("External services", "EUR 1,372.42"),
            ("Personnel expenses", "EUR 2,624.44"),
            ("Net result", "EUR -4,575.68"),
        ],
        "body": [
            "The interim result has not been annualized and does not represent a full-year forecast.",
            "Low cash, negative equity, and supplier liabilities make funding timing, cost discipline, and working-capital control key investor diligence topics.",
            "The reviewed source set does not establish subsequent cash receipts, investor proceeds, customer collections, final EIC payment schedule, or full-year FY2026 forecast.",
        ],
    },
    {
        "filename": "breastscreeningai_ir_letter_2024.pdf",
        "type": "IR Letter",
        "title": "IR Letter 2024",
        "period": "Year ended 31 December 2024",
        "summary": "Founder-style note covering the FY2024 financial baseline and reporting priorities.",
        "metrics": [("Total assets", "EUR 1,123.38"), ("Cash", "EUR 721.34"), ("Net result", "EUR -711.69")],
        "body": [
            "FY2024 established the company's baseline for future investor reporting.",
            "The period should be understood as early formation and operating baseline rather than evidence of commercial scale.",
            "Management's priority after FY2024 was to improve documentation quality, preserve source-backed claims, and prepare for more structured financial, grant, and investor communication.",
        ],
    },
    {
        "filename": "breastscreeningai_ir_letter_2025.pdf",
        "type": "IR Letter",
        "title": "FY2025 Investor Relations Letter",
        "period": "Year ended 31 December 2025",
        "summary": "Founder-style note covering FY2025 financial development, subsidy dependence, and reporting priorities.",
        "metrics": [("Total assets", "EUR 12,458.22"), ("Equity", "EUR 3,510.80"), ("Net result", "EUR 1,122.49")],
        "body": [
            "FY2025 marked an expanded operating base for BreastScreening-AI.",
            "The company recorded EUR 24,500.00 in subsidies, EUR 3,000.00 in other income, and EUR 100.00 in sales and services.",
            "The positive result is useful, but it should be read together with limited commercial revenue and continued dependence on grant-backed execution.",
            "Management's response was to strengthen the reporting base around evidence, finance, public claims, and investor communication.",
        ],
    },
    {
        "filename": "breastscreeningai_ir_letter_2026.pdf",
        "type": "IR Letter",
        "title": "IR Letter 2026",
        "period": "Interim period ended 28 February 2026",
        "summary": "Founder-style interim note covering constrained resources, funding context, and next priorities.",
        "metrics": [("Cash", "EUR 258.30"), ("Equity", "EUR -1,064.88"), ("Net result", "EUR -4,575.68")],
        "body": [
            "The first months of 2026 were defined by disciplined execution under constrained resources.",
            "For the interim period ended 28 February 2026, BreastScreening-AI reported total assets of EUR 7,476.39, cash and deposits of EUR 258.30, equity of EUR -1,064.88, liabilities of EUR 8,541.27, and supplier liabilities of EUR 7,866.32.",
            "The interim net result was EUR -4,575.68. The interim result has not been annualized and should not be interpreted as a full-year forecast.",
            "Operationally, the company continued to develop a human-centered, multimodal breast-imaging decision-support project grounded in a long research lineage.",
            "Source-backed records indicate that BreastScreening-AI was selected for the EIC Pre-Accelerator, with potential support of up to EUR 500,000 under Horizon Europe Lump Sum Grant proposal 101310071 for an 18-month duration.",
            "The Grant Agreement was ready for signature on 10 June 2026 and signed by the coordinator on 12 June 2026. EU services signature, the final payment schedule, the pre-financing percentage, the first tranche amount, and the exact cash receipt date were not confirmed in the reviewed source set.",
            "Priorities for the next period are to confirm grant-payment terms, maintain working-capital discipline, consolidate clinical analysis, preserve funding-compliance documentation, and keep public claims source-backed.",
        ],
    },
]


PRESENTATIONS = [
    {
        "filename": "breastscreeningai_ir_presentation_2024.pdf",
        "title": "IR Presentation 2024",
        "period": "Year ended 31 December 2024",
        "slides": [
            ("Executive Snapshot", ["Early public financial baseline.", "Negative equity and small operating scale.", "No source-backed customer, valuation, or regulatory authorization claim."]),
            ("Financial Baseline", ["Total assets: EUR 1,123.38.", "Cash and deposits: EUR 721.34.", "Equity: EUR -611.69.", "Liabilities: EUR 1,735.07."]),
            ("Investor Diligence Focus", ["Confirm account approval and statutory filing status.", "Maintain evidence-backed public communication.", "Avoid treating subsidies as recurring commercial traction."]),
        ],
    },
    {
        "filename": "breastscreeningai_ir_presentation_2025.pdf",
        "title": "FY2025 Investor Relations Presentation",
        "period": "Year ended 31 December 2025",
        "slides": [
            ("Executive Snapshot", ["FY2025 closed with positive equity and a positive net result.", "Commercial revenue remained limited.", "Subsidies were the main income driver in the reviewed financial records."]),
            ("Financial Highlights", ["Total assets: EUR 12,458.22.", "Cash and deposits: EUR 3,856.90.", "Equity: EUR 3,510.80.", "Net result: EUR 1,122.49."]),
            ("Investor Diligence Focus", ["Validate grant-backed development model.", "Confirm statutory filing and accounting-note status.", "Do not present FY2025 as recurring commercial traction."]),
        ],
    },
]


def hex_color(value):
    return colors.HexColor(f"#{value}")


def styles():
    base = getSampleStyleSheet()
    return {
        "kicker": ParagraphStyle("kicker", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=8, leading=10, textColor=hex_color(BLUE), spaceAfter=6),
        "title": ParagraphStyle("title", parent=base["Title"], fontName="Helvetica-Bold", fontSize=23, leading=27, textColor=hex_color(NAVY), alignment=TA_LEFT, spaceAfter=8),
        "subtitle": ParagraphStyle("subtitle", parent=base["Normal"], fontName="Helvetica", fontSize=10, leading=13, textColor=hex_color(MUTED), spaceAfter=12),
        "h2": ParagraphStyle("h2", parent=base["Heading2"], fontName="Helvetica-Bold", fontSize=12.5, leading=15, textColor=hex_color(NAVY), spaceBefore=10, spaceAfter=6),
        "body": ParagraphStyle("body", parent=base["Normal"], fontName="Helvetica", fontSize=9.5, leading=13.2, textColor=hex_color(INK), spaceAfter=6),
        "table": ParagraphStyle("table", parent=base["Normal"], fontName="Helvetica", fontSize=8.5, leading=11, textColor=hex_color(INK)),
        "table_head": ParagraphStyle("table_head", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=8.5, leading=11, textColor=colors.white),
    }


def header(canvas, doc, title):
    width, height = A4
    canvas.saveState()
    canvas.setFillColor(hex_color(NAVY))
    canvas.rect(0, height - 13 * mm, width, 13 * mm, stroke=0, fill=1)
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica-Bold", 8.5)
    canvas.drawString(18 * mm, height - 8.5 * mm, "BreastScreening-AI")
    canvas.setFont("Helvetica", 7.5)
    canvas.drawRightString(width - 18 * mm, height - 8.5 * mm, title)
    canvas.setFillColor(hex_color(MUTED))
    canvas.setFont("Helvetica", 7.2)
    canvas.drawString(18 * mm, 9.5 * mm, "Company communication asset.")
    canvas.drawRightString(width - 18 * mm, 9.5 * mm, f"Page {doc.page}")
    canvas.restoreState()


def build_document_pdf(item):
    s = styles()
    path = OUTPUT / item["filename"]
    doc = BaseDocTemplate(str(path), pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm, topMargin=22 * mm, bottomMargin=20 * mm, title=item["title"], author="BreastScreening-AI")
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal")
    doc.addPageTemplates([PageTemplate(id="page", frames=frame, onPage=lambda c, d: header(c, d, item["title"]))])
    story = [
        Spacer(1, 5 * mm),
        Paragraph(item["type"].upper(), s["kicker"]),
        Paragraph(item["title"], s["title"]),
        Paragraph(f"{item['period']}<br/>Publication date: 15 June 2026<br/>Currency: Euro (EUR)", s["subtitle"]),
        Paragraph(item["summary"], s["body"]),
        Paragraph("Key Figures", s["h2"]),
    ]
    data = [[Paragraph("Metric", s["table_head"]), Paragraph("Value", s["table_head"])]]
    data.extend([Paragraph(k, s["table"]), Paragraph(v, s["table"])] for k, v in item["metrics"])
    table = Table(data, colWidths=[88 * mm, 70 * mm], hAlign="LEFT")
    table.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), hex_color(NAVY)), ("BOX", (0, 0), (-1, -1), 0.6, hex_color(LINE)), ("INNERGRID", (0, 0), (-1, -1), 0.35, hex_color(LINE)), ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7), ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]))
    story.append(table)
    story.append(Paragraph("Management Context", s["h2"]))
    story.extend(Paragraph(p, s["body"]) for p in item["body"])
    story.append(Paragraph("Evidence Boundary", s["h2"]))
    story.append(Paragraph("The reviewed source set does not establish unsupported revenue, customers, investments, valuation, regulatory authorization, or clinical deployment.", s["body"]))
    doc.build(story)


def build_presentation_pdf(item):
    s = styles()
    path = OUTPUT / item["filename"]
    doc = SimpleDocTemplate(str(path), pagesize=landscape((13.333 * inch, 7.5 * inch)), leftMargin=0.55 * inch, rightMargin=0.55 * inch, topMargin=0.55 * inch, bottomMargin=0.45 * inch, title=item["title"], author="BreastScreening-AI")
    story = []
    for slide_no, (title, bullets) in enumerate(item["slides"], 1):
        story.append(Paragraph(f"{slide_no:02d} | {item['title']}", s["kicker"]))
        story.append(Paragraph(title, s["title"]))
        story.append(Paragraph(item["period"], s["subtitle"]))
        story.extend(Paragraph(f"- {line}", s["body"]) for line in bullets)
        if slide_no < len(item["slides"]):
            from reportlab.platypus import PageBreak
            story.append(PageBreak())
    doc.build(story)


def main():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for item in DOCUMENTS:
        build_document_pdf(item)
        print(item["filename"])
    for item in PRESENTATIONS:
        build_presentation_pdf(item)
        print(item["filename"])


if __name__ == "__main__":
    main()

import fs from "node:fs/promises";
import path from "node:path";
import { Presentation, PresentationFile } from "/Users/francisco/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/.pnpm/@oai+artifact-tool@file+local-deps+-oai-artifact-tool-oai-artifact_tool-2.8.11.tgz/node_modules/@oai/artifact-tool/dist/artifact_tool.mjs";

const ROOT = "/Users/francisco/Git/breastscreeningai.github.io";
const WORK = path.join(ROOT, "tmp/presentations/fy2025-ir/tmp");
const SLIDES_DIR = path.join(WORK, "slides");
const LAYOUT_DIR = path.join(WORK, "layout");
const OUT_PPTX = path.join(ROOT, "media/reports/breastscreeningai_ir_presentation_2025.pptx");

async function writeBlob(filePath, blob) {
  await fs.writeFile(filePath, new Uint8Array(await blob.arrayBuffer()));
}

const W = 1280;
const H = 720;
const C = {
  navy: "#0B1F3A",
  ink: "#172033",
  muted: "#5F6B7A",
  blue: "#1066FF",
  lightBlue: "#EEF5FF",
  line: "#DCE6F2",
  white: "#FFFFFF",
  teal: "#16A06D",
  amber: "#C68215",
  amberLight: "#FFF6E6",
  redLight: "#FFF1F1",
  slate: "#F7FAFD",
};

const presentation = Presentation.create({ slideSize: { width: W, height: H } });
presentation.theme.colorScheme = {
  name: "BreastScreening-AI IR",
  themeColors: {
    accent1: C.blue,
    accent2: C.teal,
    accent3: C.amber,
    accent4: "#D84A4A",
    accent5: "#6C63FF",
    accent6: "#2F80ED",
    bg1: C.white,
    bg2: C.slate,
    tx1: C.ink,
    tx2: C.muted,
    dk1: "#000000",
    dk2: C.navy,
    lt1: C.white,
    lt2: C.line,
    hlink: C.blue,
    folHlink: "#6C63FF",
  },
};

function addShape(slide, cfg) {
  return slide.shapes.add(cfg);
}

function addText(slide, text, x, y, w, h, opts = {}) {
  const sh = addShape(slide, {
    geometry: "textbox",
    name: opts.name,
    position: { left: x, top: y, width: w, height: h },
    fill: "none",
    line: { style: "solid", fill: "none", width: 0 },
  });
  sh.text = text;
  sh.text.style = {
    fontSize: opts.size ?? 20,
    bold: opts.bold ?? false,
    color: opts.color ?? C.ink,
    alignment: opts.align ?? "left",
    fontFace: opts.font ?? "Aptos",
  };
  return sh;
}

function addBox(slide, x, y, w, h, opts = {}) {
  return addShape(slide, {
    geometry: "roundRect",
    position: { left: x, top: y, width: w, height: h },
    fill: opts.fill ?? C.white,
    line: { style: "solid", fill: opts.line ?? C.line, width: opts.lineWidth ?? 1 },
    borderRadius: opts.radius ?? "rounded-2xl",
    shadow: opts.shadow ?? "shadow-sm",
  });
}

function addFooter(slide, n, source = "Source-backed company materials and accounting records") {
  addShape(slide, {
    geometry: "line",
    position: { left: 70, top: 666, width: 1140, height: 0 },
    fill: "none",
    line: { style: "solid", fill: C.line, width: 1 },
  });
  addText(slide, source, 72, 675, 850, 22, { size: 10, color: "#758398" });
  addText(slide, String(n).padStart(2, "0"), 1148, 675, 60, 22, { size: 10, color: "#758398", align: "right" });
}

function addHeader(slide, kicker, title, subtitle, n) {
  slide.background.fill = C.white;
  addText(slide, "BreastScreening-AI", 70, 38, 260, 24, { size: 13, bold: true, color: C.navy });
  addBox(slide, 70, 66, 150, 6, { fill: C.blue, line: C.blue, radius: "rounded-full", shadow: "shadow-none" });
  addText(slide, kicker.toUpperCase(), 70, 104, 460, 24, { size: 12, bold: true, color: C.blue });
  addText(slide, title, 70, 136, 760, 100, { size: 38, bold: true, color: C.navy, font: "Aptos Display" });
  if (subtitle) addText(slide, subtitle, 70, 232, 850, 54, { size: 18, color: C.muted });
  addFooter(slide, n);
}

function addKpi(slide, x, y, w, h, value, label, color = C.navy) {
  addBox(slide, x, y, w, h, { fill: C.lightBlue, line: "#CFE0F7", shadow: "shadow-none" });
  addText(slide, value, x + 18, y + 20, w - 36, 44, { size: 30, bold: true, color });
  addText(slide, label, x + 18, y + 74, w - 36, 42, { size: 14, color: C.muted });
}

function addBulletText(slide, items, x, y, w, h, opts = {}) {
  addText(slide, items.map((item) => `- ${item}`).join("\\n"), x, y, w, h, {
    size: opts.size ?? 17,
    color: opts.color ?? C.ink,
  });
}

function addPill(slide, text, x, y, w, color = C.blue, fill = C.lightBlue) {
  addBox(slide, x, y, w, 34, { fill, line: fill, radius: "rounded-full", shadow: "shadow-none" });
  addText(slide, text, x + 14, y + 8, w - 28, 18, { size: 11, bold: true, color });
}

function addSectionCard(slide, x, y, w, h, heading, body, accent = C.blue) {
  addBox(slide, x, y, w, h, { fill: C.white, line: C.line, shadow: "shadow-sm" });
  addBox(slide, x + 18, y + 18, 42, 6, { fill: accent, line: accent, radius: "rounded-full", shadow: "shadow-none" });
  addText(slide, heading, x + 18, y + 38, w - 36, 34, { size: 20, bold: true, color: C.navy });
  addText(slide, body, x + 18, y + 78, w - 36, h - 92, { size: 15, color: C.muted });
}

function slideCover() {
  const s = presentation.slides.add();
  s.background.fill = `linear(140deg, ${C.navy} 0%, #123C6C 62%, ${C.blue} 100%)`;
  addText(s, "BreastScreening-AI", 72, 58, 320, 30, { size: 16, bold: true, color: C.white });
  addText(s, "FY2025 Investor Relations Presentation", 72, 164, 760, 130, { size: 54, bold: true, color: C.white, font: "Aptos Display" });
  addText(s, "Fiscal year ended 31 December 2025 | Published 15 June 2026", 76, 318, 680, 34, { size: 18, color: "#DDEBFF" });
  addText(s, "Source-backed overview for investor review. No unsupported commercial, regulatory, partnership, customer, or valuation claims are included.", 76, 410, 640, 80, { size: 20, color: C.white });
  addKpi(s, 810, 170, 300, 124, "EUR 1,122.49", "FY2025 net result", C.navy);
  addKpi(s, 810, 318, 300, 124, "EUR 24,500.00", "FY2025 subsidies", C.navy);
  addKpi(s, 810, 466, 300, 124, "EUR 500,000", "maximum expected EIC support", C.navy);
  addFooter(s, 1, "FY2025 signed accounting records; EIC Pre-Accelerator records summary");
}

slideCover();

{
  const s = presentation.slides.add();
  addHeader(s, "Executive snapshot", "Transition year with a stronger FY2025 baseline", "The strongest narrative is progress with discipline: improved financial baseline, grant-backed development, and transparent evidence boundaries.", 2);
  addKpi(s, 80, 310, 250, 120, "EUR 12,458.22", "FY2025 total assets");
  addKpi(s, 360, 310, 250, 120, "EUR 3,510.80", "FY2025 equity");
  addKpi(s, 640, 310, 250, 120, "EUR 3,856.90", "FY2025 cash and deposits");
  addKpi(s, 920, 310, 250, 120, "EUR 8,947.42", "FY2025 liabilities", C.amber);
  addSectionCard(s, 80, 470, 340, 130, "What improved", "FY2025 moved from FY2024 negative net result and negative equity to a positive net result and positive equity.", C.teal);
  addSectionCard(s, 470, 470, 340, 130, "What remains early", "Commercial revenue recognition was EUR 100.00 in sales and services. Subsidies remained central.", C.amber);
  addSectionCard(s, 860, 470, 310, 130, "What to verify next", "Cash-flow, payment timing, regulatory status, customer evidence, and management-approved KPIs.", C.blue);
}

{
  const s = presentation.slides.add();
  addHeader(s, "Vision and mission", "Make breast imaging AI useful inside clinical workflows", "The company direction is grounded in multimodality breast imaging, evidence development, and hospital-facing value.", 3);
  addSectionCard(s, 78, 320, 340, 210, "Vision", "AI that strengthens clinical judgement in breast imaging and supports safer, more efficient screening and diagnostic pathways.", C.blue);
  addSectionCard(s, 470, 320, 340, 210, "Mission", "Develop evidence-backed software that connects model performance, multimodality workflow, and operational decision support.", C.teal);
  addSectionCard(s, 860, 320, 320, 210, "Evidence boundary", "The current source set supports research and development positioning. It does not establish regulatory authorization or clinical deployment at scale.", C.amber);
}

{
  const s = presentation.slides.add();
  addHeader(s, "Problem", "Breast imaging needs accuracy, throughput, and trust at the same time", "The investor case is strongest when framed around clinical workflow pressure and evidence translation, not unsupported market claims.", 4);
  addSectionCard(s, 80, 308, 260, 230, "Clinical complexity", "Breast imaging combines mammography, ultrasound, MRI, prior exams, reports, and clinician judgement.", C.blue);
  addSectionCard(s, 370, 308, 260, 230, "Workflow pressure", "Screening and diagnosis require prioritization, consistency, documentation, and efficient reader support.", C.teal);
  addSectionCard(s, 660, 308, 260, 230, "Economic pressure", "False positives, delays, workload, and repeat procedures create cost and resource exposure.", C.amber);
  addSectionCard(s, 950, 308, 230, 230, "Trust gap", "Adoption depends on usability, transparency, governance, and validation evidence.", C.navy);
}

{
  const s = presentation.slides.add();
  addHeader(s, "Solution", "A platform thesis around multimodality, workflow, and evidence", "The product story should connect decision support to measurable hospital value while preserving clear clinical responsibility.", 5);
  addSectionCard(s, 90, 292, 330, 210, "1. Platform", "A software layer for breast imaging AI use cases, evidence packaging, analytics, and reporting.", C.blue);
  addSectionCard(s, 475, 292, 330, 210, "2. Workflow", "Clinical workflow orientation across imaging modalities, review steps, decision points, and governance.", C.teal);
  addSectionCard(s, 860, 292, 330, 210, "3. Evidence", "Scientific publications, financial discipline, and source-backed communications that separate facts from assumptions.", C.amber);
  addText(s, "Management principle: communicate only what the source set supports; use gaps as an execution roadmap.", 92, 552, 980, 36, { size: 20, bold: true, color: C.navy });
}

{
  const s = presentation.slides.add();
  addHeader(s, "Product overview", "Four public product surfaces, one diligence narrative", "The website architecture now separates business value, workflow impact, overall evidence, and investor reporting.", 6);
  const labels = [
    ["Platform", "Business value, market framing, and multimodality rationale."],
    ["Workflow", "Operational clinical workflow impact and process logic."],
    ["Evidence", "Overall evidence, research maturity, and validation roadmap."],
    ["Reports", "Financial statements, IR presentations, letters, news, and notices."],
  ];
  labels.forEach(([head, body], i) => {
    const x = 80 + i * 285;
    addSectionCard(s, x, 310, 250, 210, head, body, [C.blue, C.teal, C.amber, C.navy][i]);
  });
}

{
  const s = presentation.slides.add();
  addHeader(s, "Technology", "Multimodality is the practical AI architecture for breast imaging", "The source-backed story supports MG, US, and MRI as complementary clinical information channels to be detailed through workflow evidence.", 7);
  addSectionCard(s, 90, 300, 300, 220, "MG", "Screening backbone and population-scale imaging channel. Useful for detection and triage workflows.", C.blue);
  addSectionCard(s, 490, 300, 300, 220, "US", "Complementary assessment channel, often relevant when mammography alone is insufficient for clinical decisions.", C.teal);
  addSectionCard(s, 890, 300, 300, 220, "MRI", "High-information modality for selected diagnostic contexts and multimodal fusion research.", C.amber);
  addText(s, "Technology thesis: value increases when AI respects clinical modality roles instead of treating breast imaging as a single-image problem.", 90, 552, 1030, 44, { size: 20, bold: true, color: C.navy });
}

{
  const s = presentation.slides.add();
  addHeader(s, "Evidence foundation", "Research strength is real, but public claims must stay bounded", "The evidence base supports breast imaging AI research, design, workflow, and translation. It does not yet support every business or clinical deployment claim.", 8);
  addSectionCard(s, 80, 310, 335, 230, "Supported", "Scientific and business materials support a medical AI project focused on breast imaging, multimodality, workflow, and evidence development.", C.teal);
  addSectionCard(s, 470, 310, 335, 230, "Not established", "No signed customers, recurring revenue, audited accounts, regulatory authorization, valuation, or customer-level deployment metrics in the reviewed source set.", C.amber);
  addSectionCard(s, 860, 310, 320, 230, "Investor implication", "The strongest position is disciplined progress plus a clear plan to convert evidence into validated commercial milestones.", C.blue);
}

{
  const s = presentation.slides.add();
  addHeader(s, "Market opportunity", "Large opportunity, source-constrained claims", "The deck can describe why the opportunity matters, but should avoid unsupported TAM, pricing, customer, or revenue projections.", 9);
  addBox(s, 86, 314, 1030, 170, { fill: C.lightBlue, line: "#CFE0F7", shadow: "shadow-none" });
  addText(s, "Opportunity thesis", 118, 340, 360, 32, { size: 22, bold: true, color: C.navy });
  addText(s, "Breast imaging combines population screening scale, diagnostic complexity, scarce clinical time, multimodality data, and increasing demand for transparent AI validation.", 118, 382, 910, 60, { size: 22, color: C.ink });
  addPill(s, "No unsupported TAM", 118, 512, 180, C.amber, C.amberLight);
  addPill(s, "No customer claims", 320, 512, 170, C.amber, C.amberLight);
  addPill(s, "No valuation claim", 510, 512, 165, C.amber, C.amberLight);
  addPill(s, "Use pilots and validation next", 698, 512, 230, C.blue, C.lightBlue);
}

{
  const s = presentation.slides.add();
  addHeader(s, "Business model", "Business model categories are plausible, but not yet proven by revenue", "FY2025 sales and services were EUR 100.00. Future model design should be presented as strategy until contracts and repeatable revenue exist.", 10);
  addSectionCard(s, 90, 296, 250, 220, "Current evidence", "EUR 100.00 in FY2025 sales and services. Subsidies were EUR 24,500.00.", C.amber);
  addSectionCard(s, 370, 296, 250, 220, "Potential SaaS", "Hospital or imaging-center software access, subject to validation, procurement, compliance, and pricing evidence.", C.blue);
  addSectionCard(s, 650, 296, 250, 220, "Potential services", "Evidence packaging, integration, training, or workflow analytics, if supported by contracts later.", C.teal);
  addSectionCard(s, 930, 296, 250, 220, "Potential grants", "Non-dilutive funding remains important for validation and development execution.", C.navy);
}

{
  const s = presentation.slides.add();
  addHeader(s, "Partnerships and ecosystem", "Use documented ecosystem signals, not unsupported partnership claims", "The EIC Pre-Accelerator record is the clearest funding ecosystem signal available in the current source set.", 11);
  addKpi(s, 90, 310, 300, 124, "EUR 500,000", "maximum expected EIC support");
  addKpi(s, 430, 310, 240, 124, "18 months", "project duration");
  addKpi(s, 710, 310, 250, 124, "101310071", "proposal identifier");
  addKpi(s, 1000, 310, 190, 124, "12 Jun 2026", "coordinator signature");
  addText(s, "Important boundary: final EU services signature, payment schedule, and pre-financing percentage were not available in the reviewed evidence.", 92, 492, 1000, 54, { size: 21, bold: true, color: C.navy });
}

{
  const s = presentation.slides.add();
  addHeader(s, "Financial highlights", "FY2025 improved; interim FY2026 flags cash planning", "These figures should anchor investor diligence before any forward-looking forecast is issued.", 12);
  slide_charts_financial(s);
}

function slide_charts_financial(s) {
  slide_charts_bar(s, 85, 320, 500, 245, ["FY2024", "FY2025"], [-711.69, 1122.49], "Net result (EUR)", [C.amber, C.teal]);
  slide_charts_bar(s, 650, 320, 500, 245, ["FY2024", "FY2025", "Interim 2026"], [721.34, 3856.9, 258.3], "Cash and deposits (EUR)", [C.blue, C.teal, C.amber]);
  addText(s, "FY2025 source-backed signals: EUR 12,458.22 assets, EUR 3,510.80 equity, EUR 8,947.42 liabilities, EUR 24,500.00 subsidies, EUR 100.00 sales and services.", 88, 578, 1050, 38, { size: 18, color: C.ink });
}

function slide_charts_bar(s, x, y, w, h, cats, vals, title, colors) {
  addBox(s, x, y, w, h, { fill: C.white, line: C.line, shadow: "shadow-sm" });
  addText(s, title, x + 20, y + 18, w - 40, 26, { size: 18, bold: true, color: C.navy });
  const maxAbs = Math.max(...vals.map((v) => Math.abs(v)));
  const baseY = y + 168;
  const barW = 70;
  cats.forEach((cat, i) => {
    const v = vals[i];
    const bh = Math.max(8, Math.abs(v) / maxAbs * 104);
    const bx = x + 75 + i * 135;
    const by = v >= 0 ? baseY - bh : baseY;
    addShape(s, { geometry: "rect", position: { left: bx, top: by, width: barW, height: bh }, fill: colors[i] ?? C.blue, line: { style: "solid", fill: "none", width: 0 } });
    addText(s, `EUR ${v.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`, bx - 18, v >= 0 ? by - 26 : by + bh + 6, 110, 22, { size: 11, bold: true, color: C.navy, align: "center" });
    addText(s, cat, bx - 15, y + h - 38, 100, 22, { size: 12, color: C.muted, align: "center" });
  });
  addShape(s, { geometry: "line", position: { left: x + 50, top: baseY, width: w - 90, height: 0 }, fill: "none", line: { style: "solid", fill: C.line, width: 1 } });
}

{
  const s = presentation.slides.add();
  addHeader(s, "Milestones and risks", "Progress is credible when the risk register is explicit", "The public story should convert gaps into diligence tasks and execution milestones.", 13);
  const riskCards = [
    ["Financials", "Supported: FY2025 positive net result.", "Risk: cash planning after interim FY2026.", "Next: cash-flow and accounting notes.", C.teal],
    ["Funding", "Supported: EIC up to EUR 500,000.", "Risk: payment timing not confirmed.", "Next: final GA and payment schedule.", C.blue],
    ["Commercial", "Supported: EUR 100.00 sales/services.", "Risk: revenue model unproven.", "Next: contracts and repeatability.", C.amber],
    ["Clinical/regulatory", "Supported: research and workflow evidence.", "Risk: authorization not established.", "Next: validation and regulatory milestones.", C.navy],
  ];
  riskCards.forEach(([head, status, risk, next, accent], i) => {
    const x = 80 + i * 280;
    addBox(s, x, 300, 250, 255, { fill: C.white, line: C.line, shadow: "shadow-sm" });
    addBox(s, x + 18, 320, 42, 6, { fill: accent, line: accent, radius: "rounded-full", shadow: "shadow-none" });
    addText(s, head, x + 18, 344, 210, 30, { size: 20, bold: true, color: C.navy });
    addText(s, status, x + 18, 388, 210, 42, { size: 14, color: C.ink });
    addText(s, risk, x + 18, 442, 210, 42, { size: 14, color: C.ink });
    addText(s, next, x + 18, 496, 210, 42, { size: 14, bold: true, color: C.navy });
  });
}

{
  const s = presentation.slides.add();
  addHeader(s, "Growth strategy and outlook", "Next phase: convert evidence into validated operating milestones", "The most credible investor path is to show disciplined funding execution, validation progress, and commercial proof as each becomes documented.", 14);
  addSectionCard(s, 80, 310, 250, 210, "1. Funding execution", "Confirm final EIC signature, pre-financing percentage, first tranche amount, and receipt timing.", C.blue);
  addSectionCard(s, 360, 310, 250, 210, "2. Evidence conversion", "Translate research and workflow findings into validation plans, endpoints, and governance materials.", C.teal);
  addSectionCard(s, 640, 310, 250, 210, "3. Commercial proof", "Move from model categories to source-backed contracts, pilots, pricing, and repeatability.", C.amber);
  addSectionCard(s, 920, 310, 250, 210, "4. Reporting maturity", "Add cash-flow statements, accounting notes, KPI definitions, and board-approved forward guidance.", C.navy);
  addText(s, "Closing position: BreastScreening-AI has a stronger FY2025 baseline and a documented non-dilutive funding opportunity, but must now evidence cash, validation, and commercial milestones.", 82, 560, 1030, 54, { size: 20, bold: true, color: C.navy });
}

await fs.mkdir(SLIDES_DIR, { recursive: true });
await fs.mkdir(LAYOUT_DIR, { recursive: true });

for (const [index, slide] of presentation.slides.items.entries()) {
  const stem = `slide-${String(index + 1).padStart(2, "0")}`;
  await writeBlob(path.join(SLIDES_DIR, `${stem}.png`), await presentation.export({ slide, format: "png", scale: 1 }));
  const layout = await slide.export({ format: "layout" });
  await fs.writeFile(path.join(LAYOUT_DIR, `${stem}.layout.json`), await layout.text());
}

await writeBlob(path.join(WORK, "deck-montage.webp"), await presentation.export({ format: "webp", montage: { columns: 4, slideWidth: 320, padding: 24, gap: 18, background: "#F7FAFD" }, scale: 1 }));

const pptx = await PresentationFile.exportPptx(presentation);
await pptx.save(OUT_PPTX);
console.log(OUT_PPTX);

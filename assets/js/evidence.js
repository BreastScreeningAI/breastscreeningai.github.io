(function () {
  "use strict";

  if (typeof Plotly === "undefined") return;

  var colors = { navy: "#10233c", blue: "#5f8fd8", green: "#36a887", pink: "#da4f91", gray: "#66758a" };
  var baseLayout = {
    font: { family: "Inter, Arial, sans-serif", color: colors.navy },
    margin: { l: 48, r: 20, t: 34, b: 52 },
    paper_bgcolor: "rgba(0,0,0,0)",
    plot_bgcolor: "rgba(0,0,0,0)",
    showlegend: true,
    legend: { orientation: "h", y: -0.2 }
  };
  var config = { responsive: true, displayModeBar: false };

  var milestones = [
    { x: 2017, y: 4, label: "Touch annotation", detail: "Foundational interaction and annotation research", color: colors.blue, size: 16 },
    { x: 2020, y: 4, label: "Multimodality workflow", detail: "Mammography, ultrasound and MRI interaction design", color: colors.blue, size: 18 },
    { x: 2021, y: 3, label: "Human-centric assistant", detail: "Clinician-facing explanations and multimodal classification", color: colors.green, size: 20 },
    { x: 2022, y: 2, label: "Clinician-AI evaluation", detail: "Controlled comparison across nine institutions", color: colors.pink, size: 24 },
    { x: 2022.35, y: 3, label: "Adoption model", detail: "Trust and adoption research", color: colors.green, size: 17 },
    { x: 2023, y: 3, label: "Personalized communication", detail: "Assertiveness-based human-AI interaction", color: colors.green, size: 20 },
    { x: 2023.25, y: 1, label: "External validation", detail: "Breast-density model validation", color: colors.pink, size: 18 },
    { x: 2023.55, y: 1, label: "MRI model research", detail: "Multimodal fusion and weak supervision", color: colors.pink, size: 20 },
    { x: 2024, y: 2, label: "Research synthesis", detail: "Doctoral thesis and protected intellectual property", color: colors.gray, size: 18 },
    { x: 2025, y: 3, label: "Adaptive explanations", detail: "Communication adapted to clinician expertise", color: colors.green, size: 20 },
    { x: 2025.75, y: 0, label: "Hospital integration", detail: "Exploratory workflow and usability activity", color: colors.navy, size: 24 },
    { x: 2026, y: 0, label: "Clinical reporting", detail: "CHTMAD structured-reporting research", color: colors.navy, size: 20 }
  ];

  Plotly.newPlot("validation-timeline-chart", [{
    x: milestones.map(function (item) { return item.x; }),
    y: milestones.map(function (item) { return item.y; }),
    text: milestones.map(function (item) { return item.label; }),
    customdata: milestones.map(function (item) { return item.detail; }),
    mode: "markers+text",
    type: "scatter",
    textposition: milestones.map(function (item, index) { return index % 2 ? "bottom center" : "top center"; }),
    textfont: { size: 11, color: colors.navy },
    hovertemplate: "<b>%{text}</b><br>%{customdata}<extra></extra>",
    marker: {
      size: milestones.map(function (item) { return item.size; }),
      color: milestones.map(function (item) { return item.color; }),
      line: { color: "#ffffff", width: 2 }
    }
  }], Object.assign({}, baseLayout, {
    showlegend: false,
    hoverlabel: { bgcolor: colors.navy, font: { color: "#ffffff" } },
    xaxis: { range: [2016.55, 2026.45], dtick: 1, fixedrange: true, gridcolor: "#dfe7f0", zeroline: false },
    yaxis: {
      range: [-0.55, 4.55],
      tickvals: [0, 1, 2, 3, 4],
      ticktext: ["Clinical integration", "Model validation", "Clinical evaluation", "Human factors", "Interface design"],
      fixedrange: true,
      gridcolor: "#edf1f6",
      zeroline: false
    },
    shapes: [
      { type: "rect", x0: 2016.55, x1: 2020.5, y0: -0.55, y1: 4.55, fillcolor: "rgba(95,143,216,0.08)", line: { width: 0 }, layer: "below" },
      { type: "rect", x0: 2020.5, x1: 2024.5, y0: -0.55, y1: 4.55, fillcolor: "rgba(54,168,135,0.08)", line: { width: 0 }, layer: "below" },
      { type: "rect", x0: 2024.5, x1: 2026.45, y0: -0.55, y1: 4.55, fillcolor: "rgba(218,79,145,0.08)", line: { width: 0 }, layer: "below" }
    ],
    annotations: [
      { x: 2018.5, y: 4.42, text: "FOUNDATIONS", showarrow: false, font: { size: 11, color: colors.blue } },
      { x: 2022.5, y: 4.42, text: "EVALUATION", showarrow: false, font: { size: 11, color: colors.green } },
      { x: 2025.45, y: 4.42, text: "INTEGRATION", showarrow: false, font: { size: 11, color: colors.pink } }
    ],
    margin: { l: 145, r: 34, t: 30, b: 52 }
  }), config);
}());

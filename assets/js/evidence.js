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

  Plotly.newPlot("outputs-chart", [
    { name: "Scholarly", x: [2017, 2020, 2021, 2022, 2023, 2024, 2025], y: [2, 1, 1, 2, 4, 1, 1], type: "bar", marker: { color: colors.blue } },
    { name: "Patent families", x: [2017, 2020, 2021, 2022, 2023, 2024, 2025], y: [0, 0, 0, 1, 1, 0, 0], type: "bar", marker: { color: colors.pink } }
  ], Object.assign({}, baseLayout, { title: { text: "Curated outputs by year", font: { size: 17 } }, barmode: "stack", xaxis: { dtick: 1, fixedrange: true }, yaxis: { title: "Outputs", dtick: 1, fixedrange: true } }), config);

  Plotly.newPlot("reach-chart", [{
    x: [31, 45, 52, 7], y: ["Early human-centred study", "2022 clinician-AI study", "Adoption/personalization research", "Hospital da Luz pilot"],
    type: "bar", orientation: "h", text: ["31", "45", "52", "7"], textposition: "auto", marker: { color: [colors.blue, colors.green, colors.pink, colors.gray] }
  }], Object.assign({}, baseLayout, { title: { text: "Reported study participations", font: { size: 17 } }, showlegend: false, xaxis: { title: "Participants", fixedrange: true }, yaxis: { autorange: "reversed", fixedrange: true }, margin: { l: 180, r: 20, t: 34, b: 52 } }), config);

  Plotly.newPlot("validation-timeline-chart", [{
    x: [2017, 2020, 2021, 2022, 2022.2, 2023, 2023.2, 2023.4, 2024, 2025, 2025.8, 2026],
    y: ["Interface design", "Interface design", "Human factors", "Clinical evaluation", "Human factors", "Human factors", "Model validation", "Model development", "IP and synthesis", "Human factors", "Clinical integration", "Clinical integration"],
    text: ["Touch annotation", "Multimodality workflow", "Human-centric assistant", "Clinician-AI comparison", "Adoption modeling", "Personalized communication", "External density validation", "MRI fusion and weak supervision", "Doctoral synthesis and patent", "Expertise-adaptive explanations", "Hospital da Luz integration", "CHTMAD reporting research"],
    mode: "markers+text", type: "scatter", textposition: "top center", hovertemplate: "%{x}: %{text}<extra></extra>",
    marker: { size: 14, color: [colors.blue, colors.blue, colors.green, colors.pink, colors.green, colors.green, colors.pink, colors.pink, colors.gray, colors.green, colors.navy, colors.navy] }
  }], Object.assign({}, baseLayout, { showlegend: false, xaxis: { range: [2016.5, 2026.5], dtick: 1, fixedrange: true }, yaxis: { fixedrange: true }, margin: { l: 135, r: 30, t: 45, b: 50 } }), config);

  Plotly.newPlot("economic-impact-chart", [{
    x: ["5%", "10%", "20%"], y: [200, 400, 800], type: "bar", text: ["$200M", "$400M", "$800M"], textposition: "auto", marker: { color: [colors.blue, colors.green, colors.pink] }
  }], Object.assign({}, baseLayout, { showlegend: false, xaxis: { title: "Scenario reduction", fixedrange: true }, yaxis: { title: "USD millions, gross opportunity", fixedrange: true }, font: { family: "Inter, Arial, sans-serif", color: "#d7e1ec" } }), config);

  Plotly.newPlot("false-negative-chart", [{
    x: ["Clinician only", "Clinician + AI"], y: [6000, 2000], type: "bar", text: ["6,000", "2,000"], textposition: "auto", marker: { color: [colors.gray, colors.green] }
  }], Object.assign({}, baseLayout, { showlegend: false, xaxis: { fixedrange: true }, yaxis: { title: "Per 100,000 classifications", fixedrange: true }, font: { family: "Inter, Arial, sans-serif", color: "#d7e1ec" } }), config);

  Plotly.newPlot("time-impact-chart", [{
    x: ["100k", "1m", "10m"], y: [1917, 19167, 191667], type: "bar", text: ["1,917h", "19,167h", "191,667h"], textposition: "auto", marker: { color: [colors.blue, colors.green, colors.pink] }
  }], Object.assign({}, baseLayout, { showlegend: false, xaxis: { title: "Annual eligible reviews", fixedrange: true }, yaxis: { title: "Capacity hours", type: "log", fixedrange: true }, font: { family: "Inter, Arial, sans-serif", color: "#d7e1ec" } }), config);
}());

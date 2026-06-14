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

  Plotly.newPlot("clinical-impact-chart", [{
    x: ["5%", "10%", "20%"], y: [5000, 10000, 20000], type: "bar", text: ["5,000", "10,000", "20,000"], textposition: "auto", marker: { color: [colors.blue, colors.green, colors.pink] }
  }], Object.assign({}, baseLayout, { showlegend: false, xaxis: { title: "Scenario reduction", fixedrange: true }, yaxis: { title: "Avoided events per 100,000", fixedrange: true }, font: { family: "Inter, Arial, sans-serif", color: "#d7e1ec" } }), config);

  Plotly.newPlot("economic-impact-chart", [{
    x: ["5%", "10%", "20%"], y: [200, 400, 800], type: "bar", text: ["$200M", "$400M", "$800M"], textposition: "auto", marker: { color: [colors.blue, colors.green, colors.pink] }
  }], Object.assign({}, baseLayout, { showlegend: false, xaxis: { title: "Scenario reduction", fixedrange: true }, yaxis: { title: "USD millions, gross opportunity", fixedrange: true }, font: { family: "Inter, Arial, sans-serif", color: "#d7e1ec" } }), config);
}());

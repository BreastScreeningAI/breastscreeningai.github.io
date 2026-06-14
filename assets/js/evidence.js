(function () {
  "use strict";

  if (typeof Plotly === "undefined") {
    return;
  }

  var font = { family: "Arial, sans-serif", color: "#243247" };
  var config = {
    displaylogo: false,
    displayModeBar: false,
    responsive: true,
    scrollZoom: false
  };

  Plotly.newPlot("chtmad-chart", [{
    type: "scatter",
    mode: "markers+text",
    x: ["2025-11-19", "2026-01-07", "2026-01-28"],
    y: [1, 1, 1],
    text: ["17-21 Nov", "5-9 Jan", "26-30 Jan"],
    textposition: ["top center", "bottom center", "top center"],
    marker: {
      color: ["#5f8fd8", "#da4f91", "#36a887"],
      line: { color: "#ffffff", width: 3 },
      size: 22
    },
    hovertext: [
      "17-21 November 2025: initial fieldwork",
      "5-9 January 2026: structured reporting research",
      "26-30 January 2026: follow-up fieldwork"
    ],
    hovertemplate: "%{hovertext}<extra></extra>"
  }], {
    font: font,
    height: 390,
    margin: { t: 64, r: 42, b: 70, l: 42 },
    paper_bgcolor: "rgba(0,0,0,0)",
    plot_bgcolor: "rgba(0,0,0,0)",
    showlegend: false,
    xaxis: { range: ["2025-11-08", "2026-02-08"], tickformat: "%b %Y", gridcolor: "#d6e7e2", fixedrange: true },
    yaxis: { range: [0.72, 1.28], showgrid: false, showticklabels: false, zeroline: true, zerolinecolor: "#7d8795", fixedrange: true }
  }, config);
}());

(function () {
  "use strict";

  function escapeHtml(value) {
    return String(value)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/\"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }

  function externalAttributes(url) {
    return /^https?:\/\//.test(url) ? ' target="_blank" rel="noopener noreferrer"' : "";
  }

  function renderPublications(items) {
    var list = document.getElementById("publication-list");
    var count = document.getElementById("publication-count");
    var buttons = document.querySelectorAll("[data-publication-filter]");
    var activeFilter = "All";

    function draw() {
      var visible = items.filter(function (item) {
        if (activeFilter === "Thesis") return /thesis$/i.test(item.type);
        return activeFilter === "All" || item.type === activeFilter;
      });

      count.textContent = visible.length + (visible.length === 1 ? " selected record" : " selected records");
      list.innerHTML = visible.map(function (item) {
        var tags = item.topics.map(function (topic) {
          return '<span class="content-tag">' + escapeHtml(topic) + "</span>";
        }).join("");
        var link = item.url
          ? '<a class="content-link" href="' + escapeHtml(item.url) + '"' + externalAttributes(item.url) + '>Open authoritative record <i class="lni lni-arrow-top-right"></i></a>'
          : '<span class="content-pending">Repository link pending verification</span>';

        return '<article class="content-card">' +
          '<div class="content-card-meta"><span>' + escapeHtml(item.year) + '</span><span>' + escapeHtml(item.type) + "</span></div>" +
          '<h2>' + escapeHtml(item.title) + "</h2>" +
          '<p class="content-authors">' + escapeHtml(item.authors) + "</p>" +
          '<p class="content-venue">' + escapeHtml(item.venue) + "</p>" +
          '<div class="content-tags">' + tags + "</div>" +
          '<p class="content-lineage"><strong>Project relationship:</strong> ' + escapeHtml(item.lineage) + "</p>" +
          link + "</article>";
      }).join("");
    }

    buttons.forEach(function (button) {
      button.addEventListener("click", function () {
        activeFilter = button.getAttribute("data-publication-filter");
        buttons.forEach(function (candidate) { candidate.classList.remove("active"); });
        button.classList.add("active");
        draw();
      });
    });

    draw();
  }

  function renderNews(items) {
    var list = document.getElementById("news-list");
    list.innerHTML = items.map(function (item) {
      var date = new Date(item.date + "T00:00:00").toLocaleDateString("en-GB", {
        day: "numeric", month: "long", year: "numeric"
      });
      return '<article class="news-entry">' +
        '<div class="news-date"><span>' + escapeHtml(item.type) + "</span><time datetime=\"" + escapeHtml(item.date) + '\">' + escapeHtml(date) + "</time></div>" +
        '<div><h2>' + escapeHtml(item.title) + "</h2><p>" + escapeHtml(item.summary) + "</p>" +
        '<a class="content-link" href="' + escapeHtml(item.url) + '"' + externalAttributes(item.url) + ">" + escapeHtml(item.linkLabel) + ' <i class="lni lni-arrow-top-right"></i></a></div>' +
        "</article>";
    }).join("");
  }

  var source = document.body.getAttribute("data-content-source");
  if (!source) return;

  fetch(source)
    .then(function (response) {
      if (!response.ok) throw new Error("Content could not be loaded.");
      return response.json();
    })
    .then(function (items) {
      if (document.getElementById("publication-list")) renderPublications(items);
      if (document.getElementById("news-list")) renderNews(items);
    })
    .catch(function () {
      var target = document.getElementById("publication-list") || document.getElementById("news-list");
      if (target) target.innerHTML = '<p class="content-error">The catalogue is temporarily unavailable. Please try again later.</p>';
    });
}());

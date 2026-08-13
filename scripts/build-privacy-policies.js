#!/usr/bin/env node
/**
 * Build privacy policies from markdown sources.
 * Generates:
 *   1. HTML at /privacy-policies/{slug}.html (for store links)
 *   2. privacy.json in each app repo's Resources/Raw/ (for in-app rendering)
 */

const fs = require("fs");
const path = require("path");

const REPO_ROOT = path.dirname(__dirname);
const PRIVACY_SRC = path.join(REPO_ROOT, "privacy");
const PRIVACY_OUT = path.join(REPO_ROOT, "privacy-policies");
const DOCS_ROOT = path.dirname(REPO_ROOT);

// Map of markdown files to their slug, app identity, and repo path
const APP_MAPPING = {
  "travel-binder.md": {
    slug: "travel-binder",
    app: "The Travel Binder",
    color: "#22314A",
    accent: "#C2442D",
    pkg: "com.eritech.travelbinder",
    repo: "travel-binder",
    project: "TravelBinder",
  },
  "the-bake-log.md": {
    slug: "the-bake-log",
    app: "The Bake Log",
    color: "#2C2523",
    accent: "#C26D43",
    pkg: "com.eritech.thebakelog",
    repo: "the-bake-log",
    project: "TheBakeLog",
  },
  "kohii.md": {
    slug: "kohii",
    app: "Kohii",
    color: "#4A2C1A",
    accent: "#C8974A",
    pkg: "com.eritech.kohii",
    repo: "kohii",
    project: "kohii-the-coffee-log",
  },
  "cellar-book.md": {
    slug: "cellar-book",
    app: "Cellar Book",
    color: "#EDEDED",
    bg: "#15171A",
    accent: "#D4B595",
    pkg: "com.eritech.cellarbook",
    repo: "cellar-book",
    project: "CellarBook",
  },
  "leaflet.md": {
    slug: "leaflet",
    app: "Leaflet",
    color: "#F1F8F1",
    bg: "#0D1F0F",
    accent: "#4CAF50",
    pkg: "com.eritech.leaflet",
    repo: "leaflet",
    project: "Leaflet",
  },
  "warranty-box.md": {
    slug: "warranty-box",
    app: "Warranty Box",
    color: "#333",
    accent: "#7A3B24",
    pkg: "com.eritech.warrantybox",
    repo: "warranty-box",
    project: "",
  },
};

function parseFrontmatter(content) {
  const match = content.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
  if (!match) return { meta: {}, body: content };

  const meta = {};
  match[1].split("\n").forEach((line) => {
    const [k, v] = line.split(": ");
    if (k && v) meta[k] = v;
  });

  return { meta, body: match[2] };
}

function parseMarkdownSections(body) {
  const sections = [];
  let current = null;

  body.split("\n").forEach((line) => {
    if (line.startsWith("## ")) {
      if (current) sections.push(current);
      current = { heading: line.replace(/^## /, "").trim(), body: [] };
    } else if (current && line.trim()) {
      current.body.push(line);
    }
  });

  if (current) sections.push(current);

  return sections.map((s) => ({
    heading: s.heading,
    body: s.body.join("\n").trim(),
  }));
}

function markdownToHtml(body) {
  return body
    .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
    .replace(/__(.*?)__/g, "<strong>$1</strong>")
    .replace(/\*(.*?)\*/g, "<em>$1</em>")
    .replace(/___(.*?)___/g, "<em>$1</em>")
    .replace(/\n\n+/g, "</p><p>")
    .replace(/^/g, "<p>")
    .replace(/$/g, "</p>");
}

function generateHtml(app, sections, updated) {
  const isDark =
    app.color === "#EDEDED" || app.color === "#F1F8F1" || app.color === "#333";
  const bgColor = app.bg || (isDark ? "#000" : "#FFF");
  const textColor = app.color || "#333";

  let html = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Privacy Policy - ${app.app}</title>
<link rel="canonical" href="https://eritech.studio/privacy-policies/${app.slug}.html">
<meta name="description" content="Privacy policy for ${app.app} by Eri Tech Studio. Fully offline — your data stays on your device. No account, no cloud, no tracking.">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<style>
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  line-height: 1.6;
  color: ${textColor};
  background-color: ${bgColor};
  max-width: 800px;
  margin: 0 auto;
  padding: 40px 20px;
}
h1 {
  font-family: Georgia, "Times New Roman", serif;
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
  color: ${textColor};
}
h2 {
  font-family: Georgia, "Times New Roman", serif;
  font-size: 1.5rem;
  margin-top: 2rem;
  margin-bottom: 1rem;
  color: ${textColor};
  border-bottom: 1px solid ${isDark ? "#333" : "#E0E0E0"};
  padding-bottom: 0.5rem;
}
p {
  margin-bottom: 1rem;
  color: ${isDark ? "#CCC" : "#666"};
}
.date {
  color: ${isDark ? "#999" : "#888"};
  font-size: 0.9rem;
  margin-bottom: 2rem;
}
a, a:visited {
  color: ${app.accent};
  text-decoration: underline;
  text-underline-offset: 2px;
  text-decoration-thickness: 1px;
}
a:hover {
  text-decoration: underline;
}
</style>
</head>
<body>
<h1>Privacy Policy</h1>
<div class="date">Last Updated: ${updated}</div>

`;

  sections.forEach((section) => {
    html += `<h2>${section.heading}</h2>\n`;
    const htmlBody = markdownToHtml(section.body);
    html += htmlBody + "\n\n";
  });

  html += `</body>
</html>`;

  return html;
}

// The HTML branch turns markdown into tags; the JSON branch must turn it into PLAIN text, or a
// MAUI Label renders "**confirmation codes**" with the asterisks showing. Strip the same inline
// marks the source can carry (bold, italic, links → their text), leaving paragraphs newline-joined.
function markdownToPlainText(body) {
  return body
    .replace(/\*\*(.*?)\*\*/g, "$1")
    .replace(/__(.*?)__/g, "$1")
    .replace(/\*(.*?)\*/g, "$1")
    .replace(/_(.*?)_/g, "$1")
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g, "$1 ($2)");
}

function generatePrivacyJson(sections, updated) {
  return {
    sections: sections.map((s) => ({
      heading: markdownToPlainText(s.heading),
      body: markdownToPlainText(s.body),
    })),
    updated,
  };
}

// Main
console.log("📋 Building privacy policies...\n");

fs.readdirSync(PRIVACY_SRC)
  .filter((f) => f.endsWith(".md"))
  .forEach((file) => {
    const mapping = APP_MAPPING[file];
    if (!mapping) {
      console.warn(`⚠️  No mapping for ${file}, skipping`);
      return;
    }

    const content = fs.readFileSync(path.join(PRIVACY_SRC, file), "utf8");
    const { meta, body } = parseFrontmatter(content);
    const sections = parseMarkdownSections(body);
    const updated = meta.updated || new Date().toISOString().split("T")[0];

    // Generate HTML
    const html = generateHtml(mapping, sections, updated);
    const htmlPath = path.join(PRIVACY_OUT, `${mapping.slug}.html`);
    fs.writeFileSync(htmlPath, html);
    console.log(`✅ ${htmlPath}`);

    // Generate JSON
    const json = generatePrivacyJson(sections, updated);
    const jsonPath = path.join(PRIVACY_SRC, `${mapping.slug}.json`);
    fs.writeFileSync(jsonPath, JSON.stringify(json, null, 2));
    console.log(`✅ ${jsonPath}`);

    // Copy JSON into the app's MAUI project so it ships inside the binary. The Resources/Raw dir is
    // under the .csproj — NOT the repo root — and only WarrantyBox keeps its project at the root.
    // The old code joined the repo root for everyone and mkdir'd the result, so four of six apps
    // silently grew a Resources/Raw at the wrong level and shipped nothing. `project` is the .csproj
    // subdirectory (empty for a root-level project), and the directory is required to already
    // exist: every app has one with the MauiAsset glob, so a missing one is a reliable wrong-path
    // signal that must fail loudly rather than be created.
    if (mapping.repo) {
      const appRepoPath = path.join(DOCS_ROOT, mapping.repo);
      const resourcesPath = path.join(
        appRepoPath,
        mapping.project || "",
        "Resources",
        "Raw"
      );
      if (!fs.existsSync(appRepoPath)) {
        console.warn(`   ⚠️  ${appRepoPath} not found — skipped`);
      } else if (!fs.existsSync(resourcesPath)) {
        throw new Error(
          `${resourcesPath} does not exist. Check the 'project' subdirectory for ${mapping.slug} ` +
            `— never mkdir it, or the app ships an unpackaged copy at the wrong level.`
        );
      } else {
        const appJsonPath = path.join(resourcesPath, "privacy.json");
        fs.writeFileSync(appJsonPath, JSON.stringify(json, null, 2));
        console.log(`   📦 ${appJsonPath}`);
      }
    }
  });

console.log(
  "\n✨ Privacy policies synced across site and all app repos.\n"
);

const projects = [
  {
    name: "PurimMonitor",
    stack: "Python · Flask · psutil",
    purpose: "Service health API with status, version, uptime, and runtime metadata.",
    tags: ["API", "Python", "Tests"],
    href: "../PurimMonitor/"
  },
  {
    name: "SecureShare",
    stack: "Node.js · Express",
    purpose: "Temporary sharing API prototype with route protection, configuration, and tests.",
    tags: ["Backend", "Node.js", "Express"],
    href: "../SecureShare/"
  },
  {
    name: "NetWatch",
    stack: "Python CLI",
    purpose: "Local diagnostic helper with explicit inputs and improved validation.",
    tags: ["CLI", "Validation", "Utility"],
    href: "../NetWatch/"
  },
  {
    name: "LogLens",
    stack: "Python CLI",
    purpose: "Log summary helper with readable and JSON output for quick reviews.",
    tags: ["Parsing", "Logs", "Automation"],
    href: "../LogLens/"
  },
  {
    name: "PortalCheck",
    stack: "Python CLI",
    purpose: "Setup-note reviewer for planning signals, checklists, and project readiness.",
    tags: ["Planning", "Text Review", "CLI"],
    href: "../PortalCheck/"
  }
];

function createProjectCard(project) {
  const card = document.createElement("article");
  card.className = "project-card";

  const tagHtml = project.tags.map((tag) => `<span>${tag}</span>`).join("");

  card.innerHTML = `
    <div>
      <p class="stack">${project.stack}</p>
      <h3>${project.name}</h3>
      <p>${project.purpose}</p>
      <div class="tags">${tagHtml}</div>
    </div>
    <a class="card-link" href="${project.href}">Open project →</a>
  `;

  return card;
}

const projectGrid = document.querySelector("#projectGrid");

projects.forEach((project) => {
  projectGrid.appendChild(createProjectCard(project));
});

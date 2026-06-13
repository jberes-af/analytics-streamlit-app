// ../../src/gui/streamlit/static/diagram/init.js
import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs";

// ../../src/gui/streamlit/static/diagram/renderers/render_common.js
function setText(elementId, value) {
  const element = document.getElementById(elementId);
  if (element) {
    element.textContent = value;
  }
}
function createMutedText(text) {
  const paragraph = document.createElement("p");
  paragraph.textContent = text;
  paragraph.className = "muted";
  return paragraph;
}
function createMutedListItem(text) {
  const item = document.createElement("li");
  item.textContent = text;
  item.className = "muted";
  return item;
}
function renderStringList(elementId, items) {
  const container = document.getElementById(elementId);
  if (!container) return;
  container.innerHTML = "";
  if (!items || items.length === 0) {
    container.appendChild(createMutedListItem("None specified."));
    return;
  }
  items.forEach((value) => {
    const item = document.createElement("li");
    item.textContent = value;
    container.appendChild(item);
  });
}
function renderNavigationRoutes(elementId, routes) {
  const container = document.getElementById(elementId);
  if (!container) return;
  container.innerHTML = "";
  if (!routes || routes.length === 0) {
    container.appendChild(createMutedListItem("No navigation routes specified."));
    return;
  }
  routes.forEach((route) => {
    const item = document.createElement("li");
    const parts = [
      route.action || "Unnamed action",
      route.target_screen_id ? `\u2192 ${route.target_screen_id}` : "",
      route.condition ? `if ${route.condition}` : "",
      route.notes ? `(${route.notes})` : ""
    ].filter(Boolean);
    item.textContent = parts.join(" ");
    container.appendChild(item);
  });
}
function renderPermissions(elementId, permissions) {
  const container = document.getElementById(elementId);
  if (!container) return;
  container.innerHTML = "";
  if (!permissions || permissions.length === 0) {
    container.appendChild(createMutedListItem("No permissions specified."));
    return;
  }
  permissions.forEach((permission) => {
    const item = document.createElement("li");
    item.textContent = `${permission.domain}:${permission.action}`;
    container.appendChild(item);
  });
}

// ../../src/gui/streamlit/static/diagram/renderers/render_workflows.js
function renderUseCases(elementId, useCases) {
  const container = document.getElementById(elementId);
  if (!container) return;
  container.innerHTML = "";
  if (!useCases || useCases.length === 0) {
    container.appendChild(createMutedText("No use cases specified."));
    return;
  }
  useCases.forEach((useCase) => {
    const card = document.createElement("div");
    card.className = "detail-card";
    const title = document.createElement("h4");
    title.textContent = useCase.name || "Unnamed use case";
    card.appendChild(title);
    if (useCase.description) {
      const description = document.createElement("p");
      description.textContent = useCase.description;
      card.appendChild(description);
    }
    if (useCase.outcome) {
      const outcome = document.createElement("p");
      outcome.textContent = `Outcome: ${useCase.outcome}`;
      outcome.className = "muted";
      card.appendChild(outcome);
    }
    container.appendChild(card);
  });
}
function renderWorkflows(elementId, workflows) {
  const container = document.getElementById(elementId);
  if (!container) return;
  container.innerHTML = "";
  if (!workflows || workflows.length === 0) {
    container.appendChild(createMutedText("No workflows specified."));
    return;
  }
  workflows.forEach((workflow) => {
    const card = document.createElement("div");
    card.className = "detail-card";
    const title = document.createElement("h4");
    title.textContent = workflow.id ? `${workflow.id}: ${workflow.name}` : workflow.name || "Unnamed workflow";
    card.appendChild(title);
    if (workflow.description) {
      const description = document.createElement("p");
      description.textContent = workflow.description;
      card.appendChild(description);
    }
    const metaParts = [];
    if (workflow.goal) metaParts.push(`Goal: ${workflow.goal}`);
    if (workflow.trigger) metaParts.push(`Trigger: ${workflow.trigger}`);
    if (workflow.success_outcome) metaParts.push(`Outcome: ${workflow.success_outcome}`);
    if (metaParts.length > 0) {
      const meta = document.createElement("p");
      meta.className = "muted";
      meta.textContent = metaParts.join(" | ");
      card.appendChild(meta);
    }
    if (workflow.flow && workflow.flow.length > 0) {
      const details = document.createElement("details");
      const summary = document.createElement("summary");
      summary.textContent = "Flow Steps";
      details.appendChild(summary);
      const list = document.createElement("ol");
      workflow.flow.forEach((step) => {
        const item = document.createElement("li");
        item.textContent = `${step.actor}: ${step.action}`;
        if (step.system_response) {
          item.textContent += ` \u2192 ${step.system_response}`;
        }
        list.appendChild(item);
      });
      details.appendChild(list);
      card.appendChild(details);
    }
    container.appendChild(card);
  });
}

// ../../src/gui/streamlit/static/diagram/renderers/render_data_objects.js
function renderDataObjects(elementId, groupedDataObjects) {
  const container = document.getElementById(elementId);
  if (!container) return;
  container.innerHTML = "";
  let hasAny = false;
  groupedDataObjects.forEach(([groupTitle, dataObjects]) => {
    if (!dataObjects || dataObjects.length === 0) return;
    hasAny = true;
    const group = document.createElement("div");
    group.className = "dto-group";
    const heading = document.createElement("h4");
    heading.textContent = groupTitle;
    group.appendChild(heading);
    dataObjects.forEach((dataObject) => {
      const card = document.createElement("div");
      card.className = "data-object-card";
      const title = document.createElement("h4");
      title.textContent = dataObject.name || "Unnamed data object";
      card.appendChild(title);
      if (dataObject.description) {
        const description = document.createElement("p");
        description.textContent = dataObject.description;
        description.className = "data-object-description";
        card.appendChild(description);
      }
      if (dataObject.code) {
        card.appendChild(createCodeDetails("DTO", dataObject.code, true));
      }
      if (dataObject.json_example) {
        card.appendChild(createCodeDetails("JSON Example", dataObject.json_example, false));
      }
      if (!dataObject.description && !dataObject.code && !dataObject.json_example) {
        card.appendChild(createMutedText("No details provided."));
      }
      group.appendChild(card);
    });
    container.appendChild(group);
  });
  if (!hasAny) {
    container.appendChild(createMutedText("No data models specified."));
  }
}
function renderDataReads(elementId, reads) {
  const container = document.getElementById(elementId);
  if (!container) return;
  container.innerHTML = "";
  if (!reads || reads.length === 0) {
    container.appendChild(createMutedText("No data reads defined."));
    return;
  }
  reads.forEach((read) => {
    const card = document.createElement("div");
    card.className = "detail-card";
    const title = document.createElement("h4");
    title.textContent = read.name || "Unnamed read";
    card.appendChild(title);
    if (read.description) {
      const description = document.createElement("p");
      description.textContent = read.description;
      card.appendChild(description);
    }
    if (read.output_dto) {
      const output = document.createElement("p");
      output.className = "muted";
      output.textContent = `Output DTO: ${read.output_dto}`;
      card.appendChild(output);
    }
    if (read.source_dtos && read.source_dtos.length > 0) {
      const sources = document.createElement("p");
      sources.className = "muted";
      sources.textContent = `Sources: ${read.source_dtos.join(", ")}`;
      card.appendChild(sources);
    }
    container.appendChild(card);
  });
}
function renderDataWrites(elementId, writes) {
  const container = document.getElementById(elementId);
  if (!container) return;
  container.innerHTML = "";
  if (!writes || writes.length === 0) {
    container.appendChild(createMutedText("No data writes defined."));
    return;
  }
  writes.forEach((write) => {
    const card = document.createElement("div");
    card.className = "detail-card";
    const title = document.createElement("h4");
    title.textContent = write.name || "Unnamed write";
    card.appendChild(title);
    if (write.description) {
      const description = document.createElement("p");
      description.textContent = write.description;
      card.appendChild(description);
    }
    if (write.target_dtos && write.target_dtos.length > 0) {
      const targets = document.createElement("p");
      targets.className = "muted";
      targets.textContent = `Targets: ${write.target_dtos.join(", ")}`;
      card.appendChild(targets);
    }
    container.appendChild(card);
  });
}
function createCodeDetails(summaryText, codeText, isOpen) {
  const details = document.createElement("details");
  details.open = isOpen;
  const summary = document.createElement("summary");
  summary.textContent = summaryText;
  details.appendChild(summary);
  const pre = document.createElement("pre");
  const code = document.createElement("code");
  code.textContent = codeText;
  pre.appendChild(code);
  details.appendChild(pre);
  return details;
}

// ../../src/gui/streamlit/static/diagram/renderers/render_images.js
function renderImages(images, title) {
  const container = document.getElementById("screen-image-container");
  const empty = document.getElementById("screen-image-empty");
  if (!container) return;
  container.innerHTML = "";
  if (!images || images.length === 0) {
    empty?.classList.remove("hidden");
    return;
  }
  empty?.classList.add("hidden");
  images.forEach((imageSrc, index) => {
    const image = document.createElement("img");
    image.src = imageSrc;
    image.alt = `${title || "Screen sketch"} ${index + 1}`;
    image.className = "drawer-screen-image";
    container.appendChild(image);
  });
}

// ../../src/gui/streamlit/static/diagram/image_drawer.js
function openScreenDrawer(info, nodeId) {
  const drawer = document.getElementById("screen-drawer");
  const title = document.getElementById("screen-drawer-title");
  if (!drawer || !title) return;
  title.textContent = info.title || nodeId;
  const images = info.screen_images || info.images || [];
  drawer.dataset.images = JSON.stringify(images);
  renderImages(
    images,
    info.title || nodeId
  );
  drawer.classList.add("open");
}
function downloadCurrentImage() {
  const drawer = document.getElementById("screen-drawer");
  if (!drawer) return;
  const images = JSON.parse(drawer.dataset.images || "[]");
  if (!images.length) {
    console.warn("No images available.");
    return;
  }
  const imageUrl = images[0];
  const link = document.createElement("a");
  link.href = imageUrl;
  const title = document.getElementById(
    "screen-drawer-title"
  )?.textContent || "screen";
  link.download = `${title.replace(/\s+/g, "_")}.png`;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}
function closeScreenDrawer() {
  document.getElementById("screen-drawer")?.classList.remove("open");
  closeDataModelDrawer();
}
function openDataModelDrawer(info) {
  const drawer = document.getElementById("data-model-drawer");
  const content = document.getElementById("data-model-content");
  if (!drawer || !content) return;
  drawer.dataset.dataModel = JSON.stringify({
    title: info.title || "Screen",
    client_contracts: info.client_contracts || {},
    backend_data_model: info.backend_data_model || {},
    rules_engine: info.rules_engine || {}
  });
  content.innerHTML = "";
  renderDtoGroup(
    content,
    "Domain Objects",
    info.backend_data_model?.definition_dtos || []
  );
  renderDtoGroup(
    content,
    "Persistence DTOs",
    info.backend_data_model?.persistence_dtos || []
  );
  renderDtoGroup(
    content,
    "Screen DTOs",
    info.client_contracts?.screen_dtos || []
  );
  drawer.classList.add("open");
}
function renderDtoGroup(parent, groupTitle, dtos) {
  const section = document.createElement("section");
  section.className = "drawer-dto-section";
  const heading = document.createElement("h4");
  heading.textContent = groupTitle;
  section.appendChild(heading);
  if (!dtos || dtos.length === 0) {
    const empty = document.createElement("p");
    empty.className = "muted";
    empty.textContent = "None specified.";
    section.appendChild(empty);
    parent.appendChild(section);
    return;
  }
  dtos.forEach((dto) => {
    section.appendChild(createDtoCard(dto));
  });
  parent.appendChild(section);
}
function createDtoCard(dto) {
  const card = document.createElement("div");
  card.className = "drawer-dto-card";
  const title = document.createElement("h4");
  title.textContent = dto.name || "Unnamed DTO";
  card.appendChild(title);
  if (dto.description) {
    const description = document.createElement("p");
    description.className = "data-object-description";
    description.textContent = dto.description;
    card.appendChild(description);
  }
  if (dto.code) {
    const details = document.createElement("details");
    details.open = true;
    const summary = document.createElement("summary");
    summary.textContent = "DTO";
    details.appendChild(summary);
    const pre = document.createElement("pre");
    const code = document.createElement("code");
    code.textContent = dto.code;
    pre.appendChild(code);
    details.appendChild(pre);
    card.appendChild(details);
  }
  if (dto.json_example) {
    const details = document.createElement("details");
    const summary = document.createElement("summary");
    summary.textContent = "JSON Example";
    details.appendChild(summary);
    const pre = document.createElement("pre");
    const code = document.createElement("code");
    code.textContent = dto.json_example;
    pre.appendChild(code);
    details.appendChild(pre);
    card.appendChild(details);
  }
  return card;
}
function closeDataModelDrawer() {
  document.getElementById("data-model-drawer")?.classList.remove("open");
}
function bindDrawerControls() {
  document.getElementById("close-screen-drawer-button")?.addEventListener(
    "click",
    closeScreenDrawer
  );
  document.getElementById("close-data-model-button")?.addEventListener(
    "click",
    closeDataModelDrawer
  );
  document.getElementById("download-image-button")?.addEventListener(
    "click",
    downloadCurrentImage
  );
  document.getElementById("download-data-model-button")?.addEventListener("click", downloadCurrentDataModel);
}
function downloadCurrentDataModel() {
  const drawer = document.getElementById("data-model-drawer");
  if (!drawer) return;
  const data = JSON.parse(drawer.dataset.dataModel || "{}");
  const markdown = buildDataModelMarkdown(data);
  const blob = new Blob(
    [markdown],
    { type: "text/markdown;charset=utf-8" }
  );
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = `${slugify(data.title || "data-model")}_data_model.md`;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
  URL.revokeObjectURL(url);
}
function buildDataModelMarkdown(data) {
  const lines = [];
  lines.push(`# ${data.title || "Screen"} Data Model`);
  lines.push("");
  appendDtoSection(
    lines,
    "Domain Objects",
    data.backend_data_model?.definition_dtos || []
  );
  appendDtoSection(
    lines,
    "Persistence DTOs",
    data.backend_data_model?.persistence_dtos || []
  );
  appendDtoSection(
    lines,
    "Screen DTOs",
    data.client_contracts?.screen_dtos || []
  );
  return lines.join("\n");
}
function appendDtoSection(lines, title, dtos) {
  lines.push(`## ${title}`);
  lines.push("");
  if (!dtos || dtos.length === 0) {
    lines.push("_None specified._");
    lines.push("");
    return;
  }
  dtos.forEach((dto) => {
    lines.push(`### ${dto.name || "Unnamed DTO"}`);
    lines.push("");
    if (dto.description) {
      lines.push(dto.description);
      lines.push("");
    }
    if (dto.code) {
      lines.push("```python");
      lines.push(dto.code);
      lines.push("```");
      lines.push("");
    }
    if (dto.json_example) {
      lines.push("```json");
      lines.push(dto.json_example);
      lines.push("```");
      lines.push("");
    }
  });
}
function slugify(value) {
  return value.toLowerCase().replace(/[^a-z0-9]+/g, "_").replace(/^_+|_+$/g, "");
}

// ../../src/gui/streamlit/static/diagram/node_details.js
function showNodeDetails(nodeId) {
  const info = window.patientFlowConfig.nodeInfo[nodeId];
  if (!info) return;
  renderNodeDetailsPanel(info, nodeId);
  openScreenDrawer(info, nodeId);
  bindDataModelButton(info);
}
function renderNodeDetailsPanel(info, nodeId) {
  setText("node-details-title", info.title || nodeId);
  const screenSpec = info.screen_spec || {};
  setText(
    "node-screen-spec",
    screenSpec.purpose || "No screen specification available."
  );
  renderStringList(
    "node-screen-displayed-data",
    screenSpec.displayed_data || []
  );
  renderStringList(
    "node-screen-user-inputs",
    screenSpec.user_inputs || []
  );
  setText(
    "node-screen-primary-action",
    screenSpec.primary_action || "None specified."
  );
  renderStringList(
    "node-screen-secondary-actions",
    screenSpec.secondary_actions || []
  );
  renderStringList(
    "node-screen-validation-rules",
    screenSpec.validation_rules || []
  );
  renderStringList(
    "node-screen-navigation-in",
    screenSpec.navigation_in || []
  );
  renderNavigationRoutes(
    "node-screen-navigation-out",
    screenSpec.navigation_out || []
  );
  setText(
    "node-screen-empty-state",
    screenSpec.states?.empty_state || "None specified."
  );
  setText(
    "node-screen-loading-state",
    screenSpec.states?.loading_state || "None specified."
  );
  setText(
    "node-screen-error-state",
    screenSpec.states?.error_state || "None specified."
  );
  renderUseCases("node-use-cases", info.use_cases || []);
  renderWorkflows("node-workflows", info.workflows || []);
  renderStringList("node-feature-groups", info.feature_groups || []);
  renderDataObjects("node-data_models_client-contracts", [
    ["Request DTOs", info.client_contracts?.request_dtos || []],
    ["Response DTOs", info.client_contracts?.response_dtos || []],
    ["Screen DTOs", info.client_contracts?.screen_dtos || []]
  ]);
  renderDataObjects("node-backend-data-model", [
    ["Definition DTOs", info.backend_data_model?.definition_dtos || []],
    ["Persistence DTOs", info.backend_data_model?.persistence_dtos || []]
  ]);
  renderDataReads(
    "node-data-reads",
    info.backend_data_model?.data_reads || []
  );
  renderDataWrites(
    "node-data-writes",
    info.backend_data_model?.data_writes || []
  );
  renderPermissions(
    "node-required-permissions",
    info.required_permissions || []
  );
  renderStringList(
    "node-rules-engines",
    info.rules_engine?.engines || []
  );
  renderStringList(
    "node-rules-purpose",
    info.rules_engine?.rules_purpose || []
  );
  renderDataObjects("node-rules-output-dtos", [
    ["Rules Output DTOs", info.rules_engine?.output_dtos || []]
  ]);
  setText(
    "node-details-description",
    info.description || "No description available."
  );
  document.getElementById("node-details-frame")?.classList.remove("hidden");
}
function bindDataModelButton(info) {
  const button = document.getElementById("show-data-model-button");
  if (!button) return;
  button.onclick = () => {
    openDataModelDrawer(info);
  };
}

// ../../src/gui/streamlit/static/diagram/init.js
mermaid.initialize({
  startOnLoad: false,
  securityLevel: "loose"
});
function findNodeIdFromMermaidNode(node) {
  if (!node) return null;
  const { nodeInfo, nodeLabelToId } = window.patientFlowConfig;
  const matchedByGeneratedId = Object.keys(nodeInfo).find(
    (nodeId) => node.id && node.id.includes(nodeId)
  );
  if (matchedByGeneratedId) return matchedByGeneratedId;
  const labelText = node.textContent.trim().replace(/\s+/g, " ");
  return nodeLabelToId[labelText] || null;
}
function bindChartClickHandler() {
  const chart = document.getElementById("chart");
  if (!chart) return;
  chart.addEventListener("click", (event) => {
    const node = event.target.closest(".node");
    const nodeId = findNodeIdFromMermaidNode(node);
    if (nodeId) {
      showNodeDetails(nodeId);
    }
  });
}
async function renderMermaidDiagram() {
  const chart = document.getElementById("chart");
  if (!chart) {
    console.error("Missing chart container.");
    return;
  }
  const chartDefinition = window.patientFlowConfig?.chartDefinition;
  if (!chartDefinition) {
    console.error("Missing chartDefinition.");
    chart.innerHTML = "<p class='muted'>Missing chart definition.</p>";
    return;
  }
  chart.innerHTML = "<p class='muted'>Rendering diagram...</p>";
  try {
    const renderId = `patient-flow-chart-${Date.now()}`;
    const { svg } = await mermaid.render(
      renderId,
      chartDefinition
    );
    chart.innerHTML = svg;
    if (window.patientFlowConfig.enableClicks) {
      bindChartClickHandler();
    }
  } catch (error) {
    console.error("Mermaid render failed:", error);
    chart.innerHTML = "<p class='muted'>Unable to render flow diagram.</p>";
  }
}
async function init() {
  if (!window.patientFlowConfig) {
    console.error("Missing patientFlowConfig.");
    return;
  }
  await renderMermaidDiagram();
  bindDrawerControls();
}
window.addEventListener("DOMContentLoaded", () => {
  init();
});

// /src/gui/streamlit/static/diagram/init.js

// /src/gui/streamlit/static/diagram/init.js

import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs";

import {showNodeDetails} from "./node_details.js";
import {bindDrawerControls} from "./image_drawer.js";

mermaid.initialize({
    startOnLoad: false,
    securityLevel: "loose",
});

function findNodeIdFromMermaidNode(node) {
    if (!node) return null;

    const {nodeInfo, nodeLabelToId} = window.patientFlowConfig;

    const matchedByGeneratedId = Object.keys(nodeInfo).find((nodeId) =>
        node.id && node.id.includes(nodeId)
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

        const {svg} = await mermaid.render(
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

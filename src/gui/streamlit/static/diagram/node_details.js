// /src/gui/streamlit/static/diagram/node_details.js

import {
    setText,
    renderStringList,
    renderNavigationRoutes,
    renderPermissions,
} from "./renderers/render_common.js";

import {
    renderUseCases,
    renderWorkflows,
} from "./renderers/render_workflows.js";

import {
    renderDataObjects,
    renderDataReads,
    renderDataWrites,
} from "./renderers/render_data_objects.js";

import {
    openScreenDrawer,
    openDataModelDrawer,
} from "./image_drawer.js";

export function showNodeDetails(nodeId) {
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
        ["Screen DTOs", info.client_contracts?.screen_dtos || []],
    ]);

    renderDataObjects("node-backend-data-model", [
        ["Definition DTOs", info.backend_data_model?.definition_dtos || []],
        ["Persistence DTOs", info.backend_data_model?.persistence_dtos || []],
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
        ["Rules Output DTOs", info.rules_engine?.output_dtos || []],
    ]);

    setText(
        "node-details-description",
        info.description || "No description available."
    );

    document
        .getElementById("node-details-frame")
        ?.classList.remove("hidden");
}

function bindDataModelButton(info) {
    const button = document.getElementById("show-data-model-button");

    if (!button) return;

    button.onclick = () => {
        openDataModelDrawer(info);
    };
}

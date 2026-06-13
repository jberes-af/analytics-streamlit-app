// /src/gui/streamlit/static/diagram/renderers/render_workflows.js

import {createMutedText} from "./render_common.js";

export function renderUseCases(elementId, useCases) {
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

export function renderWorkflows(elementId, workflows) {
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
        title.textContent = workflow.id
            ? `${workflow.id}: ${workflow.name}`
            : workflow.name || "Unnamed workflow";

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
                    item.textContent += ` → ${step.system_response}`;
                }

                list.appendChild(item);
            });

            details.appendChild(list);
            card.appendChild(details);
        }

        container.appendChild(card);
    });
}
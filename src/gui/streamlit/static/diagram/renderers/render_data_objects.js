// /src/gui/streamlit/static/diagram/renderers/render_data_objects.js

import {createMutedText} from "./render_common.js";

export function renderDataObjects(elementId, groupedDataObjects) {
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

export function renderDataReads(elementId, reads) {
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

export function renderDataWrites(elementId, writes) {
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

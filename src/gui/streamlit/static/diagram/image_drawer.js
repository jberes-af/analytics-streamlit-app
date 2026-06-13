// /src/gui/streamlit/static/diagram/image_drawer.js

import {renderImages} from "./renderers/render_images.js";

export function openScreenDrawer(info, nodeId) {

    const drawer =
        document.getElementById("screen-drawer");

    const title =
        document.getElementById("screen-drawer-title");

    if (!drawer || !title) return;

    title.textContent = info.title || nodeId;

    const images =
        info.screen_images || info.images || [];

    drawer.dataset.images =
        JSON.stringify(images);

    renderImages(
        images,
        info.title || nodeId
    );

    drawer.classList.add("open");
}

function downloadCurrentImage() {

    const drawer =
        document.getElementById("screen-drawer");

    if (!drawer) return;

    const images =
        JSON.parse(drawer.dataset.images || "[]");

    if (!images.length) {
        console.warn("No images available.");
        return;
    }

    const imageUrl = images[0];

    const link =
        document.createElement("a");

    link.href = imageUrl;

    const title =
        document.getElementById(
            "screen-drawer-title"
        )?.textContent || "screen";

    link.download =
        `${title.replace(/\s+/g, "_")}.png`;

    document.body.appendChild(link);

    link.click();

    document.body.removeChild(link);
}

export function closeScreenDrawer() {
    document.getElementById("screen-drawer")?.classList.remove("open");
    closeDataModelDrawer();
}

export function openDataModelDrawer(info) {
    const drawer = document.getElementById("data-model-drawer");
    const content = document.getElementById("data-model-content");

    if (!drawer || !content) return;

    drawer.dataset.dataModel = JSON.stringify({
        title: info.title || "Screen",
        client_contracts: info.client_contracts || {},
        backend_data_model: info.backend_data_model || {},
        rules_engine: info.rules_engine || {},
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

export function closeDataModelDrawer() {
    document.getElementById("data-model-drawer")?.classList.remove("open");
}

export function bindDrawerControls() {

    document
        .getElementById("close-screen-drawer-button")
        ?.addEventListener(
            "click",
            closeScreenDrawer
        );

    document
        .getElementById("close-data-model-button")
        ?.addEventListener(
            "click",
            closeDataModelDrawer
        );

    document
        .getElementById("download-image-button")
        ?.addEventListener(
            "click",
            downloadCurrentImage
        );

    document
        .getElementById("download-data-model-button")
        ?.addEventListener("click", downloadCurrentDataModel);
}


function downloadCurrentDataModel() {
    const drawer = document.getElementById("data-model-drawer");
    if (!drawer) return;

    const data = JSON.parse(drawer.dataset.dataModel || "{}");

    const markdown = buildDataModelMarkdown(data);

    const blob = new Blob(
        [markdown],
        {type: "text/markdown;charset=utf-8"}
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
    return value
        .toLowerCase()
        .replace(/[^a-z0-9]+/g, "_")
        .replace(/^_+|_+$/g, "");
}
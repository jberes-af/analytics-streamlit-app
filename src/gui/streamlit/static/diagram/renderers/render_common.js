// /src/gui/streamlit/static/diagram/renderers/render_common.js


export function setText(elementId, value) {
    const element = document.getElementById(elementId);
    if (element) {
        element.textContent = value;
    }
}

export function createMutedText(text) {
    const paragraph = document.createElement("p");
    paragraph.textContent = text;
    paragraph.className = "muted";
    return paragraph;
}

export function createMutedListItem(text) {
    const item = document.createElement("li");
    item.textContent = text;
    item.className = "muted";
    return item;
}

export function renderStringList(elementId, items) {
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

export function renderNavigationRoutes(elementId, routes) {
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
            route.target_screen_id ? `→ ${route.target_screen_id}` : "",
            route.condition ? `if ${route.condition}` : "",
            route.notes ? `(${route.notes})` : "",
        ].filter(Boolean);

        item.textContent = parts.join(" ");
        container.appendChild(item);
    });
}

export function renderPermissions(elementId, permissions) {
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
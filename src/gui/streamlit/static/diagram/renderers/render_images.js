// /src/gui/streamlit/static/diagram/renderers/render_images.js

export function renderImages(images, title) {
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
# /src/gui/streamlit/components/render_streamlit_features.py

import base64
from typing import Any

import streamlit as st


def _data_uri_to_bytes(data_uri: str) -> tuple[bytes, str]:
    header, encoded = data_uri.split(",", 1)
    mime_type = header.split(";")[0].replace("data:", "")
    return base64.b64decode(encoded), mime_type


def _safe_filename(name: str) -> str:
    return "".join(c if c.isalnum() or c in "-_." else "_" for c in name)


def render_node_downloads(
        prepared_nodes: dict[str, dict[str, Any]],
        # node_info: PatientFlowNodes,
) -> None:
    # prepared_nodes = _prepare_node_info(node_info)

    st.subheader("Downloads")

    for node_id, node in prepared_nodes.items():
        title = node.get("title") or node.get("label") or node_id
        filename_base = _safe_filename(str(title))

        with st.expander(str(title)):
            text_parts: list[str] = []

            for key in ("title", "description", "body", "content", "notes"):
                value = node.get(key)
                if isinstance(value, str) and value.strip():
                    text_parts.append(f"{key.upper()}\n{value.strip()}")

            text_content = "\n\n".join(text_parts)

            if text_content:
                st.download_button(
                    label="Download text",
                    data=text_content,
                    file_name=f"{filename_base}.txt",
                    mime="text/plain",
                    key=f"download-text-{node_id}",
                )

            images = node.get("screen_images", [])

            for index, image in enumerate(images, start=1):
                if not isinstance(image, str):
                    continue

                if image.startswith("data:image/"):
                    image_bytes, mime_type = _data_uri_to_bytes(image)
                    extension = mime_type.split("/")[-1]

                    st.download_button(
                        label=f"Download image {index}",
                        data=image_bytes,
                        file_name=f"{filename_base}_{index}.{extension}",
                        mime=mime_type,
                        key=f"download-image-{node_id}-{index}",
                    )

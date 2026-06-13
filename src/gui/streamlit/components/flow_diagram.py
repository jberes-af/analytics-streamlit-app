# /src/gui/streamlit/components/flow_diagram.py

from pathlib import Path
from typing import Any

from src.gui.streamlit.components.build_diagram_html_content import build_flow_html
from src.gui.streamlit.utils.convert_png_to_text import image_to_data_uri
from src.infrastructure.renderer.flow_diagram.diagram_nodes.node_content_to_diagram_ui_adapter import (
    flow_node_to_node_info,
)

from src.gui.streamlit.components.diagram_config import (
    IMAGES_DIR,
    CSS_PATH,
    JS_PATH,
    PatientFlowNodes,
)

from src.gui.streamlit.components.render_streamlit_features import (
    render_node_downloads,
)

import json
import streamlit as st


def _load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _normalize_screen_images(images: Any) -> list[str]:
    if not images:
        return []

    if isinstance(images, str):
        images = [images]

    prepared_images: list[str] = []

    for image in images:
        if image.startswith(("http://", "https://", "data:")):
            prepared_images.append(image)
            continue

        image_path = IMAGES_DIR / image

        if image_path.exists():
            prepared_images.append(image_to_data_uri(image_path))
        else:
            print(f"[WARN] Missing image: {image_path}")

    return prepared_images


def _prepare_node_info(
        node_info: PatientFlowNodes,
) -> dict[str, dict[str, Any]]:
    prepared: dict[str, dict[str, Any]] = {}

    for node_id, node_data in node_info.items():
        if hasattr(node_data, "screen_spec"):
            prepared_node = flow_node_to_node_info(node_data)
        elif isinstance(node_data, dict):
            prepared_node = dict(node_data)
        else:
            raise TypeError(
                f"Unsupported node_info value for {node_id}: {type(node_data)}"
            )

        prepared_node["screen_images"] = _normalize_screen_images(
            prepared_node.get("screen_images", [])
        )

        prepared[node_id] = prepared_node

    return prepared


def _build_flow_config_json(
        *,
        chart_definition: str,
        node_info: dict[str, dict[str, Any]],
        node_label_to_id: dict[str, str],
        click_is_enabled: bool,
) -> str:
    return json.dumps(
        {
            # "nodeInfo": _prepare_node_info(node_info),
            "nodeInfo": node_info,
            "nodeLabelToId": node_label_to_id,
            "chartDefinition": chart_definition,
            "enableClicks": click_is_enabled,
        }
    )


def render_mermaid_flow_diagram(
        chart_definition: str,
        node_info: PatientFlowNodes,
        node_label_to_id: dict[str, str],
        click_is_enabled: bool = False,
        *,
        height: int = 1100,
        scrolling: bool = True,
) -> None:
    css = _load_text(CSS_PATH)
    js = _load_text(JS_PATH)

    prepared_nodes: dict[str, dict[str, Any]] = _prepare_node_info(node_info)

    config_json = _build_flow_config_json(
        chart_definition=chart_definition,
        # node_info=node_info,
        node_info=prepared_nodes,
        node_label_to_id=node_label_to_id,
        click_is_enabled=click_is_enabled,
    )

    html = build_flow_html(
        config_json=config_json,
        css=css,
        js=js,
    )

    st.iframe(
        html,
        height=height,
    )

    # render_node_downloads(prepared_nodes)

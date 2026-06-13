# /src/gui/streamlit/screens/account_flow.py

from src.application.flow_diagram.flow_diagram_mapper import (
    build_flow_diagram_edge_tuple,
    build_flow_diagram_node_dict,
    build_node_label_to_id_map,
)

from src.application.flow_diagram.build_mermaid_diagram import (
    build_mermaid_flow_chart_definition)

from src.infrastructure.renderer.flow_diagram.diagram_nodes.account_flow_nodes import (
    ACCOUNT_FLOW_NODES,
    ACCOUNT_FLOW_EDGES,
)

from src.gui.streamlit.components.flow_diagram import (
    render_mermaid_flow_diagram)

import streamlit as st


def render_account_flow_screen() -> None:
    flow_nodes: dict[str, dict[str, str]] = (
        build_flow_diagram_node_dict(ACCOUNT_FLOW_NODES))

    flow_edge: list[tuple[str, str, str | None]] = (
        build_flow_diagram_edge_tuple(ACCOUNT_FLOW_EDGES))

    label_to_id_map: dict[str, str]  = (
        build_node_label_to_id_map(ACCOUNT_FLOW_NODES)
    )

    st.title("Account Flow")
    st.caption("Click any box in the flowchart to view details.")

    render_mermaid_flow_diagram(
        chart_definition=build_mermaid_flow_chart_definition(
            flow_nodes=flow_nodes,
            flow_edges=flow_edge,
        ),
        node_info=flow_nodes,
        node_label_to_id=label_to_id_map,
        click_is_enabled=True,
    )

# /src/gui/streamlit/screens/sensing_dashboard_flow.py

from src.application.flow_diagram.flow_diagram_mapper import (
    build_flow_diagram_edge_tuple,
    build_flow_diagram_node_dict,
    build_node_label_to_id_map,
)

from src.application.flow_diagram.build_mermaid_diagram import (
    build_mermaid_flow_chart_definition)

from src.infrastructure.renderer.flow_diagram.diagram_nodes.sensing_dashboard_flow_nodes import (
    SENSING_DASHBOARD_NODES,
    SENSING_DASHBOARD_EDGES,
)

from src.gui.streamlit.components.flow_diagram import (
    render_mermaid_flow_diagram)


from src.gui.streamlit.streamlit_settings_loader import get_last_updated_at_timestamp


import streamlit as st

def render_sensing_dashboard_flow_screen() -> None:
    flow_nodes: dict[str, dict[str, str]] = (
        build_flow_diagram_node_dict(SENSING_DASHBOARD_NODES))

    flow_edge: list[tuple[str, str, str | None]] = (
        build_flow_diagram_edge_tuple(SENSING_DASHBOARD_EDGES))

    label_to_id_map: dict[str, str]  = (
        build_node_label_to_id_map(SENSING_DASHBOARD_NODES)
    )


    last_updated_at: str = get_last_updated_at_timestamp("care")


    st.title("Sensing Dashboard")
    st.caption(f"Last updated: {last_updated_at}")
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

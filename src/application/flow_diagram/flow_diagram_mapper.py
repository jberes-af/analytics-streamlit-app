# src/application/flow_diagram/flow_diagram_mapper.py

from dataclasses import asdict

from src.application.flow_diagram.flow_diagram_types import FlowNode, FlowEdge


def build_node_label_to_id_map(
    flow_nodes: dict[str, FlowNode],
) -> dict[str, str]:
    return {
        node.label: node_id
        for node_id, node in flow_nodes.items()
    }


def build_flow_diagram_node_dict(flow_nodes: dict[str, FlowNode]) -> dict[str, dict]:
    return {
        node_id: asdict(node)
        for node_id, node in flow_nodes.items()
    }


def build_flow_diagram_edge_tuple(
        flow_edges: list[FlowEdge]
) -> list[tuple[str, str, str | None]]:
    return [
        (edge.source, edge.target, edge.action_label)
        for edge in flow_edges
    ]

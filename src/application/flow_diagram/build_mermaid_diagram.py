# /src/application/flow_diagram/build_mermaid_diagram.py

from src.application.flow_diagram.flow_diagram_types import (
    NodeClassName,
)

from typing import Any


def build_mermaid_flow_chart_definition(
        flow_nodes: dict[str, dict[str, Any]],
        flow_edges: list[tuple[str, str, str | None]],
) -> str:
    lines: list[str] = ["flowchart LR", ""]

    # Main nodes
    for node_id, node_data in flow_nodes.items():
        label = node_data["label"]

        if node_id.startswith("Filter"):
            lines.append(f"   {node_id}{{{label}}}")
        else:
            lines.append(f"   {node_id}[{label}]")

    lines.append("")
    lines.append("   %% Action label nodes")

    action_node_ids: list[str] = []
    action_edges: list[tuple[str, str, str]] = []
    unlabeled_edges: list[tuple[str, str]] = []

    action_counter = 1
    action_name_counts: dict[str, int] = {}

    for source, target, label in flow_edges:
        if not label:
            unlabeled_edges.append((source, target))
            continue

        base_id = _make_action_node_id(label)

        action_name_counts[base_id] = action_name_counts.get(base_id, 0) + 1
        count = action_name_counts[base_id]

        action_node_id = base_id if count == 1 else f"{base_id}{count}"

        # Optional: force Tap1, Tap2, etc. for labels beginning with "Tap"
        if label.startswith("Tap ") or label.startswith("Back"):
            action_node_id = f"Tap{action_counter}"
            action_counter += 1

        action_node_ids.append(action_node_id)
        action_edges.append((source, action_node_id, target))

        lines.append(f"   {action_node_id}([{label}])")

    lines.append("")

    # Edges
    for source, target in unlabeled_edges:
        lines.append(f"   {source} --> {target}")

    lines.append("")

    for source, action_node_id, target in action_edges:

        lines.append(f"   {source} --> {action_node_id} --> {target}")

    lines.extend(
        [
            "",
            "   %% Styling",
            "   classDef page fill:#e3f2fd,stroke:#1e88e5,stroke-width:1px,color:#0d47a1;",
            "   classDef form fill:#e8f5e9,stroke:#43a047,stroke-width:1px,color:#1b5e20;",
            "   classDef utility fill:#e9cfe3,stroke:#b02c0b,stroke-width:1px,color:#b02c0b;",
            "   classDef tap fill:#f8f8f8,stroke:#989898,stroke-width:1px,color:#444444;",
            "   classDef action fill:#fff3e0,stroke:#fb8c00,stroke-width:1px,color:#e65100;",
            "   classDef queue fill:#e7d0f5,stroke:#896deb,stroke-width:1px,color:#896deb;",
            "",
        ]
    )

    # Main node classes
    class_groups: dict[str, list[str]] = {}

    for node_id, node_data in flow_nodes.items():
        class_name = node_data["class_name"]

        # Normalize enum → string
        if isinstance(class_name, NodeClassName):
            class_name = class_name.value

        class_groups.setdefault(class_name, []).append(node_id)

    for class_name, node_ids in class_groups.items():
        lines.append(f"   class {','.join(node_ids)} {class_name};")

    """
    # Queue nodes (main nodes, not action nodes)
    queue_main_nodes = [
        node_id
        for node_id in flow_nodes.keys()
        if node_id.startswith("Queue")
    ]

    if queue_main_nodes:
        lines.append(f"   class {','.join(queue_main_nodes)} queue;")
    """

    # Action node classes
    tap_nodes = [node_id for node_id in action_node_ids if node_id.startswith("Tap")]

    other_action_nodes = [
        node_id
        for node_id in action_node_ids
        if not node_id.startswith("Tap") and not node_id.startswith("Queue")
    ]

    if tap_nodes:
        lines.append(f"   class {','.join(tap_nodes)} tap;")

    if other_action_nodes:
        lines.append(f"   class {','.join(other_action_nodes)} action;")

    return "\n".join(lines)


def _make_action_node_id(label: str) -> str:
    return (
        label.replace(" ", "")
        .replace("-", "")
        .replace("/", "")
        .replace("(", "")
        .replace(")", "")
    )

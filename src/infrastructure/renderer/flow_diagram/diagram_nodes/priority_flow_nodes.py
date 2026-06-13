# /src/infrastructure/renderer/flow_diagram/diagram_nodes/priority_flow_nodes.py

from src.application.flow_diagram.flow_diagram_types import (
    FlowNode,
    FlowEdge
)

from src.infrastructure.renderer.flow_diagram.design_definitions.priority_item_diagram_node_definitions import (
    CREATE_PRIORITY_ITEM_NODE,
    PRIORITY_ITEMS_NODE,
    PRIORITY_ITEM_RECORD_NODE,
    UPDATE_PRIORITY_ITEM_NODE,
)

PRIORITY_ITEM_FLOW_NODES: dict[str, FlowNode] = {
    "Priority_Items": PRIORITY_ITEMS_NODE,
    "Priority_Item_Record": PRIORITY_ITEM_RECORD_NODE,
    "Create_Priority_Item": CREATE_PRIORITY_ITEM_NODE,
    "Update_Priority_Item": UPDATE_PRIORITY_ITEM_NODE,
}

PRIORITY_ITEM_FLOW_EDGES: list[FlowEdge] = [

    FlowEdge(
        source="Priority_Items",
        target="Priority_Item_Record",
        action_label=None,
    ),

    FlowEdge(
        source="Priority_Item_Record",
        target="Create_Priority_Item",
        action_label=None,
    ),

    FlowEdge(
        source="Priority_Item_Record",
        target="Update_Priority_Item",
        action_label=None,
    ),

]

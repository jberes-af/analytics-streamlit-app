# /src/infrastructure/flow_diagram/account_flow_nodes.py

from src.application.flow_diagram.flow_diagram_types import FlowNode, FlowEdge

from src.infrastructure.renderer.flow_diagram.design_definitions.account_diagram_node_definitions import (
    ACCOUNT_HOME_NODE,
    NOTIFICATION_RECIPIENT_SETUP_NODE,
    ORGANIZATION_PROFILE_NODE,
    USER_ACCOUNT_NODE,
)

ACCOUNT_FLOW_NODES: dict[str, FlowNode] = {
    "Account_Home": ACCOUNT_HOME_NODE,
    "Notification_Recipient_Config": NOTIFICATION_RECIPIENT_SETUP_NODE,
    "Organization_Config": ORGANIZATION_PROFILE_NODE,
    "User_Config": USER_ACCOUNT_NODE,
}

ACCOUNT_FLOW_EDGES: list[FlowEdge] = [

    FlowEdge(
        source="Account_Home",
        target="User_Config",
        action_label=None,
    ),

    FlowEdge(
        source="Account_Home",
        target="Organization_Config",
        action_label=None,
    ),

    FlowEdge(
        source="Account_Home",
        target="Notification_Recipient_Config",
        action_label=None,
    ),

]

# /src/infrastructure/flow_diagram/more_flow_nodes.py

from src.application.flow_diagram.flow_diagram_types import FlowNode, FlowEdge

from src.infrastructure.renderer.flow_diagram.design_definitions.more_diagram_node_definitions import (
    MORE_ROOT_NODE,
    SETTINGS_NODE,
    SETUP_NODE,
    GUIDES_NODE,
    TIPS_NODE,
    ABOUT_NODE,
    NOTIFICATION_SETTING_NODE,
    UOM_SETTING_NODE,
)

from src.infrastructure.renderer.flow_diagram.design_definitions.account_diagram_node_definitions import (
    ACCOUNT_HOME_NODE,
)

MORE_FLOW_NODES: dict[str, FlowNode] = {
    "More_Root": MORE_ROOT_NODE,
    "Account_Home": ACCOUNT_HOME_NODE,
    "Settings": SETTINGS_NODE,
    "Setup": SETUP_NODE,
    "Guides": GUIDES_NODE,
    "Tips": TIPS_NODE,
    "About": ABOUT_NODE,
    "Notification_Setting": NOTIFICATION_SETTING_NODE,
    "Units_of_Measure": UOM_SETTING_NODE,
}

MORE_FLOW_EDGES: list[FlowEdge] = [

    FlowEdge(
        source="More_Root",
        target="Account_Home",
        action_label=None,
    ),

    FlowEdge(
        source="More_Root",
        target="Settings",
        action_label=None,
    ),

    FlowEdge(
        source="More_Root",
        target="Setup",
        action_label=None,
    ),

    FlowEdge(
        source="More_Root",
        target="Guides",
        action_label=None,
    ),

    FlowEdge(
        source="More_Root",
        target="Tips",
        action_label=None,
    ),

    FlowEdge(
        source="More_Root",
        target="About",
        action_label=None,
    ),

    FlowEdge(
        source="Settings",
        target="Units_of_Measure",
        action_label=None,
    ),

    FlowEdge(
        source="Settings",
        target="Notification_Setting",
        action_label=None,
    ),

]

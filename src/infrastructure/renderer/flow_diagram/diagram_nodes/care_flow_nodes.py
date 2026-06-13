# /src/infrastructure/renderer/flow_diagram/diagram_nodes/care_flow_nodes.py

## aswgaa asdfask

from src.application.flow_diagram.flow_diagram_types import (
    FlowNode,
    FlowEdge,
)

from src.infrastructure.renderer.flow_diagram.design_definitions.care_diagram_node_definitions import (
    CARE_ROOT_NODE,
    RESIDENTS_DASHBOARD_NODE,
    RESIDENT_NOTES_NODE,
    RESIDENT_RECORD_NODE,
)

from src.infrastructure.renderer.flow_diagram.design_definitions.plan_diagram_node_definitions import (
    THERAPEUTIC_PLAN_DASHBOARD_NODE,
)

from src.infrastructure.renderer.flow_diagram.design_definitions.priority_item_diagram_node_definitions import (
    PRIORITY_ITEMS_NODE,
    PRIORITY_ITEM_RECORD_NODE,
    # CREATE_PRIORITY_ITEM_NODE
)

from src.infrastructure.renderer.flow_diagram.design_definitions.adl_resident_diagram_node_definitions import (
    RESIDENT_ADL_SUMMARY_NODE,
    DEVICE_ADL_LINK_NODE,
    DEVICE_ADL_TRENDS_NODE,
)

CARE_FLOW_NODES: dict[str, FlowNode] = {
    "Care_Root": CARE_ROOT_NODE,

    "Residents_Dashboard": RESIDENTS_DASHBOARD_NODE,
    "Resident_Record": RESIDENT_RECORD_NODE,
    "Resident_Notes": RESIDENT_NOTES_NODE,

    "Device-ADL_Link": DEVICE_ADL_LINK_NODE,
    "Device-ADL_Trends": DEVICE_ADL_TRENDS_NODE,
    "Resident_ADL_Summary": RESIDENT_ADL_SUMMARY_NODE,

    "Therapeutic_Plans": THERAPEUTIC_PLAN_DASHBOARD_NODE,

    "Priority_Items": PRIORITY_ITEMS_NODE,
    "Priority_Item_Record": PRIORITY_ITEM_RECORD_NODE,
    # "Create_Priority_Item": CREATE_PRIORITY_ITEM_NODE,
}

CARE_FLOW_EDGES: list[FlowEdge] = [

    FlowEdge(
        source="Care_Root",
        target="Residents_Dashboard",
        action_label=None,
    ),

    FlowEdge(
        source="Care_Root",
        target="Resident_Record",
        action_label=None,
    ),

    FlowEdge(
        source="Care_Root",
        target="Priority_Items",
        action_label=None,
    ),

    FlowEdge(
        source="Care_Root",
        target="Device-ADL_Link",
        action_label=None,
    ),

    FlowEdge(
        source="Care_Root",
        target="Therapeutic_Plans",
        action_label=None,
    ),

    FlowEdge(
        source="Care_Root",
        target="Resident_Notes",
        action_label=None,
    ),

    FlowEdge(
        source="Priority_Items",
        target="Priority_Item_Record",
        action_label=None,
    ),

    FlowEdge(
        source="Residents_Dashboard",
        target="Resident_Record",
        action_label=None,
    ),

    FlowEdge(
        source="Resident_Record",
        target="Resident_ADL_Summary",
        action_label=None,
    ),

    FlowEdge(
        source="Resident_Record",
        target="Resident_Notes",
        action_label=None,
    ),

    FlowEdge(
        source="Resident_Record",
        target="Priority_Item_Record",
        action_label=None,
    ),

    FlowEdge(
        source="Device-ADL_Link",
        target="Device-ADL_Trends",
        action_label=None,
    ),

]

# /src/infrastructure/renderer/flow_diagram/diagram_nodes/adl_resident_flow_nodes.py

from src.application.flow_diagram.flow_diagram_types import FlowNode, FlowEdge

from src.infrastructure.renderer.flow_diagram.design_definitions.adl_resident_diagram_node_definitions import (
    ADL_ASSESSMENT_NODE,
    ADL_OBSERVATION_NODE,
    ADL_TRENDS_NODE,
    RESIDENT_ADL_SUMMARY_NODE,
    DEVICE_ADL_LINK_NODE,
)

from src.infrastructure.renderer.flow_diagram.design_definitions.priority_item_diagram_node_definitions import (
    CREATE_PRIORITY_ITEM_NODE,
)

# ⚠️ Sequence of keys determines flow chart layout
ADL_RESIDENT_FLOW_NODES: dict[str, FlowNode] = {
    "Resident_ADL_Summary": RESIDENT_ADL_SUMMARY_NODE,
    "ADL_Trends": ADL_TRENDS_NODE,
    "ADL_Assessment": ADL_ASSESSMENT_NODE,
    "ADL_Observation": ADL_OBSERVATION_NODE,
    "Create_Priority_Item": CREATE_PRIORITY_ITEM_NODE,
    "Device-ADL_Link": DEVICE_ADL_LINK_NODE,
}

ADL_RESIDENT_FLOW_EDGES: list[FlowEdge] = [
    FlowEdge(
        source="Resident_ADL_Summary",
        target="ADL_Trends",
        action_label=None,
    ),

    FlowEdge(
        source="Resident_ADL_Summary",
        target="ADL_Assessment",
        action_label=None,
        # action_label="Tap Enter ADL"
    ),

    FlowEdge(
        source="Resident_ADL_Summary",
        target="ADL_Observation",
        action_label=None,
        # action_label="Tap Add Observation"
    ),

    FlowEdge(
        source="Resident_ADL_Summary",
        target="Create_Priority_Item",
        action_label=None,
        # action_label="Tap Prioritize"
    ),

    FlowEdge(
        source="Resident_ADL_Summary",
        target="Device-ADL_Link",
        action_label=None,
    ),
]

# /src/infrastructure/flow_diagram/adl_queue_flow_nodes.py

from src.application.flow_diagram.flow_diagram_types import FlowNode, FlowEdge

from src.infrastructure.renderer.flow_diagram.design_definitions.adl_resident_diagram_node_definitions import (
    ADL_ASSESSMENT_NODE,
    RESIDENT_ADL_SUMMARY_NODE,
    ADL_OBSERVATION_NODE,
    RESIDENT_SUMMARY_NODE,
    PRIORITY_NODE,
)

from src.infrastructure.renderer.flow_diagram.design_definitions.adl_queue_diagram_node_definitions import (
    ADL_QUEUE_REVIEW_NODE,
    ADL_QUEUE_DETAIL_NODE,

    NOTIFICATION_EDGE_1,
    NOTIFICATION_EDGE_2,
    NOTIFICATION_EDGE_3,
    NOTIFICATION_EDGE_4,
    NOTIFICATION_EDGE_5,
    NOTIFICATION_EDGE_6,
    NOTIFICATION_EDGE_7,
    NOTIFICATION_EDGE_8,

)

NOTIFICATION_FLOW_NODES: dict[str, FlowNode] = {
    "ADL_Home": RESIDENT_ADL_SUMMARY_NODE,
    "Queue_Review": ADL_QUEUE_REVIEW_NODE,
    "Queue_Detail": ADL_QUEUE_DETAIL_NODE,
    "Patient_Summary": RESIDENT_SUMMARY_NODE,
    "Priority": PRIORITY_NODE,
    "ADL_Entry": ADL_ASSESSMENT_NODE,
    "OBS_Entry": ADL_OBSERVATION_NODE,
}

NOTIFICATION_FLOW_EDGES: list[FlowEdge] = [
    NOTIFICATION_EDGE_1,
    NOTIFICATION_EDGE_2,
    NOTIFICATION_EDGE_3,
    NOTIFICATION_EDGE_4,
    NOTIFICATION_EDGE_5,
    NOTIFICATION_EDGE_6,
    NOTIFICATION_EDGE_7,
    NOTIFICATION_EDGE_8,
]

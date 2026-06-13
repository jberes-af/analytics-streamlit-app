# /src/infrastructure/renderer/flow_diagram/diagram_nodes/plan_flow_nodes.py

from src.application.flow_diagram.flow_diagram_types import FlowNode, FlowEdge

from src.infrastructure.renderer.flow_diagram.design_definitions.plan_diagram_node_definitions import (
    THERAPEUTIC_PLAN_DASHBOARD_NODE,
    THERAPEUTIC_PLAN_RECORD_NODE,
    CREATE_THERAPEUTIC_PLAN_NODE,
    REVISE_THERAPEUTIC_PLAN_NODE,
    UPDATE_PROGRESS_THERAPEUTIC_PLAN_NODE,
)

THERAPEUTIC_PLAN_FLOW_NODES: dict[str, FlowNode] = {
    "Therapeutic_Plans": THERAPEUTIC_PLAN_DASHBOARD_NODE,
    "Therapeutic_Plan_Record": THERAPEUTIC_PLAN_RECORD_NODE,
    "Create_Therapeutic_Plan": CREATE_THERAPEUTIC_PLAN_NODE,
    "Revise_Therapeutic_Plan": REVISE_THERAPEUTIC_PLAN_NODE,
    "Update_Therapeutic_Plan_Progress": UPDATE_PROGRESS_THERAPEUTIC_PLAN_NODE
}

THERAPEUTIC_PLAN_FLOW_EDGES: list[FlowEdge] = [

    FlowEdge(
        source="Therapeutic_Plans",
        target="Therapeutic_Plan_Record",
        action_label=None,
    ),

    FlowEdge(
        source="Therapeutic_Plans",
        target="Create_Therapeutic_Plan",
        action_label=None,
    ),

    FlowEdge(
        source="Therapeutic_Plan_Record",
        target="Revise_Therapeutic_Plan",
        action_label=None,
    ),

    FlowEdge(
        source="Therapeutic_Plan_Record",
        target="Update_Therapeutic_Plan_Progress",
        action_label=None,
    ),

]

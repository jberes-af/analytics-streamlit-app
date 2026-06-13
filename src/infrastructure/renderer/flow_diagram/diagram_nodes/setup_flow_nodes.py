# /src/infrastructure/flow_diagram/setup_flow_nodes.py

from src.application.flow_diagram.flow_diagram_types import FlowNode, FlowEdge

from src.infrastructure.renderer.flow_diagram.design_definitions.setup_diagram_node_definitions import (
    SENSOR_ASSIGN_RESIDENT_NODE,
    SETUP_NODE,
)
from src.infrastructure.renderer.flow_diagram.design_definitions.care_diagram_node_definitions import (
    RESIDENT_PROFILES_NODE,
    RESIDENT_PROFILE_CONFIG_NODE,
)

from src.infrastructure.renderer.flow_diagram.design_definitions.sensing_diagram_node_definitions import (
    SENSOR_PROFILES_NODE,
    SENSOR_CONFIG_NODE,
    SENSOR_GROUPS_NODE,
    ALERTA_ROUTINE_CONFIG_NODE,
)

from src.infrastructure.renderer.flow_diagram.design_definitions.analytics_diagram_node_definitions import (
    ANALYTICS_BASELINE_SETUP
)

SETUP_FLOW_NODES: dict[str, FlowNode] = {
    "Setup": SETUP_NODE,
    "Sensor_Profiles": SENSOR_PROFILES_NODE,
    "Resident_Profiles": RESIDENT_PROFILES_NODE,
    "Sensor_Groups": SENSOR_GROUPS_NODE,
    "Sensor_Configuration": SENSOR_CONFIG_NODE,
    "Sensor_Attach_Resident": SENSOR_ASSIGN_RESIDENT_NODE,
    "Resident_Configuration": RESIDENT_PROFILE_CONFIG_NODE,
    "Analytics_Baselines": ANALYTICS_BASELINE_SETUP,
    "Alerta_Routine_Config": ALERTA_ROUTINE_CONFIG_NODE,
}

SETUP_FLOW_EDGES: list[FlowEdge] = [

    FlowEdge(
        source="Setup",
        target="Sensor_Profiles",
        action_label=None,
    ),

    FlowEdge(
        source="Setup",
        target="Resident_Profiles",
        action_label=None,
    ),

    FlowEdge(
        source="Resident_Profiles",
        target="Resident_Configuration",
        action_label=None,
    ),

    FlowEdge(
        source="Sensor_Profiles",
        target="Sensor_Configuration",
        action_label=None,
    ),

    FlowEdge(
        source="Sensor_Profiles",
        target="Sensor_Attach_Resident",
        action_label=None,
    ),

    FlowEdge(
        source="Setup",
        target="Sensor_Groups",
        action_label=None,
    ),

    FlowEdge(
        source="Setup",
        target="Analytics_Baselines",
        action_label=None,
    ),

    FlowEdge(
        source="Setup",
        target="Alerta_Routine_Config",
        action_label=None,
    ),
]

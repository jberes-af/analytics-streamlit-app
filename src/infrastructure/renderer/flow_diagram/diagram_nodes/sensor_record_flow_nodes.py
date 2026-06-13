# /src/infrastructure/flow_diagram/sensing_root_flow_nodes.py

from src.application.flow_diagram.flow_diagram_types import FlowNode, FlowEdge

from src.infrastructure.renderer.flow_diagram.design_definitions.sensing_diagram_node_definitions import (
    SENSING_ROOT_NODE,
    SENSOR_RECORD_NODE,
    ALERTA_ROUTINES_NODE,
    ALERTA_ROUTINE_CONFIG_NODE,
    MOVEMENT_PATTERNS_NODE,
    # SENSOR_NOTIFICATION_HISTORY_NODE,
    SENSING_DASHBOARD_NODE,
    # SENSOR_LIVE_STATUS_NODE,
    SENSOR_TRENDS_NODE,
    SENSOR_GROUPS_NODE,
    SENSOR_PROFILES_NODE,
    # NOTIFICATION_DETAIL_NODE,
    SENSOR_EVENT_TIMELINE_NODE, SENSOR_CONFIG_NODE,
    FILTER_SENSOR_GROUP_ACTION,
)

SENSOR_RECORD_NODES: dict[str, FlowNode] = {
    # "Sensing_Root": SENSING_ROOT_NODE,
    "Sensor_Record": SENSOR_RECORD_NODE,
    # "Sensing_Dashboard": SENSING_DASHBOARD_NODE,
    # "Filter_Group": FILTER_SENSOR_GROUP_ACTION,
    "Sensor_Trends": SENSOR_TRENDS_NODE,
    # "Movement_Patterns": MOVEMENT_PATTERNS_NODE,
    # "Sensor_Groups": SENSOR_GROUPS_NODE,
    "Sensor_Profiles": SENSOR_PROFILES_NODE,
    # "Notification_History": SENSOR_NOTIFICATION_HISTORY_NODE,
    # "Notification_Detail": NOTIFICATION_DETAIL_NODE,
    "Notification_Timeline": SENSOR_EVENT_TIMELINE_NODE,
    # "Alerta_Routines": ALERTA_ROUTINES_NODE,
    "Sensor_Configuration": SENSOR_CONFIG_NODE,
    # "Alerta_Routine_Config": ALERTA_ROUTINE_CONFIG_NODE,
}

SENSOR_RECORD_EDGES: list[FlowEdge] = [
    FlowEdge(
        source="Sensor_Record",
        target="Sensor_Trends",
        action_label=None,
    ),

    FlowEdge(
        source="Sensor_Record",
        target="Notification_Timeline",
        action_label=None,
    ),

    FlowEdge(
        source="Sensor_Record",
        target="Sensor_Profiles",
        action_label=None,
    ),

    FlowEdge(
        source="Sensor_Profiles",
        target="Sensor_Configuration",
        action_label=None,
    ),

]

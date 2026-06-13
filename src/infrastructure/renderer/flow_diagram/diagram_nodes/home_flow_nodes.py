# /src/infrastructure/flow_diagram/home_flow_nodes.py

from src.application.flow_diagram.flow_diagram_types import FlowNode, FlowEdge

from src.infrastructure.renderer.flow_diagram.design_definitions.home_diagram_node_definitions import (
    # ACTIVITY_LIVE_STATUS_NODE,
    # SENSING_SUMMARY_NODE,
    HOME_ROOT_NODE,
    FILTER_SENSING_RESIDENT_VIEW_ACTION,
    NOTIFICATION_DETAIL_NODE,
    NOTIFICATION_SUMMARY_NODE,
    # RESIDENT_SUMMARY_NODE,
)

from src.infrastructure.renderer.flow_diagram.design_definitions.sensing_diagram_node_definitions import (
    # SENSING_HOME_NODE,
    SENSING_DASHBOARD_NODE,
    SENSOR_EVENT_TIMELINE_NODE,
    SENSING_DASHBOARD_NODE,
    SENSOR_PROFILES_NODE,
)

from src.infrastructure.renderer.flow_diagram.design_definitions.care_diagram_node_definitions import (
    RESIDENTS_DASHBOARD_NODE,
    RESIDENT_RECORD_NODE,
)

HOME_FLOW_NODES: dict[str, FlowNode] = {
    "Home_Root": HOME_ROOT_NODE,
    "Filter_View": FILTER_SENSING_RESIDENT_VIEW_ACTION,
    # "Resident_Summary": RESIDENT_SUMMARY_NODE,
    "Sensing_Dashboard": SENSING_DASHBOARD_NODE,
    "Sensor_Profiles": SENSOR_PROFILES_NODE,
    "Residents_Dashboard": RESIDENTS_DASHBOARD_NODE,
    "Resident_Record": RESIDENT_RECORD_NODE,
    "Notification_Summary": NOTIFICATION_SUMMARY_NODE,
    "Notification_Detail": NOTIFICATION_DETAIL_NODE,
    "Notification_Timeline": SENSOR_EVENT_TIMELINE_NODE,
    # "Activity_Live_Status": ACTIVITY_LIVE_STATUS_NODE,
    # "Activity_Timeline": ACTIVITY_TIMELINE_NODE,
}

HOME_FLOW_EDGES: list[FlowEdge] = [

    FlowEdge(
        source="Home_Root",
        target="Filter_View",
        action_label=None,
    ),

    FlowEdge(
        source="Filter_View",
        target="Sensing_Dashboard",
        action_label=None,
    ),

    FlowEdge(
        source="Filter_View",
        target="Sensor_Profiles",
        action_label=None,
    ),

    FlowEdge(
        source="Filter_View",
        target="Residents_Dashboard",
        action_label=None,
    ),

    FlowEdge(
        source="Filter_View",
        target="Resident_Record",
        action_label=None,
    ),

    FlowEdge(
        source="Home_Root",
        target="Notification_Summary",
        action_label=None,
    ),

    FlowEdge(
        source="Notification_Summary",
        target="Notification_Detail",
        action_label=None,
    ),

    FlowEdge(
        source="Notification_Detail",
        target="Notification_Timeline",
        action_label=None,
    ),

]

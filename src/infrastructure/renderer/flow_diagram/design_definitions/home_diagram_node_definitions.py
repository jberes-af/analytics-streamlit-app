# /src/infrastructure/renderer/flow_diagram/home_diagram_node_definitions.py

from src.domain.mobile_app_enums import (
    DomainObject,
    Action,
)

from src.domain.mobile_app_types import (
    PermissionRequirement,
)

from src.application.flow_diagram.flow_diagram_types import (
    NodeClassName,
    FlowNode,
)

# from src.infrastructure.renderer.architecture_detail.screens.care.adl.caregiver_adl import ()
# from src.infrastructure.renderer.architecture_detail.use_cases.use_cases_dtos import ()
# from src.infrastructure.renderer.architecture_detail.workflows.workflow_dtos import ()
# from src.infrastructure.renderer.architecture_detail.data_models_analytics.data_models_client.client_contracts_dtos import ()
# from src.infrastructure.renderer.architecture_detail.data_models_analytics.data_models_backend.backend_dtos import ()
# from src.infrastructure.renderer.architecture_detail.data_models_analytics.data_models_rules_engine.spec_dtos import ()

"""
HOME SCREEN FLOW DIAGRAM NODES
"""

HOME_ROOT_NODE = FlowNode(
    title="Home Root",
    label="Home Root",
    class_name=NodeClassName.PAGE,
    screen_spec=None,
    screen_images=tuple([
        "home/home-sensing.png",
        #     "home/home-resident.png",
    ]),
    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=None,
    rules_engine=None,
    description="",
)

FILTER_SENSING_RESIDENT_VIEW_ACTION = FlowNode(
    title="Filter View",
    label="Filter View",
    class_name=NodeClassName.ACTION,
    screen_spec=None,
    screen_images=tuple(),

    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=None,
    rules_engine=None,
    description="",
)


"""
SENSING_SUMMARY_NODE = FlowNode(
    title="Sensing Home",
    label="Sensing Home",
    class_name=NodeClassName.PAGE,
    screen_spec=None,
    screen_images=tuple([
        "sensing/S01-sensing-home-04.png",
    #     "care/adl/resident_view/patient-summary-option-b.png",
    ]),
    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=None,
    rules_engine=None,
    description="",
)
"""

RESIDENT_SUMMARY_NODE = FlowNode(
    title="Resident Summary",
    label="Resident Summary",
    class_name=NodeClassName.PAGE,
    screen_spec=None,
    # screen_images=tuple([
    #     "care/adl/resident_view/patient-summary.png",
    #     "care/adl/resident_view/patient-summary-option-b.png",
    # ]),
    screen_images=(),
    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=None,
    rules_engine=None,
    description="",
)

NOTIFICATION_SUMMARY_NODE = FlowNode(
    title="Notification Summary",
    label="Notification Summary",
    class_name=NodeClassName.PAGE,
    screen_spec=None,
    # screen_images=tuple([
    #     "care/adl/resident_view/patient-summary.png",
    #     "care/adl/resident_view/patient-summary-option-b.png",
    # ]),
    screen_images=(),
    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=None,
    rules_engine=None,
    description="",
)

NOTIFICATION_DETAIL_NODE = FlowNode(
    title="Notification Detail",
    label="Notification Detail",
    class_name=NodeClassName.PAGE,
    screen_spec=None,
    # screen_images=tuple([
    #     "care/adl/resident_view/patient-summary.png",
    #     "care/adl/resident_view/patient-summary-option-b.png",
    # ]),
    screen_images=(),
    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=None,
    rules_engine=None,
    description="",
)

ACTIVITY_LIVE_STATUS_NODE = FlowNode(
    title="Activity Live Status",
    label="Activity Live Status",
    class_name=NodeClassName.PAGE,
    screen_spec=None,
    # screen_images=tuple([
    #     "care/adl/resident_view/patient-summary.png",
    #     "care/adl/resident_view/patient-summary-option-b.png",
    # ]),
    screen_images=(),
    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=None,
    rules_engine=None,
    description="",
)

"""
FLOW DIAGRAM EDGES

HOME_EDGE_1 = FlowEdge(
    source="Home",
    target="Sensing_Summary",
    action_label=None,
)

HOME_EDGE_2 = FlowEdge(
    source="Home",
    target="Resident_Summary",
    action_label=None,
)

HOME_EDGE_3 = FlowEdge(
    source="Home",
    target="Notification_Summary",
    action_label=None,
)


HOME_EDGE_4 = FlowEdge(
    source="Sensing_Summary",
    target="Sensing_Dashboard",
    action_label=None,
)

HOME_EDGE_5 = FlowEdge(
    source="Sensing_Summary",
    target="Sensor_Profile",
    action_label=None,
)

HOME_EDGE_6 = FlowEdge(
    source="Resident_Summary",
    target="Residents_Dashboard",
    action_label=None,
)

HOME_EDGE_7 = FlowEdge(
    source="Resident_Summary",
    target="Resident_Record",
    action_label=None,
)

HOME_EDGE_8 = FlowEdge(
    source="Notification_Summary",
    target="Notification_Detail",
    action_label=None,
)

HOME_EDGE_9 = FlowEdge(
    source="Notification_Detail",
    target="Notification_Timeline",
    action_label=None,
)
"""

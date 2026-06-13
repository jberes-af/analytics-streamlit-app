# /src/infrastructure/renderer/flow_diagram/sensing_diagram_node_definitions.py

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

from src.infrastructure.renderer.architecture_detail.data_models_domain.sensing.sensing_domain_dtos import (
    SENSING_HOME_BACKEND_DTOS,
    SENSING_DASHBOARD_BACKEND_DTOS,
    SENSING_TRENDS_BACKEND_DTOS,
    SENSING_MOVEMENTS_BACKEND_DTOS,
    SENSING_ALERTA_ROUTINES_BACKEND_DTOS,
    SENSING_SENSOR_EVENT_TIMELINE_BACKEND_DTOS,
    SENSING_SENSOR_PROFILES_BACKEND_DTOS,
)


"""
SENSING FLOW DIAGRAM NODES
"""

SENSING_ROOT_NODE = FlowNode(
    title="Sensing Root",
    label="Sensing Root",
    class_name=NodeClassName.PAGE,
    screen_spec=None,
    screen_images=tuple([
        "sensing/S01-sensing-home-04.png",
    ]),
    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=SENSING_HOME_BACKEND_DTOS,
    rules_engine=None,
    description="",
)

SENSING_DASHBOARD_NODE = FlowNode(
    title="Sensing Dashboard",
    label="Sensing Dashboard",
    class_name=NodeClassName.PAGE,
    screen_spec=None,
    screen_images=tuple([
        "sensing/S02-sensing-dashboard-04.png",
    ]),
    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=SENSING_DASHBOARD_BACKEND_DTOS,
    rules_engine=None,
    description="",
)

SENSOR_RECORD_NODE = FlowNode(
    title="Sensor Record",
    label="Sensor Record",
    class_name=NodeClassName.PAGE,
    screen_spec=None,
    screen_images=tuple([]),
    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=SENSING_DASHBOARD_BACKEND_DTOS,
    rules_engine=None,
    description="",
)

MOVEMENT_PATTERNS_NODE = FlowNode(
    title="Movement Patterns",
    label="Movement Patterns",
    class_name=NodeClassName.PAGE,
    screen_spec=None,
    screen_images=tuple([
        "sensing/S04-movements-05.png",
    ]),
    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=SENSING_MOVEMENTS_BACKEND_DTOS,
    rules_engine=None,
    description="",
)

SENSOR_TRENDS_NODE = FlowNode(
    title="Sensor Trends",
    label="Sensor Trends & Analytics",
    class_name=NodeClassName.PAGE,
    screen_spec=None,
    screen_images=tuple([
        "sensing/S03-sensor-trends-01.png",
    ]),
    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=SENSING_TRENDS_BACKEND_DTOS,
    rules_engine=None,
    description="",
)


ALERTA_ROUTINES_NODE = FlowNode(
    title="Alerta Routines",
    label="Alerta Routines",
    class_name=NodeClassName.PAGE,
    screen_spec=None,
    screen_images=tuple([
        "sensing/S06-routines-profile-01.png",
        "sensing/S06-routines-profile-02.png",
    ]),
    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=SENSING_ALERTA_ROUTINES_BACKEND_DTOS,
    rules_engine=None,
    description="",
)

SENSOR_EVENT_TIMELINE_NODE = FlowNode(
    title="Notification Timeline",
    label="Notification Timeline",
    class_name=NodeClassName.PAGE,
    screen_spec=None,
    screen_images=tuple([
        "sensing/S05-sensor-event-timeline-01.png",
    ]),
    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=SENSING_SENSOR_EVENT_TIMELINE_BACKEND_DTOS,
    rules_engine=None,
    description="",
)

ALERTA_ROUTINE_CONFIG_NODE = FlowNode(
    title="Alerta Routine Config",
    label="Alerta Routine Config",
    class_name=NodeClassName.FORM,
    screen_spec=None,
    screen_images=tuple([
        "sensing/create-routine-01.png",
        "sensing/create-routine-02.png",
        "sensing/create-routine-03.png",
    ]),
    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=None,
    rules_engine=None,
    description="",
)

SENSOR_PROFILES_NODE = FlowNode(
    title="Sensor Profiles",
    label="Sensor Profiles",
    class_name=NodeClassName.PAGE,
    screen_spec=None,
    screen_images=tuple(["sensing/S07-sensor-profiles.png"]),
    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=SENSING_SENSOR_PROFILES_BACKEND_DTOS,
    rules_engine=None,
    description="",
)

SENSOR_CONFIG_NODE = FlowNode(
    title="Sensor Configuration",
    label="Sensor Configuration",
    class_name=NodeClassName.FORM,
    screen_spec=None,
    screen_images=tuple(["shared/sensor-config.png"]),
    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=None,
    rules_engine=None,
    description="",
)

SENSOR_GROUPS_NODE = FlowNode(
    title="Sensor Groups",
    label="Sensor Groups",
    class_name=NodeClassName.FORM,
    screen_spec=None,
    screen_images=tuple(["shared/groups-summary.png"]),

    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=None,
    rules_engine=None,
    description="",
)

FILTER_SENSOR_GROUP_ACTION = FlowNode(
    title="Filter Group",
    label="Filter Group",
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

SENSOR_NOTIFICATION_HISTORY_NODE = FlowNode(
    title="Notification History",
    label="Notification History",
    class_name=NodeClassName.PAGE,
    screen_spec=None,
    screen_images=tuple([
        "sensing/S05-sensor-event-timeline-01.png",
    ]),
    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=None,
    rules_engine=None,
    description="",
)

SENSOR_PROFILE_NODE = FlowNode(
    title="Sensor Profile",
    label="Sensor Profile",
    class_name=NodeClassName.PAGE,
    screen_spec=None,
    screen_images=tuple([
        "care/adl/resident_view/patient-summary.png",
        "care/adl/resident_view/patient-summary-option-b.png",
    ]),
    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=None,
    data_models_rules_engine=None,
    description="",
)

NOTIFICATION_DETAIL_NODE = FlowNode(
    title="Notification Detail",
    label="Notification Detail",
    class_name=NodeClassName.FORM,
    screen_spec=None,
    screen_images=tuple([
        "care/adl/resident_view/patient-summary.png",
        "care/adl/resident_view/patient-summary-option-b.png",
    ]),
    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=None,
    data_models_rules_engine=None,
    description="",
)

SENSOR_LIVE_STATUS_NODE = FlowNode(
    title="Sensor Live Status",
    label="Sensor Live Status",
    class_name=NodeClassName.PAGE,
    screen_spec=None,
    screen_images=tuple([
        "care/adl/resident_view/patient-summary.png",
        "care/adl/resident_view/patient-summary-option-b.png",
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

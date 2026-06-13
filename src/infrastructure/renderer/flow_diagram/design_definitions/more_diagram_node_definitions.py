# /src/infrastructure/renderer/flow_diagram/more_diagram_node_definitions.py

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
SETUP FLOW DIAGRAM NODES
"""

MORE_ROOT_NODE = FlowNode(
    title="More Root",
    label="More Root",
    class_name=NodeClassName.PAGE,
    screen_spec=None,
    screen_images=tuple([]),

    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=None,
    rules_engine=None,
    description="",
)

SETTINGS_NODE = FlowNode(
    title="Settings",
    label="Settings",
    class_name=NodeClassName.FORM,
    screen_spec=None,
    screen_images=tuple([]),

    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=None,
    rules_engine=None,
    description="",
)

SETUP_NODE = FlowNode(
    title="Setup",
    label="Setup",
    class_name=NodeClassName.FORM,
    screen_spec=None,
    screen_images=tuple([]),

    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=None,
    rules_engine=None,
    description="",
)


GUIDES_NODE = FlowNode(
    title="Guides",
    label="How-To Guides",
    class_name=NodeClassName.PAGE,
    screen_spec=None,
    screen_images=tuple([]),

    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=None,
    rules_engine=None,
    description="",
)

TIPS_NODE = FlowNode(
    title="Tips",
    label="Safety & Caregiving Tips",
    class_name=NodeClassName.PAGE,
    screen_spec=None,
    screen_images=tuple([]),

    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=None,
    rules_engine=None,
    description="",
)

ABOUT_NODE = FlowNode(
    title="About",
    label="About",
    class_name=NodeClassName.PAGE,
    screen_spec=None,
    screen_images=tuple(["shared/about.png"]),

    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=None,
    rules_engine=None,
    description="",
)

UOM_SETTING_NODE = FlowNode(
    title="Units of Measure",
    label="Units of Measure",
    class_name=NodeClassName.FORM,
    screen_spec=None,
    screen_images=tuple([]),

    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=None,
    rules_engine=None,
    description="",
)

NOTIFICATION_SETTING_NODE = FlowNode(
    title="Notification Setting",
    label="Notification Setting",
    class_name=NodeClassName.FORM,
    screen_spec=None,
    screen_images=tuple(["shared/notification-settings.png"]),
    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=None,
    rules_engine=None,
    description="",
)

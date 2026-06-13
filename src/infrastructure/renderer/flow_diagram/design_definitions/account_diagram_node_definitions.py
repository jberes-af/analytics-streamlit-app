# /src/infrastructure/renderer/flow_diagram/account_diagram_node_definitions.py

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
USER FLOW DIAGRAM NODES
"""

ACCOUNT_HOME_NODE = FlowNode(
    title="Account",
    label="Account",
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

USER_ACCOUNT_NODE = FlowNode(
    title="User Account",
    label="User Profile",
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

ORGANIZATION_PROFILE_NODE = FlowNode(
    title="Organization Profile",
    label="Organization Profile",
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

NOTIFICATION_RECIPIENT_SETUP_NODE = FlowNode(
    title="Notification Recipient Setup",
    label="Notification Recipient Profiles",
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

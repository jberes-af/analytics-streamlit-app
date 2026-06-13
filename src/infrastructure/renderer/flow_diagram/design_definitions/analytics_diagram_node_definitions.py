# /src/infrastructure/renderer/flow_diagram/design_definitions/analytics_diagram_node_definitions.py


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


"""
ADL FLOW DIAGRAM NODES
"""

ANALYTICS_BASELINE_SETUP = FlowNode(
    title="Analytics Baselines",
    label="Analytics Baselines",
    class_name=NodeClassName.PAGE,
    screen_spec=None,
    screen_images=tuple([]),
    required_permissions=tuple([
        PermissionRequirement(
            domain=DomainObject.ADL_ASSESSMENT,
            action=Action.CREATE,
        )]
    ),
    use_cases=tuple([]),
    workflows=tuple([]),
    client_contracts=None,
    backend_data_model=None,
    rules_engine=None,
    description="Setup Baselines.",
)


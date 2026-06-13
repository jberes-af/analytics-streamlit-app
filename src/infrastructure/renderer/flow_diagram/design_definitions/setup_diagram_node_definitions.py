# /src/infrastructure/renderer/flow_diagram/setup_diagram_node_definitions.py

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

SETUP_NODE = FlowNode(
    title="Setup",
    label="Setup",
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

SENSOR_ASSIGN_RESIDENT_NODE = FlowNode(
    title="Sensor Assign Resident",
    label="Attach Resident to Sensor",
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

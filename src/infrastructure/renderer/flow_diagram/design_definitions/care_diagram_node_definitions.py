# /src/infrastructure/renderer/flow_diagram/design_definitions/care_diagram_node_definitions.py

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
CARE FLOW DIAGRAM NODES
"""

CARE_ROOT_NODE = FlowNode(
    title="Care Root",
    label="Care Root",
    class_name=NodeClassName.PAGE,
    screen_spec=None,
    screen_images=tuple(["care/C00-care-root-page-02.png"],
                        ),
    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=None,
    rules_engine=None,
    description="",
)

RESIDENTS_DASHBOARD_NODE = FlowNode(
    title="Residents Dashboard",
    label="Residents Dashboard",
    class_name=NodeClassName.PAGE,
    screen_spec=None,
    screen_images=tuple(
        ["care/CR01-resident-dashboard-05.png"],
    ),
    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=None,
    rules_engine=None,
    description="",
)

RESIDENT_RECORD_NODE = FlowNode(
    title="Resident Record",
    label="Resident Record",
    class_name=NodeClassName.PAGE,
    screen_spec=None,
    screen_images=tuple(["care/CR02-resident-record-01.png"]),
    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=None,
    rules_engine=None,
    description="",
)

RESIDENT_NOTES_NODE = FlowNode(
    title="Resident Notes",
    label="Freeform Notes",
    class_name=NodeClassName.FORM,
    screen_spec=None,
    screen_images=tuple(["care/free-form-notes-create.png"]),
    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=None,
    rules_engine=None,
    description="",
)

RESIDENT_PROFILES_NODE = FlowNode(
    title="Resident Profiles",
    label="Resident Profiles",
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

RESIDENT_PROFILE_CONFIG_NODE = FlowNode(
    title="Resident Configuration",
    label="Resident Configuration",
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

# plan_diagram_node_definitions.py

from src.application.flow_diagram.flow_diagram_types import (
    FlowNode,
    NodeClassName
)

from src.infrastructure.renderer.architecture_detail.data_models_domain.care.plan_domain_dtos import (
    THERAPEUTIC_PLAN_DASHBOARD_BACKEND_DTOS,
    THERAPEUTIC_PLAN_RECORD_BACKEND_DTOS,
    CREATE_THERAPEUTIC_PLAN_BACKEND_DTOS,
    REVISE_THERAPEUTIC_PLAN_BACKEND_DTOS,
    UPDATE_PROGRESS_THERAPEUTIC_PLAN_BACKEND_DTOS,
)

THERAPEUTIC_PLAN_DASHBOARD_NODE = FlowNode(
    title="Therapy Plans",
    label="Therapeutic Plans",
    class_name=NodeClassName.PAGE,
    screen_spec=None,
    screen_images=tuple(["care/therapy/TP01-therapeutic-plan-dashboard-01.png"]),
    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=THERAPEUTIC_PLAN_DASHBOARD_BACKEND_DTOS,
    rules_engine=None,
    description="",
)

THERAPEUTIC_PLAN_RECORD_NODE = FlowNode(
    title="Therapy Plan Record",
    label="Therapeutic Plan Record",
    class_name=NodeClassName.PAGE,
    screen_spec=None,
    screen_images=tuple([
        "care/therapy/TP02-therapeutic-plan-record-01.png",
    ]),

    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=THERAPEUTIC_PLAN_RECORD_BACKEND_DTOS,
    rules_engine=None,
    description="",
)

CREATE_THERAPEUTIC_PLAN_NODE = FlowNode(
    title="Create Therapeutic Plan",
    label="Create Therapeutic Plan",
    class_name=NodeClassName.FORM,
    screen_spec=None,
    screen_images=tuple([
        "care/therapy/TP03-create-therapeutic-plan-01.png",
        "care/therapy/TP06-therapeutic-plan-set-metrics-01.png",
    ]),

    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=CREATE_THERAPEUTIC_PLAN_BACKEND_DTOS,
    rules_engine=None,
    description="",
)

REVISE_THERAPEUTIC_PLAN_NODE = FlowNode(
    title="Revise Therapeutic Plan",
    label="Revise Therapeutic Plan",
    class_name=NodeClassName.FORM,
    screen_spec=None,
    screen_images=tuple([
        "care/therapy/TP04-revise-therapeutic-plan-01.png",
    ]),

    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=REVISE_THERAPEUTIC_PLAN_BACKEND_DTOS,
    rules_engine=None,
    description="",
)

UPDATE_PROGRESS_THERAPEUTIC_PLAN_NODE = FlowNode(
    title="Update Therapeutic Plan Progress",
    label="Update Plan Progress",
    class_name=NodeClassName.FORM,
    screen_spec=None,
    screen_images=tuple([
        "care/therapy/TP05-update-progress-therapeutic-plan-01.png",
    ]),

    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=UPDATE_PROGRESS_THERAPEUTIC_PLAN_BACKEND_DTOS,
    rules_engine=None,
    description="",
)

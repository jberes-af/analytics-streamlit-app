# /src/infrastructure/renderer/flow_diagram/design_definitions/adl_resident_diagram_node_definitions.py

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

from src.infrastructure.renderer.architecture_detail.screens.care.adl.caregiver_adl import (
    ADL_HOME_SCREEN_SPEC,
    ADL_ENTRY_SCREEN_SPEC,
    PATIENT_HISTORY_SCREEN_SPEC,
    OBSERVATION_ENTRY_SCREEN_SPEC,
)

from src.infrastructure.renderer.architecture_detail.use_cases.use_cases_dtos import (
    UC_HOME_01,
    UC_HOME_02,
    UC_HOME_03,
    UC_ADL_01,
    UC_OBS_01,
    UC_CORR_01,
    UC_ESC_01,
    UC_HIST_01,
    UC_HIST_02,
)

from src.infrastructure.renderer.architecture_detail.workflows.workflow_dtos import (
    WF_HOME_01, WF_HOME_02, WF_HOME_03, WF_HOME_04, WF_HOME_05,
    WF_ADL_01, WF_ADL_02, WF_ADL_03, WF_ADL_04, WF_ADL_05, WF_ADL_06, WF_ADL_07,
    WF_OBS_01, WF_OBS_02, WF_OBS_03, WF_OBS_04, WF_OBS_05,
    WF_HIST_01, WF_HIST_02, WF_HIST_03, WF_HIST_04, WF_HIST_05,
    WF_ESC_01, WF_ESC_02, WF_ESC_03, WF_ESC_04, WF_ESC_05, WF_ESC_06, WF_ESC_07,
)

"""
from src.infrastructure.renderer.architecture_detail.data_models_client.care.adl.adl_client_contracts_dtos import (
    ADL_HOME_CLIENT_CONTRACTS,
    ADL_ENTRY_CLIENT_CONTRACTS,
    ESCALATION_CLIENT_CONTRACTS,
    OBSERVATION_ENTRY_CLIENT_CONTRACTS,
    PATIENT_HISTORY_CLIENT_CONTRACTS,
)

from src.infrastructure.renderer.architecture_detail.data_models_backend.care.adl.adl_backend_dtos import (
    ADL_HOME_BACKEND_DTOS,
    ADL_ENTRY_BACKEND_DTOS,
    ESCALATION_BACKEND_DTOS,
    OBSERVATION_ENTRY_BACKEND_DTOS,
    PATIENT_HISTORY_BACKEND_DTOS,
)

from src.infrastructure.renderer.architecture_detail.data_models_rules_engine.spec_dtos import (
    ADL_ENTRY_RULES_ENGINE,
)
"""

from src.infrastructure.renderer.architecture_detail.data_models_domain.care.adl_domain_dtos import (
    ADL_ASSESSMENT_BACKEND_DTOS,
    ADL_DEVICE_LINK_BACKEND_DTOS,
    ADL_DEVICE_TRENDS_BACKEND_DTOS,
    ADL_OBSERVATION_BACKEND_DTOS,
    ADL_RESIDENT_SUMMARY_BACKEND_DTOS,
)

"""
ADL FLOW DIAGRAM NODES
"""

RESIDENT_ADL_SUMMARY_NODE = FlowNode(
    title="Resident ADL Summary",
    label="Resident ADL Summary",
    class_name=NodeClassName.PAGE,
    screen_spec=ADL_HOME_SCREEN_SPEC,
    screen_images=tuple(
        ["care/adl/ADL01-resident-adl-obs-dashboard-02.png"]),

    required_permissions=tuple([
        PermissionRequirement(
            domain=DomainObject.ADL_ASSESSMENT,
            action=Action.CREATE,
        )]
    ),
    use_cases=tuple([
        UC_HOME_01, UC_HOME_02, UC_HOME_03,
    ]),
    workflows=tuple([
        WF_HOME_01, WF_HOME_02, WF_HOME_03, WF_HOME_04, WF_HOME_05,
    ]),
    client_contracts=None,
    backend_data_model=ADL_RESIDENT_SUMMARY_BACKEND_DTOS,
    rules_engine=None,
    description="Main landing page for the Resident-specific ADL workflow.",
)

ADL_ASSESSMENT_NODE = FlowNode(
    title="ADL Assessment",
    label="ADL Assessment",
    class_name=NodeClassName.FORM,
    screen_spec=ADL_ENTRY_SCREEN_SPEC,
    screen_images=tuple(["care/adl/ADL04-adl-entry-score-slider-01.png"]),
    required_permissions=tuple([
        PermissionRequirement(
            domain=DomainObject.ADL_ASSESSMENT,
            action=Action.CREATE,
        )
    ]
    ),
    use_cases=tuple([
        UC_ADL_01, UC_CORR_01,
    ]),
    workflows=tuple([
        WF_ADL_01, WF_ADL_02, WF_ADL_03, WF_ADL_04, WF_ADL_05, WF_ADL_06, WF_ADL_07,
    ]),
    client_contracts=None,
    backend_data_model=ADL_ASSESSMENT_BACKEND_DTOS,
    rules_engine=None,
    description="Form for entering ADL information.",
)

ADL_OBSERVATION_NODE = FlowNode(
    title="ADL Observation",
    label="ADL Observation",
    class_name=NodeClassName.FORM,
    screen_spec=OBSERVATION_ENTRY_SCREEN_SPEC,
    screen_images=tuple(["care/adl/ADL05-adl-obs-entry-01.png",
                         "care/adl/ADL05-adl-obs-entry-02.png"]),
    required_permissions=tuple([
        PermissionRequirement(
            domain=DomainObject.ADL_ASSESSMENT,
            action=Action.CREATE,
        )]
    ),
    use_cases=tuple([
        UC_OBS_01, UC_CORR_01,
    ]),
    workflows=tuple([
        WF_OBS_01, WF_OBS_02, WF_OBS_03, WF_OBS_04, WF_OBS_05,
    ]),
    client_contracts=None,
    backend_data_model=ADL_OBSERVATION_BACKEND_DTOS,
    rules_engine=None,
    description="Form for entering observations.",
)

"""
HISTORY_NODE = FlowNode(
    title="View History",
    label="View History",
    class_name=NodeClassName.PAGE,
    screen_spec=PATIENT_HISTORY_SCREEN_SPEC,
    screen_images=tuple([]),

    required_permissions=tuple([
        PermissionRequirement(
            domain=DomainObject.ADL_ASSESSMENT,
            action=Action.CREATE,
        )]
    ),
    use_cases=tuple([
        UC_HIST_01, UC_HIST_02, UC_CORR_01,
    ]),
    workflows=tuple([
        WF_HIST_01, WF_HIST_02, WF_HIST_03, WF_HIST_04, WF_HIST_05,
    ]),
    client_contracts=tuple(),
    backend_data_model=tuple(),
    rules_engine=None,
    description="Historical ADL and observation records.",
)
"""

ADL_TRENDS_NODE = FlowNode(
    title="ADL Trends",
    label="ADL Trends",
    class_name=NodeClassName.PAGE,
    screen_spec=PATIENT_HISTORY_SCREEN_SPEC,
    screen_images=tuple(
        ["care/adl/ADL03-adl-trends-01.png"],
    ),

    required_permissions=tuple([
        PermissionRequirement(
            domain=DomainObject.ADL_ASSESSMENT,
            action=Action.CREATE,
        )]
    ),
    use_cases=tuple([
        UC_HIST_01, UC_HIST_02, UC_CORR_01,
    ]),
    workflows=tuple([
        WF_HIST_01, WF_HIST_02, WF_HIST_03, WF_HIST_04, WF_HIST_05,
    ]),
    client_contracts=None,
    backend_data_model=ADL_DEVICE_TRENDS_BACKEND_DTOS,
    rules_engine=None,
    description="Historical ADL and observation records.",
)

DEVICE_ADL_LINK_NODE = FlowNode(
    title="Device-ADL Link",
    label="Device-ADL Link",
    class_name=NodeClassName.FORM,
    screen_spec=None,
    screen_images=tuple(
        ["care/adl/ADL02-device-adl-links-dashboard-01.png"]
    ),
    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=None,
    rules_engine=None,
    description="",
)

DEVICE_ADL_TRENDS_NODE = FlowNode(
    title="ADL-Device Trends",
    label="ADL-Device Trends",
    class_name=NodeClassName.PAGE,
    screen_spec=None,
    screen_images=tuple(
        [
            "care/adl/ADL03-adl-trends-01.png",
        ]
    ),
    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=None,
    rules_engine=None,
    description="",
)

# /src/infrastructure/renderer/flow_diagram/notification_diagram_node_definitions.py

from src.domain.mobile_app_enums import (
    DomainObject,
    Action,
)

from src.domain.mobile_app_types import (
    PermissionRequirement,
)

from src.application.flow_diagram.flow_diagram_types import (
    NodeClassName,
    FlowEdge,
    FlowNode,
)

from src.infrastructure.renderer.screen_design_detail.screens.care.adl import (
    ADL_HOME_SCREEN_SPEC,
    ADL_ENTRY_SCREEN_SPEC,
    ESCALATION_SCREEN_SPEC,
    PATIENT_SUMMARY_SCREEN_SPEC,
    PATIENT_HISTORY_SCREEN_SPEC,
    OBSERVATION_ENTRY_SCREEN_SPEC,
)

from src.infrastructure.renderer.screen_design_detail.use_cases.use_cases_dtos import (
    UC_HOME_01,
    UC_HOME_02,
    UC_HOME_03,
    UC_PAT_01,
    UC_PAT_02,
    UC_PAT_03,
    UC_ADL_01,
    UC_OBS_01,
    UC_CORR_01,
    UC_ESC_01,
    UC_HIST_01,
    UC_HIST_02,
)

from src.infrastructure.renderer.screen_design_detail.workflows.workflow_dtos import (
    WF_HOME_01, WF_HOME_02, WF_HOME_03, WF_HOME_04, WF_HOME_05,
    WF_ADL_01, WF_ADL_02, WF_ADL_03, WF_ADL_04, WF_ADL_05, WF_ADL_06, WF_ADL_07,
    WF_OBS_01, WF_OBS_02, WF_OBS_03, WF_OBS_04, WF_OBS_05,
    WF_HIST_01, WF_HIST_02, WF_HIST_03, WF_HIST_04, WF_HIST_05,
    WF_PAT_01, WF_PAT_02, WF_PAT_03, WF_PAT_04, WF_PAT_05, WF_PAT_06,
    WF_ESC_01, WF_ESC_02, WF_ESC_03, WF_ESC_04, WF_ESC_05, WF_ESC_06, WF_ESC_07,
)

from src.infrastructure.renderer.screen_design_detail.data_models.client.client_contracts_dtos import (
    ADL_HOME_CLIENT_CONTRACTS,
    ADL_ENTRY_CLIENT_CONTRACTS,
    ESCALATION_CLIENT_CONTRACTS,
    OBSERVATION_ENTRY_CLIENT_CONTRACTS,
    PATIENT_HISTORY_CLIENT_CONTRACTS,
    PATIENT_SUMMARY_CLIENT_CONTRACTS,
)

from src.infrastructure.renderer.screen_design_detail.data_models.backend.backend_dtos import (
    ADL_HOME_BACKEND_DTOS,
    ADL_ENTRY_BACKEND_DTOS,
    ESCALATION_BACKEND_DTOS,
    OBSERVATION_ENTRY_BACKEND_DTOS,
    PATIENT_HISTORY_BACKEND_DTOS,
    PATIENT_SUMMARY_BACKEND_DTOS,
)

from src.infrastructure.renderer.screen_design_detail.data_models.rules_engine.spec_dtos import (
    ADL_ENTRY_RULES_ENGINE,
)

"""
PATIENT FLOW DIAGRAM NODES
"""

ADL_HOME_NODE = FlowNode(
    title="ADL Home Page",
    label="ADL Home Page",
    class_name=NodeClassName.PAGE,
    screen_spec=ADL_HOME_SCREEN_SPEC,
    screen_images=tuple(["adl_home/adl-home-page-01.png"]),

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
    client_contracts=ADL_HOME_CLIENT_CONTRACTS,
    backend_data_model=ADL_HOME_BACKEND_DTOS,
    rules_engine=None,
    description="Main landing page for the ADL workflow.",
)

PATIENT_SUMMARY_NODE = FlowNode(
    title="Patient View",
    label="Patient View",
    class_name=NodeClassName.PAGE,
    screen_spec=PATIENT_SUMMARY_SCREEN_SPEC,
    screen_images=tuple([
        "resident_view/patient-summary.png",
        "resident_view/patient-summary-option-b.png",
    ]),
    required_permissions=tuple([
        PermissionRequirement(
            domain=DomainObject.ADL_ASSESSMENT,
            action=Action.CREATE,
        )]
    ),
    use_cases=tuple([
        UC_PAT_01, UC_PAT_02, UC_PAT_03,
    ]),
    workflows=tuple([
        WF_PAT_01, WF_PAT_02, WF_PAT_03, WF_PAT_04, WF_PAT_05, WF_PAT_06,
    ]),
    client_contracts=PATIENT_SUMMARY_CLIENT_CONTRACTS,
    backend_data_model=PATIENT_SUMMARY_BACKEND_DTOS,
    rules_engine=None,
    description="Displays patient-specific ADL actions.",
)

ADL_ENTRY_NODE = FlowNode(
    title="ADL Entry",
    label="ADL Entry",
    class_name=NodeClassName.FORM,
    screen_spec=ADL_ENTRY_SCREEN_SPEC,
    screen_images=tuple(["adl_entry/adl-entry-score-slider-bathing.png"]),

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
    client_contracts=ADL_ENTRY_CLIENT_CONTRACTS,
    backend_data_model=ADL_ENTRY_BACKEND_DTOS,
    rules_engine=ADL_ENTRY_RULES_ENGINE,
    description="Form for entering ADL information.",
)

OBS_ENTRY_NODE = FlowNode(
    title="Observation Entry",
    label="Observation Entry",
    class_name=NodeClassName.FORM,
    screen_spec=OBSERVATION_ENTRY_SCREEN_SPEC,
    # dto_code=OBS_ENTRY_DTO,
    screen_images=tuple(["observation_entry/obs-entry-score-and-notes.png",
                         "observation_entry/obs-entry-select-observation.png"]),
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
    client_contracts=OBSERVATION_ENTRY_CLIENT_CONTRACTS,
    backend_data_model=OBSERVATION_ENTRY_BACKEND_DTOS,
    rules_engine=None,
    description="Form for entering observations.",
)

PRIORITY_NODE = FlowNode(
    title="Prioritize",
    label="Prioritize",
    class_name=NodeClassName.UTILITY,
    screen_spec=ESCALATION_SCREEN_SPEC,
    screen_images=tuple(["priority_escalate/escalate.png"]),
    use_cases=tuple([
        UC_ESC_01,
    ]),
    workflows=tuple([
        WF_ESC_01, WF_ESC_02, WF_ESC_03, WF_ESC_04, WF_ESC_05, WF_ESC_06, WF_ESC_07,
    ]),
    client_contracts=ESCALATION_CLIENT_CONTRACTS,
    backend_data_model=ESCALATION_BACKEND_DTOS,
    rules_engine=None,
    description="Prioritization workflow.",
)

HISTORY_NODE = FlowNode(
    title="View History",
    label="View History",
    class_name=NodeClassName.UTILITY,
    screen_spec=PATIENT_HISTORY_SCREEN_SPEC,
    screen_images=tuple(["history/daily-trends.png",
                         "history/view-history.png"]),

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
    client_contracts=PATIENT_HISTORY_CLIENT_CONTRACTS,
    backend_data_model=PATIENT_HISTORY_BACKEND_DTOS,
    rules_engine=None,
    description="Historical ADL and observation records.",
)

"""
FLOW DIAGRAM EDGES
"""

NOTIFICATION_EDGE_1 = FlowEdge(
    source="ADL_Home",
    target="Patient_Summary",
    action_label=None
)

NOTIFICATION_EDGE_2 = FlowEdge(
    source="Patient_Summary",
    target="ADL_Entry",
    action_label="Tap Enter ADL"
)

NOTIFICATION_EDGE_3 = FlowEdge(
    source="ADL_Entry",
    target="Patient_Summary",
    action_label="Save")

NOTIFICATION_EDGE_4 = FlowEdge(
    source="Patient_Summary",
    target="OBS_Entry",
    action_label="Tap Add Observation"
)

NOTIFICATION_EDGE_5 = FlowEdge(
    source="OBS_Entry",
    target="Patient_Summary",
    action_label="Save"
)

NOTIFICATION_EDGE_6 = FlowEdge(
    source="Patient_Summary",
    target="Priority",
    action_label="Tap Prioritize"
)

NOTIFICATION_EDGE_7 = FlowEdge(
    source="Priority",
    target="Patient_Summary",
    action_label="Submit"
)

NOTIFICATION_EDGE_8 = FlowEdge(
    source="Patient_Summary",
    target="History",
    action_label="Tap View History"
)

NOTIFICATION_EDGE_9 = FlowEdge(
    source="History",
    target="ADL_Home",
    action_label="Back"
)

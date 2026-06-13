# /src/infrastructure/renderer/architecture_detail/use_cases/use_case_dtos.py

from src.domain.mobile_app_enums import (
    Role,
    UseCaseType,
)

from src.domain.mobile_app_types import UseCase

from src.infrastructure.renderer.architecture_detail.workflows.workflow_dtos import (
    WF_HOME_01, WF_HOME_02, WF_HOME_03, WF_HOME_04, WF_HOME_05,
    WF_QUEUE_01, WF_QUEUE_02, WF_QUEUE_03, WF_QUEUE_04,
    WF_QUEUE_DET_01, WF_QUEUE_DET_02, WF_QUEUE_DET_03, WF_QUEUE_DET_04,
    WF_ADL_01, WF_ADL_02, WF_ADL_03, WF_ADL_04, WF_ADL_05, WF_ADL_06, WF_ADL_07,
    WF_OBS_01, WF_OBS_02, WF_OBS_03, WF_OBS_04, WF_OBS_05,
    WF_HIST_01, WF_HIST_02, WF_HIST_03, WF_HIST_04, WF_HIST_05,
    WF_PAT_01, WF_PAT_02, WF_PAT_03, WF_PAT_04, WF_PAT_05, WF_PAT_06,
    WF_ESC_01, WF_ESC_02, WF_ESC_03, WF_ESC_04, WF_ESC_05, WF_ESC_06, WF_ESC_07,
    WF_CORR_01, WF_CORR_02, WF_CORR_03,
)

UC_HOME_01 = UseCase(
    name="View shift dashboard",
    use_case_id="UC-HOME-01",
    use_case_types=(UseCaseType.REVIEW,),
    description="Display assigned patients with status indicators and priority signals.",
    primary_actors=(
        Role.INFORMAL_CAREGIVER,
        Role.PROFESSIONAL_CAREGIVER_NON_CMS,
        Role.CMS_BILLING_PROVIDER,
    ),
    outcome=(
        "User sees assigned patients grouped by priority with current ADL completion indicators."
    ),
    related_workflows=tuple(
        [WF_HOME_01, WF_HOME_02, WF_HOME_03, WF_HOME_04, WF_HOME_05]
    ),
)

UC_HOME_02 = UseCase(
    name="Identify patients needing attention",
    use_case_id="UC-HOME-02",
    use_case_types=(UseCaseType.ANALYZE,),
    description=(
        "Highlight patients requiring review based on missing data, decline signals, or alerts."
    ),
    primary_actors=(
        Role.PROFESSIONAL_CAREGIVER_NON_CMS,
        Role.CMS_BILLING_PROVIDER,
    ),
    outcome=(
        "User can quickly identify patients who need review or action during the shift."
    ),
    related_workflows=tuple(
        [WF_HOME_02, WF_HOME_03, WF_QUEUE_01, WF_QUEUE_02]
    ),
)

UC_HOME_03 = UseCase(
    name="Track ADL completion",
    use_case_id="UC-HOME-03",
    use_case_types=(UseCaseType.REVIEW,),
    description=(
        "View completion status of required ADLs for each patient during the current shift."
    ),
    primary_actors=(
        Role.PROFESSIONAL_CAREGIVER_NON_CMS,
        Role.CMS_BILLING_PROVIDER,
    ),
    outcome=(
        "User sees which required ADL assessments are complete, missing, or unable to assess."
    ),
    related_workflows=tuple(
        [WF_HOME_01, WF_HOME_03]
    ),
)

UC_PAT_01 = UseCase(
    name="View patient summary",
    use_case_id="UC-PAT-01",
    use_case_types=(UseCaseType.REVIEW,),
    description="Display ADL status, recent changes, and observations for a selected patient.",
    primary_actors=(
        Role.INFORMAL_CAREGIVER,
        Role.PROFESSIONAL_CAREGIVER_NON_CMS,
        Role.CMS_BILLING_PROVIDER,
    ),
    outcome=(
        "User understands the selected patient's current ADL status, recent changes, and required actions."
    ),
    related_workflows=tuple(
        [WF_PAT_01, WF_PAT_02, WF_PAT_03, WF_PAT_04, WF_PAT_05, WF_PAT_06]
    ),
)

UC_PAT_02 = UseCase(
    name="Review recent ADL status",
    use_case_id="UC-PAT-02",
    use_case_types=(UseCaseType.REVIEW,),
    description=(
        "Display current and recent ADL status across ADL categories for the selected patient."
    ),
    primary_actors=(
        Role.INFORMAL_CAREGIVER,
        Role.PROFESSIONAL_CAREGIVER_NON_CMS,
        Role.CMS_BILLING_PROVIDER,
    ),
    outcome=(
        "User reviews the patient's current ADL status across categories "
        "and identifies any recent changes."
    ),
    related_workflows=tuple(
        [WF_PAT_02, WF_PAT_04]
    ),
)

UC_PAT_03 = UseCase(
    name="Review recent Observations",
    use_case_id="UC-PAT-03",
    use_case_types=tuple([UseCaseType.REVIEW]),
    description="Display recent narrative observations associated with the patient.",
    primary_actors=tuple([
        Role.INFORMAL_CAREGIVER,
        Role.PROFESSIONAL_CAREGIVER_NON_CMS,
        Role.CMS_BILLING_PROVIDER,
    ]),
    outcome=(
        "User reviews recent observation notes that provide context for the patient's condition."
    ),
    related_workflows=tuple(
        [WF_PAT_01, WF_PAT_03, WF_PAT_05]
    ),
)

UC_ADL_01 = UseCase(
    name="Enter ADL assessment",
    use_case_id="UC-ADL-01",
    use_case_types=(UseCaseType.CAPTURE, UseCaseType.DOCUMENT),
    description="Record a structured assessment for a specific ADL category.",
    primary_actors=(
        Role.INFORMAL_CAREGIVER,
        Role.PROFESSIONAL_CAREGIVER_NON_CMS,
    ),
    outcome=(
        "User saves a timestamped ADL assessment that is reflected in the patient's record."
    ),
    related_workflows=tuple(
        [WF_ADL_01, WF_ADL_02, WF_ADL_03, WF_ADL_04, WF_ADL_05, WF_ADL_06, WF_ADL_07]
    ),
)

UC_OBS_01 = UseCase(
    name="Enter observation note",
    use_case_id="UC-OBS-01",
    use_case_types=(UseCaseType.CAPTURE, UseCaseType.DOCUMENT),
    description="Record a narrative observation for a selected category.",
    primary_actors=(
        Role.INFORMAL_CAREGIVER,
        Role.PROFESSIONAL_CAREGIVER_NON_CMS,
    ),
    outcome=(
        "User saves a timestamped observation note that appears in the patient's timeline."
    ),
    related_workflows=tuple(
        [WF_OBS_01, WF_OBS_02, WF_OBS_03, WF_OBS_04, WF_OBS_05]
    ),
)

UC_CORR_01 = UseCase(
    name="Correct entry",
    use_case_id="UC-CORR-01",
    use_case_types=(UseCaseType.CORRECT,),
    description="Fix an incorrect ADL score, note, or timestamp while preserving audit history.",
    primary_actors=(
        Role.INFORMAL_CAREGIVER,
        Role.PROFESSIONAL_CAREGIVER_NON_CMS,
        Role.CMS_BILLING_PROVIDER,
    ),
    outcome=(
        "User corrects an inaccurate entry while preserving the original record for audit history."
    ),
    related_workflows=tuple(
        [WF_CORR_01, WF_CORR_02, WF_CORR_03]
    ),
)

UC_QUEUE_01 = UseCase(
    name="View review queue",
    use_case_id="UC-QUEUE-01",
    use_case_types=(UseCaseType.REVIEW,),
    description="Display prioritized list of patients or issues requiring review.",
    primary_actors=(
        Role.PROFESSIONAL_CAREGIVER_NON_CMS,
        Role.CMS_BILLING_PROVIDER,
    ),
    outcome=(
        "User sees a prioritized list of patients or issues requiring review."
    ),
    related_workflows=tuple(
        [WF_QUEUE_01, WF_QUEUE_02, WF_QUEUE_03, WF_QUEUE_04]
    ),
)

UC_QUEUE_02 = UseCase(
    name="Review flagged issue",
    use_case_id="UC-QUEUE-02",
    use_case_types=(UseCaseType.REVIEW, UseCaseType.ANALYZE),
    description="Display detailed context, trends, and supporting data for a flagged issue.",
    primary_actors=(
        Role.PROFESSIONAL_CAREGIVER_NON_CMS,
        Role.CMS_BILLING_PROVIDER,
    ),
    outcome=(
        "User understands why the issue was flagged and what supporting data should be reviewed."
    ),
    related_workflows=tuple(
        [WF_QUEUE_DET_01, WF_QUEUE_DET_02, WF_QUEUE_DET_03, WF_QUEUE_DET_04]
    ),
)

UC_QUEUE_03 = UseCase(
    name="Acknowledge review item",
    use_case_id="UC-QUEUE-03",
    use_case_types=(UseCaseType.ACKNOWLEDGE,),
    description="Mark a review item as reviewed or handled.",
    primary_actors=(
        Role.PROFESSIONAL_CAREGIVER_NON_CMS,
        Role.CMS_BILLING_PROVIDER,
    ),
    outcome=(
        "User marks the review item as handled so its status is updated in the queue."
    ),
    related_workflows=tuple(
        [WF_QUEUE_DET_03, WF_QUEUE_DET_04]
    ),
)

UC_ESC_01 = UseCase(
    name="Escalate concern",
    use_case_id="UC-ESC-01",
    use_case_types=(UseCaseType.ESCALATE,),
    description="Create a structured escalation for a patient concern.",
    primary_actors=(
        Role.INFORMAL_CAREGIVER,
        Role.PROFESSIONAL_CAREGIVER_NON_CMS,
        Role.CMS_BILLING_PROVIDER,
    ),
    outcome=(
        "User creates an escalation that is assigned for follow-up and "
        "linked to the patient record."
    ),
    related_workflows=tuple(
        [WF_ESC_01, WF_ESC_02, WF_ESC_03, WF_ESC_04, WF_ESC_05, WF_ESC_06, WF_ESC_07]
    ),
)

UC_HIST_01 = UseCase(
    name="View patient history",
    use_case_id="UC-HIST-01",
    use_case_types=(UseCaseType.REVIEW,),
    description="Display chronological ADL and observation history.",
    primary_actors=(
        Role.INFORMAL_CAREGIVER,
        Role.PROFESSIONAL_CAREGIVER_NON_CMS,
        Role.CMS_BILLING_PROVIDER,
    ),
    outcome=(
        "User reviews the patient's ADL and observation history in chronological context."
    ),
    related_workflows=tuple(
        [WF_HIST_01, WF_HIST_03, WF_HIST_04, WF_HIST_05]
    ),
)

UC_HIST_02 = UseCase(
    name="Analyze ADL trends",
    use_case_id="UC-HIST-02",
    use_case_types=(UseCaseType.ANALYZE,),
    description="Display trends and patterns derived from historical ADL data.",
    primary_actors=(
        Role.INFORMAL_CAREGIVER,
        Role.PROFESSIONAL_CAREGIVER_NON_CMS,
        Role.CMS_BILLING_PROVIDER,
    ),
    outcome=(
        "User identifies ADL trends and changes in functional status over time."
    ),
    related_workflows=tuple(
        [WF_HIST_01, WF_HIST_02, WF_HIST_03, WF_HIST_05]
    ),
)

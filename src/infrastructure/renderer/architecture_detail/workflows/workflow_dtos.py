from src.domain.mobile_app_enums import (
    Role,
    WorkflowComplexity,
)

from src.domain.mobile_app_types import (
    AuditRule,
    DataState,
    EdgeCase,
    FlowStep,
    SystemBehavior,
    Workflow,
)

# ============================================================
# ADL HOME PAGE
# ============================================================

WF_HOME_01 = Workflow(
    workflow_id="WF-HOME-01",
    name="Load caregiver shift dashboard",
    primary_actor="Caregiver",
    goal="Load assigned patients and shift-level ADL status.",
    trigger="User opens ADL Home screen.",
    entry_conditions=("User is authenticated.", "Shift context is available."),
    exit_conditions=("Shift dashboard data is loaded.",),
    success_outcome="Caregiver sees assigned patients, priority counts, and ADL completion status.",
    complexity=WorkflowComplexity.L2,
    flow=(
        FlowStep(1, "Caregiver", "Opens ADL Home screen."),
        FlowStep(2, "System", "Loads assigned patients for the active shift."),
        FlowStep(3, "System", "Loads ADL completion, alerts, escalations, and review signals."),
        FlowStep(4, "System", "Returns home screen response data."),
    ),
    system_behaviors=(
        SystemBehavior("Resolve current caregiver and shift context.", "ShiftContextService"),
        SystemBehavior("Build ADL Home response DTO.", "AdlHomeApplicationService"),
    ),
    data_state=(
        DataState("caregiver_id", True),
        DataState("shift_id", True),
        DataState("assigned_patients", True),
        DataState("adl_completion_status", True),
        DataState("review_signals", False),
    ),
    related_use_case="UC-HOME-01",
    related_screens=("screen.adl.home",),
    related_backend_contracts=("AdlHomeQueryDTO", "AdlHomeResponseDTO"),
)

WF_HOME_02 = Workflow(
    workflow_id="WF-HOME-02",
    name="Group patients by priority",
    primary_actor="System",
    goal="Organize patients into high, review, and stable groups.",
    trigger="ADL Home data is loaded.",
    entry_conditions=("Assigned patients are loaded.", "Review signals are available."),
    exit_conditions=("Patients are grouped by priority.",),
    success_outcome="Caregiver sees patients organized by attention level.",
    complexity=WorkflowComplexity.L2,
    flow=(
        FlowStep(1, "System", "Evaluates review signals for each assigned patient."),
        FlowStep(2, "System", "Calculates patient priority level."),
        FlowStep(3, "System", "Groups patients into priority sections."),
    ),
    system_behaviors=(
        SystemBehavior("Apply priority rules.", "PriorityGroupingService"),
    ),
    data_state=(
        DataState("patient_priority_level", True),
        DataState("priority_patients", False),
        DataState("routine_patients", False),
    ),
    related_use_case="UC-HOME-02",
    related_screens=("screen.adl.home",),
    related_backend_contracts=("ReviewSignalDTO", "PatientHomeCardDTO"),
)

WF_HOME_03 = Workflow(
    workflow_id="WF-HOME-03",
    name="Display patient cards with signals",
    primary_actor="System",
    goal="Show patient cards with status, completion, and attention signals.",
    trigger="Patients are grouped by priority.",
    entry_conditions=("Patient card data is available.",),
    exit_conditions=("Patient cards are displayed.",),
    success_outcome="Caregiver can quickly scan patient status and required attention.",
    complexity=WorkflowComplexity.L1,
    flow=(
        FlowStep(1, "System", "Builds patient card DTOs."),
        FlowStep(2, "System", "Displays status, reason, ADL completion, and signal badges."),
    ),
    data_state=(
        DataState("patient_home_cards", True),
        DataState("adl_completion_status", True),
        DataState("review_signals", False),
    ),
    related_use_case="UC-HOME-01",
    related_screens=("screen.adl.home",),
    related_backend_contracts=("PatientHomeCardDTO", "AdlCompletionStatusDTO", "ReviewSignalDTO"),
)

WF_HOME_04 = Workflow(
    workflow_id="WF-HOME-04",
    name="Route to Patient Summary",
    primary_actor="Caregiver",
    goal="Open the selected patient's shift snapshot.",
    trigger="User taps a patient card.",
    entry_conditions=("Patient card is visible.",),
    exit_conditions=("Patient Summary screen opens.",),
    success_outcome="Caregiver enters the selected patient's clinical context.",
    complexity=WorkflowComplexity.L1,
    flow=(
        FlowStep(1, "Caregiver", "Taps patient card."),
        FlowStep(2, "System", "Navigates to Patient Summary for selected patient."),
    ),
    data_state=(DataState("patient_id", True),),
    related_use_case="UC-PAT-01",
    related_screens=("screen.adl.home", "screen.patient.summary"),
    related_backend_contracts=("PatientSnapshotQueryDTO", "PatientShiftSnapshotResponseDTO"),
)

WF_HOME_05 = Workflow(
    workflow_id="WF-HOME-05",
    name="Route to Review Queue",
    primary_actor="Caregiver",
    goal="Open full list of patients or issues requiring review.",
    trigger="User taps View Review Queue.",
    entry_conditions=("Review queue entry point is visible.",),
    exit_conditions=("Review Queue screen opens.",),
    success_outcome="Caregiver sees prioritized review items.",
    complexity=WorkflowComplexity.L1,
    flow=(
        FlowStep(1, "Caregiver", "Taps Review Queue."),
        FlowStep(2, "System", "Navigates to Review Queue screen."),
    ),
    related_use_case="UC-QUEUE-01",
    related_screens=("screen.adl.home", "screen.review.queue"),
    related_backend_contracts=("ReviewQueueQueryDTO", "ReviewQueueResponseDTO"),
)

# ============================================================
# PATIENT SUMMARY
# ============================================================

WF_PAT_01 = Workflow(
    workflow_id="WF-PAT-01",
    name="Load patient shift snapshot",
    primary_actor="Caregiver",
    goal="Load patient-specific ADL, observation, alert, and task context.",
    trigger="User opens Patient Summary.",
    entry_conditions=("Patient is selected.",),
    exit_conditions=("Patient snapshot data is loaded.",),
    success_outcome="Caregiver sees current patient status and recent changes.",
    complexity=WorkflowComplexity.L2,
    flow=(
        FlowStep(1, "System", "Loads patient demographic and shift context."),
        FlowStep(2, "System", "Loads ADL, observation, alert, escalation, and task data."),
        FlowStep(3, "System", "Builds Patient Shift Snapshot DTO."),
    ),
    data_state=(
        DataState("patient_id", True),
        DataState("shift_id", True),
        DataState("adl_cards", True),
        DataState("recent_observations", False),
        DataState("open_escalations", False),
    ),
    related_use_case="UC-PAT-01",
    related_screens=("screen.patient.summary",),
    related_backend_contracts=("PatientSnapshotQueryDTO", "PatientShiftSnapshotResponseDTO"),
)

WF_PAT_02 = Workflow(
    workflow_id="WF-PAT-02",
    name="Compute ADL deltas",
    primary_actor="System",
    goal="Compare current ADL scores against previous shift and baseline.",
    trigger="Patient ADL data is loaded.",
    entry_conditions=("Current, previous, or baseline ADL data is available.",),
    exit_conditions=("ADL comparison status is computed.",),
    success_outcome="Caregiver sees whether each ADL is stable, improved, or declined.",
    complexity=WorkflowComplexity.L2,
    flow=(
        FlowStep(1, "System", "Retrieves current ADL values."),
        FlowStep(2, "System", "Retrieves previous shift and baseline values."),
        FlowStep(3, "System", "Computes change status and trend direction."),
    ),
    system_behaviors=(
        SystemBehavior("Compare ADL scores against baseline and prior values.", "AdlComparisonService"),
    ),
    data_state=(
        DataState("current_score", False),
        DataState("previous_score", False),
        DataState("baseline_score", False),
        DataState("change_status", True),
    ),
    related_use_case="UC-PAT-02",
    related_screens=("screen.patient.summary",),
    related_backend_contracts=("AdlStatusCardDTO",),
)

WF_PAT_03 = Workflow(
    workflow_id="WF-PAT-03",
    name="Generate shift summary",
    primary_actor="System",
    goal="Generate concise auto-text summary of important patient changes.",
    trigger="ADL deltas and observations are available.",
    entry_conditions=("ADL comparison data is computed.",),
    exit_conditions=("Shift summary is generated.",),
    success_outcome="Caregiver understands the most important changes quickly.",
    complexity=WorkflowComplexity.L2,
    flow=(
        FlowStep(1, "System", "Evaluates ADL deltas, observations, alerts, and escalations."),
        FlowStep(2, "System", "Selects highest-salience changes."),
        FlowStep(3, "System", "Generates concise shift summary text."),
    ),
    system_behaviors=(
        SystemBehavior("Generate natural-language summary from structured signals.", "ShiftSummaryService"),
    ),
    data_state=(DataState("shift_summary", True),),
    related_use_case="UC-PAT-01",
    related_screens=("screen.patient.summary",),
    related_backend_contracts=("PatientShiftSnapshotResponseDTO",),
)

WF_PAT_04 = Workflow(
    workflow_id="WF-PAT-04",
    name="Display ADL cards",
    primary_actor="System",
    goal="Render ADL cards for each ADL category.",
    trigger="Patient snapshot DTO is available.",
    entry_conditions=("ADL card data is available.",),
    exit_conditions=("ADL cards are visible.",),
    success_outcome="Caregiver can review ADL status and select an ADL for detail or entry.",
    complexity=WorkflowComplexity.L1,
    flow=(
        FlowStep(1, "System", "Displays one card per ADL category."),
        FlowStep(2, "System", "Shows current status, trend, last update, and add/detail actions."),
    ),
    data_state=(DataState("adl_cards", True),),
    related_use_case="UC-PAT-02",
    related_screens=("screen.patient.summary",),
    related_backend_contracts=("AdlStatusCardDTO",),
)

WF_PAT_05 = Workflow(
    workflow_id="WF-PAT-05",
    name="Surface alerts and tasks",
    primary_actor="System",
    goal="Show required actions, open alerts, and unresolved escalations.",
    trigger="Patient snapshot is loaded.",
    entry_conditions=("Alert/task data is available or empty.",),
    exit_conditions=("Actions and alerts are displayed.",),
    success_outcome="Caregiver knows what needs attention for the patient.",
    complexity=WorkflowComplexity.L2,
    flow=(
        FlowStep(1, "System", "Evaluates missing ADLs, open alerts, and unresolved escalations."),
        FlowStep(2, "System", "Builds recommended action list."),
        FlowStep(3, "System", "Displays tasks and alerts on Patient Summary."),
    ),
    data_state=(
        DataState("actions_required", False),
        DataState("active_alerts", False),
        DataState("open_escalations", False),
    ),
    related_use_case="UC-PAT-01",
    related_screens=("screen.patient.summary",),
    related_backend_contracts=("AlertSummaryDTO", "EscalationSummaryDTO"),
)

WF_PAT_06 = Workflow(
    workflow_id="WF-PAT-06",
    name="Route from Patient Summary",
    primary_actor="Caregiver",
    goal="Navigate from Patient Summary to entry, history, or escalation screens.",
    trigger="User taps an action on Patient Summary.",
    entry_conditions=("Patient Summary screen is visible.",),
    exit_conditions=("Target screen opens.",),
    success_outcome="Caregiver reaches the appropriate action screen in patient context.",
    complexity=WorkflowComplexity.L1,
    flow=(
        FlowStep(1, "Caregiver", "Taps Enter ADL, Add Observation, Escalate, or View History."),
        FlowStep(2, "System", "Preserves patient context."),
        FlowStep(3, "System", "Navigates to selected target screen."),
    ),
    data_state=(DataState("patient_id", True),),
    related_use_case="UC-PAT-01",
    related_screens=(
        "screen.patient.summary",
        "screen.adl.entry",
        "screen.observation.entry",
        "screen.escalate",
        "screen.history",
    ),
)

# ============================================================
# REVIEW QUEUE
# ============================================================

WF_QUEUE_01 = Workflow(
    workflow_id="WF-QUEUE-01",
    name="Aggregate signals across patients",
    primary_actor="System",
    goal="Collect review signals for assigned or visible patients.",
    trigger="Review Queue screen loads.",
    entry_conditions=("Shift or caregiver context is available.",),
    exit_conditions=("Review signals are aggregated.",),
    success_outcome="System has candidate queue items for triage.",
    complexity=WorkflowComplexity.L2,
    flow=(
        FlowStep(1, "System", "Loads patients in scope."),
        FlowStep(2, "System", "Aggregates ADL declines, missing ADLs, observations, alerts, and escalations."),
        FlowStep(3, "System", "Creates candidate queue items."),
    ),
    data_state=(DataState("review_signals", True),),
    related_use_case="UC-QUEUE-01",
    related_screens=("screen.review.queue",),
    related_backend_contracts=("ReviewQueueQueryDTO", "ReviewQueueResponseDTO"),
)

WF_QUEUE_02 = Workflow(
    workflow_id="WF-QUEUE-02",
    name="Rank by severity",
    primary_actor="System",
    goal="Prioritize queue items by urgency and clinical/operational importance.",
    trigger="Review signals are aggregated.",
    entry_conditions=("Candidate queue items exist.",),
    exit_conditions=("Queue items are ranked.",),
    success_outcome="Caregiver sees most important issues first.",
    complexity=WorkflowComplexity.L2,
    flow=(
        FlowStep(1, "System", "Evaluates severity, recency, signal type, and open escalation status."),
        FlowStep(2, "System", "Assigns priority level."),
        FlowStep(3, "System", "Sorts queue items."),
    ),
    system_behaviors=(SystemBehavior("Apply queue priority rules.", "ReviewQueueRankingService"),),
    data_state=(DataState("priority", True),),
    related_use_case="UC-QUEUE-01",
    related_screens=("screen.review.queue",),
    related_backend_contracts=("ReviewQueueItemDTO",),
)

WF_QUEUE_03 = Workflow(
    workflow_id="WF-QUEUE-03",
    name="Display queue items",
    primary_actor="System",
    goal="Render prioritized review queue.",
    trigger="Queue items are ranked.",
    entry_conditions=("Ranked queue data is available.",),
    exit_conditions=("Review Queue screen displays items.",),
    success_outcome="Caregiver can scan and select review items.",
    complexity=WorkflowComplexity.L1,
    flow=(
        FlowStep(1, "System", "Displays queue item cards."),
        FlowStep(2, "System", "Shows reason, priority, patient, status, and recommended action."),
    ),
    data_state=(DataState("queue_items", True),),
    related_use_case="UC-QUEUE-01",
    related_screens=("screen.review.queue",),
    related_backend_contracts=("ReviewQueueResponseDTO", "ReviewQueueItemDTO"),
)

WF_QUEUE_04 = Workflow(
    workflow_id="WF-QUEUE-04",
    name="Route to Review Queue Detail",
    primary_actor="Caregiver",
    goal="Open detailed context for a selected queue item.",
    trigger="User taps a queue item.",
    entry_conditions=("Queue item is visible.",),
    exit_conditions=("Review Queue Detail screen opens.",),
    success_outcome="Caregiver sees why the issue was flagged.",
    complexity=WorkflowComplexity.L1,
    flow=(
        FlowStep(1, "Caregiver", "Taps queue item."),
        FlowStep(2, "System", "Navigates to Review Queue Detail."),
    ),
    data_state=(DataState("queue_item_id", True),),
    related_use_case="UC-QUEUE-02",
    related_screens=("screen.review.queue", "screen.review.queue.detail"),
    related_backend_contracts=("ReviewQueueDetailQueryDTO", "ReviewQueueDetailResponseDTO"),
)

# ============================================================
# REVIEW QUEUE DETAIL
# ============================================================

WF_QUEUE_DET_01 = Workflow(
    workflow_id="WF-QUEUE-DET-01",
    name="Load issue context",
    primary_actor="System",
    goal="Load full context for a selected review item.",
    trigger="Review Queue Detail opens.",
    entry_conditions=("Queue item is selected.",),
    exit_conditions=("Issue context is loaded.",),
    success_outcome="Caregiver has enough context to understand the flagged issue.",
    complexity=WorkflowComplexity.L2,
    flow=(
        FlowStep(1, "System", "Loads queue item."),
        FlowStep(2, "System", "Loads related patient, ADLs, observations, alerts, and escalations."),
        FlowStep(3, "System", "Builds review queue detail DTO."),
    ),
    data_state=(DataState("queue_item_id", True),),
    related_use_case="UC-QUEUE-02",
    related_screens=("screen.review.queue.detail",),
    related_backend_contracts=("ReviewQueueDetailQueryDTO", "ReviewQueueDetailResponseDTO"),
)

WF_QUEUE_DET_02 = Workflow(
    workflow_id="WF-QUEUE-DET-02",
    name="Display supporting data",
    primary_actor="System",
    goal="Show ADL changes, observations, and alert context supporting the issue.",
    trigger="Issue context is loaded.",
    entry_conditions=("Supporting data is available or empty.",),
    exit_conditions=("Supporting data is displayed.",),
    success_outcome="Caregiver can validate why the issue was flagged.",
    complexity=WorkflowComplexity.L1,
    flow=(
        FlowStep(1, "System", "Displays reason summary."),
        FlowStep(2, "System", "Displays supporting ADL changes."),
        FlowStep(3, "System", "Displays related observations and escalation status."),
    ),
    data_state=(
        DataState("supporting_adl_changes", False),
        DataState("supporting_observations", False),
        DataState("related_escalations", False),
    ),
    related_use_case="UC-QUEUE-02",
    related_screens=("screen.review.queue.detail",),
    related_backend_contracts=("SupportingAdlChangeDTO", "ObservationSummaryDTO"),
)

WF_QUEUE_DET_03 = Workflow(
    workflow_id="WF-QUEUE-DET-03",
    name="Suggest actions",
    primary_actor="System",
    goal="Recommend next actions for the flagged issue.",
    trigger="Supporting issue context is displayed.",
    entry_conditions=("Issue type and severity are known.",),
    exit_conditions=("Recommended actions are displayed.",),
    success_outcome="Caregiver knows whether to review, reassess, escalate, or acknowledge.",
    complexity=WorkflowComplexity.L2,
    flow=(
        FlowStep(1, "System", "Evaluates issue type and severity."),
        FlowStep(2, "System", "Builds recommended action list."),
        FlowStep(3, "System", "Displays actions on detail screen."),
    ),
    related_use_case="UC-QUEUE-02",
    related_screens=("screen.review.queue.detail",),
)

WF_QUEUE_DET_04 = Workflow(
    workflow_id="WF-QUEUE-DET-04",
    name="Route from Review Queue Detail",
    primary_actor="Caregiver",
    goal="Navigate to the appropriate next action.",
    trigger="User taps Open Patient, Escalate, Enter ADL, or Acknowledge.",
    entry_conditions=("Review Queue Detail is visible.",),
    exit_conditions=("Target action is started or item status is updated.",),
    success_outcome="Caregiver acts on the flagged issue.",
    complexity=WorkflowComplexity.L1,
    flow=(
        FlowStep(1, "Caregiver", "Selects a recommended action."),
        FlowStep(2, "System", "Routes to Patient Summary, ADL Entry, Escalation, or status update."),
    ),
    data_state=(DataState("queue_item_id", True), DataState("patient_id", True)),
    related_use_case="UC-QUEUE-03",
    related_screens=(
        "screen.review.queue.detail",
        "screen.patient.summary",
        "screen.adl.entry",
        "screen.escalate",
    ),
    related_backend_contracts=("UpdateReviewQueueStatusRequestDTO", "UpdateReviewQueueStatusResponseDTO"),
)

# ============================================================
# ADL ENTRY
# ============================================================

WF_ADL_01 = Workflow(
    workflow_id="WF-ADL-01",
    name="Pre-fill ADL and patient",
    primary_actor="System",
    goal="Initialize ADL Entry with known patient and ADL context.",
    trigger="User opens ADL Entry from Patient Summary or ADL detail.",
    entry_conditions=("Patient context is available.",),
    exit_conditions=("ADL Entry form is initialized.",),
    success_outcome="Caregiver starts entry without reselecting known context.",
    complexity=WorkflowComplexity.L1,
    flow=(
        FlowStep(1, "System", "Loads ADL entry context."),
        FlowStep(2, "System", "Pre-fills patient, ADL type, previous score, and baseline."),
    ),
    related_use_case="UC-ADL-01",
    related_screens=("screen.adl.entry",),
    related_backend_contracts=("AdlEntryContextResponseDTO",),
)

WF_ADL_02 = Workflow(
    workflow_id="WF-ADL-02",
    name="Select score",
    primary_actor="Caregiver",
    goal="Select current ADL performance level.",
    trigger="ADL Entry form is active.",
    entry_conditions=("ADL score options are loaded.",),
    exit_conditions=("Score is selected.",),
    success_outcome="Caregiver has captured structured ADL score.",
    complexity=WorkflowComplexity.L1,
    flow=(
        FlowStep(1, "Caregiver", "Reviews score options."),
        FlowStep(2, "Caregiver", "Selects score."),
        FlowStep(3, "System", "Stores score in form state."),
    ),
    related_use_case="UC-ADL-01",
    related_screens=("screen.adl.entry",),
)

WF_ADL_03 = Workflow(
    workflow_id="WF-ADL-03",
    name="Compare to previous and baseline",
    primary_actor="System",
    goal="Interpret selected score against recent and baseline status.",
    trigger="Score is selected.",
    entry_conditions=("Selected score is available.",),
    exit_conditions=("Comparison result is available.",),
    success_outcome="Caregiver sees whether selected score represents change.",
    complexity=WorkflowComplexity.L2,
    flow=(
        FlowStep(1, "System", "Compares selected score to previous score."),
        FlowStep(2, "System", "Compares selected score to baseline score."),
        FlowStep(3, "System", "Displays comparison result."),
    ),
    related_use_case="UC-ADL-01",
    related_screens=("screen.adl.entry",),
)

WF_ADL_04 = Workflow(
    workflow_id="WF-ADL-04",
    name="Require note if needed",
    primary_actor="System",
    goal="Require explanatory note when policy or score change requires context.",
    trigger="Score comparison or special score condition is detected.",
    entry_conditions=("Selected score is available.",),
    exit_conditions=("Note requirement is resolved.",),
    success_outcome="Clinically meaningful changes have sufficient context.",
    complexity=WorkflowComplexity.L2,
    flow=(
        FlowStep(1, "System", "Evaluates note requirement rules."),
        FlowStep(2, "System", "Marks note as required or optional."),
        FlowStep(3, "Caregiver", "Adds note when required."),
    ),
    edge_cases=(
        EdgeCase("Required note is missing.", "Block save and show note requirement message."),
    ),
    related_use_case="UC-ADL-01",
    related_screens=("screen.adl.entry",),
)

WF_ADL_05 = Workflow(
    workflow_id="WF-ADL-05",
    name="Confirm timestamp",
    primary_actor="Caregiver",
    goal="Confirm when the ADL observation occurred.",
    trigger="Before saving ADL assessment.",
    entry_conditions=("Score is selected.",),
    exit_conditions=("Observed time is confirmed.",),
    success_outcome="ADL assessment has accurate observation time.",
    complexity=WorkflowComplexity.L1,
    flow=(
        FlowStep(1, "System", "Displays default observed time."),
        FlowStep(2, "Caregiver", "Confirms or adjusts observed time."),
        FlowStep(3, "System", "Validates timestamp."),
    ),
    edge_cases=(
        EdgeCase("Observed time is in the future.", "Block save and show validation message."),
    ),
    data_state=(DataState("observed_at", True),),
    related_use_case="UC-ADL-01",
    related_screens=("screen.adl.entry",),
)

WF_ADL_06 = Workflow(
    workflow_id="WF-ADL-06",
    name="Save assessment",
    primary_actor="Caregiver",
    goal="Save completed ADL assessment.",
    trigger="User taps Save.",
    entry_conditions=("Required fields are complete.",),
    exit_conditions=("Assessment is stored.",),
    success_outcome="Timestamped ADL assessment is reflected in the patient record.",
    complexity=WorkflowComplexity.L3,
    flow=(
        FlowStep(1, "Caregiver", "Taps Save."),
        FlowStep(2, "System", "Validates form."),
        FlowStep(3, "System", "Submits ADL assessment request."),
        FlowStep(4, "System", "Stores assessment and audit metadata."),
        FlowStep(5, "System", "Shows save confirmation."),
    ),
    edge_cases=(
        EdgeCase("Save fails.", "Preserve form state and show retry option."),
        EdgeCase("Duplicate save attempt.", "Use idempotency key or disable save button."),
    ),
    audit_rules=(AuditRule("adl_assessment_saved", compliance_relevant=True),),
    related_use_case="UC-ADL-01",
    related_screens=("screen.adl.entry",),
    related_backend_contracts=("SubmitAdlAssessmentRequestDTO", "SubmitAdlAssessmentResponseDTO"),
)

WF_ADL_07 = Workflow(
    workflow_id="WF-ADL-07",
    name="Return to Patient Summary",
    primary_actor="System",
    goal="Return caregiver to patient context after save or cancel.",
    trigger="ADL assessment is saved or user exits entry.",
    entry_conditions=("Patient context is available.",),
    exit_conditions=("Patient Summary is displayed.",),
    success_outcome="Caregiver returns to updated patient context.",
    complexity=WorkflowComplexity.L1,
    flow=(
        FlowStep(1, "System", "Navigates back to Patient Summary."),
        FlowStep(2, "System", "Refreshes patient snapshot data if assessment was saved."),
    ),
    related_use_case="UC-PAT-01",
    related_screens=("screen.adl.entry", "screen.patient.summary"),
)

# ============================================================
# OBSERVATION ENTRY
# ============================================================

WF_OBS_01 = Workflow(
    workflow_id="WF-OBS-01",
    name="Select category",
    primary_actor="Caregiver",
    goal="Choose the observation category.",
    trigger="Observation Entry screen opens.",
    entry_conditions=("Patient context is available.",),
    exit_conditions=("Observation category is selected.",),
    success_outcome="Observation note can be categorized.",
    complexity=WorkflowComplexity.L1,
    flow=(
        FlowStep(1, "System", "Loads observation categories."),
        FlowStep(2, "Caregiver", "Selects category."),
    ),
    related_use_case="UC-OBS-01",
    related_screens=("screen.observation.entry",),
    related_backend_contracts=("ObservationEntryContextResponseDTO",),
)

WF_OBS_02 = Workflow(
    workflow_id="WF-OBS-02",
    name="Enter note",
    primary_actor="Caregiver",
    goal="Capture narrative observation.",
    trigger="Category is selected.",
    entry_conditions=("Observation category is selected.",),
    exit_conditions=("Observation note is entered.",),
    success_outcome="Narrative context is captured.",
    complexity=WorkflowComplexity.L1,
    flow=(
        FlowStep(1, "Caregiver", "Types observation note."),
        FlowStep(2, "System", "Stores note in form state."),
    ),
    related_use_case="UC-OBS-01",
    related_screens=("screen.observation.entry",),
)

WF_OBS_03 = Workflow(
    workflow_id="WF-OBS-03",
    name="Confirm timestamp",
    primary_actor="Caregiver",
    goal="Confirm when observation occurred.",
    trigger="Before saving observation.",
    entry_conditions=("Observation note is entered.",),
    exit_conditions=("Observed time is confirmed.",),
    success_outcome="Observation has accurate observed time.",
    complexity=WorkflowComplexity.L1,
    flow=(
        FlowStep(1, "System", "Displays default observed time."),
        FlowStep(2, "Caregiver", "Confirms or adjusts observed time."),
        FlowStep(3, "System", "Validates timestamp."),
    ),
    related_use_case="UC-OBS-01",
    related_screens=("screen.observation.entry",),
)

WF_OBS_04 = Workflow(
    workflow_id="WF-OBS-04",
    name="Save observation",
    primary_actor="Caregiver",
    goal="Save narrative observation.",
    trigger="User taps Save.",
    entry_conditions=("Required observation fields are complete.",),
    exit_conditions=("Observation is stored.",),
    success_outcome="Timestamped observation appears in patient timeline.",
    complexity=WorkflowComplexity.L3,
    flow=(
        FlowStep(1, "Caregiver", "Taps Save."),
        FlowStep(2, "System", "Validates observation."),
        FlowStep(3, "System", "Submits observation request."),
        FlowStep(4, "System", "Stores observation and audit metadata."),
    ),
    audit_rules=(AuditRule("observation_saved", compliance_relevant=True),),
    related_use_case="UC-OBS-01",
    related_screens=("screen.observation.entry",),
    related_backend_contracts=("SubmitObservationRequestDTO", "SubmitObservationResponseDTO"),
)

WF_OBS_05 = Workflow(
    workflow_id="WF-OBS-05",
    name="Return to Patient Summary",
    primary_actor="System",
    goal="Return caregiver to patient context after observation entry.",
    trigger="Observation is saved or user exits entry.",
    entry_conditions=("Patient context is available.",),
    exit_conditions=("Patient Summary is displayed.",),
    success_outcome="Caregiver returns to updated patient context.",
    complexity=WorkflowComplexity.L1,
    flow=(
        FlowStep(1, "System", "Navigates back to Patient Summary."),
        FlowStep(2, "System", "Refreshes recent observations if saved."),
    ),
    related_use_case="UC-PAT-03",
    related_screens=("screen.observation.entry", "screen.patient.summary"),
)

# ============================================================
# ESCALATE
# ============================================================

WF_ESC_01 = Workflow(
    workflow_id="WF-ESC-01",
    name="Load escalation context",
    primary_actor="System",
    goal="Load ADL, observation, alert, and queue context for escalation.",
    trigger="User opens Escalation screen.",
    entry_conditions=("Patient context is available.",),
    exit_conditions=("Escalation context is loaded.",),
    success_outcome="Caregiver sees pre-filled escalation context.",
    complexity=WorkflowComplexity.L2,
    flow=(
        FlowStep(1, "System", "Loads patient and source context."),
        FlowStep(2, "System", "Loads supporting ADLs, observations, alerts, and queue item references."),
        FlowStep(3, "System", "Builds escalation context DTO."),
    ),
    related_use_case="UC-ESC-01",
    related_screens=("screen.escalate",),
    related_backend_contracts=("EscalationContextResponseDTO",),
)

WF_ESC_02 = Workflow(
    workflow_id="WF-ESC-02",
    name="Generate escalation summary",
    primary_actor="System",
    goal="Create concise summary of escalation reason and supporting evidence.",
    trigger="Escalation context is loaded.",
    entry_conditions=("Supporting evidence is available.",),
    exit_conditions=("Auto-summary is generated.",),
    success_outcome="Caregiver does not need to manually reconstruct the concern.",
    complexity=WorkflowComplexity.L2,
    flow=(
        FlowStep(1, "System", "Evaluates source issue and supporting evidence."),
        FlowStep(2, "System", "Generates escalation summary."),
    ),
    related_use_case="UC-ESC-01",
    related_screens=("screen.escalate",),
)

WF_ESC_03 = Workflow(
    workflow_id="WF-ESC-03",
    name="Capture caregiver input",
    primary_actor="Caregiver",
    goal="Add context, reason, classification, and priority.",
    trigger="Escalation form is displayed.",
    entry_conditions=("Escalation context is loaded.",),
    exit_conditions=("Required escalation fields are complete.",),
    success_outcome="Escalation contains caregiver-provided context.",
    complexity=WorkflowComplexity.L2,
    flow=(
        FlowStep(1, "Caregiver", "Reviews auto-summary."),
        FlowStep(2, "Caregiver", "Selects or confirms reason."),
        FlowStep(3, "Caregiver", "Adds optional note and priority/classification."),
    ),
    related_use_case="UC-ESC-01",
    related_screens=("screen.escalate",),
)

WF_ESC_04 = Workflow(
    workflow_id="WF-ESC-04",
    name="Assign recipients",
    primary_actor="Caregiver",
    goal="Assign escalation to role, person, or team.",
    trigger="Caregiver reaches assignment section.",
    entry_conditions=("Assignable recipients are loaded.",),
    exit_conditions=("Recipient assignment is selected.",),
    success_outcome="Escalation has an accountable follow-up owner.",
    complexity=WorkflowComplexity.L2,
    flow=(
        FlowStep(1, "System", "Displays assignable roles and users."),
        FlowStep(2, "Caregiver", "Selects recipient or role."),
    ),
    related_use_case="UC-ESC-01",
    related_screens=("screen.escalate",),
    related_backend_contracts=("AssignableRecipientDTO",),
)

WF_ESC_05 = Workflow(
    workflow_id="WF-ESC-05",
    name="Submit escalation",
    primary_actor="Caregiver",
    goal="Create structured escalation record.",
    trigger="User taps Submit Escalation.",
    entry_conditions=("Required escalation fields are complete.",),
    exit_conditions=("Escalation record is created.",),
    success_outcome="Escalation is assigned and linked to patient record.",
    complexity=WorkflowComplexity.L3,
    flow=(
        FlowStep(1, "Caregiver", "Taps Submit Escalation."),
        FlowStep(2, "System", "Validates escalation payload."),
        FlowStep(3, "System", "Stores escalation record."),
        FlowStep(4, "System", "Sends notification if selected."),
    ),
    audit_rules=(AuditRule("escalation_created", compliance_relevant=True),),
    related_use_case="UC-ESC-01",
    related_screens=("screen.escalate",),
    related_backend_contracts=("SubmitEscalationRequestDTO", "SubmitEscalationResponseDTO"),
)

WF_ESC_06 = Workflow(
    workflow_id="WF-ESC-06",
    name="Update system state after escalation",
    primary_actor="System",
    goal="Update related alert, queue, and patient state.",
    trigger="Escalation is successfully created.",
    entry_conditions=("Escalation record exists.",),
    exit_conditions=("Related system records are updated.",),
    success_outcome="Escalation is visible in review queue and patient snapshot.",
    complexity=WorkflowComplexity.L2,
    flow=(
        FlowStep(1, "System", "Links escalation to source records."),
        FlowStep(2, "System", "Updates related alert or queue item status."),
        FlowStep(3, "System", "Refreshes patient context."),
    ),
    related_use_case="UC-ESC-01",
    related_screens=("screen.escalate", "screen.patient.summary", "screen.review.queue"),
)

WF_ESC_07 = Workflow(
    workflow_id="WF-ESC-07",
    name="Return to Patient Summary",
    primary_actor="System",
    goal="Return caregiver to patient context after escalation.",
    trigger="Escalation submission completes.",
    entry_conditions=("Patient context is available.",),
    exit_conditions=("Patient Summary is displayed.",),
    success_outcome="Caregiver sees updated escalation state on Patient Summary.",
    complexity=WorkflowComplexity.L1,
    flow=(
        FlowStep(1, "System", "Navigates back to Patient Summary."),
        FlowStep(2, "System", "Refreshes open escalations and alerts."),
    ),
    related_use_case="UC-PAT-01",
    related_screens=("screen.escalate", "screen.patient.summary"),
)

# ============================================================
# HISTORY
# ============================================================

WF_HIST_01 = Workflow(
    workflow_id="WF-HIST-01",
    name="Load historical data",
    primary_actor="System",
    goal="Load ADLs, observations, escalations, and corrections for selected patient and range.",
    trigger="User opens History screen.",
    entry_conditions=("Patient context is available.",),
    exit_conditions=("Historical data is loaded.",),
    success_outcome="User can review patient history.",
    complexity=WorkflowComplexity.L2,
    flow=(
        FlowStep(1, "System", "Loads history query parameters."),
        FlowStep(2, "System", "Fetches timeline items for selected patient and range."),
        FlowStep(3, "System", "Builds patient history response."),
    ),
    related_use_case="UC-HIST-01",
    related_screens=("screen.history",),
    related_backend_contracts=("PatientHistoryQueryDTO", "PatientHistoryResponseDTO"),
)

WF_HIST_02 = Workflow(
    workflow_id="WF-HIST-02",
    name="Compute trends",
    primary_actor="System",
    goal="Compute ADL trends from historical ADL assessments.",
    trigger="Historical ADL data is loaded.",
    entry_conditions=("ADL history exists.",),
    exit_conditions=("Trend summaries are computed.",),
    success_outcome="User can identify direction of functional change.",
    complexity=WorkflowComplexity.L2,
    flow=(
        FlowStep(1, "System", "Groups ADL entries by ADL type."),
        FlowStep(2, "System", "Computes trend direction and recent points."),
        FlowStep(3, "System", "Builds ADL trend summaries."),
    ),
    related_use_case="UC-HIST-02",
    related_screens=("screen.history",),
    related_backend_contracts=("AdlTrendsQueryDTO", "AdlTrendsResponseDTO"),
)

WF_HIST_03 = Workflow(
    workflow_id="WF-HIST-03",
    name="Generate summary insights",
    primary_actor="System",
    goal="Summarize meaningful historical changes.",
    trigger="Trends and timeline data are available.",
    entry_conditions=("Historical data is loaded.",),
    exit_conditions=("Summary insights are generated.",),
    success_outcome="User sees key changes without reading every entry.",
    complexity=WorkflowComplexity.L2,
    flow=(
        FlowStep(1, "System", "Evaluates trends and significant timeline events."),
        FlowStep(2, "System", "Generates concise insight bullets."),
    ),
    related_use_case="UC-HIST-02",
    related_screens=("screen.history",),
)

WF_HIST_04 = Workflow(
    workflow_id="WF-HIST-04",
    name="Display timeline",
    primary_actor="System",
    goal="Render chronological patient history.",
    trigger="Patient history response is available.",
    entry_conditions=("Timeline items are available or empty.",),
    exit_conditions=("Timeline is displayed.",),
    success_outcome="User reviews patient activity in chronological context.",
    complexity=WorkflowComplexity.L1,
    flow=(
        FlowStep(1, "System", "Sorts timeline items by observed time."),
        FlowStep(2, "System", "Displays timeline items with type, title, and body."),
    ),
    related_use_case="UC-HIST-01",
    related_screens=("screen.history",),
    related_backend_contracts=("TimelineItemDTO",),
)

WF_HIST_05 = Workflow(
    workflow_id="WF-HIST-05",
    name="Route to Detailed Trends",
    primary_actor="Caregiver",
    goal="Open detailed ADL trend view.",
    trigger="User taps View Detailed Trends or an ADL trend row.",
    entry_conditions=("Trend summary is visible.",),
    exit_conditions=("Detailed Trends screen opens.",),
    success_outcome="User can examine ADL trend details.",
    complexity=WorkflowComplexity.L1,
    flow=(
        FlowStep(1, "Caregiver", "Taps detailed trend action."),
        FlowStep(2, "System", "Navigates to Detailed Trends screen."),
    ),
    related_use_case="UC-HIST-02",
    related_screens=("screen.history", "screen.detailed.trends"),
    related_backend_contracts=("AdlTrendsQueryDTO", "AdlTrendsResponseDTO"),
)

WF_CORR_01 = Workflow(
    workflow_id="WF-CORR-01",
    name="Load existing entry",
    primary_actor="Caregiver",
    goal="Load the original ADL or observation entry for correction.",
    trigger="User selects 'Edit' or 'Correct' on an existing entry.",
    entry_conditions=(
        "Entry exists.",
        "User has permission to correct the entry.",
    ),
    exit_conditions=("Original entry data is loaded into correction form.",),
    success_outcome=(
        "User sees the existing entry values pre-filled for correction."
    ),
    complexity=WorkflowComplexity.L1,
    flow=(
        FlowStep(1, "Caregiver", "Selects entry to correct."),
        FlowStep(2, "System", "Retrieves original entry data."),
        FlowStep(3, "System", "Loads data into correction form."),
    ),
    system_behaviors=(
        SystemBehavior("Fetch original entry by ID.", "EntryRepository"),
        SystemBehavior("Load entry into editable form state.", "CorrectionService"),
    ),
    data_state=(
        DataState("target_entry_id", True),
        DataState("original_entry_data", True),
    ),
    related_use_case="UC-CORR-01",
    related_screens=("screen.adl.entry", "screen.observation.entry"),
    related_backend_contracts=("CorrectEntryRequestDTO",),
)

WF_CORR_02 = Workflow(
    workflow_id="WF-CORR-02",
    name="Edit corrected values",
    primary_actor="Caregiver",
    goal="Modify incorrect values while preserving context.",
    trigger="Correction form is displayed.",
    entry_conditions=("Original entry data is loaded.",),
    exit_conditions=("Corrected values are captured.",),
    success_outcome=(
        "User updates incorrect values and provides correction context if required."
    ),
    complexity=WorkflowComplexity.L2,
    flow=(
        FlowStep(1, "Caregiver", "Modifies score, note, or timestamp."),
        FlowStep(2, "System", "Tracks changes relative to original values."),
        FlowStep(3, "System", "Prompts for correction reason if required."),
        FlowStep(4, "Caregiver", "Enters correction reason (if required)."),
    ),
    system_behaviors=(
        SystemBehavior("Compare original vs updated values.", "CorrectionService"),
        SystemBehavior("Enforce correction reason rules.", "ValidationService"),
    ),
    edge_cases=(
        EdgeCase(
            "No changes made.",
            "Disable save or show message indicating no correction needed.",
        ),
    ),
    data_state=(
        DataState("original_entry_data", True),
        DataState("corrected_values", True),
        DataState("correction_reason", False),
    ),
    related_use_case="UC-CORR-01",
    related_screens=("screen.adl.entry", "screen.observation.entry"),
)

WF_CORR_03 = Workflow(
    workflow_id="WF-CORR-03",
    name="Save correction with audit trail",
    primary_actor="Caregiver",
    goal="Persist corrected entry while preserving original record.",
    trigger="User submits correction.",
    entry_conditions=(
        "Corrected values are valid.",
        "Correction reason is provided if required.",
    ),
    exit_conditions=("Correction is saved with audit history.",),
    success_outcome=(
        "User sees corrected entry reflected in the record, with original data preserved for audit."
    ),
    complexity=WorkflowComplexity.L3,
    flow=(
        FlowStep(1, "Caregiver", "Submits correction."),
        FlowStep(2, "System", "Validates correction payload."),
        FlowStep(3, "System", "Creates new corrected record version."),
        FlowStep(4, "System", "Links corrected record to original."),
        FlowStep(5, "System", "Stores audit event."),
        FlowStep(6, "System", "Updates downstream state (history, trends, queue)."),
    ),
    system_behaviors=(
        SystemBehavior("Create new version of entry (no overwrite).", "CorrectionService"),
        SystemBehavior("Persist audit event.", "AuditService"),
        SystemBehavior("Recompute trends and signals if needed.", "AnalyticsService"),
    ),
    edge_cases=(
        EdgeCase(
            "Correction conflicts with newer data.",
            "Warn user or require confirmation before saving.",
        ),
        EdgeCase(
            "Save fails.",
            "Preserve form state and allow retry.",
        ),
    ),
    audit_rules=(
        AuditRule("entry_corrected", compliance_relevant=True),
    ),
    data_state=(
        DataState("corrected_record", True),
        DataState("original_record", True),
        DataState("audit_event", True),
    ),
    related_use_case="UC-CORR-01",
    related_screens=("screen.adl.entry", "screen.observation.entry"),
    related_backend_contracts=(
        "CorrectEntryRequestDTO",
        "CorrectEntryResponseDTO",
    ),
)


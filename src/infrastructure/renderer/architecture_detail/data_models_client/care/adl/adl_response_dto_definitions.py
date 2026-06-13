# /src/infrastructure/architecture_detail/data_models_analytics/data_models_client/care/adl/adl_response_dto_definitions.py

"""
Supporting or Nested DTOs
- PatientHomeCardDTO           → view model
- AdlCompletionStatusDTO       → derived aggregate
- ReviewSignalDTO              → rule output
- AdlStatusCardDTO
- ObservationSummaryDTO
- TimelineItemDTO
- AdlTrendPointDTO

Context (Screen Initialization) DTOs
- AdlEntryContextResponseDTO
- ObservationEntryContextResponseDTO
- EscalationContextResponseDTO

"""

ADL_COMPLETION_STATUS_DTO: str = """
@dataclass(frozen=True)
class AdlCompletionStatusDTO:
    required_count: int
    completed_count: int
    missing_adls: tuple[str, ...] = ()
    unable_to_assess_adls: tuple[str, ...] = ()
"""

REVIEW_SIGNAL_DTO: str = """
@dataclass(frozen=True)
class ReviewSignalDTO:
    signal_type: str
    severity: PriorityLevel
    title: str
    summary: str
    related_adl_category: str | None = None

"""

PATIENT_HOME_CARD_DTO: str = """
@dataclass(frozen=True)
class PatientHomeCardDTO:
    patient_id: str
    display_name: str
    location_label: str | None = None

    priority_level: PriorityLevel
    status_label: str
    status_reason: str

    last_adl_update_at_iso: str | None
    adl_completion: AdlCompletionStatusDTO

    review_signals: tuple[ReviewSignalDTO, ...] = ()
"""

ADL_HOME_RESPONSE_DTO: str = """
@dataclass(frozen=True)
class AdlHomeResponseDTO:
    caregiver_id: str
    shift_id: str
    generated_at_iso: str

    assigned_patient_count: int
    needs_attention_count: int

    priority_patients: tuple[PatientHomeCardDTO, ...] = ()
    routine_patients: tuple[PatientHomeCardDTO, ...] = ()
"""

REVIEW_QUEUE_SUMMARY_DTO: str = """
@dataclass(frozen=True)
class ReviewQueueSummaryDTO:
    shift_id: str
    total_items: int
    high_priority_count: int
    medium_priority_count: int
    low_priority_count: int

"""

ADL_STATUS_CARD_DTO: str = """
@dataclass(frozen=True)
class AdlStatusCardDTO:
    adl_category: str
    display_label: str

    current_score_label: str | None
    previous_score_label: str | None
    baseline_score_label: str | None

    trend_direction: TrendDirection
    change_status: ChangeStatus

    last_observed_at_iso: str | None

"""

OBSERVATION_SUMMARY_DTO: str = """
@dataclass(frozen=True)
class ObservationSummaryDTO:
    observation_id: str
    category: str
    note_preview: str
    observed_at_iso: str

"""

ESCALATION_SUMMARY_DTO: str = """
@dataclass(frozen=True)
class EscalationSummaryDTO:
    escalation_id: str
    priority: PriorityLevel
    reason_label: str
    status: str
    created_at_iso: str
"""

PATIENT_SHIFT_SNAPSHOT_RESPONSE_DTO: str = """
@dataclass(frozen=True)
class PatientShiftSnapshotResponseDTO:
    patient_id: str
    display_name: str
    shift_id: str

    generated_at_iso: str
    shift_summary: str

    adl_cards: tuple[AdlStatusCardDTO, ...] = ()
    recent_observations: tuple[ObservationSummaryDTO, ...] = ()
    open_escalations: tuple[EscalationSummaryDTO, ...] = ()
"""

OBSERVATION_HISTORY_ITEM_DTO: str = """
@dataclass(frozen=True)
class ObservationHistoryItemDTO:
    observation_id: str
    category: str
    note: str
    observed_at_iso: str
"""

OBSERVATION_HISTORY_RESPONSE_DTO: str = """
@dataclass(frozen=True)
class ObservationHistoryResponseDTO:
    patient_id: str
    range: str
    items: tuple[ObservationHistoryItemDTO, ...] = ()
"""

SUBMIT_ADL_ASSESSMENT_RESPONSE_DTO: str = """
@dataclass(frozen=True)
class SubmitAdlAssessmentResponseDTO:
    assessment_id: str
    patient_id: str
    adl_category: str
    score_label: str
    observed_at_iso: str
    recorded_at_iso: str
    recorded_by: str
    comparison_to_previous: str
    comparison_to_baseline: str
    alert_created: bool
    escalation_recommended: bool
"""

SUBMIT_OBSERVATION_RESPONSE_DTO: str = """
@dataclass(frozen=True)
class SubmitObservationResponseDTO:
    observation_id: str
    patient_id: str
    category: str
    note_preview: str
    observed_at_iso: str
    recorded_at_iso: str
    recorded_by: str
    alert_created: bool
    escalation_recommended: bool
"""

CORRECT_ENTRY_RESPONSE_DTO: str = """
@dataclass(frozen=True)
class CorrectEntryResponseDTO:
    target_id: str
    corrected_record_id: str

    corrected_at_iso: str
    corrected_by: str

    audit_preserved: bool
"""

REVIEW_QUEUE_ITEM_DTO: str = """
@dataclass(frozen=True)
class ReviewQueueItemDTO:
    queue_item_id: str
    patient_id: str
    patient_name: str
    location_label: str | None
    priority: PriorityLevel
    reason_title: str
    reason_summary: str
    status: QueueStatus
    last_updated_at_iso: str | None
    recommended_actions: list[RecommendedActionDTO]

"""

REVIEW_QUEUE_RESPONSE_DTO: str = """
@dataclass(frozen=True)
class ReviewQueueResponseDTO:
    shift_id: str
    generated_at_iso: str

    total_count: int
    high_count: int
    medium_count: int
    low_count: int

    items: tuple[ReviewQueueItemDTO, ...] = ()
"""

REVIEW_QUEUE_DETAIL_RESPONSE_DTO: str = """
@dataclass(frozen=True)
class ReviewQueueDetailResponseDTO:
    queue_item_id: str
    patient_id: str
    reason_title: str
    reason_summary: str
    clinical_interpretation: tuple[str, ...] = ()
    supporting_adl_changes: tuple[SupportingAdlChangeDTO, ...] = ()
    supporting_observations: tuple[ObservationSummaryDTO, ...] = ()
    recommended_actions: list[RecommendedActionDTO]
    status: QueueStatus
"""

SUPPORTING_ADL_CHANGE_DTO: str = """
@dataclass(frozen=True)
class SupportingAdlChangeDTO:
    adl_category: str
    display_label: str
    previous_score_label: str | None
    current_score_label: str | None
    baseline_score_label: str | None
    change_status: ChangeStatus
    observed_at_iso: str
"""

UPDATE_REVIEW_QUEUE_STATUS_RESPONSE_DTO: str = """
@dataclass(frozen=True)
class UpdateReviewQueueStatusResponseDTO:
    queue_item_id: str
    status: QueueStatus
    updated_at_iso: str
"""

SUBMIT_ESCALATION_RESPONSE_DTO: str = """
@dataclass(frozen=True)
class SubmitEscalationResponseDTO:
    escalation_id: str
    patient_id: str
    priority: PriorityLevel
    status: str
    created_at_iso: str
    assigned_to_labels: tuple[str, ...] = ()
    notification_sent: bool = True

"""

TIMELINE_ITEM_DTO: str = """
@dataclass(frozen=True)
class TimelineItemDTO:
    item_id: str
    item_type: str
    observed_at_iso: str
    title: str
    subtitle: str | None
    body: str | None = None
    recorded_by_name: str
"""

PATIENT_HISTORY_RESPONSE_DTO: str = """
@dataclass(frozen=True)
class PatientHistoryResponseDTO:
    patient_id: str
    patient_name: str
    range_label: str    
    generated_at_iso: str
    trend_summary: list["AdlTrendSummaryDTO"]
    key_changes_summary: list[str]
    timeline_items: list["TimelineItemDTO"]
"""

ADL_TREND_POINT_DTO: str = """
@dataclass(frozen=True)
class AdlTrendPointDTO:
    observed_at_iso: str
    score_label: str
"""

ADL_TREND_SERIES_DTO: str = """
@dataclass(frozen=True)
class AdlTrendSeriesDTO:
    adl_category: str
    points: tuple[AdlTrendPointDTO, ...]
    trend_direction: TrendDirection
"""

ADL_TRENDS_RESPONSE_DTO: str = """
@dataclass(frozen=True)
class AdlTrendsResponseDTO:
    patient_id: str
    range: str
    series: tuple[AdlTrendSeriesDTO, ...] = ()
"""

ADL_ENTRY_CONTEXT_RESPONSE_DTO: str = """
@dataclass(frozen=True)
class AdlEntryContextResponseDTO:
    patient_id: str
    patient_name: str
    location_label: str | None
    adl_category: str
    adl_label: str
    last_score: int | None
    last_score_label: str | None
    last_observed_at_iso: str | None
    baseline_score: int | None
    baseline_score_label: str | None
    trend_direction: str
    score_options: list["AdlScoreOptionDTO"]
    note_requirement_rules: list[str]
"""

"""
ULES EGINER???????????????
"""

RECOMMENDED_ACTION_DTO: str = """
@dataclass(frozen=True)
class RecommendedActionDTO:
    action_type: str
    label: str
    target_screen: str
    required: bool
"""

ALERT_SUMMARY_DTO: str = """
@dataclass(frozen=True)
class AlertSummaryDTO:
    alert_id: str
    severity: PriorityLevel
    title: str
    summary: str
    status: str
"""

OBSERVATION_ENTRY_CONTEXT_RESPONSE_DTO: str = """
@dataclass(frozen=True)
class ObservationEntryContextResponseDTO:
    patient_id: str
    patient_name: str
    location_label: str | None

    categories: list["ObservationCategoryDTO"]
    suggested_category: str | None
    related_adl_category: str | None
"""

ESCALATION_CONTEXT_RESPONSE_DTO: str = """
@dataclass(frozen=True)
class EscalationContextResponseDTO:
    patient_id: str
    patient_name: str
    location_label: str | None

    default_reason_code: str | None
    default_reason_label: str | None

    auto_summary: str
    supporting_adl_changes: list[SupportingAdlChangeDTO]
    supporting_observations: list[ObservationSummaryDTO]
    related_alerts: list[AlertSummaryDTO]

    assignable_roles: list["AssignableRecipientDTO"]
    assignable_users: list["AssignableRecipientDTO"]

    priority_options: list[str]
    classification_options: list[str]
    follow_up_options: list[str]
"""

ASSIGNABLE_RECIPIENT_DTO: str = """
@dataclass(frozen=True)
class AssignableRecipientDTO:
    recipient_id: str
    display_label: str
    recipient_type: str  # role, user, team
"""

ADL_SCORE_OPTION_DTO: str = """
@dataclass(frozen=True)
class AdlScoreOptionDTO:
    value: int | str
    label: str
    description: str | None
"""

ADL_TREND_SUMMARY_DTO: str = """
@dataclass(frozen=True)
class AdlTrendSummaryDTO:
    adl_type: str
    display_label: str

    current_score_label: str | None
    baseline_score_label: str | None

    trend_direction: str
    change_status: str

    recent_points: list["AdlTrendPointDTO"]
"""

ADL_DETAIL_RESPONSE_DTO: str = """
@dataclass(frozen=True)
class AdlDetailResponseDTO:
    patient_id: str
    patient_name: str
    adl_type: str
    adl_label: str

    current_score: int | str | None
    current_score_label: str | None

    previous_score: int | str | None
    previous_score_label: str | None

    baseline_score: int | str | None
    baseline_score_label: str | None

    change_status: str
    trend_direction: str

    interpretation: list[str]

    recent_entries: list["AdlEntrySummaryDTO"]
    related_observations: list[ObservationSummaryDTO]
    recommended_actions: list[RecommendedActionDTO]
"""

ADL_ENTRY_SUMMARY_DTO: str = """
@dataclass(frozen=True)
class AdlEntrySummaryDTO:
    assessment_id: str
    observed_at: datetime
    score: int | str
    score_label: str
    note: str | None
    recorded_by_name: str
"""

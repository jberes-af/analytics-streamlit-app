# /src/infrastructure/architecture_detail/data_models_analytics/data_models_client/care/adl/adl_request_dto_definitions.py



ADL_CORRECTION_REASON_ENUM: str = """
class AdlCorrectionReasonEnum(StrEnum):
    WRONG_PATIENT = "Wrong Resident"
    WRONG_SCORE = "Wrong Score"
    WRONG_ACTIVITY = "Wrong ADL"
    DUPLICATE_ENTRY = "Duplicate Entry"
    WRONG_TIMESTAMP = "Wrong Timestamp"
    LATE_DOCUMENTATION = "Late Documentation"
    OTHER = "Other"
"""


ADL_HOME_QUERY_DTO: str = """
@dataclass(frozen=True)
class AdlHomeQueryDTO:
    caregiver_id: str
    shift_id: str
    include_stable_patients: bool = True
"""

REVIEW_QUEUE_SUMMARY_QUERY_DTO: str = """
@dataclass(frozen=True)
class ReviewQueueSummaryQueryDTO:
    shift_id: str
    caregiver_id: str | None = None
    patient_ids: tuple[str, ...] = field(default_factory=tuple)
"""

PATIENT_SNAPSHOT_QUERY_DTO: str = """
@dataclass(frozen=True)
class PatientSnapshotQueryDTO:
    patient_id: str
    shift_id: str
    include_recent_observations: bool = True
    include_active_alerts: bool = True
    include_open_escalations: bool = True
"""

OBSERVATION_HISTORY_QUERY_DTO: str = """
@dataclass(frozen=True)
class ObservationHistoryQueryDTO:
    patient_id: str
    range: TimeRange = "24h"
    categories: tuple[str, ...] = field(default_factory=tuple)
    start_at: datetime | None = None
    end_at: datetime | None = None
"""

SUBMIT_ADL_ASSESSMENT_REQUEST_DTO: str = """
@dataclass
class SubmitAdlAssessmentRequestDTO:
    patient_id: str
    adl_category: str
    score_value: int
    notes: str | None
    observed_at_iso: str | None
    recorded_by: str
"""

SUBMIT_OBSERVATION_REQUEST_DTO: str = """
@dataclass(frozen=True)
class SubmitObservationRequestDTO:
    patient_id: str
    category: str
    display_name: str
    description: str
    note: str
    observed_at_iso: Optional[str]               
    is_correction: bool = False
    recorded_by: str                
"""

CORRECT_ENTRY_REQUEST_DTO: str = """
class CorrectAdlAssessmentRequestDTO:
    target_assessment_id: str
    correction_reason: CorrectionReason
    corrected_by_user_id: str
    corrected_score: int | None = None
    corrected_notes: str | None = None
    corrected_observed_at: datetime | None = None
    correction_note: str | None = None
"""

REVIEW_QUEUE_QUERY_DTO: str = """
@dataclass(frozen=True)
class ReviewQueueQueryDTO:
    shift_id: str
    caregiver_id: str | None = None
    filter: QueueFilter = "all"
    priority_levels: tuple[PriorityLevel, ...] = field(default_factory=tuple)
    include_resolved: bool = False
"""

REVIEW_QUEUE_DETAIL_QUERY_DTO: str = """
@dataclass(frozen=True)
class ReviewQueueDetailQueryDTO:
    queue_item_id: str
    include_supporting_adls: bool = True
    include_supporting_observations: bool = True
    include_related_escalations: bool = True
"""

UPDATE_REVIEW_QUEUE_STATUS_REQUEST_DTO: str = """
@dataclass(frozen=True)
class UpdateReviewQueueStatusRequestDTO:
    queue_item_id: str
    status: QueueStatus
    note: str | None = None
    updated_by_user_id: str = ""
"""

SUBMIT_ESCALATION_REQUEST_DTO: str = """
@dataclass(frozen=True)
class SubmitEscalationRequestDTO:
    patient_id: str

    reason_code: str
    reason_label: str
    caregiver_note: str | None = None

    priority: PriorityLevel = "medium"
    classifications: tuple[str, ...] = field(default_factory=tuple)

    assigned_to_role_ids: tuple[str, ...] = field(default_factory=tuple)
    assigned_to_user_ids: tuple[str, ...] = field(default_factory=tuple)

    expected_follow_up: str = ""

    send_notification: bool = True
    notification_channels: tuple[NotificationChannel, ...] = ("in_app",)

    requires_real_time_interaction: bool = False

    related_adl_entry_ids: tuple[str, ...] = field(default_factory=tuple)
    related_observation_ids: tuple[str, ...] = field(default_factory=tuple)
    related_alert_ids: tuple[str, ...] = field(default_factory=tuple)
    related_queue_item_id: str | None = None

    source_screen: SourceScreen | None = None
"""

PATIENT_HISTORY_QUERY_DTO: str = """
@dataclass(frozen=True)
class PatientHistoryQueryDTO:
    patient_id: str
    range: TimeRange = "7d"
    types: tuple[HistoryItemType, ...] = ("adl", "observation", "escalation", "correction")
    adl_types: tuple[str, ...] = field(default_factory=tuple)
    observation_categories: tuple[str, ...] = field(default_factory=tuple)
    start_at: datetime | None = None
    end_at: datetime | None = None
    limit: int = 100
"""

ADL_TRENDS_QUERY_DTO: str = """
@dataclass(frozen=True)
class AdlTrendsQueryDTO:
    patient_id: str
    range: TimeRange = "7d"
    adl_types: tuple[str, ...] = field(default_factory=tuple)
    start_at: datetime | None = None
    end_at: datetime | None = None
    include_observation_markers: bool = True
    include_escalation_markers: bool = True
"""

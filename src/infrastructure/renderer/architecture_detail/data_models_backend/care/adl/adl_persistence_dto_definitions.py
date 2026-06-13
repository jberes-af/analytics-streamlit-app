# /src/infrastructure/renderer/architecture_detail/data_models_analytics/data_models_backend/adl_persistence_dto_definitions.py

ADL_ASSESSMENT_RECORD_DTO: str = """
@dataclass(frozen=True)
class AdlAssessmentRecordDTO:
    assessment_id: str
    patient_id: str
    adl_category: str
    score_value: int | str
    observed_at_iso: str
    recorded_at_iso: str
    recorded_by_user_id: str
    note: str | None = None
    is_correction: bool = False
    corrected_from_id: str | None = None
"""

OBSERVATION_RECORD_DTO: str = """
@dataclass(frozen=True)
class ObservationRecordDTO:
    observation_id: str
    patient_id: str
    category: str
    note: str
    observed_at_iso: str
    entered_at_iso: str
    recorded_by_user_id: str
"""

REVIEW_QUEUE_ITEM_RECORD_DTO: str = """
@dataclass(frozen=True)
class ReviewQueueItemRecordDTO:
    queue_item_id: str
    patient_id: str
    reason_code: str
    priority: str
    status: str
    created_at_iso: str
    updated_at_iso: str
    assigned_to_user_id: str | None = None
"""

ESCALATION_RECORD_DTO: str = """
@dataclass(frozen=True)
class EscalationRecordDTO:
    escalation_id: str
    patient_id: str
    reason_code: str
    priority: str
    status: str
    created_at_iso: str
    created_by_user_id: str
    caregiver_note: str | None = None
"""

AUDIT_EVENT_RECORD_DTO: str = """
@dataclass(frozen=True)
class AuditEventRecordDTO:
    audit_event_id: str
    event_name: str
    actor_user_id: str
    entity_type: str
    entity_id: str
    occurred_at_iso: str
    notes: str = ""
"""

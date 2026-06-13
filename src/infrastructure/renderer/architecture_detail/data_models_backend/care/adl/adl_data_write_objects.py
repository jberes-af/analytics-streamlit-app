# # /src/infrastructure/renderer/architecture_detail/data_models_analytics/data_models_backend/adl_data_write_objects.py

from src.domain.mobile_app_types import (
    DataWrite
)

ADL_HOME_DATA_WRITES = ()

PATIENT_SUMMARY_DATA_WRITES = ()

ADL_ENTRY_DATA_WRITES = (
    DataWrite(
        name="write_adl_assessment_record",
        target_dtos=("AdlAssessmentRecordDTO",),
        description="Persist ADL assessment.",
    ),
    DataWrite(
        name="write_audit_event_adl_assessment_saved",
        target_dtos=("AuditEventDTO",),
        description="Record audit event for ADL save.",
    ),
    DataWrite(
        name="write_review_signal_if_decline_detected",
        target_dtos=("ReviewSignalDTO",),
        description="Generate review signal if decline detected.",
    ),
    DataWrite(
        name="write_review_queue_item_if_required",
        target_dtos=("ReviewQueueItemRecordDTO",),
        description="Create queue item if action required.",
    ),
)

OBSERVATION_ENTRY_DATA_WRITES = (
    DataWrite(
        name="write_observation_record",
        target_dtos=("ObservationRecordDTO",),
        description="Persist observation.",
    ),
    DataWrite(
        name="write_audit_event_observation_saved",
        target_dtos=("AuditEventDTO",),
        description="Record audit event.",
    ),
    DataWrite(
        name="write_review_signal_if_concerning_observation_detected",
        target_dtos=("ReviewSignalDTO",),
        description="Generate review signal.",
    ),
    DataWrite(
        name="write_review_queue_item_if_required",
        target_dtos=("ReviewQueueItemRecordDTO",),
        description="Create queue item.",
    ),
)

REVIEW_QUEUE_DATA_WRITES = ()

REVIEW_QUEUE_DETAIL_DATA_WRITES = (
    DataWrite(
        name="write_review_queue_status_update",
        target_dtos=("ReviewQueueItemRecordDTO",),
        description="Update queue item status.",
    ),
    DataWrite(
        name="write_audit_event_review_item_acknowledged",
        target_dtos=("AuditEventDTO",),
        description="Audit acknowledgment.",
    ),
)

ESCALATION_DATA_WRITES = (
    DataWrite(
        name="write_escalation_record",
        target_dtos=("EscalationRecordDTO",),
        description="Persist escalation.",
    ),
    DataWrite(
        name="write_escalation_assignment_records",
        target_dtos=("EscalationAssignmentDTO",),
        description="Persist assignments.",
    ),
    DataWrite(
        name="write_notification_records_if_enabled",
        target_dtos=("NotificationDTO",),
        description="Send notifications.",
    ),
    DataWrite(
        name="write_audit_event_escalation_created",
        target_dtos=("AuditEventDTO",),
        description="Audit escalation.",
    ),
    DataWrite(
        name="update_related_review_queue_item_status",
        target_dtos=("ReviewQueueItemRecordDTO",),
        description="Update queue item.",
    ),
)

PATIENT_HISTORY_DATA_WRITES = ()

CORRECTION_DATA_WRITES = (
    DataWrite(
        name="write_corrected_record_version",
        target_dtos=("AdlAssessmentRecordDTO",),
        description="Create corrected version.",
    ),
    DataWrite(
        name="link_corrected_record_to_original",
        target_dtos=("CorrectionLinkDTO",),
        description="Link records.",
    ),
    DataWrite(
        name="write_correction_audit_event",
        target_dtos=("AuditEventDTO",),
        description="Audit correction.",
    ),
)
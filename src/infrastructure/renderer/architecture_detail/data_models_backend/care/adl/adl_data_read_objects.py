# # /src/infrastructure/renderer/architecture_detail/data_models_analytics/data_models_backend/adl_data_read_objects.py

from src.domain.mobile_app_types import (
    DataRead
)

ADL_HOME_DATA_READS = (
    DataRead(
        name="read_caregiver_shift_assignments",
        source_dtos=("CaregiverAssignmentRecordDTO",),
        output_dto="CaregiverShiftAssignmentReadDTO",
        description="Retrieve patients assigned to caregiver for current shift.",
    ),
    DataRead(
        name="read_patient_home_card_projection",
        source_dtos=("PatientRecordDTO", "AdlAssessmentRecordDTO", "ObservationRecordDTO"),
        output_dto="PatientHomeCardDTO",
        description="Build patient home card view model.",
    ),
    DataRead(
        name="read_adl_completion_status_by_patient",
        source_dtos=("AdlAssessmentRecordDTO", "AdlCategoryDefinitionDTO"),
        output_dto="AdlCompletionStatusDTO",
        description="Compute ADL completion status per patient.",
    ),
    DataRead(
        name="read_review_signals_by_patient",
        source_dtos=("ReviewQueueItemRecordDTO", "AdlAssessmentRecordDTO"),
        output_dto="ReviewSignalDTO",
        description="Retrieve or compute review signals per patient.",
    ),
    DataRead(
        name="read_open_escalation_counts_by_patient",
        source_dtos=("EscalationRecordDTO",),
        output_dto="EscalationSummaryDTO",
        description="Count open escalations per patient.",
    ),
)

PATIENT_SUMMARY_DATA_READS = (
    DataRead(
        name="read_patient_summary_projection",
        source_dtos=("PatientRecordDTO",),
        output_dto="PatientShiftSnapshotResponseDTO",
        description="Build full patient summary snapshot.",
    ),
    DataRead(
        name="read_current_adl_status_cards",
        source_dtos=("AdlAssessmentRecordDTO",),
        output_dto="AdlStatusCardDTO",
        description="Retrieve current ADL status cards.",
    ),
    DataRead(
        name="read_previous_shift_adl_values",
        source_dtos=("AdlAssessmentRecordDTO",),
        output_dto="AdlPreviousValueDTO",
        description="Retrieve previous shift ADL values.",
    ),
    DataRead(
        name="read_patient_adl_baselines",
        source_dtos=("AdlBaselineRecordDTO",),
        output_dto="AdlBaselineDTO",
        description="Retrieve ADL baseline values.",
    ),
    DataRead(
        name="read_recent_observations",
        source_dtos=("ObservationRecordDTO",),
        output_dto="ObservationSummaryDTO",
        description="Retrieve recent patient observations.",
    ),
    DataRead(
        name="read_active_alerts",
        source_dtos=("AlertRecordDTO",),
        output_dto="AlertSummaryDTO",
        description="Retrieve active alerts.",
    ),
    DataRead(
        name="read_open_escalations",
        source_dtos=("EscalationRecordDTO",),
        output_dto="EscalationSummaryDTO",
        description="Retrieve open escalations.",
    ),
    DataRead(
        name="read_required_actions",
        source_dtos=("ReviewQueueItemRecordDTO",),
        output_dto="ActionRequiredDTO",
        description="Determine required actions for patient.",
    ),
)

ADL_ENTRY_DATA_READS = (
    DataRead(
        name="read_adl_category_definitions",
        source_dtos=("AdlCategoryDefinitionDTO",),
        output_dto="AdlCategoryDefinitionDTO",
        description="Retrieve ADL category definitions.",
    ),
    DataRead(
        name="read_adl_score_scale_definitions",
        source_dtos=("AdlScoreScaleDefinitionDTO",),
        output_dto="AdlScoreOptionDTO",
        description="Retrieve ADL scoring options.",
    ),
    DataRead(
        name="read_latest_adl_assessment_for_patient_adl",
        source_dtos=("AdlAssessmentRecordDTO",),
        output_dto="AdlStatusCardDTO",
        description="Retrieve latest ADL assessment.",
    ),
    DataRead(
        name="read_patient_adl_baseline",
        source_dtos=("AdlBaselineRecordDTO",),
        output_dto="AdlBaselineDTO",
        description="Retrieve ADL baseline.",
    ),
)

OBSERVATION_ENTRY_DATA_READS = (
    DataRead(
        name="read_observation_category_definitions",
        source_dtos=("ObservationCategoryDefinitionDTO",),
        output_dto="ObservationCategoryDTO",
        description="Retrieve observation categories.",
    ),
    DataRead(
        name="read_patient_context",
        source_dtos=("PatientRecordDTO",),
        output_dto="PatientContextDTO",
        description="Retrieve patient context.",
    ),
    DataRead(
        name="read_related_adl_context_if_present",
        source_dtos=("AdlAssessmentRecordDTO",),
        output_dto="AdlContextDTO",
        description="Retrieve related ADL context.",
    ),
)

REVIEW_QUEUE_DATA_READS = (
    DataRead(
        name="read_review_queue_items_for_shift",
        source_dtos=("ReviewQueueItemRecordDTO",),
        output_dto="ReviewQueueItemDTO",
        description="Retrieve queue items.",
    ),
    DataRead(
        name="read_review_queue_summary_counts",
        source_dtos=("ReviewQueueItemRecordDTO",),
        output_dto="ReviewQueueSummaryDTO",
        description="Compute queue summary counts.",
    ),
    DataRead(
        name="read_patient_identifiers_for_queue_items",
        source_dtos=("PatientRecordDTO",),
        output_dto="PatientIdentifierDTO",
        description="Resolve patient info.",
    ),
    DataRead(
        name="read_latest_signal_per_queue_item",
        source_dtos=("ReviewSignalDTO",),
        output_dto="ReviewSignalDTO",
        description="Retrieve latest signal per item.",
    ),
)

REVIEW_QUEUE_DETAIL_DATA_READS = (
    DataRead(
        name="read_review_queue_item_by_id",
        source_dtos=("ReviewQueueItemRecordDTO",),
        output_dto="ReviewQueueDetailResponseDTO",
        description="Retrieve queue item detail.",
    ),
    DataRead(
        name="read_supporting_adl_changes",
        source_dtos=("AdlAssessmentRecordDTO",),
        output_dto="SupportingAdlChangeDTO",
        description="Retrieve ADL changes.",
    ),
    DataRead(
        name="read_supporting_observations",
        source_dtos=("ObservationRecordDTO",),
        output_dto="ObservationSummaryDTO",
        description="Retrieve observations.",
    ),
    DataRead(
        name="read_related_alerts",
        source_dtos=("AlertRecordDTO",),
        output_dto="AlertSummaryDTO",
        description="Retrieve alerts.",
    ),
    DataRead(
        name="read_related_escalations",
        source_dtos=("EscalationRecordDTO",),
        output_dto="EscalationSummaryDTO",
        description="Retrieve escalations.",
    ),
    DataRead(
        name="read_recommended_actions",
        source_dtos=("ReviewQueueItemRecordDTO",),
        output_dto="RecommendedActionDTO",
        description="Compute recommended actions.",
    ),
)

ESCALATION_DATA_READS = (
    DataRead(
        name="read_escalation_reason_definitions",
        source_dtos=("EscalationReasonDefinitionDTO",),
        output_dto="EscalationReasonDTO",
        description="Retrieve escalation reasons.",
    ),
    DataRead(
        name="read_escalation_priority_options",
        source_dtos=("EscalationPriorityDefinitionDTO",),
        output_dto="PriorityOptionDTO",
        description="Retrieve priority options.",
    ),
    DataRead(
        name="read_assignable_recipients",
        source_dtos=("UserDefinitionDTO",),
        output_dto="AssignableRecipientDTO",
        description="Retrieve recipients.",
    ),
    DataRead(
        name="read_escalation_supporting_context",
        source_dtos=("AdlAssessmentRecordDTO", "ObservationRecordDTO"),
        output_dto="EscalationContextResponseDTO",
        description="Retrieve escalation context.",
    ),
)

PATIENT_HISTORY_DATA_READS = (
    DataRead(
        name="read_patient_timeline_items",
        source_dtos=("AdlAssessmentRecordDTO", "ObservationRecordDTO"),
        output_dto="TimelineItemDTO",
        description="Retrieve timeline items.",
    ),
    DataRead(
        name="read_historical_adl_assessments",
        source_dtos=("AdlAssessmentRecordDTO",),
        output_dto="AdlAssessmentRecordDTO",
        description="Retrieve ADL history.",
    ),
    DataRead(
        name="read_adl_trend_points",
        source_dtos=("AdlAssessmentRecordDTO",),
        output_dto="AdlTrendPointDTO",
        description="Compute trend points.",
    ),
)

CORRECTION_DATA_READS = (
    DataRead(
        name="read_existing_entry_for_correction",
        source_dtos=("AdlAssessmentRecordDTO", "ObservationRecordDTO"),
        output_dto="CorrectionContextDTO",
        description="Retrieve original entry.",
    ),
    DataRead(
        name="read_original_entry_audit_context",
        source_dtos=("AuditEventDTO",),
        output_dto="AuditContextDTO",
        description="Retrieve audit context.",
    ),
)

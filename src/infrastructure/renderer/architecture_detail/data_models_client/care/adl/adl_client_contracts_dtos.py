# /src/infrastructure/architecture_detail/data_models_analytics/data_models_client/client_contract_dtos.py

from src.domain.mobile_app_types import (
    DataObject
)
from src.infrastructure.renderer.architecture_detail.data_models_client.build_client_dtos import build_contract

from src.infrastructure.renderer.architecture_detail.data_models_client.care.adl.adl_request_dto_definitions import (
    ADL_CORRECTION_REASON_ENUM,
    ADL_HOME_QUERY_DTO,
    ADL_TRENDS_QUERY_DTO,
    CORRECT_ENTRY_REQUEST_DTO,
    OBSERVATION_HISTORY_QUERY_DTO,
    PATIENT_HISTORY_QUERY_DTO,
    PATIENT_SNAPSHOT_QUERY_DTO,
    REVIEW_QUEUE_DETAIL_QUERY_DTO,
    REVIEW_QUEUE_QUERY_DTO,
    REVIEW_QUEUE_SUMMARY_QUERY_DTO,
    SUBMIT_ADL_ASSESSMENT_REQUEST_DTO,
    SUBMIT_ESCALATION_REQUEST_DTO,
    SUBMIT_OBSERVATION_REQUEST_DTO,
    UPDATE_REVIEW_QUEUE_STATUS_REQUEST_DTO,
)
from src.infrastructure.renderer.architecture_detail.data_models_client.care.adl.adl_response_dto_definitions import (
    ADL_COMPLETION_STATUS_DTO,
    ADL_DETAIL_RESPONSE_DTO,
    ADL_ENTRY_CONTEXT_RESPONSE_DTO,
    ADL_ENTRY_SUMMARY_DTO,
    ADL_HOME_RESPONSE_DTO,
    ADL_SCORE_OPTION_DTO,
    ADL_STATUS_CARD_DTO,
    ADL_TRENDS_RESPONSE_DTO,
    ADL_TREND_POINT_DTO,
    ADL_TREND_SERIES_DTO,
    ADL_TREND_SUMMARY_DTO,
    ALERT_SUMMARY_DTO,
    ASSIGNABLE_RECIPIENT_DTO,
    CORRECT_ENTRY_RESPONSE_DTO,
    ESCALATION_CONTEXT_RESPONSE_DTO,
    ESCALATION_SUMMARY_DTO,
    OBSERVATION_ENTRY_CONTEXT_RESPONSE_DTO,
    OBSERVATION_HISTORY_ITEM_DTO,
    OBSERVATION_HISTORY_RESPONSE_DTO,
    OBSERVATION_SUMMARY_DTO,
    PATIENT_HISTORY_RESPONSE_DTO,
    PATIENT_HOME_CARD_DTO,
    PATIENT_SHIFT_SNAPSHOT_RESPONSE_DTO,
    RECOMMENDED_ACTION_DTO,
    REVIEW_QUEUE_DETAIL_RESPONSE_DTO,
    REVIEW_QUEUE_ITEM_DTO,
    REVIEW_QUEUE_RESPONSE_DTO,
    REVIEW_QUEUE_SUMMARY_DTO,
    REVIEW_SIGNAL_DTO,
    SUBMIT_ADL_ASSESSMENT_RESPONSE_DTO,
    SUBMIT_ESCALATION_RESPONSE_DTO,
    SUBMIT_OBSERVATION_RESPONSE_DTO,
    SUPPORTING_ADL_CHANGE_DTO,
    TIMELINE_ITEM_DTO,
    UPDATE_REVIEW_QUEUE_STATUS_RESPONSE_DTO,
)

from src.infrastructure.renderer.architecture_detail.data_models_client.json_contract_definitions import (
    SUBMIT_ADL_ASSESSMENT_REQUEST_JSON,
)

"""
ADL HOME
"""

ADL_HOME_REQUESTS = [
    DataObject(
        name="AdlHomeQueryDTO",
        description="Query the ADL home screen for a caregiver and shift.",
        code=ADL_HOME_QUERY_DTO,
    ),
]

ADL_HOME_RESPONSES = [
    DataObject(
        name="AdlHomeResponseDTO",
        code=ADL_HOME_RESPONSE_DTO,
    ),
]

"""
ADL ENTRY
"""

ADL_ENTRY_REQUESTS = [
    DataObject(
        name="SubmitAdlAssessmentRequestDTO",
        description="Submit ADL assessment from mobile app.",
        code=SUBMIT_ADL_ASSESSMENT_REQUEST_DTO,
        json_example=SUBMIT_ADL_ASSESSMENT_REQUEST_JSON,
    ),
    DataObject(
        name="CorrectAdlAssessmentRequestDTO",
        description="Submit a correction for an existing ADL, observation, escalation, or review record.",
        code=CORRECT_ENTRY_REQUEST_DTO,
    ),
    DataObject(
        name="AdlCorrectionReasonEnum",
        description="Reason codes for user corrections.",
        code=ADL_CORRECTION_REASON_ENUM,
    ),
]

ADL_ENTRY_RESPONSES = [
    DataObject(
        name="SubmitAdlAssessmentResponseDTO",
        code=SUBMIT_ADL_ASSESSMENT_RESPONSE_DTO,
    ),
    DataObject(
        name="AdlEntryContextResponseDTO",
        code=ADL_ENTRY_CONTEXT_RESPONSE_DTO,
    ),
    DataObject(
        name="AdlScoreOptionDTO",
        code=ADL_SCORE_OPTION_DTO,
    ),
    DataObject(
        name="AdlEntrySummaryDTO",
        code=ADL_ENTRY_SUMMARY_DTO,
    ),
    DataObject(
        name="CorrectEntryResponseDTO",
        code=CORRECT_ENTRY_RESPONSE_DTO,
    ),

]

"""
ESCALATION
"""

ESCALATION_REQUESTS = [
    DataObject(
        name="SubmitEscalationRequestDTO",
        code=SUBMIT_ESCALATION_REQUEST_DTO,
    )
]

ESCALATION_RESPONSES = [
    DataObject(
        name="SubmitEscalationResponseDTO",
        code=SUBMIT_ESCALATION_RESPONSE_DTO,
    ),
    DataObject(
        name="EscalationContextResponseDTO",
        code=ESCALATION_CONTEXT_RESPONSE_DTO,
    ),
    DataObject(
        name="AlertSummaryDTO",
        code=ALERT_SUMMARY_DTO,
    ),
    DataObject(
        name="AssignableRecipientDTO",
        code=ASSIGNABLE_RECIPIENT_DTO,
    ),
]

"""
OBSERVATION ENTRY
"""

OBSERVATION_ENTRY_REQUESTS = [
    DataObject(
        name="SubmitObservationRequestDTO",
        code=SUBMIT_OBSERVATION_REQUEST_DTO,
    )
]

OBSERVATION_ENTRY_RESPONSES = [

    DataObject(
        name="ObservationSummaryDTO",
        code=OBSERVATION_SUMMARY_DTO,
    ),
    DataObject(
        name="SubmitObservationResponseDTO",
        code=SUBMIT_OBSERVATION_RESPONSE_DTO,
    ),
    DataObject(
        name="ObservationEntryContextResponseDTO",
        code=OBSERVATION_ENTRY_CONTEXT_RESPONSE_DTO,
    ),
    DataObject(
        name="ObservationHistoryItemDTO",
        code=OBSERVATION_HISTORY_ITEM_DTO,
    ),
    DataObject(
        name="ObservationHistoryResponseDTO",
        code=OBSERVATION_HISTORY_RESPONSE_DTO,
    ),

]

"""
PATIENT HISTORY
"""

PATIENT_HISTORY_REQUESTS = [
    DataObject(
        name="AdlTrendsQueryDTO",
        description="Query ADL trend data for a patient over a selected time range.",
        code=ADL_TRENDS_QUERY_DTO,
    ),
    DataObject(
        name="ObservationHistoryQueryDTO",
        description="Query observation history for a patient over a selected time range.",
        code=OBSERVATION_HISTORY_QUERY_DTO,
    ),
    DataObject(
        name="PatientHistoryQueryDTO",
        description="Query patient history, including ADLs, observations, escalations, and corrections.",
        code=PATIENT_HISTORY_QUERY_DTO,
    ),
]

PATIENT_HISTORY_RESPONSES = [
    DataObject(
        name="TimelineItemDTO",
        code=TIMELINE_ITEM_DTO,
    ),
    DataObject(
        name="PatientHistoryResponseDTO",
        code=PATIENT_HISTORY_RESPONSE_DTO,
    ),

    DataObject(
        name="AdlTrendSeriesDTO",
        code=ADL_TREND_SERIES_DTO,
    ),

    DataObject(
        name="AdlTrendPointDTO",
        code=ADL_TREND_POINT_DTO,
    ),
    DataObject(
        name="AdlTrendsResponseDTO",
        code=ADL_TRENDS_RESPONSE_DTO,
    ),
    DataObject(
        name="AdlTrendSummaryDTO",
        code=ADL_TREND_SUMMARY_DTO,
    ),
]

"""
PATIENT SUMMARY
"""

PATIENT_SUMMARY_REQUESTS = [
    DataObject(
        name="PatientSnapshotQueryDTO",
        description="Query the patient shift snapshot for summary, ADL status, observations, and escalations.",
        code=PATIENT_SNAPSHOT_QUERY_DTO,
    ),
]

PATIENT_SUMMARY_RESPONSES = [
    DataObject(
        name="PatientShiftSnapshotResponseDTO",
        code=PATIENT_SHIFT_SNAPSHOT_RESPONSE_DTO,
    ),
    DataObject(
        name="PatientHomeCardDTO",
        code=PATIENT_HOME_CARD_DTO,
    ),
    DataObject(
        name="AdlCompletionStatusDTO",
        code=ADL_COMPLETION_STATUS_DTO,
    ),
    DataObject(
        name="AdlDetailResponseDTO",
        code=ADL_DETAIL_RESPONSE_DTO,
    ),

    DataObject(
        name="AdlEntryContextResponseDTO",
        code=ADL_ENTRY_CONTEXT_RESPONSE_DTO,
    ),
    DataObject(
        name="AdlStatusCardDTO",
        code=ADL_STATUS_CARD_DTO,
    ),
    DataObject(
        name="EscalationSummaryDTO",
        code=ESCALATION_SUMMARY_DTO,
    ),
]

"""
QUEUE REVIEW
"""

QUEUE_REVIEW_REQUESTS = [
    DataObject(
        name="ReviewQueueQueryDTO",
        description="Query review queue items for a caregiver, shift, priority, or status filter.",
        code=REVIEW_QUEUE_QUERY_DTO,
    ),
    DataObject(
        name="ReviewQueueSummaryQueryDTO",
        description="Query aggregate review queue counts and priority totals.",
        code=REVIEW_QUEUE_SUMMARY_QUERY_DTO,
    ),
    DataObject(
        name="UpdateReviewQueueStatusRequestDTO",
        description="Update the status or note for a review queue item.",
        code=UPDATE_REVIEW_QUEUE_STATUS_REQUEST_DTO,
    ),
]

QUEUE_REVIEW_RESPONSES = [
    DataObject(
        name="ReviewQueueResponseDTO",
        code=REVIEW_QUEUE_RESPONSE_DTO,
    ),
    DataObject(
        name="ReviewQueueSummaryDTO",
        code=REVIEW_QUEUE_SUMMARY_DTO,
    ),
    DataObject(
        name="ReviewQueueItemDTO",
        code=REVIEW_QUEUE_ITEM_DTO,
    ),
    DataObject(
        name="ReviewSignalDTO",
        code=REVIEW_SIGNAL_DTO,
    ),
    DataObject(
        name="SupportingAdlChangeDTO",
        code=SUPPORTING_ADL_CHANGE_DTO,
    ),
    DataObject(
        name="UpdateReviewQueueStatusResponseDTO",
        code=UPDATE_REVIEW_QUEUE_STATUS_RESPONSE_DTO,
    ),
]

"""
REVIEW QUEUE DETAIL
"""

REVIEW_QUEUE_DETAIL_REQUESTS = [
    DataObject(
        name="ReviewQueueDetailQueryDTO",
        description="Query detailed review queue item context, including supporting ADLs, observations, and escalations.",
        code=REVIEW_QUEUE_DETAIL_QUERY_DTO,
    ),
]

REVIEW_QUEUE_DETAIL_RESPONSES = [
    DataObject(
        name="ReviewQueueDetailResponseDTO",
        code=REVIEW_QUEUE_DETAIL_RESPONSE_DTO,
    ),
    DataObject(
        name="SupportingAdlChangeDTO",
        code=SUPPORTING_ADL_CHANGE_DTO,
    ),
    DataObject(
        name="ObservationSummaryDTO",
        code=OBSERVATION_SUMMARY_DTO,
    ),
    DataObject(
        name="RecommendedActionDTO",
        code=RECOMMENDED_ACTION_DTO,
    ),
]

"""
CLIENT CONTRACTS
"""
ADL_HOME_CLIENT_CONTRACTS = build_contract(
    ADL_HOME_REQUESTS,
    ADL_HOME_RESPONSES,
)

ADL_ENTRY_CLIENT_CONTRACTS = build_contract(
    ADL_ENTRY_REQUESTS,
    ADL_ENTRY_RESPONSES,
)

ESCALATION_CLIENT_CONTRACTS = build_contract(
    ESCALATION_REQUESTS,
    ESCALATION_RESPONSES,
)

OBSERVATION_ENTRY_CLIENT_CONTRACTS = build_contract(
    OBSERVATION_ENTRY_REQUESTS,
    OBSERVATION_ENTRY_RESPONSES,
)

PATIENT_HISTORY_CLIENT_CONTRACTS = build_contract(
    PATIENT_HISTORY_REQUESTS,
    PATIENT_HISTORY_RESPONSES,
)

PATIENT_SUMMARY_CLIENT_CONTRACTS = build_contract(
    PATIENT_SUMMARY_REQUESTS,
    PATIENT_SUMMARY_RESPONSES,
)

REVIEW_QUEUE_CLIENT_CONTRACTS = build_contract(
    QUEUE_REVIEW_REQUESTS,
    QUEUE_REVIEW_RESPONSES,
)

REVIEW_QUEUE_DETAIL_CLIENT_CONTRACTS = build_contract(
    REVIEW_QUEUE_DETAIL_REQUESTS,
    REVIEW_QUEUE_DETAIL_RESPONSES,
)

# /src/infrastructure/architecture_detail/data_models_analytics/data_models_backend/adl_backend_dtos.py

from src.infrastructure.renderer.architecture_detail.data_models_backend.build_backend_dtos import build_backend_data_model, \
    build_dto

from src.infrastructure.renderer.architecture_detail.data_models_backend.care.adl.adl_definition_dto_definitions import (
    ADL_CATEGORY_DEFINITION_DTO,
    ADL_SCORE_SCALE_DEFINITION_DTO,
    ESCALATION_REASON_DEFINITION_DTO,
    OBSERVATION_CATEGORY_DEFINITION_DTO,
    REVIEW_SIGNAL_RULE_DEFINITION_DTO,
)

from src.infrastructure.renderer.architecture_detail.data_models_backend.care.adl.adl_persistence_dto_definitions import (
    ADL_ASSESSMENT_RECORD_DTO,
    AUDIT_EVENT_RECORD_DTO,
    ESCALATION_RECORD_DTO,
    OBSERVATION_RECORD_DTO,
    REVIEW_QUEUE_ITEM_RECORD_DTO,
)

from src.infrastructure.renderer.architecture_detail.data_models_backend.care.adl.adl_data_read_objects import (
    ADL_HOME_DATA_READS,
    PATIENT_SUMMARY_DATA_READS,
    ADL_ENTRY_DATA_READS,
    OBSERVATION_ENTRY_DATA_READS,
    REVIEW_QUEUE_DATA_READS,
    REVIEW_QUEUE_DETAIL_DATA_READS,
    ESCALATION_DATA_READS,
    PATIENT_HISTORY_DATA_READS,
    CORRECTION_DATA_READS,
)

from src.infrastructure.renderer.architecture_detail.data_models_backend.care.adl.adl_data_write_objects import (
    ADL_HOME_DATA_WRITES,
    PATIENT_SUMMARY_DATA_WRITES,
    ADL_ENTRY_DATA_WRITES,
    OBSERVATION_ENTRY_DATA_WRITES,
    REVIEW_QUEUE_DATA_WRITES,
    REVIEW_QUEUE_DETAIL_DATA_WRITES,
    ESCALATION_DATA_WRITES,
    PATIENT_HISTORY_DATA_WRITES,
    CORRECTION_DATA_WRITES,
)

"""
HELPER FUNCTIONS
"""

"""
ADL HOME DTOs
"""

ADL_HOME_DEFINITION_DTOS = []

ADL_HOME_PERSISTENCE_DTOS = []

"""
ADL ENTRY DTOs
"""

ADL_ENTRY_DEFINITION_DTOS = [
    build_dto(
        name="AdlCategoryDefinitionDTO",
        description="Defines ADL category metadata and display attributes.",
        code=ADL_CATEGORY_DEFINITION_DTO,
    ),
    build_dto(
        name="AdlScoreScaleDefinitionDTO",
        description="Defines scoring options and labels for ADL assessments.",
        code=ADL_SCORE_SCALE_DEFINITION_DTO,
    ),
]

ADL_ENTRY_PERSISTENCE_DTOS = [
    build_dto(
        name="AdlAssessmentRecordDTO",
        description="Stored ADL assessment record.",
        code=ADL_ASSESSMENT_RECORD_DTO,
    ),
    build_dto(
        name="AuditEventRecordDTO",
        description="Audit trail record for create, update, correction, or review actions.",
        code=AUDIT_EVENT_RECORD_DTO,
    ),
]

"""
ESCALATION_BACKEND_DTOS
"""

ESCALATION_DEFINITION_DTOS = [
    build_dto(
        name="EscalationReasonDefinitionDTO",
        description="",
        code=ESCALATION_REASON_DEFINITION_DTO,
    ),

]

ESCALATION_PERSISTENCE_DTOS = [
    build_dto(
        name="EscalationRecordDTO",
        description="",
        code=ESCALATION_RECORD_DTO,
    ),

]

"""
OBSERVATION ENTRY BACKEND DTOS
"""

OBSERVATION_ENTRY_DEFINITION_DTOS = [
    build_dto(
        name="ObservationCategoryDefinitionDTO",
        description="",
        code=OBSERVATION_CATEGORY_DEFINITION_DTO,
    ),

]

OBSERVATION_ENTRY_PERSISTENCE_DTOS = [
    build_dto(
        name="ObservationRecordDTO",
        description="",
        code=OBSERVATION_RECORD_DTO,
    ),
]

"""
PATIENT SUMMARY ENTRY BACKEND DTOS
"""

PATIENT_SUMMARY_DEFINITION_DTOS = []

PATIENT_SUMMARY_PERSISTENCE_DTOS = []

"""
PATIENT HISTORY DATA MODELS
"""

PATIENT_HISTORY_DEFINITION_DTOS = [
    build_dto(
        name="ReviewSignalRuleDefinitionDTO",
        description="",
        code=REVIEW_SIGNAL_RULE_DEFINITION_DTO,
    ),

]

PATIENT_HISTORY_PERSISTENCE_DTOS = [
    build_dto(
        name="AuditEventRecordDTO",
        description="",
        code=AUDIT_EVENT_RECORD_DTO,
    ),
]

"""
REVIEW QUEUE BACKEND DTOS
"""

REVIEW_QUEUE_DEFINITION_DTOS = [
    build_dto(
        name="ReviewSignalRuleDefinitionDTO",
        description="",
        code=REVIEW_SIGNAL_RULE_DEFINITION_DTO,
    ),

]

REVIEW_QUEUE_PERSISTENCE_DTOS = [

    build_dto(
        name="ReviewQueueItemRecordDTO",
        description="",
        code=REVIEW_QUEUE_ITEM_RECORD_DTO,
    ),
]

"""
REVIEW QUEUE DETAIL BACKEND DTOS
"""

REVIEW_QUEUE_DETAIL_DEFINITION_DTOS = [
    build_dto(
        name="ReviewSignalRuleDefinitionDTO",
        description="",
        code=REVIEW_SIGNAL_RULE_DEFINITION_DTO,
    ),

]

REVIEW_QUEUE_DETAIL_PERSISTENCE_DTOS = [

    build_dto(
        name="ReviewQueueItemRecordDTO",
        description="",
        code=REVIEW_QUEUE_ITEM_RECORD_DTO,
    ),
]

"""
CORRECTION DTOs
"""
CORRECTION_DEFINITION_DTOS = []

CORRECTION_PERSISTENCE_DTOS = [
    build_dto(
        name="AdlAssessmentRecordDTO",
        description="Stored ADL assessment record that may be corrected by creating a linked corrected version.",
        code=ADL_ASSESSMENT_RECORD_DTO,
    ),
    build_dto(
        name="ObservationRecordDTO",
        description="Stored observation record that may be corrected by creating a linked corrected version.",
        code=OBSERVATION_RECORD_DTO,
    ),
    build_dto(
        name="AuditEventRecordDTO",
        description="Audit trail record for correction actions.",
        code=AUDIT_EVENT_RECORD_DTO,
    ),
]

CORRECTION_BACKEND_DTOS = build_backend_data_model(
    definitions=CORRECTION_DEFINITION_DTOS,
    persistences=CORRECTION_PERSISTENCE_DTOS,
    reads=CORRECTION_DATA_READS,
    writes=CORRECTION_DATA_WRITES,
)

"""
BACKEND DATA MODELS
"""

ADL_ENTRY_BACKEND_DTOS = build_backend_data_model(
    definitions=ADL_ENTRY_DEFINITION_DTOS,
    persistences=ADL_ENTRY_PERSISTENCE_DTOS,
    reads=ADL_ENTRY_DATA_READS,
    writes=ADL_ENTRY_DATA_WRITES,
)

ADL_HOME_BACKEND_DTOS = build_backend_data_model(
    definitions=ADL_HOME_DEFINITION_DTOS,
    persistences=ADL_HOME_PERSISTENCE_DTOS,
    reads=ADL_HOME_DATA_READS,
    writes=ADL_HOME_DATA_WRITES,
)

ESCALATION_BACKEND_DTOS = build_backend_data_model(
    definitions=ESCALATION_DEFINITION_DTOS,
    persistences=ESCALATION_PERSISTENCE_DTOS,
    reads=ESCALATION_DATA_READS,
    writes=ESCALATION_DATA_WRITES,
)

OBSERVATION_ENTRY_BACKEND_DTOS = build_backend_data_model(
    definitions=OBSERVATION_ENTRY_DEFINITION_DTOS,
    persistences=OBSERVATION_ENTRY_PERSISTENCE_DTOS,
    reads=OBSERVATION_ENTRY_DATA_READS,
    writes=OBSERVATION_ENTRY_DATA_WRITES,
)

PATIENT_SUMMARY_BACKEND_DTOS = build_backend_data_model(
    definitions=PATIENT_SUMMARY_DEFINITION_DTOS,
    persistences=PATIENT_SUMMARY_PERSISTENCE_DTOS,
    reads=PATIENT_SUMMARY_DATA_READS,
    writes=PATIENT_SUMMARY_DATA_WRITES,
)

PATIENT_HISTORY_BACKEND_DTOS = build_backend_data_model(
    definitions=PATIENT_HISTORY_DEFINITION_DTOS,
    persistences=PATIENT_HISTORY_PERSISTENCE_DTOS,
    reads=PATIENT_HISTORY_DATA_READS,
    writes=PATIENT_HISTORY_DATA_WRITES,
)

REVIEW_QUEUE_BACKEND_DTOS = build_backend_data_model(
    definitions=REVIEW_QUEUE_DEFINITION_DTOS,
    persistences=REVIEW_QUEUE_PERSISTENCE_DTOS,
    reads=REVIEW_QUEUE_DATA_READS,
    writes=REVIEW_QUEUE_DATA_WRITES,
)

REVIEW_QUEUE_DETAIL_BACKEND_DTOS = build_backend_data_model(
    definitions=REVIEW_QUEUE_DETAIL_DEFINITION_DTOS,
    persistences=REVIEW_QUEUE_DETAIL_PERSISTENCE_DTOS,
    reads=REVIEW_QUEUE_DETAIL_DATA_READS,
    writes=REVIEW_QUEUE_DETAIL_DATA_WRITES,
)

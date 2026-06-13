# /src/infrastructure/architecture_detail/data_models_analytics/data_models_domain/care/adl_domain_dtos.py

"""
groups domain DTOs by screen
"""

from src.infrastructure.renderer.architecture_detail.data_models_domain.build_domain_dtos import (
    build_domain_data_model,
    build_dto,
)

from src.infrastructure.renderer.architecture_detail.data_models_domain.care.raw_dtos.raw_adl import (
    ADL_ASSESSMENT_CATEGORY_ENUM,
    ADL_ASSESSMENT_RECORD_DTO,
    ADL_CATEGORY_DEFINITIONS_LOOKUP,
    ADL_OBSERVATION_CATEGORY_DEFINITIONS_LOOKUP,
    ADL_OBSERVATION_CATEGORY_ENUM,
    ADL_OBSERVATION_RECORD_DTO,
    ADL_SCORE_DEFINITIONS_BATHING_LOOKUP,
    ADL_SCORE_DEFINITIONS_CONTINENCE_LOOKUP,
    ADL_SCORE_DEFINITIONS_DRESSING_LOOKUP,
    ADL_SCORE_DEFINITIONS_EATING_LOOKUP,
    ADL_SCORE_DEFINITIONS_TOILETING_LOOKUP,
    ADL_SCORE_DEFINITIONS_TRANSFERRING_LOOKUP,
    ADL_SCORE_DEFINITION_ENTITY_DTO,
    ADL_SCORE_LABELS_BATHING_LOOKUP,
    ADL_SCORE_LABELS_CONTINENCE_LOOKUP,
    ADL_SCORE_LABELS_DRESSING_LOOKUP,
    ADL_SCORE_LABELS_EATING_LOOKUP,
    ADL_SCORE_LABELS_TOILETING_LOOKUP,
    ADL_SCORE_LABELS_TRANSFERRING_LOOKUP,
)

# from src.infrastructure.renderer.architecture_detail.data_models_backend.care.adl.adl_persistence_dto_definitions import ()
# from src.infrastructure.renderer.architecture_detail.data_models_backend.care.adl.adl_data_read_objects import ()
# from src.infrastructure.renderer.architecture_detail.data_models_backend.care.adl.adl_data_write_objects import ()

"""
UI-ADL-01
"""

ADL_RESIDENT_SUMMARY_DOMAIN_DTOS = [

    build_dto(
        name="AdlScoreDefinitionsBathingLookup",
        description="",
        code=ADL_SCORE_DEFINITIONS_BATHING_LOOKUP,
    ),

    build_dto(
        name="AdlScoreDefinitionsContinenceLookup",
        description="",
        code=ADL_SCORE_DEFINITIONS_CONTINENCE_LOOKUP,
    ),

    build_dto(
        name="AdlScoreDefinitionsDressingLookup",
        description="",
        code=ADL_SCORE_DEFINITIONS_DRESSING_LOOKUP,
    ),

    build_dto(
        name="AdlScoreDefinitionsEatingLookup",
        description="",
        code=ADL_SCORE_DEFINITIONS_EATING_LOOKUP,
    ),

    build_dto(
        name="AdlScoreDefinitionsToiletingLookup",
        description="",
        code=ADL_SCORE_DEFINITIONS_TOILETING_LOOKUP,
    ),

    build_dto(
        name="AdlScoreDefinitionsTransferringLookup",
        description="",
        code=ADL_SCORE_DEFINITIONS_TRANSFERRING_LOOKUP,
    ),

    build_dto(
        name="AdlObservationCategoryDefinitionsLookup",
        description="",
        code=ADL_OBSERVATION_CATEGORY_DEFINITIONS_LOOKUP,
    ),

    build_dto(
        name="AdlScoreLabelsBathingLookup",
        description="",
        code=ADL_SCORE_LABELS_BATHING_LOOKUP,
    ),

    build_dto(
        name="AdlScoreLabelsContinenceLookup",
        description="",
        code=ADL_SCORE_LABELS_CONTINENCE_LOOKUP,
    ),

    build_dto(
        name="AdlScoreLabelsDressingLookup",
        description="",
        code=ADL_SCORE_LABELS_DRESSING_LOOKUP,
    ),

    build_dto(
        name="AdlScoreLabelsEatingLookup",
        description="",
        code=ADL_SCORE_LABELS_EATING_LOOKUP,
    ),

    build_dto(
        name="AdlScoreLabelsToiletingLookup",
        description="",
        code=ADL_SCORE_LABELS_TOILETING_LOOKUP,
    ),

    build_dto(
        name="AdlScoreLabelsTransferringLookup",
        description="",
        code=ADL_SCORE_LABELS_TRANSFERRING_LOOKUP,
    ),

    build_dto(
        name="AdlScoreDefinitionEntityDTO",
        description="",
        code=ADL_SCORE_DEFINITION_ENTITY_DTO,
    ),

    build_dto(
        name="AdlObservationRecordDTO",
        description="",
        code=ADL_OBSERVATION_RECORD_DTO,
    ),

]

"""
UI-ADL-02
"""

ADL_DEVICE_LINK_DOMAIN_DTOS = []

"""
UI-ADL-03
"""

ADL_TRENDS_DOMAIN_DTOS = []

"""
UI-ADL-04
"""

ADL_ASSESSMENT_DOMAIN_DTOS = [
    build_dto(
        name="AdlAssessmentCategoryEnum",
        description="",
        code=ADL_ASSESSMENT_CATEGORY_ENUM,
    ),
    build_dto(
        name="AdlCategoryDefinitionsLookup",
        description="",
        code=ADL_CATEGORY_DEFINITIONS_LOOKUP,
    ),
    build_dto(
        name="AdlScoreDefinitionEntityDTO",
        description="",
        code=ADL_SCORE_DEFINITION_ENTITY_DTO,
    ),

    build_dto(
        name="AdlAssessmentRecordDTO",
        description="",
        code=ADL_ASSESSMENT_RECORD_DTO,
    ),

]

"""
UI-ADL-05
"""

ADL_OBSERVATION_DOMAIN_DTOS = [
    build_dto(
        name="AdlObservationCategoryEnum",
        description="",
        code=ADL_OBSERVATION_CATEGORY_ENUM,
    ),

    build_dto(
        name="AdlObservationRecordDTO",
        description="",
        code=ADL_OBSERVATION_RECORD_DTO,
    ),
]

"""
UI-ADL-06
"""

ADL_DEVICE_TRENDS_DOMAIN_DTOS = []

"""
BACKEND DATA MODELS
"""

ADL_ASSESSMENT_BACKEND_DTOS = build_domain_data_model(
    definitions=ADL_ASSESSMENT_DOMAIN_DTOS,
    persistences=tuple(),
    reads=tuple(),
    writes=tuple(),
)

ADL_DEVICE_LINK_BACKEND_DTOS = build_domain_data_model(
    definitions=ADL_DEVICE_LINK_DOMAIN_DTOS,
    persistences=tuple(),
    reads=tuple(),
    writes=tuple(),
)

ADL_DEVICE_TRENDS_BACKEND_DTOS = build_domain_data_model(
    definitions=ADL_DEVICE_TRENDS_DOMAIN_DTOS,
    persistences=tuple(),
    reads=tuple(),
    writes=tuple(),
)

ADL_OBSERVATION_BACKEND_DTOS = build_domain_data_model(
    definitions=ADL_OBSERVATION_DOMAIN_DTOS,
    persistences=tuple(),
    reads=tuple(),
    writes=tuple(),
)

ADL_RESIDENT_SUMMARY_BACKEND_DTOS = build_domain_data_model(
    definitions=ADL_RESIDENT_SUMMARY_DOMAIN_DTOS,
    persistences=tuple(),
    reads=tuple(),
    writes=tuple(),
)

ADL_TRENDS_BACKEND_DTOS = build_domain_data_model(
    definitions=ADL_TRENDS_DOMAIN_DTOS,
    persistences=tuple(),
    reads=tuple(),
    writes=tuple(),
)

# /src/infrastructure/architecture_detail/data_models_analytics/data_models_domain/care/plan_domain_dtos

from src.infrastructure.renderer.architecture_detail.data_models_domain.build_domain_dtos import (
    build_domain_data_model,
    build_dto,
)

from src.infrastructure.renderer.architecture_detail.data_models_domain.care.raw_dtos.raw_plans import (
    CARE_PLAN_TYPE_ENUM,
    PLAN_ACTION_DTO,
    PLAN_METRIC_DTO,
    PLAN_MILESTONE_DTO,
    PLAN_PROGRESS_ENTRY_DTO,
    PLAN_RECORD_DTO,
    PLAN_REVIEW_DTO,
    PLAN_SCHEDULE_DTO,
    PLAN_STATUS_ENUM,
    PROGRESS_STATUS_ENUM,
    SESSION_NOTE_DTO,
)

# from src.infrastructure.renderer.architecture_detail.data_models_backend.care.adl.adl_persistence_dto_definitions import ()
# from src.infrastructure.renderer.architecture_detail.data_models_backend.care.adl.adl_data_read_objects import ()
# from src.infrastructure.renderer.architecture_detail.data_models_backend.care.adl.adl_data_write_objects import ()

"""
UI-TP-01
"""

THERAPEUTIC_PLAN_DASHBOARD_DOMAIN_DTOS = [

    build_dto(
        name="PlanReviewDTO",
        description="",
        code=PLAN_REVIEW_DTO,
    ),

]

"""
UI-TP-02
"""

THERAPEUTIC_PLAN_RECORD_DOMAIN_DTOS = [

    build_dto(
        name="PlanRecordDTO",
        description="",
        code=PLAN_RECORD_DTO,
    ),

    build_dto(
        name="PlanReviewDTO",
        description="",
        code=PLAN_REVIEW_DTO,
    ),

]

"""
UI-TP-03
"""

CREATE_THERAPEUTIC_PLAN_DOMAIN_DTOS = [

    build_dto(
        name="CarePlanTypeEnum",
        description="",
        code=CARE_PLAN_TYPE_ENUM,
    ),

    build_dto(
        name="PlanStatusEnum",
        description="",
        code=PLAN_STATUS_ENUM,
    ),

    build_dto(
        name="ProgressStatusEnum",
        description="",
        code=PROGRESS_STATUS_ENUM,
    ),

    build_dto(
        name="SessionNoteDTO",
        description="",
        code=SESSION_NOTE_DTO,
    ),

    build_dto(
        name="PlanActionDTO",
        description="",
        code=PLAN_ACTION_DTO,
    ),

    build_dto(
        name="PlanMilestoneDTO",
        description="",
        code=PLAN_MILESTONE_DTO,
    ),

    build_dto(
        name="PlanScheduleDTO",
        description="",
        code=PLAN_SCHEDULE_DTO,
    ),

    build_dto(
        name="PlanMetricDTO",
        description="",
        code=PLAN_METRIC_DTO,
    ),

]

"""
UI-TP-04
"""

REVISE_THERAPEUTIC_PLAN_DOMAIN_DTOS = [

    build_dto(
        name="CarePlanTypeEnum",
        description="",
        code=CARE_PLAN_TYPE_ENUM,
    ),

    build_dto(
        name="PlanStatusEnum",
        description="",
        code=PLAN_STATUS_ENUM,
    ),

    build_dto(
        name="ProgressStatusEnum",
        description="",
        code=PROGRESS_STATUS_ENUM,
    ),

    build_dto(
        name="SessionNoteDTO",
        description="",
        code=SESSION_NOTE_DTO,
    ),

    build_dto(
        name="PlanActionDTO",
        description="",
        code=PLAN_ACTION_DTO,
    ),

    build_dto(
        name="PlanMilestoneDTO",
        description="",
        code=PLAN_MILESTONE_DTO,
    ),

    build_dto(
        name="PlanScheduleDTO",
        description="",
        code=PLAN_SCHEDULE_DTO,
    ),

    build_dto(
        name="PlanMetricDTO",
        description="",
        code=PLAN_METRIC_DTO,
    ),

]

"""
UI-TP-05
"""

UPDATE_PROGRESS_THERAPEUTIC_PLAN_DOMAIN_DTOS = [
    build_dto(
        name="ProgressStatusEnum",
        description="",
        code=PROGRESS_STATUS_ENUM,
    ),
    build_dto(
        name="SessionNoteDTO",
        description="",
        code=SESSION_NOTE_DTO,
    ),
    build_dto(
        name="PlanMilestoneDTO",
        description="",
        code=PLAN_MILESTONE_DTO,
    ),

    build_dto(
        name="PlanMetricDTO",
        description="",
        code=PLAN_METRIC_DTO,
    ),

    build_dto(
        name="PlanProgressEntryDTO",
        description="",
        code=PLAN_PROGRESS_ENTRY_DTO,
    ),

]
# --------------------------------------------------------------------
# --------------------------------------------------------------------


"""
BACKEND DATA MODELS
"""

THERAPEUTIC_PLAN_DASHBOARD_BACKEND_DTOS = build_domain_data_model(
    definitions=THERAPEUTIC_PLAN_DASHBOARD_DOMAIN_DTOS,
    persistences=tuple(),
    reads=tuple(),
    writes=tuple(),
)

THERAPEUTIC_PLAN_RECORD_BACKEND_DTOS = build_domain_data_model(
    definitions=THERAPEUTIC_PLAN_RECORD_DOMAIN_DTOS,
    persistences=tuple(),
    reads=tuple(),
    writes=tuple(),
)

CREATE_THERAPEUTIC_PLAN_BACKEND_DTOS = build_domain_data_model(
    definitions=CREATE_THERAPEUTIC_PLAN_DOMAIN_DTOS,
    persistences=tuple(),
    reads=tuple(),
    writes=tuple(),
)

REVISE_THERAPEUTIC_PLAN_BACKEND_DTOS = build_domain_data_model(
    definitions=REVISE_THERAPEUTIC_PLAN_DOMAIN_DTOS,
    persistences=tuple(),
    reads=tuple(),
    writes=tuple(),
)

UPDATE_PROGRESS_THERAPEUTIC_PLAN_BACKEND_DTOS = build_domain_data_model(
    definitions=UPDATE_PROGRESS_THERAPEUTIC_PLAN_DOMAIN_DTOS,
    persistences=tuple(),
    reads=tuple(),
    writes=tuple(),
)

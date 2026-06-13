# /src/infrastructure/architecture_detail/data_models_analytics/data_models_domain/care/priority_item_domain_dtos

from src.infrastructure.renderer.architecture_detail.data_models_domain.build_domain_dtos import (
    build_domain_data_model,
    build_dto,
)

from src.infrastructure.renderer.architecture_detail.data_models_domain.care.raw_dtos.raw_priority_item import (
    PRIORITY_ITEM_LEVEL_ENUM,
    PRIORITY_ITEM_STATUS_ENUM,
    PRIORITY_ITEM_NOTE_DTO,
    PRIORITY_ITEM_RECORD_DTO,
)

# from src.infrastructure.renderer.architecture_detail.data_models_backend.care.adl.adl_persistence_dto_definitions import ()
# from src.infrastructure.renderer.architecture_detail.data_models_backend.care.adl.adl_data_read_objects import ()
# from src.infrastructure.renderer.architecture_detail.data_models_backend.care.adl.adl_data_write_objects import ()

"""
UI-PI-01
"""

PRIORITY_ITEM_DASHBOARD_DOMAIN_DTOS = []
build_dto(
    name="PriorityItemRecordDTO",
    description="",
    code=PRIORITY_ITEM_RECORD_DTO,
),

"""
UI-PI-02
"""

PRIORITY_ITEM_RECORD_DOMAIN_DTOS = [
    build_dto(
        name="PriorityItemRecordDTO",
        description="",
        code=PRIORITY_ITEM_RECORD_DTO,
    ),

]

"""
UI-PI-03
"""

CREATE_PRIORITY_ITEM_DOMAIN_DTOS = [
    build_dto(
        name="PriorityItemLevelEnum",
        description="",
        code=PRIORITY_ITEM_LEVEL_ENUM,
    ),

    build_dto(
        name="PriorityItemStatusEnum",
        description="",
        code=PRIORITY_ITEM_STATUS_ENUM,
    ),

    build_dto(
        name="PriorityItemNoteDTO",
        description="",
        code=PRIORITY_ITEM_NOTE_DTO,
    ),

    build_dto(
        name="PriorityItemRecordDTO",
        description="",
        code=PRIORITY_ITEM_RECORD_DTO,
    ),

]

"""
UI-PI-04
"""

UPDATE_PRIORITY_ITEM_DOMAIN_DTOS = [
    build_dto(
        name="PriorityItemLevelEnum",
        description="",
        code=PRIORITY_ITEM_LEVEL_ENUM,
    ),

    build_dto(
        name="PriorityItemStatusEnum",
        description="",
        code=PRIORITY_ITEM_STATUS_ENUM,
    ),

    build_dto(
        name="PriorityItemNoteDTO",
        description="",
        code=PRIORITY_ITEM_NOTE_DTO,
    ),

    build_dto(
        name="PriorityItemRecordDTO",
        description="",
        code=PRIORITY_ITEM_RECORD_DTO,
    ),

]

# --------------------------------------------------------------------
# --------------------------------------------------------------------


"""
BACKEND DATA MODELS
"""

PRIORITY_ITEM_DASHBOARD_BACKEND_DTOS = build_domain_data_model(
    definitions=PRIORITY_ITEM_DASHBOARD_DOMAIN_DTOS,
    persistences=tuple(),
    reads=tuple(),
    writes=tuple(),
)

PRIORITY_ITEM_RECORD_BACKEND_DTOS = build_domain_data_model(
    definitions=PRIORITY_ITEM_RECORD_DOMAIN_DTOS,
    persistences=tuple(),
    reads=tuple(),
    writes=tuple(),
)

CREATE_PRIORITY_ITEM_BACKEND_DTOS = build_domain_data_model(
    definitions=CREATE_PRIORITY_ITEM_DOMAIN_DTOS,
    persistences=tuple(),
    reads=tuple(),
    writes=tuple(),
)

UPDATE_PRIORITY_ITEM_BACKEND_DTOS = build_domain_data_model(
    definitions=UPDATE_PRIORITY_ITEM_DOMAIN_DTOS,
    persistences=tuple(),
    reads=tuple(),
    writes=tuple(),
)

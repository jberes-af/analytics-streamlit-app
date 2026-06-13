# /src/infrastructure/architecture_detail/data_models_analytics/data_models_backend/shared_backend_dtos.py

from src.infrastructure.renderer.architecture_detail.data_models_backend.build_backend_dtos import (
    build_backend_data_model,
    build_dto,
)

from src.infrastructure.renderer.architecture_detail.data_models_backend.shared.shared_definition_dto_definitions import (
    USER_ORGANIZATION_DEFINITION_DTO,
    USER_ACCOUNT_DEFINITION_DTO,
)

from src.infrastructure.renderer.architecture_detail.data_models_backend.shared.shared_persistence_dto_definitions import (
    USER_ACCOUNT_RECORD_DTO,
    USER_ORGANIZATION_RECORD_DTO,
)

# from src.infrastructure.renderer.architecture_detail.data_models_analytics.data_models_backend.care.adl.adl_data_read_objects import (
# from src.infrastructure.renderer.architecture_detail.data_models_analytics.data_models_backend.shared.shared_data_write_objects import ()

"""
HELPER FUNCTIONS
"""

"""
ADL HOME DTOs
"""

ACCOUNT_HOME_DEFINITION_DTOS = []

ACCOUNT_HOME_PERSISTENCE_DTOS = []

"""
USER CONFIG DTOs
"""

ACCOUNT_DEFINITION_DTOS = [
    build_dto(
        name="UserAccountDefinitionDTO",
        description="Defines user account attributes.",
        code=USER_ACCOUNT_DEFINITION_DTO,
    ),
    build_dto(
        name="UserOrganizationDefinitionDTO",
        description="Defines user organization attributes.",
        code=USER_ORGANIZATION_DEFINITION_DTO,
    ),
]

ACCOUNT_PERSISTENCE_DTOS = [
    build_dto(
        name="UserAccountRecordDTO",
        description="Stored user account record.",
        code=USER_ACCOUNT_RECORD_DTO,
    ),
    build_dto(
        name="UserOrganizationRecordDTO",
        description="Stored user organization record.",
        code=USER_ORGANIZATION_RECORD_DTO,
    ),
]

"""
BACKEND DATA MODELS
"""

ACCOUNT_BACKEND_DTOS = build_backend_data_model(
    definitions=ACCOUNT_DEFINITION_DTOS,
    persistences=ACCOUNT_PERSISTENCE_DTOS,
    reads=(),
    writes=(),
)

# /src/infrastructure/renderer/architecture_detail/data_models_analytics/data_models_backend/resident_definition_dto_definitions.py

RESIDENT_DEFINITION_DTO: str = """
class ResidentDefinitionDTO:
    resident_id: str
    organization_id: str
    first_name: str
    last_name: str
    preferred_name: str | None = None
    is_active: bool = True
    created_at_iso: str
    updated_at_iso: str
"""


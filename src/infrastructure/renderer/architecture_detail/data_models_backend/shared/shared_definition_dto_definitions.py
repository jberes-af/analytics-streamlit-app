# /src/infrastructure/renderer/architecture_detail/data_models_analytics/data_models_backend/shared_definition_dto_definitions.py

USER_ORGANIZATION_DEFINITION_DTO: str = """
class UserOrganizationDefinitionDTO:
    organization_id: str
    name: str
    organization_type: str
"""

USER_ACCOUNT_DEFINITION_DTO: str = """
class UserAccountDefinitionDTO:
    user_id: str
    organization_id: str
    name: str
    email: str
    phone: str | None = None
    role: str
    is_active: bool = True
"""

# /src/infrastructure/renderer/architecture_detail/data_models_analytics/data_models_backend/adl_persistence_dto_definitions.py


USER_ORGANIZATION_RECORD_DTO: str = """
@dataclass(frozen=True)
class UserOrganizationRecordDTO:
    organization_id: str
    name: str
    organization_type: str
    created_at_iso: str
    updated_at_iso: str
"""

USER_ACCOUNT_RECORD_DTO: str = """
@dataclass(frozen=True)
class UserAccountRecordDTO:
    user_id: str
    organization_id: str
    name: str
    email: str
    phone: str | None = None
    role: str
    is_active: bool = True
    created_at_iso: str
    updated_at_iso: str
"""

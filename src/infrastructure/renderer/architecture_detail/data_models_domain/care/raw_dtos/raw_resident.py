# /src/infrastructure/renderer/architecture_detail/data_models_analytics/data_models_domain/care/raw_resident.py


RESIDENT_CONTACT_INFORMATION_DTO: str = """
@dataclass(frozen=True)
class ResidentContactInformationDTO:
    resident_id: str
    resident_name: str
    primary_contact_name: str
    primary_contact_email: str
    primary_contact_telephone: str
    primary_contact_address: str
"""

RESIDENT_PROFILE_DTO: str = """
@dataclass(frozen=True)
class ResidentProfileDTO:
    resident_id: str
    resident_name: str
    preferred_name: str
    contact_information: ResidentContactInformationDTO
    care_facility_profile: CareFacilityProfileDTO
"""

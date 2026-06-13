# /src/infrastructure/renderer/architecture_detail/data_models_analytics/data_models_domain/user.py

CARE_FACILITY_TYPE_ENUM: str = """
class CareFacilityTypeEnum(StrEnum):
    SINGLE_FAMILY_HOME = "Single Family Home"
    RESIDENTIAL_CARE_HOME = "Residential Care Home"
    ASSISTED_LIVING_FACILITY = "Assisted Living Facility"
    SKILLED_NURSING_FACILITY = "Skilled Nursing Facility"
    RETIREMENT_COMMUNITY = "Retirement Community"
    INDEPENDENT_LIVING_COMMUNITY = "Independent Living Community"
    THERAPY_CLINIC = "Therapy Clinic"
    RESEARCH_FACILITY = "Research Facility"
    HOSPITAL = "Hospital"
    MEMORY_CARE_FACILITY = "Memory Care Facility"
    DAY_CARE_FACILITY = "Day Care Facility"
"""

CARE_FACILITY_PROFILE_DTO: str = """
@dataclass(frozen=True)
class CareFacilityProfileDTO:
    facility_id: str
    facility_type: str
    facility_address: str
    facility_telephone: str
    facility_manager: str
"""

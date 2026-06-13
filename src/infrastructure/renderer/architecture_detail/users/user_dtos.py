# /src/infrastructure/renderer/architecture_detail/users/user_dtos.py

from src.domain.mobile_app_enums import (
    Role,
    UserResponsibility,
)

from src.domain.mobile_app_types import (
    PermissionRule,
    UserDefinition,
)

"""
USER PERMISSIONS

COMMON_ADL_PERMISSIONS = (
    PermissionRule(
        role=Role.INFORMAL_CAREGIVER,
        allowed=True,
        notes="May enter ADL observations for assigned patient.",
    ),
    PermissionRule(
        role=Role.PROFESSIONAL_CAREGIVER_NON_CMS,
        allowed=True,
        notes="May enter ADL observations using clinical presentation.",
    ),
    PermissionRule(
        role=Role.CMS_BILLING_PROVIDER,
        allowed=True,
        notes="May enter, review, and use ADL observations in CMS context.",
    ),
)

COMMON_OBS_PERMISSIONS = (
    PermissionRule(
        role=Role.INFORMAL_CAREGIVER,
        allowed=True,
        notes="May create and review observations for assigned patient.",
    ),
    PermissionRule(
        role=Role.PROFESSIONAL_CAREGIVER_NON_CMS,
        allowed=True,
        notes="May create and review observations using clinical presentation.",
    ),
    PermissionRule(
        role=Role.CMS_BILLING_PROVIDER,
        allowed=True,
        notes="May create, review, and use observations in CMS context.",
    ),
)

COMMON_REVIEW_PERMISSIONS = (
    PermissionRule(
        role=Role.INFORMAL_CAREGIVER,
        allowed=True,
        notes="May review and correct entries they are permitted to access.",
    ),
    PermissionRule(
        role=Role.PROFESSIONAL_CAREGIVER_NON_CMS,
        allowed=True,
        notes="May review and correct entries using clinical presentation.",
    ),
    PermissionRule(
        role=Role.CMS_BILLING_PROVIDER,
        allowed=True,
        notes="May review, correct, and use records in CMS documentation context.",
    ),
)
"""

"""
USER DTOs
"""

FAMILY_CAREGIVER = UserDefinition(
    user_id="user.informal_caregiver",
    name="Family Caregiver",
    role=Role.INFORMAL_CAREGIVER,
    description=(
        "Unpaid caregiver, such as a family member, using the app for "
        "at-home support and day-to-day care observations."
    ),
    responsibilities=(
        UserResponsibility.RECORD_ADL_ASSESSMENTS,
        UserResponsibility.RECORD_OBSERVATIONS,
        UserResponsibility.ADD_CONTEXTUAL_NOTES,
        UserResponsibility.CONFIRM_OBSERVATION_TIME,

        UserResponsibility.REVIEW_PRIOR_ENTRIES,
        UserResponsibility.REVIEW_DAILY_SUMMARY,

        UserResponsibility.CORRECT_RECENT_ENTRIES,

        UserResponsibility.REPORT_CONCERNS,
        UserResponsibility.RESPOND_TO_PROMPTS,
    ),
)




NON_CMS_BILLING_PROFESSIONAL = UserDefinition(
    user_id="user.non_cms_billing_professional",
    name="Professional Caregiver (Non-CMS-Billing)",
    role=Role.PROFESSIONAL_CAREGIVER_NON_CMS,
    description=(
        "Paid caregiver or staff who uses the app for clinical or operational care, "
        "but does not submit CMS RTM claims."
    ),
    responsibilities=(
        # Core usage (same as others)
        UserResponsibility.RECORD_ADL_ASSESSMENTS,
        UserResponsibility.RECORD_OBSERVATIONS,
        UserResponsibility.REVIEW_PRIOR_ENTRIES,

        UserResponsibility.REVIEW_PATIENT_DATA,
        UserResponsibility.IDENTIFY_TRENDS,
        UserResponsibility.ESCALATE_CONCERNS,

        UserResponsibility.ADD_CONTEXTUAL_NOTES,
        UserResponsibility.UPDATE_RECENT_ENTRIES,

        UserResponsibility.FOLLOW_CARE_PROTOCOLS,
    ),
)

CMS_BILLING_PROVIDER = UserDefinition(
    user_id="user.cms_billing_provider",
    name="CMS RTM Billing Provider",
    role=Role.CMS_BILLING_PROVIDER,
    responsibilities=(
        # Core clinical responsibilities
        UserResponsibility.REVIEW_PATIENT_DATA,
        UserResponsibility.INTERPRET_TRENDS,
        UserResponsibility.VALIDATE_CLINICAL_RELEVANCE,

        UserResponsibility.DOCUMENT_CLINICAL_REVIEW,
        UserResponsibility.DOCUMENT_INTERVENTIONS,
        UserResponsibility.ATTRIBUTE_ACTIONS_TO_PROVIDER,

        UserResponsibility.MONITOR_ADHERENCE,
        UserResponsibility.RESPOND_TO_ALERTS,
        UserResponsibility.ENGAGE_WITH_PATIENT,

        UserResponsibility.TRACK_TIME_FOR_RTM,
        UserResponsibility.VERIFY_DATA_SOURCE_DEVICE,
        UserResponsibility.MAINTAIN_AUDIT_TRAIL,
        UserResponsibility.SUPPORT_CLAIM_SUBMISSION,
    ),
)
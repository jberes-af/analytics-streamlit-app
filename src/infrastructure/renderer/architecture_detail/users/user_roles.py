# /src/infrastructure/renderer/architecture_detail/users/user_roles.py

from src.domain.mobile_app_enums import (
    Role,
    UserResponsibility,
    DomainObject,
    Action,
    Scope,
)

from src.domain.mobile_app_types import (
    PermissionRule,
    RoleDefinition,
)

PROFESSIONAL_CAREGIVER_NON_CMS = RoleDefinition(
    role=Role.PROFESSIONAL_CAREGIVER_NON_CMS,
    name="Professional Caregiver",
    description="Paid caregiver using the mobile app for ADL capture, observation capture, review, and escalation.",
    responsibilities=(
        UserResponsibility.RECORD_ADL_ASSESSMENTS,
        UserResponsibility.RECORD_OBSERVATIONS,
        UserResponsibility.REVIEW_PATIENT_SUMMARY,
        UserResponsibility.REVIEW_PATIENT_HISTORY,
        UserResponsibility.IDENTIFY_TRENDS,
        UserResponsibility.ESCALATE_CONCERNS,
        UserResponsibility.CORRECT_RECENT_ENTRIES,
    ),
    permissions=(
        PermissionRule(DomainObject.ADL_ASSESSMENT, Action.CREATE, True),
        PermissionRule(DomainObject.ADL_ASSESSMENT, Action.VIEW, True),
        PermissionRule(DomainObject.ADL_ASSESSMENT, Action.CORRECT, True),
        PermissionRule(DomainObject.OBSERVATION, Action.CREATE, True),
        PermissionRule(DomainObject.OBSERVATION, Action.VIEW, True),
        PermissionRule(DomainObject.PATIENT_SUMMARY, Action.VIEW, True),
        PermissionRule(DomainObject.REVIEW_QUEUE, Action.VIEW, True),
        PermissionRule(DomainObject.ESCALATION, Action.CREATE, True),
        PermissionRule(DomainObject.HISTORY, Action.VIEW, True),
    ),
)

CMS_BILLING_PROVIDER = RoleDefinition(
    role=Role.CMS_BILLING_PROVIDER,
    name="CMS RTM Billing Provider",
    description="Clinical or qualified provider responsible for RTM review, documentation, and billing-supporting activity.",
    responsibilities=(
        UserResponsibility.REVIEW_PATIENT_SUMMARY,
        UserResponsibility.REVIEW_PATIENT_HISTORY,
        UserResponsibility.IDENTIFY_TRENDS,
        UserResponsibility.ESCALATE_CONCERNS,
        UserResponsibility.ACKNOWLEDGE_REVIEW_ITEMS,
        UserResponsibility.TRACK_RTM_TIME,
        UserResponsibility.SUPPORT_CLAIM_SUBMISSION,
    ),
    permissions=(
        PermissionRule(DomainObject.ADL_ASSESSMENT, Action.VIEW, True),
        PermissionRule(DomainObject.OBSERVATION, Action.VIEW, True),
        PermissionRule(DomainObject.PATIENT_SUMMARY, Action.VIEW, True),
        PermissionRule(DomainObject.REVIEW_QUEUE, Action.VIEW, True, Scope.ORGANIZATION),
        PermissionRule(DomainObject.ESCALATION, Action.CREATE, True),
        PermissionRule(DomainObject.ESCALATION, Action.ACKNOWLEDGE, True),
        PermissionRule(DomainObject.ESCALATION, Action.RESOLVE, True),
        PermissionRule(DomainObject.HISTORY, Action.VIEW, True),
        PermissionRule(DomainObject.RTM_BILLING_RECORD, Action.BILL, True, Scope.ORGANIZATION),
    ),
)

ROLE_DEFINITIONS: dict[Role, RoleDefinition] = {
    PROFESSIONAL_CAREGIVER_NON_CMS.role: PROFESSIONAL_CAREGIVER_NON_CMS,
    CMS_BILLING_PROVIDER.role: CMS_BILLING_PROVIDER,
}

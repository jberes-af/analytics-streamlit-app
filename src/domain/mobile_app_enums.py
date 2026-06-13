# /src/domain/mobile_app_enums.py


from enum import Enum

"""
USER
"""


class Role(str, Enum):
    INFORMAL_CAREGIVER = "informal_caregiver"
    PROFESSIONAL_CAREGIVER_NON_CMS = "non_cms_billing_professional"
    CMS_BILLING_PROVIDER = "cms_billing_provider"
    ADMIN = "admin"


class UserResponsibility(str, Enum):
    # Data capture
    RECORD_ADL_ASSESSMENTS = "Record ADL assessments"
    RECORD_OBSERVATIONS = "Record ADL observations"
    CONFIRM_OBSERVATION_TIME = "Confirm observation time"

    # Correction
    CORRECT_RECENT_ENTRIES = "Correct recent entries"

    # Documentation responsibilities (CRITICAL for CMS)
    DOCUMENT_CLINICAL_REVIEW = "Document clinical review"
    DOCUMENT_INTERVENTIONS = "Document interventions"
    ATTRIBUTE_ACTIONS_TO_PROVIDER = "Attribute actions to provider"

    # CMS-specific responsibilities
    MONITOR_ADHERENCE = "Monitor adherence"
    RESPOND_TO_ALERTS = "Respond to alerts"
    ENGAGE_WITH_PATIENT = "Engage with patient"

    # CMS Billing / compliance responsibilities
    TRACK_TIME_FOR_RTM = "Track time for CMS"
    VERIFY_DATA_SOURCE_DEVICE = "Verify data source device"
    MAINTAIN_AUDIT_TRAIL = "Maintain audit trail"
    SUPPORT_CLAIM_SUBMISSION = "Support claim submission"

    # All caregivers
    IDENTIFY_TRENDS = "Identify trends"
    ESCALATE_CONCERNS = "Prioritize / Escalate concerns"

    # Light documentation (Non-CMS billing-grade)
    ADD_CONTEXTUAL_NOTES = "Add contextual notes"
    UPDATE_RECENT_ENTRIES = "Update recent entries"

    # Operational responsibilities
    FOLLOW_CARE_PROTOCOLS = "Follow protocols"
    INTERPRET_TRENDS = "Interpret trends"
    VALIDATE_CLINICAL_RELEVANCE = "Validate clinical relevance"

    # Review
    REVIEW_DAILY_SUMMARY = "Review daily summary"
    REVIEW_PRIOR_ENTRIES = "Review prior entries"
    REVIEW_PATIENT_DATA = "Review patient data"

    # Escalation / communication
    REPORT_CONCERNS = "Report concerns"
    RESPOND_TO_PROMPTS = "Respond to prompts"


"""
PERMISSIONS
"""


class DomainObject(str, Enum):
    ADL_ASSESSMENT = "adl_assessment"
    OBSERVATION = "observation"
    PATIENT_SUMMARY = "patient_summary"
    REVIEW_QUEUE = "review_queue"
    ESCALATION = "escalation"
    HISTORY = "history"
    CMS_BILLING_RECORD = "cms_billing_record"


class Action(str, Enum):
    VIEW = "view"
    CREATE = "create"
    READ = "read"
    UPDATE = "update"
    REVIEW = "review"
    CORRECT = "correct"
    SUBMIT_FOR_BILLING = "submit_for_billing"
    ESCALATE = "escalate"
    ACKNOWLEDGE = "acknowledge"
    RESOLVE = "resolve"


class Scope(str, Enum):
    OWN_ENTRIES = "own_entries"
    ASSIGNED_PATIENT = "assigned_patient"
    ASSIGNED_ORG = "assigned_org"


"""
USE CASES
"""


class UseCaseType(str, Enum):
    # --- Core caregiver actions ---
    CAPTURE = "capture"  # record structured or narrative data
    REVIEW = "review"  # view current state / summaries
    ANALYZE = "analyze"  # interpret trends, patterns
    ESCALATE = "escalate"  # raise concern / notify others

    # --- Data quality / documentation ---
    CORRECT = "correct"  # fix or update prior data
    DOCUMENT = "document"  # add supporting context (notes)

    # --- Workflow state management ---
    ACKNOWLEDGE = "acknowledge"  # mark as seen/reviewed
    COMPLETE = "complete"  # fulfill required task

    # --- System / background ---
    SYSTEM = "system"  # auto-generated (alerts, signals)


"""
WORKFLOWS
"""


class WorkflowComplexity(str, Enum):
    L1 = "L1"
    L2 = "L2"
    L3 = "L3"


class Severity(str, Enum):
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"

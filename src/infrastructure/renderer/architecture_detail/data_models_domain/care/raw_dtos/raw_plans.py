# /raw_plans.py

CARE_PLAN_TYPE_ENUM: str = """
class CarePlanTypeEnum(StrEnum):
    CARE_PLAN = "Care Plan"
    THERAPY_PLAN = "Therapy Plan"
"""

PLAN_STATUS_ENUM: str = """
class PlanStatusEnum(StrEnum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"
    DISCONTINUED = "Discontinued"
    REPLACED = "Replaced"
"""

PROGRESS_STATUS_ENUM: str = """
class ProgressStatusEnum(StrEnum):
    ON_TRACK = "On Track"
    AT_RISK = "At Risk"
    OFF_TRACK = "Off Track"
    COMPLETED = "Completed"
"""

SESSION_NOTE_DTO: str = """
@dataclass(frozen=True)
class SessionNoteDTO:
    note_id: str
    plan_id: str
    author_user_id: str
    note_type: str
    note_text: str
    created_at: str
"""

PLAN_ACTION_DTO: str = """
@dataclass(frozen=True)
class PlanActionDTO:
    action_id: str
    title: str
    description: str
    category: str
    frequency: str
    assigned_role: str
    start_date: str
    end_date: str | None
    is_required: bool
"""

PLAN_MILESTONE_DTO: str = """
@dataclass(frozen=True)
class PlanMilestoneDTO:
    milestone_id: str
    description: str
    date: str
    expected_outcome_metric: str
"""

PLAN_SCHEDULE_DTO: str = """
@dataclass(frozen=True)
class PlanScheduleDTO:
    start_date: str
    end_date: str
    review_frequency: str
"""

PLAN_METRIC_DTO: str = """
@dataclass(frozen=True)
class PlanMetricDTO:
    metric_id: str
    name: str
    unit: str
    source: str
    sensor_id: str | None = None
"""

PLAN_PROGRESS_ENTRY_DTO: str = """
@dataclass(frozen=True)
class PlanProgressEntryDTO:
    progress_id: str
    metric_id: str
    target_value: float
    actual_value: float
    status: ProgressStatusEnum
    timestamp: str
    notes: str | None = None
"""

PLAN_REVIEW_DTO: str = """
@dataclass(frozen=True)
class PlanReviewDTO:
    review_id: str
    reviewed_by_user_id: str
    review_date: str
    summary: str
    changes_needed: bool
    next_review_date: str
"""

PLAN_RECORD_DTO: str = """
@dataclass(frozen=True)
class PlanRecordDTO:
    plan_id: str
    resident_id: str
    plan_type: CarePlanTypeEnum
    title: str
    problem: str
    baseline_status: str
    goal_description: str
    actions: tuple[PlanActionDTO, ...]
    metrics: tuple[PlanMetricDTO, ...]
    milestones: tuple[PlanMilestoneDTO, ...]
    progress_entries: tuple[PlanProgressEntryDTO, ...]
    session_notes: tuple[SessionNoteDTO, ...]
    plan_schedule: PlanScheduleDTO
    plan_status: PlanStatusEnum
    created_at: str
    updated_at: str
"""

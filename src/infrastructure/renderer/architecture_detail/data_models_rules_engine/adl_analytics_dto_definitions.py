# /adl_analytics_dto_definitions.py


ADL_CORRECTION_REASON_ENUM: str = """
class AdlWindowType(StrEnum):
    CURRENT_DAY = "current_day"
    PREVIOUS_DAY = "previous_day"
    CURRENT_7D = "current_7d"
    PREVIOUS_7D = "previous_7d"
    CURRENT_14D = "current_14d"
    PREVIOUS_14D = "previous_14d"
    CURRENT_30D = "current_30d"
    PREVIOUS_30D = "previous_30d"
    BASELINE = "baseline"
"""

SIGNAL_DIRECTION_ENUM: str = """
class SignalDirection(StrEnum):
    POSITIVE = "positive"
    NEGATIVE = "negative"
    NEUTRAL = "neutral"
"""

DECISION_TYPE_ENUM: str = """
class DecisionType(StrEnum):
    NO_ACTION = "no_action"
    LOG_ONLY = "log_only"
    MONITOR = "monitor"
    NOTIFY = "notify"
    REVIEW = "review"
    ESCALATE = "escalate"
"""

DECISION_STATUS_ENUM: str = """
class DecisionStatus(StrEnum):
    READY = "ready"
    INSUFFICIENT_DATA = "insufficient_data"
    SUPPRESSED = "suppressed"
    ERROR = "error"
from enum import StrEnum
"""

ADL_PERIOD_SUMMARY_DTO: str = """
@dataclass(frozen=True)
class AdlPeriodSummaryDTO:
    patient_id: str
    adl_code: str
    window_type: AdlWindowType
    start_date_iso: str
    end_date_iso: str
    mean_score: float | None
    median_score: float | None
    mode_score: int | None
    min_score: int | None
    max_score: int | None
    latest_score: int | None
    worst_score: int | None
    assessment_count: int
    days_observed: int
    expected_days: int
    completeness_pct: float
"""

ADL_COMPARISON_DTO: str = """
@dataclass(frozen=True)
class AdlComparisonDTO:
    patient_id: str
    adl_code: str
    current_window: AdlWindowType
    comparison_window: AdlWindowType
    current_mean_score: float | None
    comparison_mean_score: float | None
    delta_score: float | None
    pct_change: float | None
    current_worst_score: int | None
    comparison_worst_score: int | None
    current_assessment_count: int
    comparison_assessment_count: int
    direction: SignalDirection
    severity: SignalSeverity
    status: DecisionStatus
    explanation: str
"""

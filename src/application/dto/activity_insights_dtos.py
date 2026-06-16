# /src/application/dto/activity_insights_dtos.py

from dataclasses import dataclass
from datetime import date


"""
@dataclass(frozen=True)
class ActivityInsightDTO:
    insight_id: str
    sensor_id: str | None
    title: str
    message: str
    severity: str  # "info", "warning", "critical"
    start_date: date
    end_date: date
    metric_name: str
    current_value: float | None = None
    comparison_value: float | None = None
    change_percent: float | None = None
"""



@dataclass(frozen=True)
class ActivityInsightDTO:
    sensor_id: str | None
    message_line_1: str
    end_date: date
    metric_name: str
    current_value: float | None = None
    change_percent: float | None = None
    message_header: str | None = None
    section_header: str | None = None
    message_line_2: str | None = None


@dataclass(frozen=True)
class ActivityInsightsDTO:
    weekly_activity_insights: list[ActivityInsightDTO]
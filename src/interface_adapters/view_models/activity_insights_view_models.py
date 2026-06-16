# src/interface_adapters/view_models/activity_insights_view_models.py

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class ActivityInsightViewModel:
    sensor_id: str | None
    message_line_1: str
    end_date: date
    end_date_label: str
    metric_name: str
    current_value: float | None
    current_value_label: str
    change_percent: float | None
    change_percent_label: str
    message_header: str | None = None
    section_header: str | None = None
    message_line_2: str | None = None


@dataclass(frozen=True)
class ActivityInsightsViewModel:
    weekly_activity_insights: list[ActivityInsightViewModel]
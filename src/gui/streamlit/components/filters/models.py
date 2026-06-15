# /src/gui/streamlit/components/filters/models.py

from dataclasses import dataclass
from datetime import date


@dataclass
class AnalysisFilters:
    start_date: date
    end_date: date
    selected_sensor_ids: list[str]
    run_analysis: bool
    is_valid: bool
    local_timezone: str

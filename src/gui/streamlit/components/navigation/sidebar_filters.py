# /src/gui/streamlit/components/navigation/sidebar_filters.py

from dataclasses import dataclass
from datetime import date


@dataclass
class SidebarFilters:
    start_date: date
    end_date: date
    sensor_ids: list[str]


def render_sidebar(
    available_sensor_ids: list[str],
) -> SidebarFilters:
    ...
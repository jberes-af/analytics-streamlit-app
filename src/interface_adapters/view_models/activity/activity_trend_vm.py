# /src/interface_adapters/view_models/activity/activity_trend_vm.py

from dataclasses import dataclass

from src.interface_adapters.view_models.table_view_model import TableColumnVM


@dataclass(frozen=True)
class ActivityTrendRowVM:
    sensor_id: str
    metric_name: str

    start_date: str
    end_date: str
    period_label: str

    direction: str
    direction_label: str

    slope_per_day: float
    slope_per_day_label: str

    intercept: float
    intercept_label: str


@dataclass(frozen=True)
class ActivityTrendSensorGroupVM:
    sensor_id: str
    title: str
    rows: list[ActivityTrendRowVM]


@dataclass(frozen=True)
class ActivityTrendViewModel:
    title: str
    subtitle: str

    columns: list[TableColumnVM]
    sensor_groups: list[ActivityTrendSensorGroupVM]

    has_data: bool
    empty_message: str | None


ACTIVITY_TREND_COLUMNS = [
    TableColumnVM(key="period_label", label="Period"),
    TableColumnVM(key="direction_label", label="Direction"),
    TableColumnVM(key="slope_per_day_label", label="Slope / Day"),
    TableColumnVM(key="intercept_label", label="Intercept"),
]

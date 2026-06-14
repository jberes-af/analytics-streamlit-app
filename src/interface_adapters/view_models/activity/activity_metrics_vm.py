# /src/interface_adapters/view_models/activity_metrics_vm.py

from dataclasses import dataclass

from src.interface_adapters.view_models.table_view_model import TableColumnVM

"""
ROW OR DATAPOINT VIEW MODELS
"""


@dataclass(frozen=True)
class DailyActivityRowVM:
    date: str
    total_activations: int
    total_activations_label: str
    first_activation: str
    last_activation: str
    active_day_length: str


@dataclass(frozen=True)
class SensorActivityRowVM:
    sensor_id: str
    total_activations: int
    total_activations_label: str
    percentage_of_total: float
    percentage_of_total_label: str


@dataclass(frozen=True)
class HourlyActivityPointVM:
    date: str
    hour: int
    hour_label: str
    activation_count: int
    activation_count_label: str


@dataclass(frozen=True)
class RollingActivityPointVM:
    window_start: str
    window_end: str
    window_label: str
    activation_count: int
    activation_count_label: str


@dataclass(frozen=True)
class PeakActivityRowVM:
    rank: int
    rank_label: str
    window_start: str
    window_end: str
    window_label: str
    activation_count: int
    activation_count_label: str


@dataclass(frozen=True)
class InactivityPeriodRowVM:
    start_time: str
    end_time: str
    period_label: str
    duration_seconds: int
    duration_label: str


"""
PRESENTER VIEW MODELS
"""


@dataclass(frozen=True)
class DailyActivityViewModel:
    title: str
    columns: list[TableColumnVM]
    rows: list[DailyActivityRowVM]


@dataclass(frozen=True)
class SensorActivityViewModel:
    title: str
    columns: list[TableColumnVM]
    rows: list[SensorActivityRowVM]


@dataclass(frozen=True)
class HourlyActivityViewModel:
    title: str
    columns: list[TableColumnVM]
    rows: list[HourlyActivityPointVM]


@dataclass(frozen=True)
class RollingActivityViewModel:
    title: str
    columns: list[TableColumnVM]
    rows: list[RollingActivityPointVM]


@dataclass(frozen=True)
class PeakActivityViewModel:
    title: str
    columns: list[TableColumnVM]
    rows: list[PeakActivityRowVM]


@dataclass(frozen=True)
class InactivityPeriodsViewModel:
    title: str
    columns: list[TableColumnVM]
    rows: list[InactivityPeriodRowVM]


@dataclass(frozen=True)
class ActivityDistributionViewModel:
    title: str
    entropy: float
    entropy_label: str
    most_active_hour: int | None
    most_active_hour_label: str
    least_active_hour: int | None
    least_active_hour_label: str


"""
ORCHESTRATOR VIEW MODEL
"""


@dataclass(frozen=True)
class ActivityAnalysisViewModel:
    title: str
    subtitle: str
    summary_text: str

    # user_id: str
    date_range: str

    daily_activity: DailyActivityViewModel
    sensor_activity: SensorActivityViewModel
    hourly_activity: HourlyActivityViewModel
    rolling_activity: RollingActivityViewModel
    peak_activity: PeakActivityViewModel
    inactivity_periods: InactivityPeriodsViewModel
    activity_distribution: ActivityDistributionViewModel

    has_data: bool
    empty_message: str | None


"""
COLUMN HEADINGS
"""

DAILY_ACTIVITY_COLUMNS = [
    TableColumnVM(key="date", label="Date"),
    TableColumnVM(key="total_activations_label", label="Total Activations"),
    TableColumnVM(key="first_activation", label="First Activation"),
    TableColumnVM(key="last_activation", label="Last Activation"),
    TableColumnVM(key="active_day_length", label="Active Day Length"),
]

SENSOR_ACTIVITY_COLUMNS = [
    TableColumnVM(key="sensor_id", label="Sensor ID"),
    TableColumnVM(key="total_activations_label", label="Total Activations"),
    TableColumnVM(key="percentage_of_total_label", label="Percentage of Total"),
]

HOURLY_ACTIVITY_COLUMNS = [
    TableColumnVM(key="date", label="Date"),
    TableColumnVM(key="hour_label", label="Hour"),
    TableColumnVM(key="activation_count_label", label="Activation Count"),
]

ROLLING_ACTIVITY_COLUMNS = [
    TableColumnVM(key="window_start", label="Start Time"),
    TableColumnVM(key="window_end", label="End Time"),
    TableColumnVM(key="activation_count_label", label="Activation Count"),
]

PEAK_ACTIVITY_COLUMNS = [
    TableColumnVM(key="rank_label", label="Rank"),
    TableColumnVM(key="window_label", label="Peak Window"),
    TableColumnVM(key="activation_count_label", label="Activation Count"),
]

INACTIVITY_PERIOD_COLUMNS = [
    TableColumnVM(key="period_label", label="Inactivity Period"),
    TableColumnVM(key="duration_label", label="Duration"),
]

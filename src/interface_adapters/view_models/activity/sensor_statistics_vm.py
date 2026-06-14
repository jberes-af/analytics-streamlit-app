# /src/interface_adapters/view_models/activity/sensor_statistics_vm.py

from dataclasses import dataclass

from src.interface_adapters.view_models.table_view_model import TableColumnVM


@dataclass(frozen=True)
class SensorTimePeriodStatisticsRowVM:
    sensor_id: str

    start_date: str
    end_date: str
    date_range_label: str
    days_in_period: int
    days_in_period_label: str

    total_activation_count: int
    total_activation_count_label: str

    average_daily_activation_count: float
    average_daily_activation_count_label: str

    median_daily_activation_count: float
    median_daily_activation_count_label: str

    maximum_daily_activation: int
    maximum_daily_activation_label: str
    maximum_daily_activation_date: str

    minimum_daily_activation: int
    minimum_daily_activation_label: str
    minimum_daily_activation_date: str

    percentile_25_daily_activation_count: float
    percentile_25_daily_activation_count_label: str

    percentile_75_daily_activation_count: float
    percentile_75_daily_activation_count_label: str

    standard_deviation_daily_activations: float
    standard_deviation_daily_activations_label: str

    coefficient_variation: float
    coefficient_variation_label: str

    active_day_count: int
    active_day_count_label: str

    inactive_day_count: int
    inactive_day_count_label: str


@dataclass(frozen=True)
class SensorTimePeriodStatisticsViewModel:
    title: str
    subtitle: str
    columns: list[TableColumnVM]
    rows: list[SensorTimePeriodStatisticsRowVM]

    has_data: bool
    empty_message: str | None


SENSOR_TIME_PERIOD_STATISTICS_COLUMNS = [
    TableColumnVM(key="sensor_id", label="Sensor ID"),
    TableColumnVM(key="date_range_label", label="Period"),
    TableColumnVM(key="days_in_period_label", label="Days"),
    TableColumnVM(key="total_activation_count_label", label="Total Activations"),
    TableColumnVM(key="average_daily_activation_count_label", label="Avg / Day"),
    TableColumnVM(key="median_daily_activation_count_label", label="Median / Day"),
    TableColumnVM(key="maximum_daily_activation_label", label="Max Day"),
    TableColumnVM(key="maximum_daily_activation_date", label="Max Date"),
    TableColumnVM(key="minimum_daily_activation_label", label="Min Day"),
    TableColumnVM(key="minimum_daily_activation_date", label="Min Date"),
    TableColumnVM(key="percentile_25_daily_activation_count_label", label="25th %ile"),
    TableColumnVM(key="percentile_75_daily_activation_count_label", label="75th %ile"),
    TableColumnVM(key="standard_deviation_daily_activations_label", label="Std Dev"),
    TableColumnVM(key="coefficient_variation_label", label="CV"),
    TableColumnVM(key="active_day_count_label", label="Active Days"),
    TableColumnVM(key="inactive_day_count_label", label="Inactive Days"),
]

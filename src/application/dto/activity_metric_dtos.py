# /src/application/dto/activity_metric_dtos.py

from dataclasses import dataclass
from datetime import datetime, date, timedelta


@dataclass
class DailyActivityDTO:
    date: date
    total_activations: int
    first_activation: datetime | None
    last_activation: datetime | None
    active_day_length: timedelta | None
    # activity_rate_per_hour: float | None


@dataclass
class CombinedSensorActivityDTO:
    sensor_id: str
    total_activations: int
    percentage_of_total: float


@dataclass(frozen=True)
class SensorByIdByDateActivityDTO:
    date: date
    sensor_id: str
    activation_count: int


"""
@dataclass
class SensorActivityByDateByTimePeriodDTO:
    date: date
    time_start: time
    time_end: time
    sensor_id: str
    activation_count: int
"""


@dataclass
class HourlyActivityDTO:
    date: date
    hour: int
    activation_count: int


@dataclass
class RollingActivityDTO:
    window_start: datetime
    window_end: datetime
    activation_count: int


@dataclass
class PeakActivityDTO:
    window_start: datetime
    window_end: datetime
    activation_count: int
    rank: int


@dataclass
class InactivityPeriodDTO:
    start_time: datetime
    end_time: datetime
    duration: timedelta


@dataclass
class ActivityDistributionDTO:
    entropy: float
    most_active_hour: int | None
    least_active_hour: int | None


@dataclass(frozen=True)
class ActivityTrendDTO:
    metric_name: str
    slope_per_day: float
    intercept: float
    direction: str
    start_date: date
    end_date: date
    sensor_id: str | None = None


@dataclass
class SensorWeeklyActivityDTO:
    sensor_id: str
    week_start: date
    week_end: date
    total_activations_week: int
    maximum_daily_activations: int
    minimum_daily_activations: int
    average_daily_activations: float
    standard_deviation_daily_activations: float
    coefficient_variation: float
    change_percent: float | None


@dataclass
class ActivityMetricsCalculatorResultDTO:
    # user_id: str
    start_date: date
    end_date: date
    daily_activity: list[DailyActivityDTO]
    combined_sensor_activity: list[CombinedSensorActivityDTO]
    sensor_by_id_activity: list[SensorByIdByDateActivityDTO]
    hourly_activity: list[HourlyActivityDTO]
    rolling_activity: list[RollingActivityDTO]
    peak_activity: list[PeakActivityDTO]
    inactivity_periods: list[InactivityPeriodDTO]
    activity_distribution: ActivityDistributionDTO
    activity_trends_by_sensor_id: list[ActivityTrendDTO]
    weekly_activity_by_sensor_id: list[SensorWeeklyActivityDTO]

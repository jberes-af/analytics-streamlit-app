# /src/application/dto/activity_uc_dtos.py

from dataclasses import dataclass
from datetime import date, datetime

from src.domain.entities.sensor import SensorEvent

from src.application.dto.activity_metric_dtos import (
    ActivityDistributionDTO,
    FirstLastDailyActivityDTO,
    HourlyActivityAllSensorsDTO,
    HourlyActivityBySensorIdDTO,
    InactivityPeriodDTO,
    PeakActivityDTO,
    RollingActivityDTO,
    SensorActivityPercentOfTotalDTO,
    DailyActivityBySensorIdDTO,
    DailyActivityAllSensorsDTO,
    ActivityTrendDTO,
    SensorWeeklyActivityDTO,
    SensorTimePeriodStatisticsDTO,
)


@dataclass(frozen=True)
class ActivityAnalysisRequestDTO:
    # user_id: str
    start_time: datetime
    end_time: datetime
    # sensor_ids: tuple[str, ...]
    rolling_window: str
    rolling_frequency: str
    sensor_events: tuple[SensorEvent, ...]


@dataclass
class ActivityAnalysisResultDTO:
    # user_id: str
    start_date: date
    end_date: date

    daily_activity: list[FirstLastDailyActivityDTO]
    combined_sensor_activity: list[SensorActivityPercentOfTotalDTO]

    sensor_by_id_by_date_activity: list[DailyActivityBySensorIdDTO]
    all_sensors_by_date_activity: list[DailyActivityAllSensorsDTO]

    sensor_by_id_by_hour_activity: list[HourlyActivityBySensorIdDTO]
    all_sensors_by_hour_activity: list[HourlyActivityAllSensorsDTO]

    rolling_activity: list[RollingActivityDTO]
    peak_activity: list[PeakActivityDTO]
    inactivity_periods: list[InactivityPeriodDTO]
    activity_distribution: ActivityDistributionDTO
    sensor_activity_trends: list[ActivityTrendDTO]
    weekly_sensor_activity: list[SensorWeeklyActivityDTO]
    sensor_time_period_statistics: list[SensorTimePeriodStatisticsDTO]

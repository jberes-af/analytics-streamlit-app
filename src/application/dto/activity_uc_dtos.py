# /src/application/dto/activity_uc_dtos.py

from dataclasses import dataclass
from datetime import date, datetime

from src.domain.entities.sensor import SensorEvent

from src.application.dto.activity_metric_dtos import (
    ActivityDistributionDTO,
    DailyActivityDTO,
    HourlyActivityDTO,
    InactivityPeriodDTO,
    PeakActivityDTO,
    RollingActivityDTO,
    CombinedSensorActivityDTO,
    SensorByIdByDateActivityDTO,
    ActivityTrendDTO,
    SensorWeeklyActivityDTO,

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

    daily_activity: list[DailyActivityDTO]
    combined_sensor_activity: list[CombinedSensorActivityDTO]
    sensor_by_id_activity: list[SensorByIdByDateActivityDTO]
    hourly_activity: list[HourlyActivityDTO]
    rolling_activity: list[RollingActivityDTO]
    peak_activity: list[PeakActivityDTO]
    inactivity_periods: list[InactivityPeriodDTO]
    activity_distribution: ActivityDistributionDTO
    sensor_activity_trends: list[ActivityTrendDTO]
    weekly_sensor_activity: list[SensorWeeklyActivityDTO]

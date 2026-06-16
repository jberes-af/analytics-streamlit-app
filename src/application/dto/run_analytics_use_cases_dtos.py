# /src/application/dto/run_analytics_use_cases_dtos.py

from dataclasses import dataclass
from datetime import date

from src.application.dto.sensor_timeline_uc_dtos import (
    SensorEventTimelineResultDTO,
)
from src.domain.entities.sensor import SensorProfile

"""
from src.application.dto.movement_uc_dtos import (
    MovementAnalysisResultDTO,
)
"""

from src.application.dto.activity_uc_dtos import (
    ActivityAnalysisResultDTO,
)

from src.application.dto.insights_uc_dtos import (
    GenerateInsightsResultDTO,
)

@dataclass(frozen=True)
class RunAnalyticsUseCasesRequestDTO:
    sensor_ids: list[str]
    start_date: date
    end_date: date
    rolling_window: str
    rolling_frequency: str
    local_timezone: str  # e.g. America / New_York
    sensor_profiles: list[SensorProfile]


@dataclass(frozen=True)
class RunAnalyticsUseCasesResultDTO:
    run_request: RunAnalyticsUseCasesRequestDTO
    build_sensor_timeline_result: SensorEventTimelineResultDTO
    analyze_activity_result: ActivityAnalysisResultDTO
    # analyze_movements_result: MovementAnalysisResultDTO
    generate_insights_result: GenerateInsightsResultDTO

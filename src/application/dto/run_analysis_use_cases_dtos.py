# /src/application/dto/run_analysis_use_cases_dtos.py

from dataclasses import dataclass
from datetime import date

from src.application.dto.sensor_timeline_uc_dtos import (
    SensorEventTimelineResultDTO,
)

"""
from src.application.dto.movement_uc_dtos import (
    MovementAnalysisResultDTO,
)
"""

from src.application.dto.activity_uc_dtos import (
    ActivityAnalysisResultDTO,
)


@dataclass(frozen=True)
class RunAnalysisUseCasesRequestDTO:
    sensor_ids: list[str]
    start_date: date
    end_date: date
    rolling_window: str
    rolling_frequency: str
    local_timezone: str  # e.g. America / New_York
    # path_results: Path


@dataclass(frozen=True)
class RunAnalysisUseCasesResultDTO:
    run_request: RunAnalysisUseCasesRequestDTO
    build_sensor_timeline_result: SensorEventTimelineResultDTO
    analyze_activity_result: ActivityAnalysisResultDTO
    # analyze_movements_result: MovementAnalysisResultDTO

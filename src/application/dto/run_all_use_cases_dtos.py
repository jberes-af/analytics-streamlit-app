# /src/application/dto/run_all_use_cases_dtos.py

from dataclasses import dataclass
from datetime import date
from pathlib import Path

from src.application.dto.sensor_timeline_uc_dtos import (
    SensorEventTimelineResultDTO,
)

from src.application.dto.movement_uc_dtos import (
    MovementAnalysisResultDTO,
)

from src.application.dto.activity_uc_dtos import (
    ActivityAnalysisResultDTO,
)


@dataclass(frozen=True)
class RunAllUseCasesRequestDTO:
    scenario_id: str
    user_reference: str
    user_id: str
    start_date: date
    end_date: date
    rolling_window: str
    rolling_frequency: str
    path_results: Path


@dataclass(frozen=True)
class RunAllUseCasesResultDTO:
    run_all_request: RunAllUseCasesRequestDTO
    build_sensor_timeline_result: SensorEventTimelineResultDTO
    analyze_movements_result: MovementAnalysisResultDTO
    analyze_activity_result: ActivityAnalysisResultDTO

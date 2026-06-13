# /src/application/dto/run_startup_use_cases_dtos.py

from dataclasses import dataclass

from src.application.dto.sensor_by_user_uc_dtos import (
    SensorByUserResultDTO,
)


@dataclass(frozen=True)
class RunStartupUseCasesRequestDTO:
    user_id: str
    # scenario_id: str | None = None
    # user_reference: str | None = None


@dataclass(frozen=True)
class RunStartupUseCasesResultDTO:
    run_startup_request: RunStartupUseCasesRequestDTO
    lookup_sensor_by_user_result: SensorByUserResultDTO

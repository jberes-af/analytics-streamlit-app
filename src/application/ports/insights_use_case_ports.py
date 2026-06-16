# /src/application/ports/insights_use_case_ports.py

from typing import Protocol

from src.domain.entities.sensor import SensorProfile
from src.application.dto.activity_uc_dtos import ActivityAnalysisResultDTO
from src.application.dto.activity_insights_dtos import ActivityInsightsDTO


class ActivityInsightsGeneratorPort(Protocol):
    def generate(
            self,
            sensor_ids: list[str],
            sensor_profiles: list[SensorProfile],
            analysis_results: ActivityAnalysisResultDTO,
    ) ->  ActivityInsightsDTO:
        ...

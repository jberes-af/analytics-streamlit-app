# /src/application/dto/insights_uc_dtos.py

from dataclasses import dataclass

from src.domain.entities.sensor import SensorProfile

from src.application.dto.activity_uc_dtos import ActivityAnalysisResultDTO

from src.application.dto.activity_insights_dtos import ActivityInsightsDTO


@dataclass(frozen=True)
class GenerateInsightsRequestDTO:
    sensor_ids: list[str]
    sensor_profiles: list[SensorProfile]
    analyze_activity_result: ActivityAnalysisResultDTO


@dataclass(frozen=True)
class GenerateInsightsResultDTO:
    insights: ActivityInsightsDTO

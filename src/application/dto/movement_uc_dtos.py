# /src/application/dto/run_all_use_cases_dtos.py

from dataclasses import dataclass
from datetime import date

from src.domain.entities.sensor import SensorEvent

from src.domain.services.movement_analysis.time_bucket_comparator import TimeBucketComparisonResult


@dataclass(frozen=True)
class MovementAnalysisRequestDTO:
    scenario_id: str
    user_reference: str
    user_id: str
    # start_date: date
    # end_date: date
    # sensor_ids: tuple[str, ...]
    sensor_events: tuple[SensorEvent, ...]


@dataclass(frozen=True)
class MovementAnalysisResultDTO:
    scenario_id: str
    user_reference: str
    user_id: str
    # start_date: date
    # end_date: date
    # sensor_ids: list[str]
    # collapsed_events: list[SensorEvent]
    sequence_counts: dict
    transition_probabilities: dict
    time_bucket_comparison: TimeBucketComparisonResult | None

# /src/application/ports/activity_use_case_ports.py

from datetime import datetime
from typing import Protocol

from src.domain.entities.sensor import SensorEvent

from src.application.dto.activity_metric_dtos import (
    ActivityMetricsCalculatorResultDTO,
)


"""
class SensorEventRepositoryPort(Protocol):
    def get_events(
            self,
            user_id: str,
            start_time: datetime,
            end_time: datetime,
    ) -> list[SensorEvent]:
        ...
"""

class ActivityMetricsCalculatorPort(Protocol):
    def calculate(
            self,
            user_id: str,
            start_time: datetime,
            end_time: datetime,
            events: list[SensorEvent],
    ) -> ActivityMetricsCalculatorResultDTO:
        ...

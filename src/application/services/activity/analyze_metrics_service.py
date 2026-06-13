# /src/application/services/analyze_metrics_service.py

"""
Application service that delegates metric calculation to a calculator port.

This service owns the application meaning:
    "calculate activity metrics"

The infrastructure implementation owns the technical details:
    pandas, SQL, Polars, Spark, etc.
"""

from datetime import datetime

from src.domain.entities.sensor import SensorEvent

from src.application.dto.activity_metric_dtos import (
    ActivityMetricsCalculatorResultDTO,
)

from src.application.ports.activity_use_case_ports import (
    ActivityMetricsCalculatorPort,
)


class ActivityMetricsService:

    def __init__(
            self,
            calculator: ActivityMetricsCalculatorPort,
    ) -> None:
        self.calculator = calculator

    def calculate_activity_metrics(
            self,
            user_id: str,
            start_time: datetime,
            end_time: datetime,
            events: list[SensorEvent],
    ) -> ActivityMetricsCalculatorResultDTO:
        return self.calculator.calculate(
            user_id=user_id,
            start_time=start_time,
            end_time=end_time,
            events=events,
        )

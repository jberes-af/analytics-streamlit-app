# /src/application/use_cases/analyze_activity_levels_use_case.py

from src.domain.entities.sensor import SensorEvent

from src.application.services.activity.analyze_metrics_service import (
    ActivityMetricsService,
)

from src.application.dto.activity_uc_dtos import (
    ActivityAnalysisRequestDTO,
    ActivityAnalysisResultDTO,
)


class AnalyzeActivityLevelsUseCase:
    def __init__(
            self,
            activity_metrics_service: ActivityMetricsService,
    ) -> None:
        self.activity_metrics_service = activity_metrics_service

    def execute(
            self,
            request: ActivityAnalysisRequestDTO,
    ) -> ActivityAnalysisResultDTO | None:
        events: list[SensorEvent] = list(request.sensor_events)

        result = self.activity_metrics_service.calculate_activity_metrics(
            user_id=request.user_id,
            start_time=request.start_time,
            end_time=request.end_time,
            events=events,
        )

        return ActivityAnalysisResultDTO(
            user_id=request.user_id,
            start_date=request.start_time,
            end_date=request.end_time,
            daily_activity=result.daily_activity,
            combined_sensor_activity=result.combined_sensor_activity,
            sensor_by_id_activity=result.sensor_by_id_activity,
            hourly_activity=result.hourly_activity,
            rolling_activity=result.rolling_activity,
            peak_activity=result.peak_activity,
            inactivity_periods=result.inactivity_periods,
            activity_distribution=result.activity_distribution,
            sensor_activity_trends=result.activity_trends_by_sensor_id,
            weekly_sensor_activity=result.weekly_activity_by_sensor_id,
        )

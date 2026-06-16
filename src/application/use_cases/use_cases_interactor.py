# /src/application/use_cases/use_cases_interactor.py


from typing import Protocol

from src.application.dto.run_startup_use_cases_dtos import (
    RunStartupUseCasesRequestDTO,
    RunStartupUseCasesResultDTO,
)

from src.application.dto.run_analytics_use_cases_dtos import (
    RunAnalyticsUseCasesRequestDTO,
    RunAnalyticsUseCasesResultDTO,
)

from src.application.dto.sensor_by_user_uc_dtos import (
    SensorByUserRequestDTO,
    SensorByUserResultDTO,
)

from src.application.dto.sensor_timeline_uc_dtos import (
    SensorEventTimelineRequestDTO,
    SensorEventTimelineResultDTO,
)

"""
from src.application.dto.movement_uc_dtos import (
    MovementAnalysisRequestDTO,
    MovementAnalysisResultDTO,
)
"""

from src.application.dto.activity_uc_dtos import (
    ActivityAnalysisRequestDTO,
    ActivityAnalysisResultDTO,
)

from src.application.dto.insights_uc_dtos import (
    GenerateInsightsRequestDTO,
    GenerateInsightsResultDTO,
)

import logging

logger = logging.getLogger(__name__)

"""
USE CASE INTERACTOR
"""


class LookupSensorByUserInteractor(Protocol):
    def execute(
            self,
            request: SensorByUserRequestDTO,
    ) -> SensorByUserResultDTO:
        ...


class BuildSensorEventTimelineInteractor(Protocol):
    def execute(
            self,
            request: SensorEventTimelineRequestDTO,
    ) -> SensorEventTimelineResultDTO:
        ...


"""
class AnalyzeMovementPatternsInteractor(Protocol):
    def execute(
            self,
            request: MovementAnalysisRequestDTO,
    ) -> MovementAnalysisResultDTO:
        ...
"""


class AnalyzeActivityLevelsInteractor(Protocol):
    def execute(
            self,
            request: ActivityAnalysisRequestDTO,
    ) -> ActivityAnalysisResultDTO:
        ...


class GenerateInsightsInteractor(Protocol):
    def execute(
            self,
            request: GenerateInsightsRequestDTO,
    ) -> GenerateInsightsResultDTO:
        ...


class RunStartupUseCasesInteractor(Protocol):
    def __init__(
            self,
            lookup_sensor_by_user_use_case: LookupSensorByUserInteractor,
    ) -> None:
        self._lookup_sensor_uc = lookup_sensor_by_user_use_case

    def execute(
            self,
            request: RunStartupUseCasesRequestDTO,
    ) -> RunStartupUseCasesResultDTO:
        lookup_sensor_by_user_result: SensorByUserResultDTO = (
            self._lookup_sensor_by_user(
                request=request,
            ))

        return RunStartupUseCasesResultDTO(
            run_startup_request=request,
            lookup_sensor_by_user_result=lookup_sensor_by_user_result,
        )

    def _lookup_sensor_by_user(
            self,
            request: RunStartupUseCasesRequestDTO,
    ) -> SensorByUserResultDTO:
        logger.info("Looking-up sensor(s) by user...")

        request = SensorByUserRequestDTO(
            user_id=request.user_id,
        )

        result: SensorByUserResultDTO = (
            self._lookup_sensor_uc.execute(request))

        logger.info("... sensor by user lookup complete.")
        return result


class RunAnalyticsUseCasesInteractor(Protocol):
    def __init__(
            self,
            build_sensor_event_timeline_use_case: BuildSensorEventTimelineInteractor,
            analyze_activity_use_case: AnalyzeActivityLevelsInteractor,
            generate_insights_use_case: GenerateInsightsInteractor,
    ) -> None:
        self._build_sensor_timeline_uc = build_sensor_event_timeline_use_case
        self._analyze_activity_uc = analyze_activity_use_case
        self._generate_insights_uc = generate_insights_use_case

    def execute(
            self,
            request: RunAnalyticsUseCasesRequestDTO,
    ) -> RunAnalyticsUseCasesResultDTO:
        build_sensor_timeline_result: SensorEventTimelineResultDTO = (
            self._build_sensor_timeline(request))

        analyze_activity_result: ActivityAnalysisResultDTO = (
            self._analyze_activity(
                request,
                build_sensor_timeline_result,
            ))

        generate_insights_result: GenerateInsightsResultDTO = (
            self._generate_insights(
                request,
                analyze_activity_result,
            ))
        return RunAnalyticsUseCasesResultDTO(
            run_request=request,
            build_sensor_timeline_result=build_sensor_timeline_result,
            analyze_activity_result=analyze_activity_result,
            generate_insights_result=generate_insights_result,
        )

    def _generate_insights(
            self,
            request: RunAnalyticsUseCasesRequestDTO,
            analyze_activity_result: ActivityAnalysisResultDTO,
    ) -> GenerateInsightsResultDTO:
        logger.info("Generating insights use case...")
        request = GenerateInsightsRequestDTO(
            sensor_ids=request.sensor_ids,
            sensor_profiles=request.sensor_profiles,
            analyze_activity_result=analyze_activity_result,
        )

        result: GenerateInsightsResultDTO = (
            self._generate_insights_uc.execute(request))

        logger.info("... insights generated.")
        return result

    def _build_sensor_timeline(
            self,
            request: RunAnalyticsUseCasesRequestDTO,
    ) -> SensorEventTimelineResultDTO:
        logger.info("Building sensor timeline use case...")

        request = SensorEventTimelineRequestDTO(
            sensor_ids=request.sensor_ids,
            start_date=request.start_date,
            end_date=request.end_date,
            local_timezone=request.local_timezone,
        )

        result: SensorEventTimelineResultDTO = (
            self._build_sensor_timeline_uc.execute(request))

        logger.info("... sensor timeline built.")
        return result

    def _analyze_activity(
            self,
            request: RunAnalyticsUseCasesRequestDTO,
            sensor_events_timeline: SensorEventTimelineResultDTO,
    ) -> ActivityAnalysisResultDTO:
        logger.info("Analyzing activity use case...")

        request = ActivityAnalysisRequestDTO(
            start_time=sensor_events_timeline.start_time,
            end_time=sensor_events_timeline.end_time,
            rolling_window=request.rolling_window,
            rolling_frequency=request.rolling_frequency,
            sensor_events=tuple(sensor_events_timeline.collapsed_events),
        )

        result: ActivityAnalysisResultDTO = (
            self._analyze_activity_uc.execute(request))

        logger.info("... activity analysis complete.")
        return result

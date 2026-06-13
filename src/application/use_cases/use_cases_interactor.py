# /src/application/use_cases/use_cases_interactor.py


from typing import Protocol

from src.application.dto.run_startup_use_cases_dtos import (
    RunStartupUseCasesRequestDTO,
    RunStartupUseCasesResultDTO,
)

from src.application.dto.run_all_use_cases_dtos import (
    RunAllUseCasesRequestDTO,
    RunAllUseCasesResultDTO,
)

from src.application.dto.sensor_by_user_uc_dtos import (
    SensorByUserRequestDTO,
    SensorByUserResultDTO,
)

from src.application.dto.sensor_timeline_uc_dtos import (
    SensorEventTimelineRequestDTO,
    SensorEventTimelineResultDTO,
)

from src.application.dto.movement_uc_dtos import (
    MovementAnalysisRequestDTO,
    MovementAnalysisResultDTO,
)

from src.application.dto.activity_uc_dtos import (
    ActivityAnalysisRequestDTO,
    ActivityAnalysisResultDTO,
)

import logging

logger = logging.getLogger(__name__)


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


class AnalyzeMovementPatternsInteractor(Protocol):
    def execute(
            self,
            request: MovementAnalysisRequestDTO,
    ) -> MovementAnalysisResultDTO:
        ...


class AnalyzeActivityLevelsInteractor(Protocol):
    def execute(
            self,
            request: ActivityAnalysisRequestDTO,
    ) -> ActivityAnalysisResultDTO:
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


class RunAllUseCasesInteractor(Protocol):
    def __init__(
            self,
            analyze_movements_use_case: AnalyzeMovementPatternsInteractor,
            analyze_activity_use_case: AnalyzeActivityLevelsInteractor,
            build_sensor_event_timeline_use_case: BuildSensorEventTimelineInteractor,
    ) -> None:
        self._analyze_movements_uc = analyze_movements_use_case
        self._analyze_activity_uc = analyze_activity_use_case
        self._build_sensor_timeline_uc = build_sensor_event_timeline_use_case

    def execute(
            self,
            request: RunAllUseCasesRequestDTO,
    ) -> RunAllUseCasesResultDTO:
        build_sensor_timeline_result: SensorEventTimelineResultDTO = (
            self._build_sensor_timeline(request))

        analyze_activity_result: ActivityAnalysisResultDTO = (
            self._analyze_activity(
                request,
                build_sensor_timeline_result,
            ))

        analyze_movements_result: MovementAnalysisResultDTO = (
            self._analyze_movements(
                request,
                build_sensor_timeline_result,
            ))

        return RunAllUseCasesResultDTO(
            run_all_request=request,
            build_sensor_timeline_result=build_sensor_timeline_result,
            analyze_movements_result=analyze_movements_result,
            analyze_activity_result=analyze_activity_result,
        )

    def _build_sensor_timeline(
            self,
            request: RunAllUseCasesRequestDTO,
    ) -> SensorEventTimelineResultDTO:
        # Result: user_id, start & end dates, sensor IDs, "collapsed" sensor events
        logger.info("Building sensor timeline use case...")

        request = SensorEventTimelineRequestDTO(
            user_id=request.user_id,
            start_date=request.start_date,
            end_date=request.end_date,
        )

        result: SensorEventTimelineResultDTO = (
            self._build_sensor_timeline_uc.execute(request))

        logger.info("... sensor timeline built.")
        return result

    def _analyze_activity(
            self,
            request: RunAllUseCasesRequestDTO,
            sensor_events_timeline: SensorEventTimelineResultDTO,
    ) -> ActivityAnalysisResultDTO:
        logger.info("Analyzing activity use case...")

        request = ActivityAnalysisRequestDTO(
            user_id=request.user_id,
            start_time=sensor_events_timeline.start_time,
            end_time=sensor_events_timeline.end_time,
            # sensor_ids=tuple(sensor_events_timeline.sensor_ids),
            sensor_events=tuple(sensor_events_timeline.collapsed_events),
        )

        result: ActivityAnalysisResultDTO = (
            self._analyze_activity_uc.execute(request))

        logger.info("... activity analysis complete.")
        return result

    def _analyze_movements(
            self,
            request: RunAllUseCasesRequestDTO,
            sensor_events_timeline: SensorEventTimelineResultDTO,
    ) -> MovementAnalysisResultDTO:
        logger.info("Analyzing movement analysis use case...")

        request = MovementAnalysisRequestDTO(
            scenario_id=request.scenario_id,
            user_reference=request.user_reference,
            user_id=request.user_id,
            # start_date=request.start_date,
            # end_date=request.end_date,
            # sensor_ids=tuple(sensor_events_timeline.sensor_ids),
            sensor_events=tuple(sensor_events_timeline.collapsed_events),
        )

        result: MovementAnalysisResultDTO = (
            self._analyze_movements_uc.execute(request))

        logger.info("... movement analysis complete.")
        return result

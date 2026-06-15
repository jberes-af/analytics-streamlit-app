# /src/application/use_cases/analyze_movement_patterns_use_case.py

from collections import Counter
from datetime import datetime
from typing import Any

from src.domain.entities.sensor import SensorEvent

from src.domain.entities.movement_session import MovementSession

from src.domain.services.movement_analysis.sessionizer import Sessionizer

from src.domain.services.movement_analysis.sequence_counter import SequenceCounter

from src.domain.services.movement_analysis.transition_probability_calculator import (
    TransitionProbabilityCalculator,
)

from src.domain.services.movement_analysis.time_bucket_comparator import (
    TimeBucketComparator,
    TimeBucketComparisonResult,
)

from src.application.dto.movement_uc_dtos import (
    MovementAnalysisRequestDTO,
    MovementAnalysisResultDTO,
)


class AnalyzeMovementPatternsUseCase:
    def __init__(
            self,
            # read_firebase_node_service: ReadFirebaseNodeService,
            sessionizer: Sessionizer,
            sequence_counter: SequenceCounter,
            transition_probability_calculator: TransitionProbabilityCalculator,
            time_bucket_comparator: TimeBucketComparator,
    ) -> None:
        # self._read_firebase_service = read_firebase_node_service
        self._sessionizer = sessionizer
        self._sequence_counter = sequence_counter
        self._transition_probability_calculator = transition_probability_calculator
        self._time_bucket_comparator = time_bucket_comparator

    def execute(
            self,
            request: MovementAnalysisRequestDTO,
            # sensor_ids: tuple[str, ...],
            # sensor_events: tuple[SensorEvent, ...],
    ) -> MovementAnalysisResultDTO:

        sessions: list[MovementSession] = (
            self._sessionizer.split_into_sessions(
                list(request.sensor_events)))

        sequence_counts: Counter[tuple[str, ...]] = (
            self._sequence_counter.count_sequences(
                sessions=sessions,
                sequence_length=3))

        transition_probabilities: dict[tuple[str, str], float] = (
            self._transition_probability_calculator.calculate(
                sessions=sessions))

        time_bucket_comparison: TimeBucketComparisonResult = (
            self._time_bucket_comparator.compare(
                sessions=sessions,
                sequence_length=3))

        return MovementAnalysisResultDTO(
            scenario_id=request.scenario_id,
            user_reference=request.user_id,
            user_id=request.user_id,

            sequence_counts=sequence_counts,
            transition_probabilities=transition_probabilities,
            time_bucket_comparison=time_bucket_comparison,
        )

    @staticmethod
    def _build_sensor_events(
            sensor_ids: list[str],
            events_by_sensor_id: dict[str, Any],
    ) -> list[SensorEvent]:
        events: list[SensorEvent] = []

        for sensor_id in sensor_ids:
            events_by_day = events_by_sensor_id.get(sensor_id, {})

            for timestamps_state in events_by_day.values():
                for timestamp_str, state in timestamps_state.items():
                    events.append(
                        SensorEvent(
                            sensor_id=sensor_id,
                            activated_at_utc=datetime.strptime(
                                timestamp_str,
                                "%Y%m%d%H%M%S",
                            ),
                            sensor_state=state,
                        )
                    )

        return sorted(events, key=lambda event: event.activated_at_utc)

    @staticmethod
    def _collapse_consecutive_sensor_events(
            events: list[SensorEvent],
    ) -> list[SensorEvent]:
        if not events:
            return []

        sorted_events = sorted(
            events,
            key=lambda event: event.activated_at_utc,
        )

        collapsed: list[SensorEvent] = []

        for event in sorted_events:
            if not collapsed:
                collapsed.append(event)
                continue

            previous = collapsed[-1]

            if event.sensor_id == previous.sensor_id:
                # Replace previous with later activation.
                collapsed[-1] = event
            else:
                collapsed.append(event)

        return collapsed

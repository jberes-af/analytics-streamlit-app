# /src/domain/services/time_bucket_comparator.py

from collections import Counter
from dataclasses import dataclass
from datetime import time

from src.domain.entities.movement_session import MovementSession
from src.domain.services.movement_analysis.sequence_counter import SequenceCounter
from src.domain.services.movement_analysis.transition_probability_calculator import (
    TransitionProbabilityCalculator,
)


@dataclass(frozen=True)
class TimeBucketComparisonResult:
    sequence_counts_by_bucket: dict[str, Counter[tuple[str, ...]]]
    transition_probabilities_by_bucket: dict[str, dict[tuple[str, str], float]]


class TimeBucketComparator:
    def __init__(
        self,
        sequence_counter: SequenceCounter,
        transition_probability_calculator: TransitionProbabilityCalculator,
    ) -> None:
        self._sequence_counter = sequence_counter
        self._transition_probability_calculator = transition_probability_calculator

    def compare(
        self,
        sessions: list[MovementSession],
        sequence_length: int = 3,
    ) -> TimeBucketComparisonResult:
        sessions_by_bucket = self._group_sessions_by_bucket(sessions)

        sequence_counts_by_bucket: dict[str, Counter[tuple[str, ...]]] = {}
        transition_probabilities_by_bucket: dict[str, dict[tuple[str, str], float]] = {}

        for bucket_name, bucket_sessions in sessions_by_bucket.items():
            sequence_counts_by_bucket[bucket_name] = (
                self._sequence_counter.count_sequences(
                    sessions=bucket_sessions,
                    sequence_length=sequence_length,
                )
            )

            transition_probabilities_by_bucket[bucket_name] = (
                self._transition_probability_calculator.calculate(
                    sessions=bucket_sessions,
                )
            )

        return TimeBucketComparisonResult(
            sequence_counts_by_bucket=sequence_counts_by_bucket,
            transition_probabilities_by_bucket=transition_probabilities_by_bucket,
        )

    def _group_sessions_by_bucket(
        self,
        sessions: list[MovementSession],
    ) -> dict[str, list[MovementSession]]:
        grouped: dict[str, list[MovementSession]] = {
            "night": [],
            "morning": [],
            "afternoon": [],
            "evening": [],
        }

        for session in sessions:
            if not session.events:
                continue

            # Uses the first event in the session to classify the session.
            bucket_name = self._get_bucket(session.events[0].activated_at_utc.time())
            grouped[bucket_name].append(session)

        return grouped

    def _get_bucket(self, event_time: time) -> str:
        hour = event_time.hour

        if 6 <= hour < 12:
            return "morning"

        if 12 <= hour < 18:
            return "afternoon"

        if 18 <= hour < 24:
            return "evening"

        return "night"

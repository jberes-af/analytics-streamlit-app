# /src/domain/services/transition_probability_calculator.py

# src/domain/services/transition_probability_calculator.py

from collections import Counter, defaultdict

from src.domain.entities.movement_session import MovementSession


class TransitionProbabilityCalculator:
    def calculate(
        self,
        sessions: list[MovementSession],
    ) -> dict[tuple[str, str], float]:
        transition_counts: Counter[tuple[str, str]] = Counter()
        origin_totals: defaultdict[str, int] = defaultdict(int)

        for session in sessions:
            sensor_ids = [event.sensor_id for event in session.events]

            for from_sensor, to_sensor in zip(sensor_ids, sensor_ids[1:]):
                transition = (from_sensor, to_sensor)
                transition_counts[transition] += 1
                origin_totals[from_sensor] += 1

        probabilities: dict[tuple[str, str], float] = {}

        for transition, count in transition_counts.items():
            from_sensor, _ = transition
            probabilities[transition] = count / origin_totals[from_sensor]

        return probabilities

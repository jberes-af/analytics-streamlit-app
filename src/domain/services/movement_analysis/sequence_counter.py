# /src/domain/services/sequence_counter.py

from collections import Counter

from src.domain.entities.movement_session import MovementSession


class SequenceCounter:
    def count_sequences(
        self,
        sessions: list[MovementSession],
        sequence_length: int,
    ) -> Counter[tuple[str, ...]]:
        if sequence_length < 2:
            raise ValueError("sequence_length must be at least 2.")

        counter: Counter[tuple[str, ...]] = Counter()

        for session in sessions:
            sensor_ids = [event.sensor_id for event in session.events]

            for index in range(len(sensor_ids) - sequence_length + 1):
                sequence = tuple(sensor_ids[index:index + sequence_length])
                counter[sequence] += 1

        return counter

# /src/domain/services/sessionizer.py

from datetime import timedelta

from src.domain.entities.sensor import SensorEvent
from src.domain.entities.movement_session import MovementSession


class Sessionizer:
    def __init__(self, max_gap_minutes: int = 5) -> None:
        self._max_gap = timedelta(minutes=max_gap_minutes)

    def split_into_sessions(
        self,
        events: list[SensorEvent],
    ) -> list[MovementSession]:
        if not events:
            return []

        sorted_events = sorted(events, key=lambda event: event.activated_at)

        sessions: list[MovementSession] = []
        current_session: list[SensorEvent] = [sorted_events[0]]

        for previous, current in zip(sorted_events, sorted_events[1:]):
            gap = current.activated_at - previous.activated_at

            if gap <= self._max_gap:
                current_session.append(current)
            else:
                sessions.append(MovementSession(events=current_session))
                current_session = [current]

        sessions.append(MovementSession(events=current_session))

        return sessions

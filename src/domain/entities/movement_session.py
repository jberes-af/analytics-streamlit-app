# /src/domain/entities/movement_session.py

from dataclasses import dataclass

from src.domain.entities.sensor import SensorEvent


@dataclass(frozen=True)
class MovementSession:
    events: list[SensorEvent]

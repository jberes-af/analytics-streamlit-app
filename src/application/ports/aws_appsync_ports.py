# /src/application/ports/aws_appsync_ports.py

from typing import Protocol
from src.application.dto.sensor_timeline_uc_dtos import (
    SensorLastSeenDTO,
)


class SensorLastSeenPort(Protocol):
    def get_last_seen_utc(
            self,
            *,
            device_id: str) -> SensorLastSeenDTO | None:
        ...

# /src/domain/entities/sensor.py

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class SensorEvent:
    sensor_id: str
    activated_at_utc: datetime  # UTC
    activated_at_local: datetime  # local time: default America / New_York
    sensor_state: str


@dataclass(frozen=True)
class SensorProfile:
    sensor_id: str
    sensor_type: str
    sensor_name: str | None = None
    sensor_zone: str | None = None
    sensor_location: str | None = None

# /src/application/dto/sensor_timeline_uc_dtos.py

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class MostRecentSensorEventDTO:
    sensor_id: str
    activated_at: datetime | None
    # sensor_state: str | None


@dataclass(frozen=True)
class SensorLastSeenDTO:
    sensor_id: str
    last_seen_time_utc: datetime | str
    last_seen_time_cst: datetime | str
    connectivity_status: str
    status_timestamp: datetime


@dataclass(frozen=True)
class SensorConnectivityStatusResultDTO:
    user_id: str
    sensor_ids: list[str]

    sensor_online_statuses: list[SensorLastSeenDTO]
    most_recent_events: list[MostRecentSensorEventDTO]

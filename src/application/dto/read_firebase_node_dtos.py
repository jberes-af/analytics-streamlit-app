# /src/application/dto/read_firebase_node_dtos.py

from dataclasses import dataclass
from enum import StrEnum
from typing import Any, Mapping


class NodeType(StrEnum):
    GATEWAY = "gateway"
    SENSOR_EVENTS = "sensor_events"
    SENSOR_SYSTEM = "sensor"
    SENSOR_USER = "sensor_user_config"
    USER = "user"
    USER_SENSORS = "user_sensors"


@dataclass(frozen=True)
class ReadFirebaseNodeRequestDTO:
    node_id: str
    node_type: NodeType


@dataclass(frozen=True)
class ReadFirebaseNodeResultDTO:
    node_type: NodeType
    node_id: str
    path: str
    data: Mapping[str, Any] | None

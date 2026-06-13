# /src/application/services/read_firebase_node_service.py

from typing import Any, Mapping

from src.domain.value_objects.firebase import FirebasePath
from src.domain.services.firebase_path_factory import FirebasePathFactory

from src.application.dto.read_firebase_node_dtos import (
    ReadFirebaseNodeRequestDTO,
    ReadFirebaseNodeResultDTO)

from src.application.ports.firebase_rtdb import FirebaseRtdbPort


class ReadFirebaseNodeService:

    def __init__(
            self,
            rtdb: FirebaseRtdbPort
    ):
        self._rtdb = rtdb

    def read_node(
            self,
            read_request: ReadFirebaseNodeRequestDTO,
    ) -> ReadFirebaseNodeResultDTO:
        path: FirebasePath = _resolve_read_path(
            read_request.node_type,
            read_request.node_id)

        raw = self._rtdb.read_node(path)

        data: Mapping[str, Any] | None = raw if isinstance(raw, Mapping) else None

        return ReadFirebaseNodeResultDTO(
            node_type=read_request.node_type,
            node_id=read_request.node_id,
            path=path.value,
            data=data,
        )


def _resolve_read_path(node_type: str, node_id: str) -> FirebasePath:

    if node_type == "user_sensors":
        return FirebasePathFactory.user_sensors(node_id)

    if node_type == "sensor_events":  # formerly `notification`
        return FirebasePathFactory.sensor_events(node_id)

    if node_type == "user":
        return FirebasePathFactory.user(node_id)

    if node_type == "sensor":
        return FirebasePathFactory.sensor(node_id)

    # if node_type == "sensor_user_config":
        # return FirebasePathFactory.sensor_user_config(node_id)

    if node_type == "gateway":
        return FirebasePathFactory.gateway(node_id)

    raise ValueError(f"unsupported node_type: {node_type}")

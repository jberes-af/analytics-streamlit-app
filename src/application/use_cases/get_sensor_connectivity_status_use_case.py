# /src/application/use_cases/build_sensor_event_timeline_use_case.py


from datetime import date, datetime, time
from typing import Any

from src.application.dto.read_firebase_node_dtos import NodeType

from src.domain.entities.sensor import (
    SensorProfile,
    SensorEvent,
)

from src.application.dto.read_firebase_node_dtos import (
    ReadFirebaseNodeRequestDTO,
    ReadFirebaseNodeResultDTO,
)

from src.application.dto.sensor_timeline_uc_dtos import (
    SensorEventTimelineRequestDTO,
    SensorEventTimelineResultDTO,
    SensorLastSeenDTO,
    MostRecentSensorEventDTO,
)

from src.application.ports.aws_appsync_ports import SensorLastSeenPort

from src.application.services.read_firebase_node_service import (
    ReadFirebaseNodeService,
)


class GetSensorConnectivityStatusUseCase:
    def __init__(
            self,
            read_firebase_node_service: ReadFirebaseNodeService,
            read_app_sync_last_seen_service: SensorLastSeenPort,
    ) -> None:
        self._read_firebase_service = read_firebase_node_service
        self._read_last_seen_service = read_app_sync_last_seen_service

    def execute(
            self,
            request: SensorEventTimelineRequestDTO,
    ) -> SensorConnectivityStatusResultDTO:


        # Get sensor online status ---------------------------------------

        sensor_online_statuses: list[SensorLastSeenDTO] = [
            self._read_last_seen_service.get_last_seen_utc(device_id=sensor_id)
            for sensor_id in sensor_ids
        ]

        most_recent_events: list[MostRecentSensorEventDTO] = (
            self._extract_most_recent_event_by_sensor_id(
                sensor_ids=sensor_ids,
                events=events,
            )
        )

        return SensorConnectivityStatusResultDTO(
            sensor_ids=sensor_ids,
            sensor_online_statuses=sensor_online_statuses,
            most_recent_events=most_recent_events,
        )

    @staticmethod
    def _extract_most_recent_event_by_sensor_id(
            sensor_ids: list[str],
            events: list[SensorEvent],
    ) -> list[MostRecentSensorEventDTO]:

        id_to_event: dict[str, SensorEvent | None] = {
            sensor_id: None
            for sensor_id in sensor_ids
        }

        for event in events:
            if event.sensor_id not in id_to_event:
                continue

            current_event = id_to_event[event.sensor_id]

            if (
                    current_event is None
                    or event.activated_at_utc > current_event.activated_at_utc
            ):
                id_to_event[event.sensor_id] = event

        return [
            MostRecentSensorEventDTO(
                sensor_id=sensor_id,
                activated_at=event.activated_at_utc if event else None,
                # sensor_state=event.sensor_state if event else None,
            )
            for sensor_id, event in id_to_event.items()
        ]

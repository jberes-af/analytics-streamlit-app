# /src/application/use_cases/build_sensor_event_timeline_use_case.py


from src.application.dto.read_firebase_node_dtos import NodeType

from src.domain.entities.sensor import (
    SensorProfile,
    # SensorEvent,
)

from src.application.dto.read_firebase_node_dtos import (
    ReadFirebaseNodeRequestDTO,
    ReadFirebaseNodeResultDTO,
)

from src.application.dto.sensor_by_user_uc_dtos import (
    SensorByUserRequestDTO,
    SensorByUserResultDTO,
)

# from src.application.ports.aws_appsync_ports import SensorLastSeenPort

from src.application.services.read_firebase_node_service import (
    ReadFirebaseNodeService,
)


class LookupSensorByUserUseCase:
    def __init__(
            self,
            read_firebase_node_service: ReadFirebaseNodeService,
            # read_app_sync_last_seen_service: SensorLastSeenPort,
    ) -> None:
        self._read_firebase_service = read_firebase_node_service
        # self._read_last_seen_service = read_app_sync_last_seen_service

    def execute(
            self,
            request: SensorByUserRequestDTO,
    ) -> SensorByUserResultDTO:
        # Get sensors attached to user ID --------------------------------

        raw_user_sensors: ReadFirebaseNodeResultDTO = (
            self._read_firebase_service.read_node(
                ReadFirebaseNodeRequestDTO(
                    node_id=request.user_id,
                    node_type=NodeType.USER_SENSORS
                )))

        sensor_ids: list[str] = [k for k in raw_user_sensors.data.keys()]

        # Get sensor profiles --------------------------------------------

        sensor_id_to_type: dict[str, str] = {}

        for sensor_id in sensor_ids:
            raw_system_sensors: ReadFirebaseNodeResultDTO = (
                self._read_firebase_service.read_node(
                    ReadFirebaseNodeRequestDTO(
                        node_id=sensor_id,
                        node_type=NodeType.SENSOR_SYSTEM
                    )))

            sensor_id_to_type[sensor_id] = raw_system_sensors.data.get("type", "")

        sensor_profiles: list[SensorProfile] = [
            SensorProfile(
                sensor_id=sensor_id,
                sensor_type=sensor_id_to_type[sensor_id],
                sensor_name=user_profile.get("name"),
                sensor_zone=user_profile.get("zone"),
                sensor_location=user_profile.get("location"),
            )
            for sensor_id, user_profile in raw_user_sensors.data.items()
        ]

        print("*************")
        print("answer")
        print(sensor_profiles)
        print("*************")

        return SensorByUserResultDTO(
            user_id=request.user_id,
            sensor_ids=sensor_ids,
            sensor_profiles=sensor_profiles,
        )

# domain/services/firebase_path_factory.py

from src.domain.value_objects.firebase import FirebasePath


class FirebasePathFactory:
    """
    Domain service: owns canonical path rules for node types.
    Keep string concatenation and invariants out of CLI.
    """

    @staticmethod
    def sensor(sensor_id: str) -> FirebasePath:
        s = sensor_id.strip()
        if not s:
            raise ValueError("sensor_id must be non-empty")
        return FirebasePath(f"/sensor/{s}")

    @staticmethod
    def gateway(gateway_id: str) -> FirebasePath:
        g = gateway_id.strip()
        if not g:
            raise ValueError("gateway_id must be non-empty")
        return FirebasePath(f"/iotg/{g}")

    @staticmethod
    def user(uid: str) -> FirebasePath:
        u = uid.strip()
        if not u:
            raise ValueError("uid must be non-empty")
        return FirebasePath(f"/user/{u}")

    @staticmethod
    def user_sensors(uid: str) -> FirebasePath:
        u = uid.strip()
        if not u:
            raise ValueError("uid must be non-empty")
        return FirebasePath(f"/user/{u}/device")

    @staticmethod
    def sensor_user_config(uid: str, sensor_id: str) -> FirebasePath:
        u = uid.strip()
        if not u:
            raise ValueError("uid must be non-empty")
        s = sensor_id.strip()
        if not s:
            raise ValueError("sensor_id must be non-empty")
        return FirebasePath(f"/user/{u}/device/{s}")

    @staticmethod
    def sensor_events(sensor_id: str) -> FirebasePath:
        s = sensor_id.strip()
        if not s:
            raise ValueError("sensor_id must be non-empty")
        return FirebasePath(f"/notification/all/{s}")
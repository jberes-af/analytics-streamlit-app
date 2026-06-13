# /src/application/dto/sensor_by_user_uc_dtos.py

from dataclasses import dataclass

from src.domain.entities.sensor import SensorProfile


@dataclass(frozen=True)
class SensorByUserRequestDTO:
    user_id: str


@dataclass(frozen=True)
class SensorByUserResultDTO:
    user_id: str
    sensor_ids: list[str]
    sensor_profiles: list[SensorProfile]

# /domain/entities/firebase_entities.py

from dataclasses import dataclass, field, replace


# for writing to Firebase via multi-location payload builder
@dataclass
class SensorSpec:
    brand: str  # "alerta rest"
    icon: str  # "animal_0.png"
    image: str  # "animal_0.png"
    location: str  # e.g. "Primary bedroom"
    name: str  # user-facing name, e.g. "Bed Sensor"
    sensor_id: str  # "10008"
    sensor_type: str  # "chair_pad"
    zone: str  # e.g. "Downstairs"


@dataclass
class AdlEntity:
    user_id: str
    activity: str  # "ambulating"
    sensor_ids: list[str] = field(default_factory=list)

    @classmethod
    def from_rtdb(cls, uid: str, data: dict | None) -> "AdlEntity":
        # Construct AdlEntity from Firebase RTDB data.
        data = data or {}
        return cls(
            user_id=uid,
            activity=data.get("name", ""),
            sensor_ids=data.get("sensor_ids", []),
        )


@dataclass
class UserEntity:
    email_auth: str
    email_rtdb: str
    user_id: str
    name: str
    tel_number: str
    user_adls: list["AdlEntity"] = field(default_factory=list)
    user_sensors: list["SensorEntity"] = field(default_factory=list)
    user_gateways: list["GatewayEntity"] = field(default_factory=list)
    user_routine_ids: list[str] = field(default_factory=list)
    user_gateway_ids: list[str] = field(default_factory=list)
    user_sensor_ids: list[str] = field(default_factory=list)
    user_exists: bool = False
    exists_auth: bool = False
    exists_rtdb: bool = False

    @classmethod
    def from_rtdb(cls, uid: str, data: dict | None) -> "UserEntity":
        # Construct UserEntity from Firebase RTDB data.
        data = data or {}
        return cls(
            email_rtdb=data.get("email", ""),
            email_auth=data.get("email_auth", ""),
            user_id=uid,
            name=data.get("name", ""),
            tel_number=data.get("tel", "") or data.get("phone", ""),
            user_adls=data.get("adl_entities", []),
            user_routine_ids=data.get("routine_ids", []),
            user_sensor_ids=data.get("sensor_ids", []),
            user_gateway_ids=data.get("gateway_ids", []),
            user_exists=bool(data),
            exists_auth=data.get("exists_auth", False),
            exists_rtdb=data.get("exists_rtdb", False),
        )


@dataclass
class RoutineEntity:
    count_rules: int
    routine_id: str
    user_id: str
    sensor_ids: list[str] = field(default_factory=list)
    orphan: bool = True
    exists: bool = False
    exists_in_routine: bool = False
    exists_in_user: bool = False

    @classmethod
    def from_rtdb(cls, routine_id: str, data: dict) -> "RoutineEntity":
        data = data or {}
        return cls(
            count_rules=data.get("rule_count", 0),
            routine_id=routine_id,
            sensor_ids=data.get("sensor_ids", []),
            user_id=data.get("user_id"),
            orphan=data.get("orphan", False),
            exists=bool(data),
            exists_in_routine=data.get("exists_in_routine"),
            exists_in_user=data.get("exists_in_user"),
        )


# --- System-defined, immutable ---

"""
GATEWAY
"""


@dataclass
class GatewayEntity:
    gateway_id: str
    sensors: list[str]
    users: list[str]
    timezone_name: str
    utc_offset: int
    exists: bool

    @classmethod
    def from_rtdb(cls, gateway_id: str, data: dict) -> "GatewayEntity":
        data = data or {}
        return cls(
            gateway_id=gateway_id,
            sensors=list(data.get("sensor", {})),
            users=list(data.get("user", {})),
            timezone_name=data.get("timezone_name", ""),
            utc_offset=data.get("utc_offset", -6),
            exists=bool(data),
        )


"""
NOTIFICATION
"""


@dataclass
class NotificationEntity:
    sensor_id: str
    last_time: str
    last_status: str
    all: dict[str, dict[str, str]] = field(default_factory=dict)


"""
SENSOR
"""


@dataclass(frozen=True, slots=True)
class SensorSystem:
    brand: str
    sensor_id: str
    sensor_type: str  # avoid 'type' (built-in)
    icon: str | None = None
    exists: bool = False

    @classmethod
    def from_rtdb(cls, sensor_id: str, data: dict | None) -> "SensorSystem":
        data = data or {}
        return cls(
            brand=data.get("brand", ""),
            sensor_id=sensor_id,
            sensor_type=data.get("type", ""),
            icon=data.get("icon"),
            exists=bool(data),
        )


# --- User-defined, mutable ---
@dataclass(slots=True)
class SensorUser:
    sensor_id: str
    name: str = ""
    location: str = ""
    zone: str = ""
    image: str | None = None
    exists: bool = False

    @classmethod
    def from_rtdb(cls, sensor_id: str, data: dict | None) -> "SensorUser":
        data = data or {}
        return cls(
            sensor_id=sensor_id,
            name=data.get("name", "") or "",
            location=data.get("location", "") or "",
            zone=data.get("zone", "") or "",
            image=data.get("image"),
            exists=bool(data),
        )

    def apply(self, patch: dict | None) -> "SensorUser":
        patch = patch or {}
        if "name" in patch:     self.name = patch["name"] or self.name
        if "location" in patch: self.location = patch["location"] or self.location
        if "zone" in patch:     self.zone = patch["zone"] or self.zone
        if "image" in patch:    self.image = patch["image"]  # allow None to clear
        self.exists = self.exists or bool(patch)
        return self


# --- Aggregate view ---
@dataclass(slots=True)
class SensorEntity:
    core: SensorSystem
    profile: SensorUser

    @property
    def sensor_id(self) -> str:           return self.core.sensor_id

    @property
    def sensor_type(self) -> str:         return self.core.sensor_type

    @property
    def icon(self) -> str | None:         return self.core.icon

    @property
    def name(self) -> str:                return self.profile.name

    @property
    def location(self) -> str:            return self.profile.location

    @property
    def zone(self) -> str:                return self.profile.zone

    @property
    def image(self) -> str | None:        return self.profile.image

    @property
    def exists(self) -> bool:             return self.core.exists or self.profile.exists

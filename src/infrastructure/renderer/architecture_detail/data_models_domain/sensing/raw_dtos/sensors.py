# /src/infrastructure/renderer/architecture_detail/data_models_domain/sensing/sensors.py


SENSOR_STATE_NUMERIC_CODES_ENUM: str = """
class SensorStateNumericCodesEnum(StrEnum):
    14 = "14"
    C8 = "C8"
"""

SENSOR_STATE_DEFINITION_ENUM: str = """
class SensorStateDefinitionEnum(StrEnum):
    ON = "On"
    OFF = "Off"
"""

SENSOR_STATE_DISPLAY_NAMES_ENUM: str = """
class SensorStateDisplayNamesEnum(StrEnum):
    ACTIVATED = "Activated"
    EXIT = "Exit"
"""

NOTIFICATION_MESSAGE_STATUS_ENUM: str = """
class NotificationMessageStatusEnum(StrEnum):
    CREATED = "Created"
    SENT = "Sent"
    DELIVERED = "Delivered"
    FAILED = "Failed"
"""

SENSOR_QUERY_SCOPE_ENUM: str = """
class SensorQueryScopeEnum(StrEnum):
    ALL_SENSORS = "All Sensors"
    SENSOR_ID = "Sensor Id"
    SENSOR_GROUP_ID = "Sensor Group Id"
"""

SENSOR_STATE_DEFINITION_DTO: str = """
@dataclass(frozen=True)
class SensorStateDefinitionDTO:
    numeric_code: str
    definition: str
    display_name: str
"""

SENSOR_LIVE_STATE_DTO: str = """
@dataclass(frozen=True)
class SensorLiveStateDTO:
    sensor_id: str
    current_state: SensorStateDefinitionDTO
    last_updated_at: str
"""

SENSOR_PROFILE_SYSTEM_CONFIGURATION_DTO: str = """
@dataclass(frozen=True)
class SensorProfileSystemConfigurationDTO:
    sensor_id: str
    type: str
    brand: str
    icon: str | None = None
    hardware_version: str | None = None
    firmware_version: str | None = None
"""

SENSOR_PROFILE_USER_CONFIGURATION_DTO: str = """
@dataclass(frozen=True)
class SensorProfileUserConfigurationDTO:
    sensor_id: str
    name: str | None = None
    location: str | None = None
    zone: str | None = None
    image: str | None = None
    color: str | None = None
"""

SENSOR_PROFILE_DTO: str = """
@dataclass(frozen=True)
class SensorProfileDTO:
    sensor_id: str
    system_configuration: SensorProfileSystemConfigurationDTO
    user_configuration: SensorProfileUserConfigurationDTO
    state: SensorStateDTO | None = None
"""

SENSOR_HEALTH_DTO: str = """
@dataclass(frozen=True)
class SensorHealthDTO:
    sensor_id: str
    is_online: bool
    last_seen_at: str | None = None
    signal_strength: float | None = None
    battery_level: float | None = None
    install_date: str | None = None
"""

SENSOR_EVENT_DTO: str = """
@dataclass(frozen=True)
class SensorEventDTO:
    event_id: str
    sensor_id: str
    current_state: SensorStateDefinitionDTO
    timestamp: str
"""

TIMELINE_EVENT_DTO: str = """
@dataclass(frozen=True)
class TimelineEventDTO:
    sensor_event: SensorEventDTO
    sensor_profile: SensorProfileDTO
"""

SENSOR_EVENT_NOTIFICATION_MESSAGE_DTO: str = """
@dataclass(frozen=True)
class SensorEventNotificationMessageDTO:
    notification_id: str
    source_event_id: str | None = None
    source_event_type: str
    recipient_user_id: str
    channel: str
    title: str
    message: str
    status: NotificationStatusEnum
    created_at: str
    sent_at: str | None = None
    read_at: str | None = None
"""

SENSOR_GROUP_DTO: str = """
@dataclass(frozen=True)
class SensorGroupDTO:
    group id: str
    sensors: tuple[SensorProfileDTO, ...]
    name: str
"""

SENSOR_DOMAIN_OBJECTS: dict[str, str] = {
    "sensor_event_dto": SENSOR_EVENT_DTO,
    "sensor_event_notification_message_dto": SENSOR_EVENT_NOTIFICATION_MESSAGE_DTO,
    "sensor_group_dto": SENSOR_GROUP_DTO,
    "sensor_health_dto": SENSOR_HEALTH_DTO,
    "sensor_live_state_dto": SENSOR_LIVE_STATE_DTO,
    "sensor_profile_dto": SENSOR_PROFILE_DTO,
    "sensor_profile_system_configuration_dto": SENSOR_PROFILE_SYSTEM_CONFIGURATION_DTO,
    "sensor_profile_user_configuration_dto": SENSOR_PROFILE_USER_CONFIGURATION_DTO,
    "sensor_query_scope_enum": SENSOR_QUERY_SCOPE_ENUM,
    "sensor_state_definition_dto": SENSOR_STATE_DEFINITION_DTO,
    "sensor_state_definition_enum": SENSOR_STATE_DEFINITION_ENUM,
    "sensor_state_display_names_enum": SENSOR_STATE_DISPLAY_NAMES_ENUM,
    "sensor_state_numeric_codes_enum": SENSOR_STATE_NUMERIC_CODES_ENUM,
    "timeline_event_dto": TIMELINE_EVENT_DTO,
}

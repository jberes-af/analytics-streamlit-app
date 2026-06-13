# /src/infrastructure/renderer/architecture_detail/data_models_analytics/data_models_backend/sensor_definition_dto_definitions.py


SENSOR_DEFINITION_DTO: str = """
class SensorDefinitionDTO:
    sensor_id: str
    sensor_type: SensorType
    brand: str
    firmware_version: str
    icon: str
    created_at_iso: str
    updated_at_iso: str
"""

SENSOR_STATE_DTO: str = """
class SensorDefinitionDTO:
    sensor_id: str
    sensor_state: str
    battery_level: str | None = None
    online: bool = False
    last_seen_at_iso: str | None = None
"""

SENSOR_PROFILE_DTO: str = """
class SensorDefinitionDTO:
    sensor_id: str
    name: str
    location: str
    zone: str
    image: str
"""

SENSOR_EVENT_DEFINITION_DTO: str = """
class SensorEventDefinitionDTO:
    sensor_id: str
    event_type: str
    event_value: Any
    occurred_at_iso: str
    received_at_iso: str
    metadata: dict[str, Any] = Field(default_factory=dict)
"""

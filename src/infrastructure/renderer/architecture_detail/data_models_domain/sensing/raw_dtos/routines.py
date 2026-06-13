# /src/infrastructure/renderer/architecture_detail/data_models_analytics/data_models_domain/sensing/routines.py


ALERTA_ROUTINE_TIMEFRAME_STATE_ENUM: str = """
class AlertaRoutineTimeframeStateEnum(StrEnum):
    NOT_STARTED = "Not Started"
    ACTIVE = "Active"
    EXPIRED = "Expired"
"""

ALERTA_ROUTINE_OUTCOME_STATE_ENUM: str = """
class AlertaRoutineOutcomeStateEnum(StrEnum):
    OCCURRED = "Occurred"
    DID_NOT_OCCUR = "Did Not Occur"
    NOT_AVAILABLE_-_PENDING = "Not Available - Pending"
"""

ALERTA_ROUTINE_EVALUATION_MODE_ENUM: str = """
class AlertaRoutineEvaluationModeEnum(StrEnum):
    ALL_RULES_MET = "All Rules Met"
    ANY_RULE_MET = "Any Rule Met"
    SEQUENCE_MET = "Sequence Met"
"""

ALERTA_ROUTINE_RULE_DTO: str = """
@dataclass(frozen=True)
class AlertaRoutineRuleDTO:
    sensor_id: str
    expected_sensor_state: SensorStateDefinitionEnum
"""

ALERTA_ROUTINE_STATE_DTO: str = """
@dataclass(frozen=True)
class AlertaRoutineStateDTO:
    routine_id: str
    timeframe_state: AlertaRoutineTimeframeStateEnum
    outcome_state: AlertaRoutineOutcomeStateEnum
"""

ALERTA_ROUTINE_PROFILE_DTO: str = """
@dataclass(frozen=True)
class AlertaRoutineProfileDTO:
    routine_id: str
    name: str
    start_time: str
    end_time: str
    rules: tuple[AlertaRoutineRule, ...]
    routine_state: AlertaRoutineStateDTO
    success_message: str = "Routine Occurred"
    failure_message: str = "Routine did not occur!"
"""

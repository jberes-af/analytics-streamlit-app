# /src/infrastructure/architecture_detail/data_models_analytics/data_models_domain/care/care_domain_dtos

# /src/infrastructure/architecture_detail/data_models_analytics/data_models_domain/sensing/sensing_domain_dtos.py

from src.infrastructure.renderer.architecture_detail.data_models_domain.build_domain_dtos import (
    build_domain_data_model,
    build_dto,
)

from src.infrastructure.renderer.architecture_detail.data_models_domain.sensing.raw_dtos.sensors import (
    SENSOR_EVENT_DTO,
    SENSOR_GROUP_DTO,
    SENSOR_HEALTH_DTO,
    SENSOR_PROFILE_DTO,
    SENSOR_PROFILE_SYSTEM_CONFIGURATION_DTO,
    SENSOR_PROFILE_USER_CONFIGURATION_DTO,
    TIMELINE_EVENT_DTO,
)

from src.infrastructure.renderer.architecture_detail.data_models_domain.sensing.raw_dtos.movements import (
    MOVEMENT_DTO,
    MOVEMENT_PATTERN_REQUEST_DTO,
    MOVEMENT_PATTERN_RESPONSE_DTO,
    MOVEMENT_PATTERN_SERVICE,
)

from src.infrastructure.renderer.architecture_detail.data_models_domain.sensing.raw_dtos.routines import (
    ALERTA_ROUTINE_RULE_DTO,
    ALERTA_ROUTINE_STATE_DTO,
    ALERTA_ROUTINE_PROFILE_DTO,
    ALERTA_ROUTINE_TIMEFRAME_STATE_ENUM,
    ALERTA_ROUTINE_OUTCOME_STATE_ENUM,
    ALERTA_ROUTINE_EVALUATION_MODE_ENUM,
)

from src.infrastructure.renderer.architecture_detail.data_models_analytics.shared import (
    TREND_DIRECTION_ENUM,
    METRIC_TIME_PERIOD_DTO,
    DATA_POINT_DTO,
    COUNT_METRIC_DTO,
    TREND_METRIC_DTO,
    COMPARISON_METRIC_DTO,
    PERIOD_STATISTICS_DTO,
    TREND_SERIES_DTO,
    ROLLING_AVERAGE_CONFIGURATION_DTO,
    REGRESSION_TREND_DTO,
)

# from src.infrastructure.renderer.architecture_detail.data_models_backend.care.adl.adl_persistence_dto_definitions import ()
# from src.infrastructure.renderer.architecture_detail.data_models_backend.care.adl.adl_data_read_objects import ()
# from src.infrastructure.renderer.architecture_detail.data_models_backend.care.adl.adl_data_write_objects import ()

"""
UI-S-01
"""

SENSING_HOME_DOMAIN_DTOS = [

    build_dto(
        name="TimelineEventDTO",
        description="",
        code=TIMELINE_EVENT_DTO,
    ),

    build_dto(
        name="SensorHealthDTO",
        description="",
        code=SENSOR_HEALTH_DTO,
    ),

]

"""
UI-S-02
"""

SENSING_DASHBOARD_DOMAIN_DTOS = [
    build_dto(
        name="TimelineEventDTO",
        description="",
        code=TIMELINE_EVENT_DTO,
    ),

    build_dto(
        name="SensorHealthDTO",
        description="",
        code=SENSOR_HEALTH_DTO,
    ),

]

"""
UI-S-03
"""

SENSING_TRENDS_DOMAIN_DTOS = [
    build_dto(
        name="TrendDirectionEnum",
        description="",
        code=TREND_DIRECTION_ENUM,
    ),

    build_dto(
        name="MetricTimePeriodDTO",
        description="",
        code=METRIC_TIME_PERIOD_DTO,
    ),

    build_dto(
        name="DataPointDTO",
        description="",
        code=DATA_POINT_DTO,
    ),

    build_dto(
        name="CountMetricDTO",
        description="",
        code=COUNT_METRIC_DTO,
    ),

    build_dto(
        name="TrendMetricDTO",
        description="",
        code=TREND_METRIC_DTO,
    ),

    build_dto(
        name="ComparisonMetricDTO",
        description="",
        code=COMPARISON_METRIC_DTO,
    ),

    build_dto(
        name="PeriodStatisticsDTO",
        description="",
        code=PERIOD_STATISTICS_DTO,
    ),

    build_dto(
        name="TrendSeriesDTO",
        description="",
        code=TREND_SERIES_DTO,
    ),

    build_dto(
        name="RollingAverageConfigurationDTO",
        description="",
        code=ROLLING_AVERAGE_CONFIGURATION_DTO,
    ),

    build_dto(
        name="RegressionTrendDTO",
        description="",
        code=REGRESSION_TREND_DTO,
    ),
]

"""
UI-S-04
"""

SENSING_MOVEMENTS_DOMAIN_DTOS = [
    build_dto(
        name="MovementDTO",
        description="",
        code=MOVEMENT_DTO,
    ),
    build_dto(
        name="MovementPatternRequestDTO",
        description="",
        code=MOVEMENT_PATTERN_REQUEST_DTO,
    ),
    build_dto(
        name="MovementPatternResponseDTO",
        description="",
        code=MOVEMENT_PATTERN_RESPONSE_DTO,
    ),
    build_dto(
        name="MovementPatternService",
        description="",
        code=MOVEMENT_PATTERN_SERVICE,
    ),

]

"""
UI-S-06
"""

SENSING_ALERTA_ROUTINES_DOMAIN_DTOS = [
    build_dto(
        name="AlertaRoutineTimeframeStateEnum",
        description="",
        code=ALERTA_ROUTINE_TIMEFRAME_STATE_ENUM,
    ),

    build_dto(
        name="AlertaRoutineOutcomeStateEnum",
        description="",
        code=ALERTA_ROUTINE_OUTCOME_STATE_ENUM,
    ),

    build_dto(
        name="AlertaRoutineEvaluationModeEnum",
        description="",
        code=ALERTA_ROUTINE_EVALUATION_MODE_ENUM,
    ),

    build_dto(
        name="AlertaRoutineRuleDTO",
        description="",
        code=ALERTA_ROUTINE_RULE_DTO,
    ),

    build_dto(
        name="AlertaRoutineStateDTO",
        description="",
        code=ALERTA_ROUTINE_STATE_DTO,
    ),

    build_dto(
        name="AlertaRoutineProfileDTO",
        description="",
        code=ALERTA_ROUTINE_PROFILE_DTO,
    ),
]

"""
UI-S-05
"""

SENSING_SENSOR_EVENT_TIMELINE_DOMAIN_DTOS = [
    build_dto(
        name="SensorEventDTO",
        description="",
        code=SENSOR_EVENT_DTO,
    ),
    build_dto(
        name="TimelineEventDTO",
        description="",
        code=TIMELINE_EVENT_DTO,
    ),

]

"""
UI-S-07
"""

SENSING_SENSOR_PROFILES_DOMAIN_DTOS = [
    build_dto(
        name="SensorProfileDTO",
        description="",
        code=SENSOR_PROFILE_DTO,
    ),
    build_dto(
        name="SensorProfileSystemConfigurationDTO",
        description="",
        code=SENSOR_PROFILE_SYSTEM_CONFIGURATION_DTO,
    ),
    build_dto(
        name="SensorProfileUserConfigurationDTO",
        description="",
        code=SENSOR_PROFILE_USER_CONFIGURATION_DTO,
    ),
    build_dto(
        name="SensorGroupDTO",
        description="",
        code=SENSOR_GROUP_DTO,
    ),
]

# --------------------------------------------------------------------
# --------------------------------------------------------------------


"""
BACKEND DATA MODELS
"""

SENSING_HOME_BACKEND_DTOS = build_domain_data_model(
    definitions=SENSING_HOME_DOMAIN_DTOS,
    persistences=tuple(),
    reads=tuple(),
    writes=tuple(),
)

SENSING_DASHBOARD_BACKEND_DTOS = build_domain_data_model(
    definitions=SENSING_DASHBOARD_DOMAIN_DTOS,
    persistences=tuple(),
    reads=tuple(),
    writes=tuple(),
)

SENSING_TRENDS_BACKEND_DTOS = build_domain_data_model(
    definitions=SENSING_TRENDS_DOMAIN_DTOS,
    persistences=tuple(),
    reads=tuple(),
    writes=tuple(),
)

SENSING_MOVEMENTS_BACKEND_DTOS = build_domain_data_model(
    definitions=SENSING_MOVEMENTS_DOMAIN_DTOS,
    persistences=tuple(),
    reads=tuple(),
    writes=tuple(),
)

SENSING_ALERTA_ROUTINES_BACKEND_DTOS = build_domain_data_model(
    definitions=SENSING_ALERTA_ROUTINES_DOMAIN_DTOS,
    persistences=tuple(),
    reads=tuple(),
    writes=tuple(),
)

SENSING_SENSOR_EVENT_TIMELINE_BACKEND_DTOS = build_domain_data_model(
    definitions=SENSING_SENSOR_EVENT_TIMELINE_DOMAIN_DTOS,
    persistences=tuple(),
    reads=tuple(),
    writes=tuple(),
)

SENSING_SENSOR_PROFILES_BACKEND_DTOS = build_domain_data_model(
    definitions=SENSING_SENSOR_PROFILES_DOMAIN_DTOS,
    persistences=tuple(),
    reads=tuple(),
    writes=tuple(),
)

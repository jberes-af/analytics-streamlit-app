# /src/infrastructure/renderer/architecture_detail/data_models_analytics/data_models_analytics/shared.py


TREND_DIRECTION_ENUM: str = """
class TrendDirectionEnum(StrEnum):
    UP = "Up"
    DOWN = "Down"
    FLOAT = "Float"
    UNKNOWN = "Unknown"
"""

METRIC_TIME_PERIOD_DTO: str = """
@dataclass(frozen=True)
class MetricTimePeriodDTO:
    days: int
    period_start_date: str
    period_end_date: str
"""

DATA_POINT_DTO: str = """
@dataclass(frozen=True)
class DataPointDTO:
    timestamp: str
    value: float
"""

COUNT_METRIC_DTO: str = """
@dataclass(frozen=True)
class CountMetricDTO:
    name: str
    subject: str
    window_days: MetricTimePeriodDTO
    value: float
    period_start_date: str
    period_end_date: str
"""

TREND_METRIC_DTO: str = """
@dataclass(frozen=True)
class TrendMetricDTO:
    name: str
    subject: str
    source_period: MetricTimePeriodDTO
    rolling_average_config: RollingAverageConfigDTO
    raw_values: tuple[DataPointDTO, ...]
    smoothed_values: tuple[DataPointDTO, ...]
    regression: RegressionTrendDTO
    period_start_date: str
    period_end_date: str
"""

COMPARISON_METRIC_DTO: str = """
@dataclass(frozen=True)
class ComparisonMetricDTO:
    name: str
    subject: str
    current_period: MetricTimePeriodDTO
    comparison_period: MetricTimePeriodDTO
    current_value: float
    comparison_value: float
    percent_change: float | None
    direction: TrendDirection
"""

PERIOD_STATISTICS_DTO: str = """
@dataclass(frozen=True)
class PeriodStatisticsDTO:
    subject: str
    period_start_date: str
    period_end_date: str
    minimum: float
    maximum: float
    average: float
    total: int
"""

TREND_SERIES_DTO: str = """
@dataclass(frozen=True)
class TrendSeriesDTO:
    name: str
    subject: str
    window_days: MetricTimePeriodDTO
    raw_values: tuple[DataPointDTO, ...]
    rolling_average_values: tuple[DataPointDTO, ...]
"""

ROLLING_AVERAGE_CONFIGURATION_DTO: str = """
@dataclass(frozen=True)
class RollingAverageConfigurationDTO:
    source_period_days: int
    rolling_window_days: int
    output_point_count: int
"""

REGRESSION_TREND_DTO: str = """
@dataclass(frozen=True)
class RegressionTrendDTO:
    slope: float
    intercept: float
    r_squared: float | None
    direction: TrendDirectionEnum
"""

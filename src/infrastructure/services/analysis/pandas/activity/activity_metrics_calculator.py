# /src/infrastructure/services/analysis/pandas/activity/activity_metrics_calculator.py

from datetime import datetime

from src.domain.entities.sensor import SensorEvent

from src.application.ports.activity_use_case_ports import (
    ActivityMetricsCalculatorPort,
)

from src.application.dto.activity_metric_dtos import (
    ActivityDistributionDTO,
    ActivityMetricsCalculatorResultDTO,
)

from src.infrastructure.services.analysis.pandas.activity.activity_dataframe_factory import (
    ActivityDataFrameFactory,
)

from src.infrastructure.services.analysis.pandas.activity.daily_activity_calculator import (
    DailyActivityCalculator,
)

from src.infrastructure.services.analysis.pandas.activity.hourly_activity_calculator import (
    HourlyActivityCalculator,
)

from src.infrastructure.services.analysis.pandas.activity.rolling_activity_calculator import (
    RollingActivityCalculator,
)

from src.infrastructure.services.analysis.pandas.activity.sensor_activity_calculator import (
    SensorActivityCalculator,
)

from src.infrastructure.services.analysis.pandas.activity.peak_activity_calculator import (
    PeakActivityCalculator,
)

from src.infrastructure.services.analysis.pandas.activity.inactivity_period_calculator import (
    InactivityPeriodCalculator,
)

from src.infrastructure.services.analysis.pandas.activity.activity_distribution_calculator import (
    ActivityDistributionCalculator,
)

from src.infrastructure.services.analysis.pandas.activity.sensor_activity_trend_calculator import (
    ActivityTrendCalculator,
)

from src.infrastructure.services.analysis.pandas.activity.weekly_activity_calculator import (
    WeeklyActivityCalculator,
)

from src.infrastructure.services.analysis.pandas.activity.sensor_time_period_statistics_calculator import (
    SensorTimePeriodStatisticsCalculator,
)

import pandas as pd


class PandasActivityMetricsCalculator(ActivityMetricsCalculatorPort):
    def __init__(
            self,
            dataframe_factory: ActivityDataFrameFactory,
            daily_calculator: DailyActivityCalculator,
            sensor_calculator: SensorActivityCalculator,
            hourly_calculator: HourlyActivityCalculator,
            rolling_calculator: RollingActivityCalculator,
            peak_calculator: PeakActivityCalculator,
            inactivity_calculator: InactivityPeriodCalculator,
            distribution_calculator: ActivityDistributionCalculator,
            activity_trend_calculator: ActivityTrendCalculator,
            weekly_activity_calculator: WeeklyActivityCalculator,
            time_period_statistics_calculator: SensorTimePeriodStatisticsCalculator,
    ) -> None:
        self.dataframe_factory = dataframe_factory
        self.daily_calculator = daily_calculator
        self.sensor_calculator = sensor_calculator
        self.hourly_calculator = hourly_calculator
        self.rolling_calculator = rolling_calculator
        self.peak_calculator = peak_calculator
        self.inactivity_calculator = inactivity_calculator
        self.distribution_calculator = distribution_calculator
        self.activity_trend_calculator = activity_trend_calculator
        self.weekly_activity_calculator = weekly_activity_calculator
        self.time_period_statistics_calculator = time_period_statistics_calculator

    def calculate(
            self,
            # user_id: str,
            start_time: datetime,
            end_time: datetime,
            events: list[SensorEvent],
    ) -> ActivityMetricsCalculatorResultDTO:
        df: pd.DataFrame = self.dataframe_factory.from_events(events)

        if df.empty:
            return ActivityMetricsCalculatorResultDTO(
                # user_id=user_id,
                start_date=start_time.date(),
                end_date=end_time.date(),
                daily_activity=[],
                combined_sensor_activity=[],
                sensor_by_id_by_date_activity=[],
                all_sensors_by_date_activity=[],
                sensor_by_id_by_hour_activity=[],
                all_sensors_by_hour_activity=[],
                rolling_activity=[],
                peak_activity=[],
                inactivity_periods=[],
                activity_distribution=ActivityDistributionDTO(
                    entropy=0.0,
                    most_active_hour=None,
                    least_active_hour=None,
                ),
                activity_trends_by_sensor_id=[],
                activity_trend_all_sensors=[],
                weekly_activity_by_sensor_id=[],
                time_period_statistics_by_sensor_id=[],
            )

        activity_trend_all_sensors = (
            self.activity_trend_calculator.calculate_trend_for_all_sensors_from_daily_counts(
                df=df,
                metric_name="daily_activity_trend_all_sensors",
            )
        )

        activity_trends_by_sensor = (
            self.activity_trend_calculator.calculate_trend_by_sensor_id_from_table(
                df=df,
                metric_name="daily_activity_trend_by_sensor_id",
            )
        )

        return ActivityMetricsCalculatorResultDTO(
            # user_id=user_id,
            start_date=start_time.date(),

            end_date=end_time.date(),

            daily_activity=(
                self.daily_calculator.calculate_date_time(df)
            ),

            combined_sensor_activity=(
                self.sensor_calculator.calculate_total_activity(df)
            ),

            sensor_by_id_by_date_activity=(
                self.sensor_calculator.calculate_sensor_activity_by_id_by_date(
                    df=df,
                    start_date=start_time.date(),
                    end_date=end_time.date(),
                )),

            all_sensors_by_date_activity=(
                self.sensor_calculator.calculate_all_sensors_by_date(
                    df=df,
                    start_date=start_time.date(),
                    end_date=end_time.date(),
                )),

            sensor_by_id_by_hour_activity=(
                self.hourly_calculator.calculate_hourly_by_sensor_id(df)
            ),

            all_sensors_by_hour_activity=(
                self.hourly_calculator.calculate_hourly_all_sensors(df)
            ),


            rolling_activity=(
                self.rolling_calculator.calculate_by_frequency(df)
            ),

            peak_activity=(
                self.peak_calculator.calculate_by_rolling_window(df)
            ),

            inactivity_periods=(
                self.inactivity_calculator.calculate_by_timestamp(df)
            ),

            activity_distribution=(
                self.distribution_calculator.calculate_by_hour(df)
            ),

            activity_trends_by_sensor_id=activity_trends_by_sensor,

            activity_trend_all_sensors=activity_trend_all_sensors,

            weekly_activity_by_sensor_id=(
                self.weekly_activity_calculator.calculate_from_daily_counts(df)
            ),

            time_period_statistics_by_sensor_id=(
                self.time_period_statistics_calculator.calculate(
                    df=df,
                    start_date=start_time.date(),
                    end_date=end_time.date(),
                )
            ),
        )

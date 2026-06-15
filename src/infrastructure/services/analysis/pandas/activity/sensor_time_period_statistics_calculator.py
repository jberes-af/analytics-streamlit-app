# /src/infrastructure/services/analysis/pandas/activity/sensor_time_period_statistics_calculator.py

from datetime import date

from src.application.dto.activity_metric_dtos import (
    SensorTimePeriodStatisticsDTO,
)

import pandas as pd


ALL_SENSORS_ID = "ALL"


class SensorTimePeriodStatisticsCalculator:
    required_columns = {"date", "sensor_id"}

    def calculate(
        self,
        df: pd.DataFrame,
        start_date: date,
        end_date: date,
        include_all_sensors: bool = True,
    ) -> list[SensorTimePeriodStatisticsDTO]:
        if df.empty:
            return []

        missing_columns = self.required_columns - set(df.columns)
        if missing_columns:
            raise ValueError(
                f"SensorTimePeriodStatisticsCalculator missing required columns: "
                f"{missing_columns}"
            )

        results: list[SensorTimePeriodStatisticsDTO] = []

        if include_all_sensors:
            all_daily_counts = (
                df.groupby("date")
                .size()
                .rename("activation_count")
                .sort_index()
            )

            results.append(
                self._calculate_statistics_from_daily_counts(
                    sensor_id=ALL_SENSORS_ID,
                    daily_counts=all_daily_counts,
                    start_date=start_date,
                    end_date=end_date,
                )
            )

        grouped = (
            df.groupby(["sensor_id", "date"])
            .size()
            .rename("activation_count")
            .reset_index()
            .sort_values(["sensor_id", "date"])
        )

        for sensor_id, sensor_group in grouped.groupby("sensor_id"):
            daily_counts = (
                sensor_group
                .set_index("date")["activation_count"]
                .sort_index()
            )

            results.append(
                self._calculate_statistics_from_daily_counts(
                    sensor_id=sensor_id,
                    daily_counts=daily_counts,
                    start_date=start_date,
                    end_date=end_date,
                )
            )

        return results

    @staticmethod
    def _calculate_statistics_from_daily_counts(
        sensor_id: str,
        daily_counts: pd.Series,
        start_date: date,
        end_date: date,
    ) -> SensorTimePeriodStatisticsDTO:
        date_index = pd.date_range(
            start=start_date,
            end=end_date,
            freq="D",
        ).date

        daily_counts = daily_counts.reindex(
            date_index,
            fill_value=0,
        )

        days_in_period = len(daily_counts)

        total_activation_count = int(daily_counts.sum())
        average_daily_activation_count = float(daily_counts.mean())
        median_daily_activation_count = float(daily_counts.median())

        maximum_daily_activation = int(daily_counts.max())
        minimum_daily_activation = int(daily_counts.min())

        maximum_daily_activation_date = daily_counts.idxmax()
        minimum_daily_activation_date = daily_counts.idxmin()

        percentile_25_daily_activation_count = float(
            daily_counts.quantile(0.25)
        )
        percentile_75_daily_activation_count = float(
            daily_counts.quantile(0.75)
        )

        standard_deviation = float(daily_counts.std(ddof=0))

        coefficient_variation = (
            standard_deviation / average_daily_activation_count
            if average_daily_activation_count
            else 0.0
        )

        active_day_count = int((daily_counts > 0).sum())
        inactive_day_count = days_in_period - active_day_count

        return SensorTimePeriodStatisticsDTO(
            sensor_id=sensor_id,
            start_date=start_date,
            end_date=end_date,
            days_in_period=days_in_period,
            total_activation_count=total_activation_count,
            average_daily_activation_count=average_daily_activation_count,
            median_daily_activation_count=median_daily_activation_count,
            maximum_daily_activation=maximum_daily_activation,
            maximum_daily_activation_date=maximum_daily_activation_date,
            minimum_daily_activation=minimum_daily_activation,
            minimum_daily_activation_date=minimum_daily_activation_date,
            percentile_25_daily_activation_count=percentile_25_daily_activation_count,
            percentile_75_daily_activation_count=percentile_75_daily_activation_count,
            standard_deviation_daily_activations=standard_deviation,
            coefficient_variation=coefficient_variation,
            active_day_count=active_day_count,
            inactive_day_count=inactive_day_count,
        )

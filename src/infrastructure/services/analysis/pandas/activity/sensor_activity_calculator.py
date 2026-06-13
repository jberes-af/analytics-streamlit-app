# /src/infrastructure/services/analysis/pandas/activity/sensor_activity_calculator.py

from src.application.dto.activity_metric_dtos import (
    CombinedSensorActivityDTO,
    SensorByIdByDateActivityDTO,
    # SensorActivityByDateByTimePeriodDTO,
)

import pandas as pd


class SensorActivityCalculator:

    @staticmethod
    def calculate_total_activity(
            df: pd.DataFrame,
    ) -> list[CombinedSensorActivityDTO]:
        total_count = len(df)

        grouped = (
            df.groupby("sensor_id")
            .size()
            .rename("total_activations")
            .reset_index()
        )

        results: list[CombinedSensorActivityDTO] = []

        for row in grouped.itertuples(index=False):
            count = int(row.total_activations)

            results.append(
                CombinedSensorActivityDTO(
                    sensor_id=row.sensor_id,
                    total_activations=count,
                    percentage_of_total=count / total_count if total_count else 0.0,
                )
            )

        return results

    @staticmethod
    def calculate_sensor_activity_by_id_by_date(
        df: pd.DataFrame,
    ) -> list[SensorByIdByDateActivityDTO]:

        required_columns = {"date", "sensor_id"}

        if df.empty:
            return []

        missing_columns = required_columns - set(df.columns)
        if missing_columns:
            raise ValueError(
                f"DailySensorActivityCalculator missing required columns: {missing_columns}"
            )

        grouped = (
            df.groupby(["date", "sensor_id"])
            .size()
            .rename("activation_count")
            .reset_index()
            .sort_values(["date", "sensor_id"])
        )

        results: list[SensorByIdByDateActivityDTO] = []

        for row in grouped.itertuples(index=False):
            results.append(
                SensorByIdByDateActivityDTO(
                    date=row.date,
                    sensor_id=row.sensor_id,
                    activation_count=int(row.activation_count),
                )
            )

        return results

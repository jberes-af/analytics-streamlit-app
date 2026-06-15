# /src/infrastructure/services/analysis/pandas/activity/hourly_activity_calculator.py
from src.application.dto.activity_metric_dtos import (
    HourlyActivityAllSensorsDTO,
    HourlyActivityBySensorIdDTO,
)

import pandas as pd


class HourlyActivityCalculator:

    @staticmethod
    def calculate_hourly_all_sensors(
            df: pd.DataFrame,
    ) -> list[HourlyActivityAllSensorsDTO]:

        required_columns: set[str] = {"date", "hour"}

        missing_columns = required_columns - set(df.columns)
        if missing_columns:
            raise ValueError(
                "HourlyActivityAllSensorsCalculator missing required columns: "
                f"{missing_columns}"
            )

        if df.empty:
            return []

        working_df = df.copy()
        working_df["date"] = pd.to_datetime(working_df["date"]).dt.date
        working_df["hour"] = working_df["hour"].astype(int)

        grouped = (
            working_df
            .groupby(["date", "hour"])
            .size()
            .rename("activation_count")
            .reset_index()
            .sort_values(["date", "hour"])
        )

        return [
            HourlyActivityAllSensorsDTO(
                date=row.date,
                hour=int(row.hour),
                activation_count=int(row.activation_count),
            )
            for row in grouped.itertuples(index=False)
        ]

    @staticmethod
    def calculate_hourly_by_sensor_id(
            df: pd.DataFrame,
    ) -> list[HourlyActivityBySensorIdDTO]:

        required_columns: set[str] = {"date", "hour", "sensor_id"}

        missing_columns = required_columns - set(df.columns)
        if missing_columns:
            raise ValueError(
                "HourlyActivityBySensorIdCalculator missing required columns: "
                f"{missing_columns}"
            )

        if df.empty:
            return []

        working_df = df.copy()
        working_df["date"] = pd.to_datetime(working_df["date"]).dt.date
        working_df["hour"] = working_df["hour"].astype(int)
        working_df["sensor_id"] = working_df["sensor_id"].astype(str)

        grouped = (
            working_df
            .groupby(["sensor_id", "date", "hour"])
            .size()
            .rename("activation_count")
            .reset_index()
            .sort_values(["sensor_id", "date", "hour"])
        )

        return [
            HourlyActivityBySensorIdDTO(
                sensor_id=row.sensor_id,
                date=row.date,
                hour=int(row.hour),
                activation_count=int(row.activation_count),
            )
            for row in grouped.itertuples(index=False)
        ]

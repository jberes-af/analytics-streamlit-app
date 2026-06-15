# /src/infrastructure/services/analysis/pandas/activity/sensor_activity_calculator.py

from datetime import date

from src.application.dto.activity_metric_dtos import (
    SensorActivityPercentOfTotalDTO,
    DailyActivityBySensorIdDTO,
    DailyActivityAllSensorsDTO,
    # SensorActivityByDateByTimePeriodDTO,
)

import pandas as pd


class SensorActivityCalculator:

    @staticmethod
    def calculate_total_activity(
            df: pd.DataFrame,
    ) -> list[SensorActivityPercentOfTotalDTO]:
        total_count = len(df)

        grouped = (
            df.groupby("sensor_id")
            .size()
            .rename("total_activations")
            .reset_index()
        )

        results: list[SensorActivityPercentOfTotalDTO] = []

        for row in grouped.itertuples(index=False):
            count = int(row.total_activations)

            results.append(
                SensorActivityPercentOfTotalDTO(
                    sensor_id=row.sensor_id,
                    total_activations=count,
                    percentage_of_total=count / total_count if total_count else 0.0,
                )
            )

        return results

    @staticmethod
    def calculate_sensor_activity_by_id_by_date(
            df: pd.DataFrame,
            start_date: date,
            end_date: date,
            rolling_window_days: int = 7,
    ) -> list[DailyActivityBySensorIdDTO]:

        required_columns: set[str] = {"date", "sensor_id"}

        missing_columns: set[str] = required_columns - set(df.columns)
        if missing_columns:
            raise ValueError(
                "SensorActivityByIdByDateCalculator missing required columns: "
                f"{missing_columns}"
            )

        sensor_ids: list[str] = (
            df["sensor_id"]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )

        if not sensor_ids:
            return []

        full_dates = pd.date_range(
            start=start_date,
            end=end_date,
            freq="D",
        ).date

        full_grid = pd.MultiIndex.from_product(
            [sensor_ids, full_dates],
            names=["sensor_id", "date"],
        ).to_frame(index=False)

        if df.empty:
            grouped = full_grid.copy()
            grouped["activation_count"] = 0
        else:
            working_df: pd.DataFrame = df.copy()
            working_df["sensor_id"] = working_df["sensor_id"].astype(str)
            working_df["date"] = pd.to_datetime(working_df["date"]).dt.date

            grouped_counts: pd.DataFrame = (
                working_df
                .groupby(["sensor_id", "date"])
                .size()
                .rename("activation_count")
                .reset_index()
            )

            grouped = (
                full_grid
                .merge(
                    grouped_counts,
                    on=["sensor_id", "date"],
                    how="left",
                )
                .fillna({"activation_count": 0})
            )

        grouped["activation_count"] = grouped["activation_count"].astype(int)

        grouped = grouped.sort_values(["sensor_id", "date"])

        grouped["rolling_average"] = (
            grouped
            .groupby("sensor_id")["activation_count"]
            .transform(
                lambda s: _rolling_average(
                    s,
                    rolling_window_days,
                )
            )
        )

        return [
            DailyActivityBySensorIdDTO(
                date=row.date,
                sensor_id=row.sensor_id,
                activation_count=int(row.activation_count),
                rolling_average=float(row.rolling_average),
            )
            for row in grouped.itertuples(index=False)
        ]

    @staticmethod
    def calculate_all_sensors_by_date(
            df: pd.DataFrame,
            start_date: date,
            end_date: date,
            rolling_window_days: int = 7,
    ) -> list[DailyActivityAllSensorsDTO]:

        required_columns: set[str] = {"date"}

        if df.empty:
            return [
                DailyActivityAllSensorsDTO(
                    date=current_date.date(),
                    activation_count=0,
                    rolling_average=0.0,
                )
                for current_date in pd.date_range(start=start_date, end=end_date)
            ]

        missing_columns = required_columns - set(df.columns)
        if missing_columns:
            raise ValueError(
                "AllSensorActivityByDateCalculator missing required columns: "
                f"{missing_columns}"
            )

        working_df = df.copy()
        working_df["date"] = pd.to_datetime(working_df["date"]).dt.date

        grouped = (
            working_df
            .groupby("date")
            .size()
            .rename("activation_count")
            .reset_index()
        )

        full_date_range = pd.DataFrame(
            {
                "date": [
                    d.date()
                    for d in pd.date_range(start=start_date, end=end_date)
                ]
            }
        )

        grouped = (
            full_date_range
            .merge(grouped, on="date", how="left")
            .fillna({"activation_count": 0})
            .sort_values("date")
        )

        grouped["activation_count"] = grouped["activation_count"].astype(int)

        grouped["rolling_average"] = _rolling_average(
            grouped["activation_count"],
            rolling_window_days,
        )

        return [
            DailyActivityAllSensorsDTO(
                date=row.date,
                activation_count=int(row.activation_count),
                rolling_average=float(row.rolling_average),
            )
            for row in grouped.itertuples(index=False)
        ]


def _rolling_average(
    series: pd.Series,
    window: int,
) -> pd.Series:
    if window <= 0:
        raise ValueError("rolling window must be greater than zero")

    rolling = (
        series
        .rolling(
            window=window,
            min_periods=window,
        )
        .mean()
    )

    return rolling.fillna(0.0)

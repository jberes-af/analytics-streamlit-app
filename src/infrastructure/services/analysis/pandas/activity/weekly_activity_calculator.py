# /src/infrastructure/services/analysis/pandas/activity/weekly_activity_calculator.py

import pandas as pd

from src.application.dto.activity_metric_dtos import SensorWeeklyActivityDTO


class WeeklyActivityCalculator:
    required_columns = {"date", "sensor_id"}

    def calculate_from_daily_counts(
        self,
        df: pd.DataFrame,
    ) -> list[SensorWeeklyActivityDTO]:
        if df.empty:
            return []

        missing_columns = self.required_columns - set(df.columns)
        if missing_columns:
            raise ValueError(
                f"WeeklyActivityCalculator missing required columns: {missing_columns}"
            )

        grouped = (
            df.groupby(["sensor_id", "date"])
            .size()
            .rename("activation_count")
            .reset_index()
            .sort_values(["sensor_id", "date"])
        )

        results: list[SensorWeeklyActivityDTO] = []

        for sensor_id, sensor_group in grouped.groupby("sensor_id"):
            daily_counts = (
                sensor_group
                .set_index("date")["activation_count"]
                .sort_index()
            )

            full_week_count = len(daily_counts) // 7

            if full_week_count == 0:
                continue

            # Use most recent complete weeks only.
            recent_daily_counts = daily_counts.tail(full_week_count * 7)

            previous_week_total: int | None = None

            for week_index in range(full_week_count):
                week_series = recent_daily_counts.iloc[
                    week_index * 7 : (week_index + 1) * 7
                ]

                week_start = week_series.index.min()
                week_end = week_series.index.max()

                total_activations_week = int(week_series.sum())
                maximum_daily_activations = int(week_series.max())
                minimum_daily_activations = int(week_series.min())
                average_daily_activations = float(week_series.mean())
                standard_deviation = float(week_series.std(ddof=0))

                coefficient_variation = (
                    standard_deviation / average_daily_activations
                    if average_daily_activations
                    else 0.0
                )

                change_percent = (
                    (total_activations_week / previous_week_total) - 1
                    if previous_week_total not in (None, 0)
                    else None
                )

                results.append(
                    SensorWeeklyActivityDTO(
                        sensor_id=sensor_id,
                        week_start=week_start,
                        week_end=week_end,
                        total_activations_week=total_activations_week,
                        maximum_daily_activations=maximum_daily_activations,
                        minimum_daily_activations=minimum_daily_activations,
                        average_daily_activations=average_daily_activations,
                        standard_deviation_daily_activations=standard_deviation,
                        coefficient_variation=coefficient_variation,
                        change_percent=change_percent,
                    )
                )

                previous_week_total = total_activations_week

        return results

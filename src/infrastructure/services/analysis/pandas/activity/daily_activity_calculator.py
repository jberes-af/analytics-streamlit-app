# /src/infrastructure/services/analysis/pandas/activity/daily_activity_calculator.py

from src.application.dto.activity_metric_dtos import DailyActivityDTO

import pandas as pd


class DailyActivityCalculator:
    required_columns = {"date", "timestamp"}

    def calculate_date_time(
            self,
            df: pd.DataFrame,
    ) -> list[DailyActivityDTO]:
        if df.empty:
            return []

        missing_columns = self.required_columns - set(df.columns)

        if missing_columns:
            raise ValueError(
                f"DailyActivityCalculator missing required columns: {missing_columns}"
            )

        grouped = (
            df.groupby("date")["timestamp"]
            .agg(
                total_activations="count",
                first_activation="min",
                last_activation="max",
            )
            .reset_index()
        )

        results: list[DailyActivityDTO] = []

        for row in grouped.itertuples(index=False):
            active_day_length = row.last_activation - row.first_activation

            results.append(
                DailyActivityDTO(
                    date=row.date,
                    total_activations=int(row.total_activations),
                    first_activation=row.first_activation.to_pydatetime(),
                    last_activation=row.last_activation.to_pydatetime(),
                    active_day_length=active_day_length,
                )
            )

        return results

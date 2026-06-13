# /src/infrastructure/services/analysis/pandas/activity/hourly_activity_calculator.py

from src.application.dto.activity_metric_dtos import (
    HourlyActivityDTO,
)

import pandas as pd


class HourlyActivityCalculator:

    def calculate_by_date_by_hour(
            self,
            df: pd.DataFrame,
    ) -> list[HourlyActivityDTO]:
        if df.empty:
            return []

        grouped = (
            df.groupby(["date", "hour"])
            .size()
            .rename("activation_count")
            .reset_index()
        )

        results: list[HourlyActivityDTO] = []

        for row in grouped.itertuples(index=False):
            results.append(
                HourlyActivityDTO(
                    date=row.date,
                    hour=int(row.hour),
                    activation_count=int(row.activation_count),
                )
            )

        return results

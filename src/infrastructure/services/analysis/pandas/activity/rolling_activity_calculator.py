# /src/infrastructure/services/analysis/pandas/activity/rolling_activity_calculator.py

from src.application.dto.activity_metric_dtos import (
    RollingActivityDTO,
)

import pandas as pd


class RollingActivityCalculator:

    def __init__(
            self,
            rolling_window: str = "30min",
            rolling_frequency: str = "1min",
    ) -> None:
        self.rolling_window = rolling_window
        self.rolling_frequency = rolling_frequency

    def calculate_by_frequency(
            self,
            df: pd.DataFrame,
    ) -> list[RollingActivityDTO]:
        if df.empty:
            return []

        events = df.set_index("timestamp").sort_index()

        per_minute_counts = (
            events.resample(self.rolling_frequency)
            .size()
            .rename("activation_count")
        )

        rolling_counts = (
            per_minute_counts
            .rolling(self.rolling_window)
            .sum()
            .fillna(0)
            .astype(int)
        )

        window_offset = pd.Timedelta(self.rolling_window)

        results: list[RollingActivityDTO] = []

        for window_end, activation_count in rolling_counts.items():
            window_start = window_end - window_offset

            results.append(
                RollingActivityDTO(
                    window_start=window_start.to_pydatetime(),
                    window_end=window_end.to_pydatetime(),
                    activation_count=int(activation_count),
                )
            )

        return results

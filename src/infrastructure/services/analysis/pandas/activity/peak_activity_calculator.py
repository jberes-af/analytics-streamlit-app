# /src/infrastructure/services/analysis/pandas/activity/peak_activity_calculator.py

import pandas as pd

from src.application.dto.activity_metric_dtos import PeakActivityDTO


class PeakActivityCalculator:
    required_columns = {"timestamp"}

    def __init__(
        self,
        rolling_window: str = "30min",
        rolling_frequency: str = "1min",
        top_n: int = 5,
    ) -> None:
        self.rolling_window = rolling_window
        self.rolling_frequency = rolling_frequency
        self.top_n = top_n

    def calculate_by_rolling_window(
        self,
        df: pd.DataFrame,
    ) -> list[PeakActivityDTO]:
        if df.empty:
            return []

        missing_columns = self.required_columns - set(df.columns)

        if missing_columns:
            raise ValueError(
                f"PeakActivityCalculator missing required columns: {missing_columns}"
            )

        events = df.set_index("timestamp").sort_index()

        per_minute_counts = (
            events
            .resample(self.rolling_frequency)
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

        # Remove empty windows
        rolling_counts = rolling_counts[rolling_counts > 0]

        if rolling_counts.empty:
            return []

        window_offset = pd.Timedelta(self.rolling_window)

        # Simple version: top N highest rolling windows.
        # Later, you may want to suppress overlapping windows.
        top_windows = rolling_counts.sort_values(
            ascending=False,
        ).head(self.top_n)

        results: list[PeakActivityDTO] = []

        for rank, (window_end, activation_count) in enumerate(
            top_windows.items(),
            start=1,
        ):
            window_start = window_end - window_offset

            results.append(
                PeakActivityDTO(
                    window_start=window_start.to_pydatetime(),
                    window_end=window_end.to_pydatetime(),
                    activation_count=int(activation_count),
                    rank=rank,
                )
            )

        return results

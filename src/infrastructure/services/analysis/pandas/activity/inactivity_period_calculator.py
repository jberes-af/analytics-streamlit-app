# /src/infrastructure/services/analysis/pandas/activity/inactivity_period_calculator.py

import pandas as pd

from src.application.dto.activity_metric_dtos import InactivityPeriodDTO


class InactivityPeriodCalculator:
    required_columns = {"timestamp"}

    def __init__(
        self,
        minimum_duration: str = "1h",
        top_n: int | None = None,
    ) -> None:
        self.minimum_duration = pd.Timedelta(minimum_duration)
        self.top_n = top_n

    def calculate_by_timestamp(
        self,
        df: pd.DataFrame,
    ) -> list[InactivityPeriodDTO]:
        if df.empty:
            return []

        missing_columns = self.required_columns - set(df.columns)

        if missing_columns:
            raise ValueError(
                f"InactivityPeriodCalculator missing required columns: {missing_columns}"
            )

        timestamps = (
            pd.to_datetime(df["timestamp"])
            .sort_values()
            .reset_index(drop=True)
        )

        if len(timestamps) < 2:
            return []

        gaps = timestamps.diff()

        results: list[InactivityPeriodDTO] = []

        for index, duration in gaps.items():
            if index == 0:
                continue

            if duration < self.minimum_duration:
                continue

            start_time = timestamps.iloc[index - 1]
            end_time = timestamps.iloc[index]

            results.append(
                InactivityPeriodDTO(
                    start_time=start_time.to_pydatetime(),
                    end_time=end_time.to_pydatetime(),
                    duration=duration.to_pytimedelta(),
                )
            )

        results.sort(
            key=lambda item: item.duration,
            reverse=True,
        )

        if self.top_n is not None:
            results = results[: self.top_n]

        return results
# /src/infrastructure/services/analysis/pandas/activity/inactivity_period_calculator.py

from datetime import date, timedelta
import pandas as pd

from src.application.dto.activity_metric_dtos import InactivityPeriodDTO

TIME_PERIOD: int = 7

class InactivityPeriodCalculator:
    required_columns = {"timestamp", "date"}

    def __init__(
            self,
            minimum_duration: str = "1h",
            top_n: int | None = None,
            window_days: int | None = 7,
    ) -> None:
        self.minimum_duration = pd.Timedelta(minimum_duration)
        self.top_n = top_n
        self.window_days = window_days

    def calculate_by_timestamp(
            self,
            df: pd.DataFrame,
            end_date: date,
    ) -> list[InactivityPeriodDTO]:
        if df.empty:
            return []

        missing_columns = self.required_columns - set(df.columns)

        if missing_columns:
            raise ValueError(
                f"InactivityPeriodCalculator missing required columns: {missing_columns}"
            )

        start_date = end_date - timedelta(days=self.window_days - 1)
        mask: pd.Series = df["date"].between(start_date, end_date)
        df_sliced: pd.DataFrame = df.loc[mask].copy()
        if df_sliced.empty:
            return []

        timestamps = (
            pd.to_datetime(df_sliced["timestamp"])
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

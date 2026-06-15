# /src/infrastructure/services/analysis/pandas/activity/sensor_activity_trend_calculator.py

from sklearn.linear_model import LinearRegression
from numpy.typing import NDArray

from src.application.dto.activity_metric_dtos import ActivityTrendDTO

import numpy as np
import pandas as pd

ALL_SENSORS_ID = "ALL"
TREND_PERIODS = [7, 14, 30]


class ActivityTrendCalculator:
    def __init__(
            self,
            rolling_window_days: int | None = 7,
    ) -> None:
        self._rolling_window_days = rolling_window_days

    def calculate_trend_for_all_sensors_from_daily_counts(
            self,
            df: pd.DataFrame,
            metric_name: str,
    ) -> list[ActivityTrendDTO]:

        daily_counts = (
            df.groupby("date")
            .size()
            .rename("activation_count")
            .sort_index()
        )

        date_index = pd.date_range(
            start=daily_counts.index.min(),
            end=daily_counts.index.max(),
            freq="D",
        ).date

        daily_counts = daily_counts.reindex(
            date_index,
            fill_value=0,
        )

        return self._calculate_trends_for_daily_counts(
            daily_counts=daily_counts,
            metric_name=metric_name,
            sensor_id=ALL_SENSORS_ID,
        )

    def calculate_trend_by_sensor_id_from_table(
            self,
            df: pd.DataFrame,
            metric_name: str,
    ) -> list[ActivityTrendDTO]:
        required_columns = {"date", "sensor_id"}

        if df.empty:
            return []

        missing_columns = required_columns - set(df.columns)
        if missing_columns:
            raise ValueError(
                f"ActivityTrendCalculator missing required columns: {missing_columns}"
            )

        grouped = (
            df.groupby(["sensor_id", "date"])
            .size()
            .rename("activation_count")
            .reset_index()
            .sort_values(["sensor_id", "date"])
        )

        results: list[ActivityTrendDTO] = []

        for sensor_id, sensor_group in grouped.groupby("sensor_id"):
            daily_counts = (
                sensor_group
                .set_index("date")["activation_count"]
                .sort_index()
            )

            results.extend(
                self._calculate_trends_for_daily_counts(
                    daily_counts=daily_counts,
                    metric_name=metric_name,
                    sensor_id=str(sensor_id),
                )
            )

        return results

    def _calculate_trends_for_daily_counts(
            self,
            daily_counts: pd.Series,
            metric_name: str,
            sensor_id: str,
    ) -> list[ActivityTrendDTO]:
        if daily_counts.empty or len(daily_counts) < 2:
            return []

        y_series = self._smooth_series(daily_counts)

        if len(y_series) < 2:
            return []

        results: list[ActivityTrendDTO] = []

        for points in TREND_PERIODS:
            period_series = y_series.tail(points)

            trend_result = self._calculate_trend_direction_for_period_length(
                y_series_00=y_series,
                last_smoothed_points_count=points,
            )

            if trend_result is None:
                continue

            slope, intercept, direction = trend_result

            results.append(
                ActivityTrendDTO(
                    metric_name=f"{metric_name}_{sensor_id}_last_{points}_days",
                    slope_per_day=slope,
                    intercept=intercept,
                    direction=direction,
                    start_date=period_series.index.min(),
                    end_date=period_series.index.max(),
                    sensor_id=sensor_id,
                )
            )

        return results

    def _smooth_series(
            self,
            daily_counts: pd.Series,
    ) -> pd.Series:
        daily_counts = daily_counts.sort_index()

        if self._rolling_window_days is None:
            return daily_counts

        return (
            daily_counts
            .rolling(window=self._rolling_window_days)
            .mean()
            .dropna()
        )

    def _calculate_trend_direction_for_period_length(
            self,
            y_series_00: pd.Series,
            last_smoothed_points_count: int,
    ) -> tuple[float, float, str] | None:

        y_series: pd.Series = y_series_00.tail(last_smoothed_points_count)

        if len(y_series) < 2:
            return None

        x: NDArray[np.int_] = np.arange(len(y_series)).reshape(-1, 1)
        y: NDArray[np.float64] = y_series.to_numpy()

        model: LinearRegression = LinearRegression()
        model.fit(x, y)

        slope: float = float(model.coef_[0])
        intercept: float = float(model.intercept_)

        start_value: float = float(y[0])
        end_value: float = float(y[-1])

        direction: str = self._classify_trend(
            slope_per_day=slope,
            start_value=start_value,
            end_value=end_value,
        )

        return slope, intercept, direction

    @staticmethod
    def _classify_trend(
            slope_per_day: float,
            start_value: float,
            end_value: float,
            min_slope_per_day: float = 0.15,
            min_percent_change: float = 0.20,
    ) -> str:
        if start_value == 0:
            percent_change = 0
        else:
            percent_change = (end_value - start_value) / start_value

        if slope_per_day >= min_slope_per_day and percent_change >= min_percent_change:
            return "increasing"

        if slope_per_day <= -min_slope_per_day and percent_change <= -min_percent_change:
            return "decreasing"

        return "stable"

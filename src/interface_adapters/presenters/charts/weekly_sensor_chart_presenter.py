# /src/interface/adapters/presenters/charts/weekly_sensor_chart_presenter.py

from datetime import date
from typing import Sequence

from src.application.dto.activity_metric_dtos import (
    SensorWeeklyActivityDTO,
)

from src.interface_adapters.view_models.charts_view_model import (
    PointVM,
    SeriesVM,
    ScatterLineChartWeeklyVM,
)

ALL_SENSORS_KEY = "ALL"


class SensorActivityByWeekChartPresenter:

    def present_sensor_activations_by_week_chart(
        self,
        sensor_ids: list[str],
        weekly_sensor_activity: list[SensorWeeklyActivityDTO],
    ) -> dict[str, ScatterLineChartWeeklyVM]:

        result: dict[str, ScatterLineChartWeeklyVM] = {}

        events_mapping: dict[str, list[SensorWeeklyActivityDTO]] = {}

        for item in weekly_sensor_activity:
            events_mapping.setdefault(item.sensor_id, []).append(item)

        # --- ALL SENSORS

        all_values = events_mapping.get(ALL_SENSORS_KEY, [])

        if all_values:
            result[ALL_SENSORS_KEY] = self._build_view_model(
                title="Weekly Activations - All Sensors",
                x_axis_label="Week Ending",
                y_axis_label="Activation Count",
                weekly_activity=all_values,
            )

        # --- INDIVIDUAL SENSORS

        for sensor_id in sensor_ids:
            values = events_mapping.get(sensor_id, [])

            if not values:
                continue

            result[sensor_id] = self._build_view_model(
                title=f"Weekly Activations - {sensor_id.upper()}",
                x_axis_label="Week Ending",
                y_axis_label="Activation Count",
                weekly_activity=values,
            )

        return result

    @staticmethod
    def _build_view_model(
        *,
        title: str,
        x_axis_label: str,
        y_axis_label: str,
        weekly_activity: Sequence[SensorWeeklyActivityDTO],
    ) -> ScatterLineChartWeeklyVM:

        sorted_values = sorted(
            weekly_activity,
            key=lambda item: item.week_end,
        )

        x_series: list[date] = [
            item.week_end
            for item in sorted_values
        ]

        min_points: list[PointVM] = [
            PointVM(
                x=item.week_end,
                y=item.minimum_daily_activations,
            )
            for item in sorted_values
        ]

        max_points: list[PointVM] = [
            PointVM(
                x=item.week_end,
                y=item.maximum_daily_activations,
            )
            for item in sorted_values
        ]

        avg_points: list[PointVM] = [
            PointVM(
                x=item.week_end,
                y=item.average_daily_activations,
            )
            for item in sorted_values
        ]

        x_tick_labels: list[str] = [
            week_end.strftime("%m-%d")
            for week_end in x_series
        ]

        return ScatterLineChartWeeklyVM(
            title=title,
            x_axis_label=x_axis_label,
            y_axis_label=y_axis_label,
            x_tick_labels=x_tick_labels,
            y_tick_labels=None,
            scatter_series_min=[
                SeriesVM(
                    name="Daily Minimum",
                    points=min_points,
                )
            ],
            scatter_series_max=[
                SeriesVM(
                    name="Daily Maximum",
                    points=max_points,
                )
            ],
            line_series=[
                SeriesVM(
                    name="Daily Average",
                    points=avg_points,
                )
            ],
            x_tick_coords=None,
            y_tick_coords=None,
        )

# /src/interface/adapters/presenters/charts/sensor_chart_presenter.py

from datetime import date

from typing import Sequence

from src.application.dto.activity_uc_dtos import (
    SensorByIdByDateActivityDTO,
    SensorAllByDateActivityDTO,
)

from src.interface_adapters.view_models.charts_view_model import (
    PointVM,
    SeriesVM,
    LineChartVM,
    ScatterLineChartVM,
)

ALL_SENSORS_KEY = "ALL"


class SensorActivityByDateChartPresenter:

    def present_sensor_activations_by_date_chart(
            self,
            sensor_ids: list[str],
            sensor_by_id_events: list[SensorByIdByDateActivityDTO],
            all_sensor_events: list[SensorAllByDateActivityDTO],
    ) -> dict[str, ScatterLineChartVM]:  # dict[str, LineChartVM]:

        # result: dict[str, LineChartVM] = {}
        result: dict[str, ScatterLineChartVM] = {}

        # --- ALL SENSORS FIRST

        all_sorted_by_date: list[SensorAllByDateActivityDTO] = sorted(
            all_sensor_events,
            key=lambda event: event.date,
        )

        if all_sorted_by_date:
            result[ALL_SENSORS_KEY] = self._build_view_model(
                title="Daily Activations - All Sensors",
                x_axis_label="Date",
                y_axis_label="Activation Count",
                x_series=[event.date for event in all_sorted_by_date],
                y_series_actual=[
                    event.activation_count
                    for event in all_sorted_by_date
                ],
                y_series_rolling=[
                    event.rolling_average
                    for event in all_sorted_by_date
                ],
            )

        # --- INDIVIDUAL SENSORS

        events_mapping: dict[str, list[SensorByIdByDateActivityDTO]] = {}

        for event in sensor_by_id_events:
            events_mapping.setdefault(event.sensor_id, []).append(event)

        for sensor_id in sensor_ids:
            values: list[SensorByIdByDateActivityDTO] = (
                events_mapping.get(sensor_id, []))

            if not values:
                continue

            sorted_by_date: list[SensorByIdByDateActivityDTO] = sorted(
                values,
                key=lambda event: event.date,
            )

            result[sensor_id] = self._build_view_model(
                title=f"Daily Activations - {sensor_id.upper()}",
                x_axis_label="Date",
                y_axis_label="Activation Count",
                x_series=[event.date for event in sorted_by_date],
                y_series_actual=[
                    event.activation_count
                    for event in sorted_by_date
                ],
                y_series_rolling=[
                    event.rolling_average
                    for event in sorted_by_date
                ],
            )

        return result

    @staticmethod
    def _build_view_model(
            *,
            title: str,
            x_axis_label: str,
            y_axis_label: str,
            x_series: Sequence[date | int | float],
            y_series_actual: Sequence[int | float],
            y_series_rolling: Sequence[int | float],
    ) -> ScatterLineChartVM:  # LineChartVM:
        if not (
                len(x_series) == len(y_series_actual) == len(y_series_rolling)
        ):
            raise ValueError(
                "x_series, y_series_actual, and y_series_rolling must have same length "
                f"{len(x_series)} vs {len(y_series_actual)} vs {len(y_series_rolling)}"
            )

        points_actual = [
            PointVM(x=x, y=y)
            for x, y in zip(x_series, y_series_actual)
        ]

        points_rolling = [
            PointVM(x=x, y=y)
            for x, y in zip(x_series, y_series_rolling)
        ]

        x_tick_labels = [
            x.strftime("%m%d") if isinstance(x, date) else str(x)
            for x in x_series
        ]

        return ScatterLineChartVM(
            title=title,
            x_axis_label=x_axis_label,
            y_axis_label=y_axis_label,
            x_tick_labels=x_tick_labels,
            y_tick_labels=None,
            scatter_series=[
                SeriesVM(
                    name="Actual Activations",
                    points=points_actual,
                )
            ],
            line_series=[
                SeriesVM(
                    name="Rolling Average",
                    points=points_rolling,
                )
            ],
        )

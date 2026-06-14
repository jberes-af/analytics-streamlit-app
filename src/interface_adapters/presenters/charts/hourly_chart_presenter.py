# # /src/interface/adapters/presenters/charts/hourly_chart_presenter.py

from collections import defaultdict
from datetime import date, timedelta
from typing import Sequence

from src.domain.entities.sensor import SensorEvent

from src.application.dto.activity_metric_dtos import (
    HourlyActivityDTO,
)

from src.interface_adapters.view_models.charts_view_model import (
    PointVM,
    SeriesVM,
    ScatterChartVM,
    BarVM,
    BarChartVM,
)

from src.interface_adapters.utilities_data import (
    convert_datetime_to_seconds_since_midnight,
)


class SensorActivityTimestampScatterChartPresenter:

    def present(
            self,
            date_range: list[date],
            sensor_ids: list[str],
            sensor_events: list[SensorEvent],
    ):
        result: dict[str, ScatterChartVM] = {}

        events_mapping: dict[str, list[SensorEvent]] = {}

        for event in sensor_events:
            events_mapping.setdefault(event.sensor_id, []).append(event)

        date_to_day_index: dict[date, int] = {
            current_date: index + 1
            for index, current_date in enumerate(date_range)
        }

        x_tick_coords = list(range(1, len(date_range) + 1))
        x_tick_labels = [
            current_date.strftime("%m-%d")
            for current_date in date_range
        ]

        # Keep every 2nd tick
        tick_step = 2
        x_tick_coords = x_tick_coords[::tick_step]
        x_tick_labels = x_tick_labels[::tick_step]

        y_tick_coords: Sequence[int] = [
            0, 6 * 3600, 12 * 3600, 18 * 3600, 24 * 3600,
        ]

        y_tick_labels: Sequence[str] = [
            "12 AM", "6 AM", "12 PM", "6 PM", "12 AM",
        ]

        for sensor_id in sensor_ids:
            values = events_mapping.get(sensor_id, [])

            if not values:
                continue

            sorted_events = sorted(
                values,
                key=lambda event: event.activated_at,
            )

            points: list[PointVM] = []

            for event in sorted_events:
                event_date = event.activated_at.date()

                if event_date not in date_to_day_index:
                    continue

                points.append(
                    PointVM(
                        x=date_to_day_index[event_date],
                        y=convert_datetime_to_seconds_since_midnight(
                            event.activated_at
                        ),
                    )
                )

            series = [
                SeriesVM(
                    name=f"timestamp_series_{sensor_id}",
                    points=points,
                )
            ]

            chart_vm = ScatterChartVM(
                title=f"Sensor Activation Timestamps {sensor_id.upper()}",
                x_axis_label="Date",
                y_axis_label="Time of Day",
                x_tick_coords=x_tick_coords,
                y_tick_coords=y_tick_coords,
                x_tick_labels=x_tick_labels,
                y_tick_labels=y_tick_labels,
                series=series,
            )

            result[sensor_id] = chart_vm

        return result


class HourlyActivityAllSensorsBarChartPresenter:
    def present_hourly_chart(
            self,
            hourly_activity: list[HourlyActivityDTO],
    ) -> BarChartVM:
        if not hourly_activity:
            return self._empty_chart()

        counts_by_hour: dict[int, list[int]] = defaultdict(list)

        for item in hourly_activity:
            counts_by_hour[item.hour].append(item.activation_count)

        bars: list[BarVM] = []

        for hour in range(24):
            counts = counts_by_hour.get(hour, [])

            average_count = (
                sum(counts) / len(counts)
                if counts
                else 0.0
            )

            hour_label = f"{hour:02d}:00"

            bars.append(
                BarVM(
                    category=hour_label,
                    value=average_count,
                    category_label=hour_label,
                    value_label=f"{average_count:.1f}",
                )
            )

        return BarChartVM(
            title="Average Hourly Activity - Last 7 Days",
            x_axis_label="Average Activation Count",
            y_axis_label="Hour of Day",
            bars=bars,
        )

    @staticmethod
    def _empty_chart() -> BarChartVM:
        return BarChartVM(
            title="Average Hourly Activity - Last 7 Days",
            x_axis_label="Average Activation Count",
            y_axis_label="Hour of Day",
            bars=[],
        )

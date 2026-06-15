# timestamp_dot_chart_presenter

from datetime import date, datetime
from typing import Sequence
from zoneinfo import ZoneInfo

from src.domain.entities.sensor import SensorEvent
from src.interface_adapters.utilities_data import convert_datetime_to_seconds_since_midnight
from src.interface_adapters.view_models.charts_view_model import ScatterChartVM, PointVM, SeriesVM

from src.interface_adapters.utilities_data import (
    get_start_date_from_end_date_and_days_delta,
    convert_date_to_datetime,
    filter_events_by_time_period,
    get_date_range_in_between_two_dates,
)


class SensorActivityTimestampScatterChartPresenter:

    def present_timestamp_chart(
            self,
            sensor_ids: list[str],
            sensor_events: list[SensorEvent],
            start_date: date | None,
            end_date: date | None,
            tail_day_count: int | None,
            local_timezone: str,
    ):
        result: dict[str, ScatterChartVM] = {}

        tail_days_events: list[SensorEvent] = _preprocess_input_dates(
            end_date=end_date,
            tail_day_count=tail_day_count,
            sensor_events=sensor_events,
            local_timezone=local_timezone,
        )

        events_mapping: dict[str, list[SensorEvent]] = {}

        for event in tail_days_events:
            events_mapping.setdefault(event.sensor_id, []).append(event)

        date_range: list[date] = get_date_range_in_between_two_dates(
            start_date=start_date,
            end_date=end_date,
        )

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

            result[sensor_id] = self._build_view_model(
                sensor_id=sensor_id,
                values=values,
                date_to_day_index=date_to_day_index,
                x_tick_coords=x_tick_coords,
                y_tick_coords=y_tick_coords,
                x_tick_labels=x_tick_labels,
                y_tick_labels=y_tick_labels,

            )

        return result

    @staticmethod
    def _build_view_model(
            sensor_id: str,
            values: list[SensorEvent],
            date_to_day_index: dict[date, int],
            x_tick_coords: Sequence[int],
            y_tick_coords: Sequence[int],
            x_tick_labels: Sequence[str],
            y_tick_labels: Sequence[str],

    ) -> ScatterChartVM:

        sorted_events = sorted(
            values,
            key=lambda event: event.activated_at_utc,
        )

        points: list[PointVM] = []

        for event in sorted_events:
            event_date = event.activated_at_utc.date()

            if event_date not in date_to_day_index:
                continue

            points.append(
                PointVM(
                    x=date_to_day_index[event_date],
                    y=convert_datetime_to_seconds_since_midnight(
                        event.activated_at_utc
                    ),
                )
            )

        series = [
            SeriesVM(
                name=f"timestamp_series_{sensor_id}",
                points=points,
            )
        ]

        return ScatterChartVM(
            title=f"Sensor Activation Timestamps {sensor_id.upper()}",
            x_axis_label="Date",
            y_axis_label="Time of Day",
            x_tick_coords=x_tick_coords,
            y_tick_coords=y_tick_coords,
            x_tick_labels=x_tick_labels,
            y_tick_labels=y_tick_labels,
            series=series,
        )


def _preprocess_input_dates(
        end_date: date | None,
        tail_day_count: int | None,
        sensor_events: list[SensorEvent],
        local_timezone: str,
) -> list[SensorEvent]:
    start_date: date = get_start_date_from_end_date_and_days_delta(
        end_date=end_date,
        days_delta=tail_day_count,
    )

    start_time: datetime
    end_time: datetime
    start_time, end_time = convert_date_to_datetime(
        start_date=start_date,
        end_date=end_date,
        local_timezone=local_timezone,
    )

    tail_days_events: list[SensorEvent] = filter_events_by_time_period(
        events=sensor_events,
        start_time=start_time,
        end_time=end_time,
    )

    return tail_days_events

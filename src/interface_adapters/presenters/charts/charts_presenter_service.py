# /src/interface_adapters/presenters/chart/charts_presenter_service.py

from datetime import date, datetime, timedelta
from typing import Sequence

from src.domain.entities.sensor import SensorEvent

from src.application.dto.activity_uc_dtos import (
    HourlyActivityDTO,
    SensorByIdByDateActivityDTO,
)

from src.interface_adapters.view_models.charts_view_model import (
    BarVM,
    BarChartVM,
    LineChartVM,
    ScatterChartVM,
)

from src.interface_adapters.presenters.charts.sensor_chart_presenter import (
    SensorActivityLineChartPresenter,
)

from src.interface_adapters.presenters.charts.hourly_chart_presenter import (
    HourlyActivityAllSensorsBarChartPresenter,
    SensorActivityTimestampScatterChartPresenter,
)

from src.interface_adapters.utilities_data import (
    get_start_date_from_end_date_and_days_delta,
    convert_date_to_datetime,
    filter_events_by_time_period,
)


class ChartsPresenterService:

    def present_sensor_activations_bar_chart(
            self,
            sensor_ids: list[str],
            sensor_by_id_events: list[SensorByIdByDateActivityDTO],
            start_date: date,
            end_date: date,
    ) -> dict[str, BarChartVM]:

        result: dict[str, BarChartVM] = {}

        events_mapping: dict[str, list[SensorByIdByDateActivityDTO]] = {}

        for event in sensor_by_id_events:
            events_mapping.setdefault(event.sensor_id, []).append(event)

        all_dates = self._date_range(
            start_date=start_date,
            end_date=end_date,
        )

        for sensor_id in sensor_ids:
            values = events_mapping.get(sensor_id, [])

            counts_by_date: dict[date, int] = {
                event.date: event.activation_count
                for event in values
            }

            bars: list[BarVM] = []

            for current_date in all_dates:
                activation_count = counts_by_date.get(current_date, 0)

                bars.append(
                    BarVM(
                        category=current_date.isoformat(),
                        value=activation_count,
                        category_label=current_date.strftime("%m%d"),
                        value_label=f"{activation_count:,}",
                    )
                )

            chart_vm = BarChartVM(
                title=f"Daily Activations {sensor_id.upper()}",
                x_axis_label="Date",
                y_axis_label="Activation Count",
                bars=bars,
            )

            result[sensor_id] = chart_vm

        return result

    @staticmethod
    def present_sensor_activations_line_chart(
            sensor_ids: list[str],
            sensor_by_id_events: list[SensorByIdByDateActivityDTO],
    ) -> dict[str, LineChartVM]:

        result: dict[str, LineChartVM] = {}

        events_mapping: dict[str, list[SensorByIdByDateActivityDTO]] = {}

        for event in sensor_by_id_events:
            events_mapping.setdefault(event.sensor_id, []).append(event)

        for sensor_id in sensor_ids:
            values = events_mapping.get(sensor_id, [])

            if not values:
                continue

            sorted_by_date = sorted(
                values,
                key=lambda event: event.date,
            )

            x_series: Sequence[date] = [event.date for event in sorted_by_date]
            y_series: Sequence[int] = [
                event.activation_count
                for event in sorted_by_date
            ]

            title: str = f"Daily Activations {sensor_id.upper()}"

            presenter: SensorActivityLineChartPresenter = SensorActivityLineChartPresenter()
            chart_vm: LineChartVM = presenter.present(
                title=title,
                x_axis_label="Date",
                y_axis_label="Activation Count",
                x_series=x_series,
                y_series=y_series,
            )

            result[sensor_id] = chart_vm

        return result

    def present_sensor_activations_timestamp_scatter_chart(
            self,
            sensor_ids: list[str],
            sensor_events: list[SensorEvent],
            # sensor_by_id_events: list[SensorByIdByDateActivityDTO],
            start_date: date | None,
            end_date: date | None,
            tail_day_count: int | None,
    ) -> dict[str, ScatterChartVM]:

        start_date: date = get_start_date_from_end_date_and_days_delta(
            end_date=end_date,
            days_delta=tail_day_count,
        )

        start_time: datetime
        end_time: datetime
        start_time, end_time = convert_date_to_datetime(
            start_date=start_date,
            end_date=end_date,
        )

        tail_days_events: list[SensorEvent] = filter_events_by_time_period(
            events=sensor_events,
            start_time=start_time,
            end_time=end_time,
        )

        presenter = SensorActivityTimestampScatterChartPresenter()

        return presenter.present(
            date_range=self._date_range(start_date, end_date),
            sensor_ids=sensor_ids,
            sensor_events=tail_days_events,
        )

    @staticmethod
    def present_hourly_activations_bar_chart(
            sensor_ids: list[str],
            hourly_activity: list[HourlyActivityDTO],
            start_date: date | None,
            end_date: date | None,
            tail_day_count: int | None,
    ) -> BarChartVM:  # dict[str, BarChartVM]:

        start_date: date = get_start_date_from_end_date_and_days_delta(
            end_date=end_date,
            days_delta=tail_day_count,
        )

        tail_days_activity: list[HourlyActivityDTO] = [
            item
            for item in hourly_activity
            if start_date <= item.date <= end_date
        ]

        # end_date = max(item.date for item in hourly_activity)
        # start_date: date = end_date - timedelta(days=6)

        presenter = HourlyActivityAllSensorsBarChartPresenter()

        return presenter.present_hourly_chart(
            hourly_activity=tail_days_activity,
        )

    @staticmethod
    def _date_range(
            start_date: date,
            end_date: date,
    ) -> list[date]:
        if end_date < start_date:
            raise ValueError("end_date must be greater than or equal to start_date")

        days = (end_date - start_date).days

        return [
            start_date + timedelta(days=offset)
            for offset in range(days + 1)
        ]

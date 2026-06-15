# # /src/interface/adapters/presenters/charts/hourly_chart_presenter.py

from collections import defaultdict
from datetime import date, datetime, time

from src.application.dto.activity_metric_dtos import (
    HourlyActivityAllSensorsDTO,
    HourlyActivityBySensorIdDTO,
)

from src.interface_adapters.view_models.charts_view_model import (
    BarVM,
    BarChartVM,
)

from src.interface_adapters.utilities_data import (
    get_start_date_from_end_date_and_days_delta,
)


class HourlyActivityBarChartPresenter:
    def present_hourly_chart(
        self,
        end_date: date,
        tail_day_count: int | None,
        sensor_ids: list[str],
        hourly_activity_all_sensors: list[HourlyActivityAllSensorsDTO],
        hourly_activity_by_sensor_id: list[HourlyActivityBySensorIdDTO],
    ) -> dict[str, BarChartVM]:

        result: dict[str, BarChartVM] = {}

        # --- ALL SENSORS

        all_tail_activity = _preprocess_time_period(
            end_date=end_date,
            tail_day_count=tail_day_count,
            hourly_activity=hourly_activity_all_sensors,
        )

        result["ALL"] = self._build_view_model(
            title="Average Hourly Activity - All Sensors",
            counts_by_hour=self._group_counts_by_hour(all_tail_activity),
        )

        # --- BY SENSOR ID

        by_sensor_tail_activity = _preprocess_time_period(
            end_date=end_date,
            tail_day_count=tail_day_count,
            hourly_activity=hourly_activity_by_sensor_id,
        )

        activity_by_sensor_id: dict[str, list[HourlyActivityBySensorIdDTO]] = defaultdict(list)

        for item in by_sensor_tail_activity:
            activity_by_sensor_id[item.sensor_id].append(item)

        for sensor_id in sensor_ids:
            sensor_activity = activity_by_sensor_id.get(sensor_id, [])

            result[sensor_id] = self._build_view_model(
                title=f"Average Hourly Activity - {sensor_id}",
                counts_by_hour=self._group_counts_by_hour(sensor_activity),
            )

        return result

    @staticmethod
    def _group_counts_by_hour(
        hourly_activity: list[HourlyActivityAllSensorsDTO] | list[HourlyActivityBySensorIdDTO],
    ) -> dict[int, list[int]]:
        counts_by_hour: dict[int, list[int]] = defaultdict(list)

        for item in hourly_activity:
            counts_by_hour[item.hour].append(item.activation_count)

        return counts_by_hour

    @staticmethod
    def _build_view_model(
        title: str,
        counts_by_hour: dict[int, list[int]],
    ) -> BarChartVM:

        bars: list[BarVM] = []

        for hour in range(24):
            counts = counts_by_hour.get(hour, [])

            average_count = (
                sum(counts) / len(counts)
                if counts
                else 0.0
            )

            # hour_label = f"{hour:02d}:00"
            # hour_label = f"{hour:02d}"
            hour_label = time(hour).strftime("%I %p").lstrip("0")

            bars.append(
                BarVM(
                    category=hour_label,
                    value=average_count,
                    category_label=hour_label,
                    value_label=f"{average_count:.1f}",
                )
            )

        return BarChartVM(
            title=title,
            x_axis_label="Average Activation Count",
            y_axis_label="Hour of Day",
            bars=bars,
        )


def _preprocess_time_period(
    end_date: date,
    tail_day_count: int | None,
    hourly_activity: list[HourlyActivityAllSensorsDTO] | list[HourlyActivityBySensorIdDTO],
) -> list[HourlyActivityAllSensorsDTO] | list[HourlyActivityBySensorIdDTO]:

    if tail_day_count is None:
        return hourly_activity

    start_date: date = get_start_date_from_end_date_and_days_delta(
        end_date=end_date,
        days_delta=tail_day_count,
    )

    return [
        item
        for item in hourly_activity
        if start_date <= item.date <= end_date
    ]

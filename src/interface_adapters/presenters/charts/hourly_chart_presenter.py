# # /src/interface/adapters/presenters/charts/hourly_chart_presenter.py

from collections import defaultdict
from datetime import date

from src.application.dto.activity_metric_dtos import (
    HourlyActivityDTO,
)

from src.interface_adapters.view_models.charts_view_model import (
    BarVM,
    BarChartVM,
)

from src.interface_adapters.utilities_data import (
    get_start_date_from_end_date_and_days_delta,
)


class HourlyActivityAllSensorsBarChartPresenter:
    def present_hourly_chart(
            self,
            end_date: date,
            tail_day_count: int | None,
            hourly_activity: list[HourlyActivityDTO],
    ) -> BarChartVM:
        if not hourly_activity:
            return self._empty_chart()

        tail_days_activity: list[HourlyActivityDTO] = (
            _preprocess_time_period(
                end_date=end_date,
                tail_day_count=tail_day_count,
                hourly_activity=hourly_activity,
            )
        )

        counts_by_hour: dict[int, list[int]] = defaultdict(list)

        for item in tail_days_activity:
            counts_by_hour[item.hour].append(item.activation_count)

        return self._build_view_model(counts_by_hour)

    @staticmethod
    def _build_view_model(
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


def _preprocess_time_period(
        end_date: date,
        tail_day_count: int,
        hourly_activity: list[HourlyActivityDTO],
) -> list[HourlyActivityDTO]:
    start_date: date = get_start_date_from_end_date_and_days_delta(
        end_date=end_date,
        days_delta=tail_day_count,
    )

    tail_days_activity: list[HourlyActivityDTO] = [
        item
        for item in hourly_activity
        if start_date <= item.date <= end_date
    ]

    return tail_days_activity

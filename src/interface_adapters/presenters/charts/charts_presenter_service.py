# /src/interface_adapters/presenters/charts/charts_presenter_service.py

from datetime import date, datetime, timedelta
from typing import Sequence

from src.domain.entities.sensor import SensorEvent

from src.application.dto.activity_uc_dtos import (
    DailyActivityBySensorIdDTO,
    DailyActivityAllSensorsDTO,
    HourlyActivityAllSensorsDTO,
    HourlyActivityBySensorIdDTO,
    SensorWeeklyActivityDTO,
)

from src.interface_adapters.view_models.charts_view_model import (
    BarVM,
    BarChartVM,
    LineChartVM,
    ScatterChartVM,
    ScatterLineChartVM,
    ScatterLineChartWeeklyVM,
)

from src.interface_adapters.presenters.charts.daily_sensor_chart_presenter import (
    SensorActivityByDateChartPresenter,
)

from src.interface_adapters.presenters.charts.weekly_sensor_chart_presenter import (
    SensorActivityByWeekChartPresenter,
)

from src.interface_adapters.presenters.charts.hourly_chart_presenter import (
    HourlyActivityBarChartPresenter,
)
from src.interface_adapters.presenters.charts.timestamp_dot_chart_presenter import \
    SensorActivityTimestampScatterChartPresenter


class ChartsPresenterService:

    @staticmethod
    def present_sensor_activations_by_week_chart(
            sensor_ids: list[str],
            weekly_sensor_activity: list[SensorWeeklyActivityDTO],
    ) -> dict[str, ScatterLineChartWeeklyVM]:
        presenter = SensorActivityByWeekChartPresenter()
        return presenter.present_sensor_activations_by_week_chart(
            sensor_ids=sensor_ids,
            weekly_sensor_activity=weekly_sensor_activity,
        )

    @staticmethod
    def present_sensor_activations_by_date_chart(
            sensor_ids: list[str],
            sensor_by_id_events: list[DailyActivityBySensorIdDTO],
            all_sensor_events: list[DailyActivityAllSensorsDTO],
    ) -> dict[str, ScatterLineChartVM]:  # dict[str, LineChartVM]:
        presenter = SensorActivityByDateChartPresenter()
        return presenter.present_sensor_activations_by_date_chart(
            sensor_ids=sensor_ids,
            sensor_by_id_events=sensor_by_id_events,
            all_sensor_events=all_sensor_events,
        )

    @staticmethod
    def present_sensor_activations_timestamp_scatter_chart(
            sensor_ids: list[str],
            sensor_events: list[SensorEvent],
            start_date: date | None,
            end_date: date | None,
            tail_day_count: int | None,
            local_timezone: str,
    ) -> dict[str, ScatterChartVM]:
        presenter = SensorActivityTimestampScatterChartPresenter()

        return presenter.present_timestamp_chart(
            sensor_ids=sensor_ids,
            sensor_events=sensor_events,
            start_date=start_date,
            end_date=end_date,
            tail_day_count=tail_day_count,
            local_timezone=local_timezone,
        )

    @staticmethod
    def present_hourly_activations_bar_chart(
            sensor_ids: list[str],
            hourly_activity_all_sensors: list[HourlyActivityAllSensorsDTO],
            hourly_activity_by_sensor_id: list[HourlyActivityBySensorIdDTO],
            # start_date: date | None,
            end_date: date | None,
            tail_day_count: int | None,
    ) -> dict[str, BarChartVM]:
        presenter = HourlyActivityBarChartPresenter()

        return presenter.present_hourly_chart(
            end_date=end_date,
            tail_day_count=tail_day_count,
            sensor_ids=sensor_ids,
            hourly_activity_all_sensors=hourly_activity_all_sensors,
            hourly_activity_by_sensor_id=hourly_activity_by_sensor_id,
        )

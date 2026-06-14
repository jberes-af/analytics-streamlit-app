# # /src/interface_adapters/output_handlers/activity/activity_charts_handler.py

from datetime import date
from pathlib import Path

from src.domain.entities.sensor import SensorEvent

from src.application.dto.activity_metric_dtos import (
    HourlyActivityDTO,
    SensorByIdByDateActivityDTO,
)

from src.infrastructure.services.renderers.matplotlib.matplotlib_bar_vertical_chart_renderer import (
    MatplotlibVerticalBarChartPlotter,
)

from src.infrastructure.services.renderers.matplotlib.matplotlib_bar_horizontal_chart_renderer import (
    MatplotlibHorizontalBarChartPlotter,
)

from src.infrastructure.services.renderers.matplotlib.matplotlib_line_chart_renderer import (
    MatplotlibLineChartPlotter,
)

from src.infrastructure.services.renderers.matplotlib.matplotlib_scatter_chart_renderer import (
    MatplotlibScatterChartPlotter,
)

from src.interface_adapters.presenters.charts.charts_presenter_service import (
    ChartsPresenterService,
)

from src.interface_adapters.view_models.charts_view_model import (
    LineChartVM,
    BarChartVM,
    ScatterChartVM,
)


def handle_chart_outputs(
        sensor_events: list[SensorEvent],
        sensor_ids: list[str],
        sensor_by_id_events: list[SensorByIdByDateActivityDTO],
        hourly_activity_results: list[HourlyActivityDTO],
        charts_presenter_service: ChartsPresenterService,
        bar_chart_plotter: MatplotlibVerticalBarChartPlotter,
        line_chart_plotter: MatplotlibLineChartPlotter,
        scatter_chart_plotter: MatplotlibScatterChartPlotter,
        start_date: date,
        end_date: date,
        path_results: Path,
) -> None:
    _handle_daily_activations_line_chart(
        sensor_ids=sensor_ids,
        sensor_by_id_events=sensor_by_id_events,
        charts_presenter_service=charts_presenter_service,
        line_chart_plotter=line_chart_plotter,
        start_date=start_date,
        end_date=end_date,
        path_results=path_results,

    )

    _handle_daily_activations_bar_chart(
        sensor_ids=sensor_ids,
        sensor_by_id_events=sensor_by_id_events,
        charts_presenter_service=charts_presenter_service,
        bar_chart_plotter=bar_chart_plotter,
        start_date=start_date,
        end_date=end_date,
        path_results=path_results,
    )

    _handle_sensor_activation_timestamp_scatter_chart(
        sensor_events=sensor_events,
        sensor_ids=sensor_ids,
        # sensor_by_id_events=sensor_by_id_events,
        charts_presenter_service=charts_presenter_service,
        scatter_chart_plotter=scatter_chart_plotter,
        start_date=start_date,
        end_date=end_date,
        tail_day_count=14,
        path_results=path_results,
    )

    _handle_sensor_hourly_activation_bar_chart(
        sensor_ids=sensor_ids,
        hourly_activity=hourly_activity_results,
        charts_presenter_service=charts_presenter_service,
        bar_chart_plotter=bar_chart_plotter,
        start_date=start_date,
        end_date=end_date,
        tail_day_count=7,
        path_results=path_results,
    )


def _handle_daily_activations_line_chart(
        sensor_ids: list[str],
        sensor_by_id_events: list[SensorByIdByDateActivityDTO],
        charts_presenter_service: ChartsPresenterService,
        line_chart_plotter: MatplotlibLineChartPlotter,
        start_date: date,
        end_date: date,
        path_results: Path,
) -> None:
    sensor_to_line_vm_mapping: dict[str, LineChartVM] = (
        charts_presenter_service.present_sensor_activations_line_chart(
            sensor_ids=sensor_ids,
            sensor_by_id_events=sensor_by_id_events,
        ))

    for sensor_id, vm in sensor_to_line_vm_mapping.items():
        chart_path = path_results / "plots" / f"{sensor_id}_daily_activations.png"
        line_chart_plotter.render(
            chart_vm=vm,
            output_path=chart_path,
        )


def _handle_daily_activations_bar_chart(
        sensor_ids: list[str],
        sensor_by_id_events: list[SensorByIdByDateActivityDTO],
        charts_presenter_service: ChartsPresenterService,
        bar_chart_plotter: MatplotlibVerticalBarChartPlotter,
        start_date: date,
        end_date: date,
        path_results: Path,
) -> None:
    sensor_to_bar_vm_mapping: dict[str, BarChartVM] = (
        charts_presenter_service.present_sensor_activations_bar_chart(
            sensor_ids=sensor_ids,
            sensor_by_id_events=sensor_by_id_events,
            start_date=start_date,
            end_date=end_date,
        ))

    for sensor_id, vm in sensor_to_bar_vm_mapping.items():
        chart_path = path_results / "plots" / f"{sensor_id}_daily_activations.png"
        bar_chart_plotter.render(
            chart_vm=vm,
            output_path=chart_path,
        )


def _handle_sensor_activation_timestamp_scatter_chart(
        sensor_events: list[SensorEvent],
        sensor_ids: list[str],
        # sensor_by_id_events: list[SensorByIdByDateActivityDTO],
        charts_presenter_service: ChartsPresenterService,
        scatter_chart_plotter: MatplotlibScatterChartPlotter,
        start_date: date,
        end_date: date,
        tail_day_count: int | None,
        path_results: Path,
) -> None:
    sensor_to_scatter_vm_mapping: dict[str, ScatterChartVM] = (
        charts_presenter_service.present_sensor_activations_timestamp_scatter_chart(
            sensor_ids=sensor_ids,
            sensor_events=sensor_events,
            start_date=start_date,
            end_date=end_date,
            tail_day_count=tail_day_count
        ))

    for sensor_id, vm in sensor_to_scatter_vm_mapping.items():
        chart_path = path_results / "plots" / f"{sensor_id}_timestamp_scatter.png"
        scatter_chart_plotter.render(
            chart_vm=vm,
            output_path=chart_path,
        )


def _handle_sensor_hourly_activation_bar_chart(
        sensor_ids: list[str],
        hourly_activity: list[HourlyActivityDTO],
        charts_presenter_service: ChartsPresenterService,
        bar_chart_plotter: MatplotlibVerticalBarChartPlotter,
        start_date: date,
        end_date: date,
        tail_day_count: int | None,
        path_results: Path,
) -> None:
    bar_vm: BarChartVM = (
        charts_presenter_service.present_hourly_activations_bar_chart(
            sensor_ids=sensor_ids,
            hourly_activity=hourly_activity,
            start_date=start_date,
            end_date=end_date,
            tail_day_count=tail_day_count,
        ))

    """
    for sensor_id, vm in sensor_to_bar_vm_mapping.items():
        chart_path = path_results / "plots" / f"{sensor_id}_hourly_bar_chart.png"
        bar_chart_plotter.render(
            chart_vm=vm,
            output_path=chart_path,
        )
    """

    bar_chart_plotter = MatplotlibHorizontalBarChartPlotter()

    chart_path = path_results / "plots" / f"all_sensors_hourly_bar_chart.png"
    bar_chart_plotter.render(
        chart_vm=bar_vm,
        output_path=chart_path,
    )

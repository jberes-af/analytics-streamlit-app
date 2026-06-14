# # /src/gui/streamlit/output_handlers/activity_charts_handler.py

from datetime import date
from pathlib import Path

from src.domain.entities.sensor import SensorEvent

from src.application.dto.activity_metric_dtos import (
    HourlyActivityDTO,
    SensorByIdByDateActivityDTO,
    SensorAllByDateActivityDTO,
    SensorTimePeriodStatisticsDTO,
)

from src.infrastructure.services.renderers.plotly.plotly_line_chart_renderer import (
    PlotlyLineChartRenderer,
)

from src.infrastructure.services.renderers.plotly.plotly_line_scatter_chart_renderer import (
    PlotlyScatterLineChartRenderer,
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
    ScatterLineChartVM,
)

import streamlit as st


def handle_chart_outputs(
        # sensor_events: list[SensorEvent],
        sensor_ids: list[str],
        sensor_events_sum_by_id_by_date: list[SensorByIdByDateActivityDTO],
        all_sensor_events_sum_by_id_by_date: list[SensorAllByDateActivityDTO],
        # hourly_activity_results: list[HourlyActivityDTO],
        charts_presenter_service: ChartsPresenterService,
        # bar_chart_plotter: MatplotlibVerticalBarChartPlotter,
        line_chart_plotter: PlotlyLineChartRenderer,
        scatter_line_chart_plotter: PlotlyScatterLineChartRenderer,
        # scatter_chart_plotter: MatplotlibScatterChartPlotter,
        start_date: date,
        end_date: date,
        statistics: list[SensorTimePeriodStatisticsDTO],

) -> None:
    _handle_daily_activations_chart(
        sensor_ids=sensor_ids,
        daily_sum_events_sensor_by_id=sensor_events_sum_by_id_by_date,
        daily_sum_events_all_sensors=all_sensor_events_sum_by_id_by_date,
        charts_presenter_service=charts_presenter_service,
        line_chart_plotter=line_chart_plotter,
        scatter_line_chart_plotter=scatter_line_chart_plotter,
        start_date=start_date,
        end_date=end_date,
        statistics=statistics,
    )

    """
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
    """


def _handle_daily_activations_chart(
        sensor_ids: list[str],
        daily_sum_events_sensor_by_id: list[SensorByIdByDateActivityDTO],
        daily_sum_events_all_sensors: list[SensorAllByDateActivityDTO],
        charts_presenter_service: ChartsPresenterService,
        line_chart_plotter: PlotlyLineChartRenderer,
        scatter_line_chart_plotter: PlotlyScatterLineChartRenderer,
        start_date: date,
        end_date: date,
        statistics: list[SensorTimePeriodStatisticsDTO],
) -> None:
    # sensor_to_line_vm_mapping
    # chart_vms: dict[str, LineChartVM] = (
    chart_vms: dict[str, ScatterLineChartVM] = (
        charts_presenter_service.present_sensor_activations_by_date_chart(
            sensor_ids=sensor_ids,
            sensor_by_id_events=daily_sum_events_sensor_by_id,
            all_sensor_events=daily_sum_events_all_sensors,
        )
    )

    chart_options: list[str] = list(chart_vms.keys())

    selected_chart = st.selectbox(
        label="Sensor",
        options=chart_options,
        key="daily_activations_selected_sensor",
        format_func=lambda value: "All Sensors" if value == "ALL" else value,
    )

    # st.write("Selected:", selected_chart)
    selected_vm = chart_vms[selected_chart]

    try:
        fig = scatter_line_chart_plotter.render(selected_vm)
        # fig = line_chart_plotter.render(selected_vm)

        st.plotly_chart(
            fig,
            width="stretch",
            # key=f"daily_activations_chart_{selected_chart}",
            key=f"daily_activations_chart",
        )

    except Exception as e:
        st.exception(e)


"""
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
"""


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
            # sensor_ids=sensor_ids,
            hourly_activity=hourly_activity,
            # start_date=start_date,
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

# # /src/gui/streamlit/output_handlers/activity_charts_handler.py

from datetime import date

from src.domain.entities.sensor import SensorEvent

from src.application.dto.activity_metric_dtos import (
    DailyActivityBySensorIdDTO,
    DailyActivityAllSensorsDTO,
    HourlyActivityAllSensorsDTO,
    HourlyActivityBySensorIdDTO,
    SensorTimePeriodStatisticsDTO,
)
from src.infrastructure.services.renderers.plotly.bar_vertical_chart_renderer import (
    PlotlyVerticalBarChartRenderer,
)

from src.infrastructure.services.renderers.plotly.bar_horizontal_chart_renderer import (
    PlotlyHorizontalBarChartRenderer,
)

from src.infrastructure.services.renderers.plotly.line_chart_renderer import (
    PlotlyLineChartRenderer,
)

from src.infrastructure.services.renderers.plotly.line_scatter_chart_renderer import (
    PlotlyScatterLineChartRenderer,
)

from src.infrastructure.services.renderers.plotly.scatter_chart_renderer import (
    PlotlyScatterChartRenderer,
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
        sensor_events: list[SensorEvent],
        sensor_ids: list[str],
        daily_activity_by_sensor_id: list[DailyActivityBySensorIdDTO],
        daily_activity_all_sensors: list[DailyActivityAllSensorsDTO],

        hourly_activity_all_sensors: list[HourlyActivityAllSensorsDTO],
        hourly_activity_by_sensor_id: list[HourlyActivityBySensorIdDTO],

        charts_presenter_service: ChartsPresenterService,

        bar_vertical_chart_plotter: PlotlyVerticalBarChartRenderer,
        bar_horiz_chart_plotter: PlotlyHorizontalBarChartRenderer,

        line_chart_plotter: PlotlyLineChartRenderer,
        scatter_line_chart_plotter: PlotlyScatterLineChartRenderer,
        scatter_chart_plotter: PlotlyScatterChartRenderer,
        start_date: date,
        end_date: date,
        statistics: list[SensorTimePeriodStatisticsDTO],
        local_timezone: str,
) -> None:
    """
    _handle_weekly_activations_chart(
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

    _handle_daily_activations_chart(
        sensor_ids=sensor_ids,
        daily_sum_events_sensor_by_id=daily_activity_by_sensor_id,
        daily_sum_events_all_sensors=daily_activity_all_sensors,
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
    """

    _handle_sensor_activation_timestamp_scatter_chart(
        sensor_events=sensor_events,
        sensor_ids=sensor_ids,
        # sensor_by_id_events=sensor_by_id_events,
        charts_presenter_service=charts_presenter_service,
        scatter_chart_plotter=scatter_chart_plotter,
        start_date=start_date,
        end_date=end_date,
        tail_day_count=14,
        local_timezone=local_timezone,
    )

    _handle_sensor_hourly_activation_bar_chart(
        sensor_ids=sensor_ids,
        hourly_activity_all_sensors=hourly_activity_all_sensors,
        hourly_activity_by_sensor_id=hourly_activity_by_sensor_id,
        charts_presenter_service=charts_presenter_service,
        bar_chart_plotter=bar_horiz_chart_plotter,
        start_date=start_date,
        end_date=end_date,
        tail_day_count=7,
    )


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


def _handle_daily_activations_chart(
        sensor_ids: list[str],
        daily_sum_events_sensor_by_id: list[DailyActivityBySensorIdDTO],
        daily_sum_events_all_sensors: list[DailyActivityAllSensorsDTO],
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

    with st.expander(
            "Daily Activations Analysis",
            expanded=False,
    ):
        st.markdown(
            """
            This chart shows actual daily activations and a
            7-day rolling average.
            """
        )

        selected_chart = st.selectbox(
            label="Sensor",
            options=chart_options,
            key="daily_activations_selected_sensor",
            format_func=lambda value: "All Sensors" if value == "ALL" else value,
        )

        # st.write("Selected:", selected_chart)
        selected_vm = chart_vms[selected_chart]

        # st.subheader(selected_vm.title)
        # st.subheader(selected_vm.title)
        st.markdown(f"##### {selected_vm.title}")

        try:
            fig = scatter_line_chart_plotter.render(selected_vm)
            # fig = line_chart_plotter.render(selected_vm)

            st.plotly_chart(
                fig,
                width="stretch",
                # key=f"daily_activations_chart_{selected_chart}",
                key=f"daily_activations_chart",
                config={
                    "displayModeBar": False,
                    "responsive": True,
                },
            )

        except Exception as e:
            st.exception(e)


def _handle_sensor_activation_timestamp_scatter_chart(
        sensor_events: list[SensorEvent],
        sensor_ids: list[str],
        # sensor_by_id_events: list[SensorByIdByDateActivityDTO],
        charts_presenter_service: ChartsPresenterService,
        scatter_chart_plotter: PlotlyScatterChartRenderer,
        start_date: date,
        end_date: date,
        tail_day_count: int | None,
        local_timezone: str,
) -> None:
    chart_vms: dict[str, ScatterChartVM] = (
        charts_presenter_service.present_sensor_activations_timestamp_scatter_chart(
            sensor_ids=sensor_ids,
            sensor_events=sensor_events,
            start_date=start_date,
            end_date=end_date,
            tail_day_count=tail_day_count,
            local_timezone=local_timezone,

    ))

    chart_options: list[str] = list(chart_vms.keys())

    with st.expander(
            "Activation Timestamp Chart",
            expanded=False,
    ):
        st.markdown(
            """
            This chart shows timestamps for each sensor activation for a 24-hour period.
            """
        )

        selected_chart = st.selectbox(
            label="Sensor",
            options=chart_options,
            key="timestamp_activations_selected_sensor",
            format_func=lambda value: "All Sensors" if value == "ALL" else value,
        )

        selected_vm = chart_vms[selected_chart]
        st.markdown(f"##### {selected_vm.title}")

        try:
            fig = scatter_chart_plotter.render(selected_vm)

            st.plotly_chart(
                fig,
                width="stretch",
                key=f"timestamp_chart",
                config={
                    "displayModeBar": False,
                    "responsive": True,
                },
            )

        except Exception as e:
            st.exception(e)


def _handle_sensor_hourly_activation_bar_chart(
        sensor_ids: list[str],
        hourly_activity_all_sensors: list[HourlyActivityAllSensorsDTO],
        hourly_activity_by_sensor_id: list[HourlyActivityBySensorIdDTO],
        charts_presenter_service: ChartsPresenterService,
        bar_chart_plotter: PlotlyHorizontalBarChartRenderer,
        start_date: date,
        end_date: date,
        tail_day_count: int | None,
) -> None:
    chart_vms: dict[str, BarChartVM] = (
        charts_presenter_service.present_hourly_activations_bar_chart(
            sensor_ids=sensor_ids,
            hourly_activity_all_sensors=hourly_activity_all_sensors,
            hourly_activity_by_sensor_id=hourly_activity_by_sensor_id,
            # start_date=start_date,
            end_date=end_date,
            tail_day_count=tail_day_count,
        ))


    chart_options: list[str] = list(chart_vms.keys())

    with st.expander(
            "Hourly Activations Analysis",
            expanded=False,
    ):
        st.markdown(
            """
            This chart shows average activations by hour for the last 7 days.
            """
        )

        selected_chart = st.selectbox(
            label="Sensor",
            options=chart_options,
            key="hourly_activations_selected_sensor",
            format_func=lambda value: "All Sensors" if value == "ALL" else value,
        )

        selected_vm = chart_vms[selected_chart]

        st.markdown(f"##### {selected_vm.title}")

        try:
            fig = bar_chart_plotter.render(selected_vm)

            st.plotly_chart(
                fig,
                width="stretch",
                key=f"hourly_activations_chart",
                config={
                    "displayModeBar": False,
                    "responsive": True,
                },
            )

        except Exception as e:
            st.exception(e)

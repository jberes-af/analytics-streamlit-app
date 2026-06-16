# # /src/gui/streamlit/output_handlers/activity_charts_handler-00.txt

from datetime import date

from src.application.dto.activity_metric_dtos import (
    HourlyActivityAllSensorsDTO,
    HourlyActivityBySensorIdDTO,
)

from src.infrastructure.services.renderers.plotly.bar_horizontal_chart_renderer import (
    PlotlyHorizontalBarChartRenderer,
)

from src.interface_adapters.presenters.charts.charts_presenter_service import (
    ChartsPresenterService,
)

from src.interface_adapters.view_models.charts_view_model import (
    BarChartVM,
)

import streamlit as st


def handle_hourly_activation_outputs(
        sensor_ids: list[str],
        hourly_activity_all_sensors: list[HourlyActivityAllSensorsDTO],
        hourly_activity_by_sensor_id: list[HourlyActivityBySensorIdDTO],
        charts_presenter_service: ChartsPresenterService,
        # bar_vertical_chart_plotter: PlotlyVerticalBarChartRenderer,
        bar_horiz_chart_plotter: PlotlyHorizontalBarChartRenderer,
        start_date: date,
        end_date: date,
) -> None:

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

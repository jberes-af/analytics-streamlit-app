# # /src/gui/streamlit/output_handlers/activity_charts_handler-00.txt

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


def handle_activation_timestamp_outputs(
        sensor_events: list[SensorEvent],
        sensor_ids: list[str],
        charts_presenter_service: ChartsPresenterService,
        scatter_chart_plotter: PlotlyScatterChartRenderer,
        start_date: date,
        end_date: date,
        local_timezone: str,
) -> None:
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

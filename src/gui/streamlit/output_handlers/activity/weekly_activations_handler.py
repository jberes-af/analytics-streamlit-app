# /src/gui/streamlit/output_handlers/weekly_activations_handler.py


from src.application.dto.activity_metric_dtos import (
    SensorWeeklyActivityDTO,
)

from src.application.dto.activity_insights_dtos import ActivityInsightDTO

from src.infrastructure.services.renderers.plotly.line_scatter_weekly_chart_renderer import (
    PlotlyScatterLineWeeklyChartRenderer,
)

from src.interface_adapters.presenters.activity.activity_presenter_service import (
    ActivityPresenterService,
)

from src.interface_adapters.presenters.charts.charts_presenter_service import (
    ChartsPresenterService,
)

from src.interface_adapters.presenters.insights.activity_insights_presenter_service import (
    InsightsPresenterService,
)

from src.interface_adapters.view_models.charts_view_model import (
    ScatterLineChartWeeklyVM,
)

from src.interface_adapters.view_models.activity.weekly_activity_vm import (
    WeeklyActivityViewModel,
)

from src.interface_adapters.view_models.activity_insights_view_models import (
    ActivityInsightViewModel,
    ActivityInsightsViewModel,
)

import streamlit as st


def handle_weekly_activation_outputs(
        sensor_ids: list[str],
        weekly_sensor_activity: list[SensorWeeklyActivityDTO],
        charts_presenter_service: ChartsPresenterService,
        activity_presenter_service: ActivityPresenterService,
        insights_presenter_service: InsightsPresenterService,
        scatter_line_chart_weekly_plotter: PlotlyScatterLineWeeklyChartRenderer,
        weekly_activity_insights: list[ActivityInsightDTO],
) -> None:
    chart_vms: dict[str, ScatterLineChartWeeklyVM] = (
        charts_presenter_service.present_sensor_activations_by_week_chart(
            sensor_ids=sensor_ids,
            weekly_sensor_activity=weekly_sensor_activity,
        ))
    chart_options: list[str] = list(chart_vms.keys())

    insights_vm: ActivityInsightsViewModel = (
        insights_presenter_service.present_weekly_activity_insights(
            weekly_activity_insights=weekly_activity_insights,
        ))

    _render_sensor_weekly_activation_chart(
        chart_options=chart_options,
        chart_vms=chart_vms,
        scatter_line_chart_plotter=scatter_line_chart_weekly_plotter,
        weekly_insights_vm=insights_vm.weekly_activity_insights,
    )


def _render_sensor_weekly_activation_chart(
        chart_options: list[str],
        chart_vms: dict[str, ScatterLineChartWeeklyVM],
        scatter_line_chart_plotter: PlotlyScatterLineWeeklyChartRenderer,
        weekly_insights_vm: list[ActivityInsightViewModel],
) -> None:
    with st.expander(
            "Weekly Activations Analysis",
            expanded=False,
    ):
        st.markdown(
            """
            This chart shows weekly activity patterns using the daily minimum,
            daily maximum, and daily average activation counts within each week.
            """
        )

        selected_chart = st.selectbox(
            label="Sensor",
            options=chart_options,
            key="weekly_activations_selected_sensor",
            format_func=lambda value: "All Sensors" if value == "ALL" else value,
        )

        selected_vm = chart_vms[selected_chart]

        st.markdown(f"##### {selected_vm.title}")

        try:
            fig = scatter_line_chart_plotter.render(selected_vm)

            st.plotly_chart(
                fig,
                width="stretch",
                key=f"weekly_activations_chart",
                config={
                    "displayModeBar": False,
                    "responsive": True,
                },
            )

        except Exception as e:
            st.exception(e)

        # st.subheader("Key Insights")
        st.markdown(f"#### Summary")


        section_header: str = weekly_insights_vm[0].section_header
        if section_header:
            st.markdown(f"##### {section_header}")

        for vm in weekly_insights_vm:
            if vm.message_header:
                st.markdown(f"**{vm.message_header}**")

            if vm.message_line_1:
                st.markdown(vm.message_line_1)

            if vm.message_line_2:
                st.markdown(vm.message_line_2)

            st.write("")

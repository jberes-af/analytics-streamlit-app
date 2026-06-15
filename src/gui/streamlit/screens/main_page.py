# /src/gui/streamlit/screens/main_page.py
from http.client import responses

from src.application.dto.run_startup_use_cases_dtos import (
    RunStartupUseCasesRequestDTO,
    RunStartupUseCasesResultDTO,
)

from src.application.dto.run_analysis_use_cases_dtos import (
    RunAnalysisUseCasesRequestDTO,
    RunAnalysisUseCasesResultDTO,
)

from src.application.dto.sensor_by_user_uc_dtos import (
    SensorByUserResultDTO,
)

from src.gui.streamlit.components.filters.desktop_filter_panel import (
    render_desktop_filter_panel,
)

from src.gui.streamlit.output_handlers.activity_charts_handler import (
    handle_chart_outputs,
)

from src.gui.streamlit.components.filters.models import (
    AnalysisFilters,
)

from src.interface_adapters.output_handlers.results_handler import (
    handle_result_outputs_orchestrator,
)

from src.main.composition_root_startup import StartupAppContainer
from src.main.composition_root_analysis import AnalysisAppContainer

import streamlit as st


def render_main_page(
        startup_request: RunStartupUseCasesRequestDTO,
        startup_app: StartupAppContainer,
        analysis_app: AnalysisAppContainer,
) -> None:
    startup_result: RunStartupUseCasesResultDTO = (
        startup_app.startup_controller.run(startup_request))

    lookup_results: SensorByUserResultDTO = (
        startup_result.lookup_sensor_by_user_result)

    filters: AnalysisFilters = render_desktop_filter_panel(
        available_sensor_ids=lookup_results.sensor_ids,
        sensor_names=lookup_results.sensor_names,
    )

    st.title("Alerta Home Analytics")

    if not filters.is_valid:
        st.warning("Please select a valid date range and at least one sensor.")
        return

    run_analysis_mobile = st.button(
        "Run Analysis",
        type="primary",
        # width="stretch",
        # use_container_width=True,
        key="mobile_run_analysis",
    )

    if filters.run_analysis or run_analysis_mobile:
        analysis_request = RunAnalysisUseCasesRequestDTO(
            sensor_ids=filters.selected_sensor_ids,
            start_date=filters.start_date,
            end_date=filters.end_date,
            rolling_window="7",
            rolling_frequency="7",
            local_timezone=filters.local_timezone,
        )

        analysis_result: RunAnalysisUseCasesResultDTO = (
            analysis_app.run_controller.run(analysis_request)
        )

        st.session_state["analysis_result"] = analysis_result
        st.session_state["analysis_filters"] = filters

    analysis_result = st.session_state.get("analysis_result")
    analysis_filters = st.session_state.get("analysis_filters")

    if analysis_result is None or analysis_filters is None:
        st.info("Select filters and run analysis.")
        return

    handle_result_outputs_orchestrator(
        response=analysis_result,
        activity_presenter_service=analysis_app.activity_presenter_service,
        console_view_service=analysis_app.console_view_service,
        dataframe_renderer=analysis_app.dataframe_renderer,
    )

    # must call chart-outputs object from here in order to render on main-page

    handle_chart_outputs(
        sensor_events=analysis_result.build_sensor_timeline_result.collapsed_events,
        sensor_ids=filters.selected_sensor_ids,
        daily_activity_by_sensor_id=analysis_result.analyze_activity_result.sensor_by_id_by_date_activity,
        daily_activity_all_sensors=analysis_result.analyze_activity_result.all_sensors_by_date_activity,

        hourly_activity_all_sensors=analysis_result.analyze_activity_result.all_sensors_by_hour_activity,
        hourly_activity_by_sensor_id=analysis_result.analyze_activity_result.sensor_by_id_by_hour_activity,

        charts_presenter_service=analysis_app.charts_presenter_service,
        bar_vertical_chart_plotter=analysis_app.bar_vertical_chart_plotter,
        bar_horiz_chart_plotter=analysis_app.bar_horizontal_chart_plotter,
        line_chart_plotter=analysis_app.line_chart_renderer,
        scatter_line_chart_plotter=analysis_app.scatter_line_chart_renderer,
        scatter_chart_plotter=analysis_app.scatter_chart_plotter,
        start_date=filters.start_date,
        end_date=filters.end_date,
        statistics=analysis_result.analyze_activity_result.sensor_time_period_statistics,
        local_timezone = filters.local_timezone,
    )


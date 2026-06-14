# /src/gui/streamlit/screens/main_page.py

"""
1. render_main_page calls controller
2. controller runs use case(s)
3. use case(s) return ResultDTOs
4. presenter converts ResultDTOs to ViewModels
5. output handler renders ViewModels using Streamlit + Plotly

Use cases should not know Streamlit.
Presenters should not know Streamlit.
Plotly builders should not know Streamlit.
Only output handlers/screens should call st.plotly_chart().
"""

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

# --- INTERFACE ADAPTERS

from src.interface_adapters.output_handlers.results_handler import (
    handle_result_outputs_orchestrator,
)

from src.interface_adapters.presenters.activity.activity_presenter_service import (
    ActivityPresenterService,
)

# --- INFRASTRUCTURE

from src.infrastructure.services.renderers.pandas.pandas_dataframe_renderer import (
    PandasDataFrameRenderer,
)

from src.interface_adapters.views.console.console_view_service import (
    ConsoleViewService,
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

    filters = render_desktop_filter_panel(
        available_sensor_ids=lookup_results.sensor_ids,
        sensor_names=lookup_results.sensor_names,
    )

    st.title("Alerta Home Analytics")

    if not filters.is_valid:
        st.warning("Please select a valid date range and at least one sensor.")
        return

    if filters.run_analysis:
        pass
        """
        st.write("Start:", filters.start_date)
        st.write("End:", filters.end_date)
        st.write("Sensors:", filters.selected_sensor_ids)
        
        analysis_request = RunAnalysisRequestDTO(
            user_id=startup_request.user_id,
            start_date=filters.start_date,
            end_date=filters.end_date,
            sensor_ids=filters.selected_sensor_ids,
        )
        
        analysis_result = analysis_controller.run(
            analysis_request,
        )

        analysis_output_handler.render(
            result=analysis_result,
        )
        """

        analysis_request = RunAnalysisUseCasesRequestDTO(
            sensor_ids=filters.selected_sensor_ids,
            start_date=filters.start_date,
            end_date=filters.end_date,
            rolling_window="7",
            rolling_frequency="7",
        )

        analysis_result: RunAnalysisUseCasesResultDTO = (
            analysis_app.run_controller.run(analysis_request)
        )

        handle_result_outputs_orchestrator(
            response=analysis_result,
            activity_presenter_service=analysis_app.activity_presenter_service,
            console_view_service=analysis_app.console_view_service,
            dataframe_renderer=analysis_app.dataframe_renderer,
        )

# /src/gui/streamlit/screens/main_page.py

from src.application.dto.run_startup_use_cases_dtos import (
    RunStartupUseCasesRequestDTO,
    RunStartupUseCasesResultDTO,
)

from src.gui.streamlit.components.filters.desktop_filter_panel import (
    render_desktop_filter_panel,
)

from src.interface_adapters.controllers.startup_controller import (
    RunStartupUseCasesController,
)

import streamlit as st


def render_main_page(
        startup_request: RunStartupUseCasesRequestDTO,
        startup_controller: RunStartupUseCasesController,
) -> None:
    startup_result: RunStartupUseCasesResultDTO = (
        startup_controller.run(startup_request))

    # sensor_events: SensorEventTimelineResultDTO = BuildSensorEventTimelineUseCase()
    available_sensor_ids = startup_result.lookup_sensor_by_user_result.sensor_ids

    filters = render_desktop_filter_panel(
        available_sensor_ids=available_sensor_ids,
    )

    st.title("Alerta Home Analytics")

    if not filters.is_valid:
        st.warning("Please select a valid date range and at least one sensor.")
        return

    if filters.run_analysis:
        st.write("Start:", filters.start_date)
        st.write("End:", filters.end_date)
        st.write("Sensors:", filters.selected_sensor_ids)

        # call controller/service here
        # results = controller.get_analysis(...)

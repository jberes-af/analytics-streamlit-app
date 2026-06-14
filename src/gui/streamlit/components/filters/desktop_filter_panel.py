# /src/gui/streamlit/components/filters/desktop_filter_panel.py

import streamlit as st

from src.gui.streamlit.components.filters.date_range_filter import (
    render_date_range_filter,
)

from src.gui.streamlit.components.filters.sensor_selector import (
    render_sensor_selector,
)

from src.gui.streamlit.components.filters.models import (AnalysisFilters,
                                                         )


def render_desktop_filter_panel(
        available_sensor_ids: list[str],
        sensor_names: list[str],
) -> AnalysisFilters:
    with st.sidebar:

        st.divider()

        run_analysis = st.button(
            "Run Analysis",
            type="primary",
            width="stretch",
            # use_container_width=True,
            key="desktop_run_analysis",
        )

        st.divider()

        st.title("Settings")

        st.subheader("Date Range")
        start_date, end_date = render_date_range_filter("desktop")

        st.divider()
        st.subheader("Sensor IDs")
        selected_sensor_ids = render_sensor_selector(
            available_sensor_ids=available_sensor_ids,
            key_prefix="desktop",
        )

        description: str = "\n".join(sensor_names)
        st.text(description)

        """
        st.divider()

        run_analysis = st.button(
            "Run Analysis",
            type="primary",
            width="stretch",
            # use_container_width=True,
            key="desktop_run_analysis",
        )
        """

    return AnalysisFilters(
        start_date=start_date,
        end_date=end_date,
        selected_sensor_ids=selected_sensor_ids,
        run_analysis=run_analysis,
        is_valid=start_date <= end_date and bool(selected_sensor_ids),
    )

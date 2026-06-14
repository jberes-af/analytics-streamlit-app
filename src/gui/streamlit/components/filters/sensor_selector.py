# /src/gui/streamlit/components/filters/sensor_selector.py

import streamlit as st


def render_sensor_selector(
    available_sensor_ids: list[str],
    key_prefix: str,
) -> list[str]:

    """
    select_all = st.checkbox(
        "Select all sensors",
        value=True,
        key=f"{key_prefix}_select_all_sensors",
    )
    """

    selected_sensor_ids: list[str] = []

    for sensor_id in available_sensor_ids:
        is_selected = st.checkbox(
            sensor_id,
            #
            value=True,
            key=f"{key_prefix}_sensor_{sensor_id}",
        )

        if is_selected:
            selected_sensor_ids.append(sensor_id)

    if not selected_sensor_ids:
        st.warning("Select at least one sensor.")

    return selected_sensor_ids

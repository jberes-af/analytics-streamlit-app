# /src/gui/streamlit/components/filters/date_range_filter.py

from datetime import date, timedelta

import streamlit as st


def render_date_range_filter(key_prefix: str) -> tuple[date, date]:
    default_end_date = date.today() - timedelta(days=1)
    default_start_date = default_end_date - timedelta(days=28)

    start_date = st.date_input(
        "Start Date",
        value=default_start_date,
        key=f"{key_prefix}_start_date",
        format="MM-DD-YYYY",
    )

    st.caption(
        f"Selected: {start_date.strftime('%B')} {start_date.day}, {start_date.year}"
    )

    end_date = st.date_input(
        "End Date",
        value=default_end_date,
        key=f"{key_prefix}_end_date",
        format="MM-DD-YYYY",
    )

    st.caption(
        f"Selected: {end_date.strftime('%B')} {end_date.day}, {end_date.year}"
    )

    if start_date > end_date:
        st.error("Start Date must be before End Date.")

    return start_date, end_date

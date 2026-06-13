# src/gui/streamlit/app.py

from pathlib import Path

import sys

PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT))


from src.main.composition_root import app_container
from src.gui.streamlit.auth.login_form import LoginForm
from src.gui.streamlit.routing.router import render_router

import streamlit as st

path_file_favicon = PROJECT_ROOT / "src/gui/streamlit/static/favicon" / "favicon.ico"

def configure_page() -> None:
    st.set_page_config(
        page_title="Alerta Family Mobile ADL",
        page_icon=path_file_favicon,
        layout="wide",
    )


def initialize_session_state() -> None:
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if "user" not in st.session_state:
        st.session_state["user"] = None


def render_login_phase() -> None:


    login_form = LoginForm(
        auth_controller=app_container.auth_controller,
        auth_presenter=app_container.auth_presenter,
    )

    login_form.render()


def render_authenticated_phase() -> None:

    user = st.session_state.get("user")
    if user:
        st.sidebar.success(f"Signed in as {user['email']}")

    # --- PAGE NAVIGATION / ROUTING

    render_router()

    # --- LOGOUT

    if st.sidebar.button("Logout"):
        st.session_state["logged_in"] = False
        st.session_state["user"] = None
        st.rerun()


def run_streamlit_app() -> None:
    configure_page()
    initialize_session_state()

    # if not st.session_state["logged_in"]:
        # render_login_phase()
        # st.stop()

    render_authenticated_phase()


run_streamlit_app()
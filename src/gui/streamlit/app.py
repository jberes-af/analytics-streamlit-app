# src/gui/streamlit/app.py

from pathlib import Path

import sys

PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT))

from src.application.dto.run_startup_use_cases_dtos import (
    RunStartupUseCasesRequestDTO,
)

from src.gui.streamlit.auth.login_form import LoginForm
from src.gui.streamlit.routing.router import render_router
from src.main.composition_root import startup_app_container

from src.infrastructure.config.settings_model import AppMode
from src.interface_adapters.auth.authenticated_user import AuthenticatedUser


import streamlit as st

path_file_favicon = PROJECT_ROOT / "src/gui/streamlit/static/favicon" / "favicon.ico"

DEVELOPMENT_USER_ID = "ssSOQyDrfeh8P7w9TJDFPjhlRuw2"
MODE = "DEVELOPMENT"  # or "PRODUCTION"


def configure_page() -> None:
    st.set_page_config(
        page_title="Alerta Home Analytics",
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
        auth_controller=startup_app_container.auth_controller,
        auth_presenter=startup_app_container.auth_presenter,
    )

    login_form.render()

def resolve_authenticated_user() -> AuthenticatedUser | None:
    settings = startup_app_container.settings

    if settings.app_mode == AppMode.DEVELOPMENT:
        if not settings.dev_user_id:
            raise RuntimeError(
                "DEV_USER_ID is required in development mode."
            )

        return AuthenticatedUser(
            user_id=settings.dev_user_id,
            email="developer@local",
            is_development_user=True,
        )

    user = st.session_state.get("user")

    if not user:
        return None

    return AuthenticatedUser(
        user_id=user["localId"],  # Firebase Auth uid
        email=user.get("email"),
        is_development_user=False,
    )


def get_authenticated_user_id(
        *,
        development_user_id: str | None = None,
) -> str | None:
    if development_user_id is not None:
        return development_user_id

    user = st.session_state.get("user")

    if not user:
        return None

    st.sidebar.success(f"Signed in as {user['email']}")

    return user.get("user_id")


def render_authenticated_phase(
    authenticated_user: AuthenticatedUser,
) -> None:
    st.sidebar.success(
        f"Signed in as {authenticated_user.email or authenticated_user.user_id}"
    )

    startup_request = RunStartupUseCasesRequestDTO(
        user_id=authenticated_user.user_id,
    )

    render_router(
        startup_request=startup_request,
        startup_controller=startup_app_container.startup_controller,
    )

    with st.sidebar:
        st.divider()

        if st.button(
            "Logout",
            use_container_width=True,
            type="secondary",
        ):
            st.session_state["logged_in"] = False
            st.session_state["user"] = None
            st.rerun()


def run_streamlit_app() -> None:
    configure_page()
    initialize_session_state()

    settings = startup_app_container.settings

    if settings.app_mode == AppMode.PRODUCTION:
        if not st.session_state["logged_in"]:
            render_login_phase()
            st.stop()

    authenticated_user = resolve_authenticated_user()

    if authenticated_user is None:
        st.error("Unable to resolve authenticated user.")
        st.stop()

    render_authenticated_phase(
        authenticated_user=authenticated_user,
    )



run_streamlit_app()

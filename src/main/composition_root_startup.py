# /src/main/composition_root_startup.py

from dataclasses import dataclass
from pathlib import Path
import logging

# --- APPLICATION

from src.application.auth.login_user import LoginUser
from src.application.ports.firebase_rtdb import FirebaseRtdbPort

from src.application.services.read_firebase_node_service import (
    ReadFirebaseNodeService,
)

from src.application.use_cases.use_cases_interactor import (
    RunStartupUseCasesInteractor,
    LookupSensorByUserInteractor,
)

from src.application.use_cases.lookup_sensor_by_user_use_case import (
    LookupSensorByUserUseCase,
)

# --- INFRASTRUCTURE ADAPTERS

from src.infrastructure.config.settings_model import Settings
from src.infrastructure.config.app_config_models import AppRuntimeConfig

from src.infrastructure.config.secret_provider import (
    SecretProvider,
    EnvSecretProvider,
)

from src.infrastructure.config.settings_loader import load_settings

from src.infrastructure.config.app_config_loader import AppConfigLoader

from src.infrastructure.auth.firebase_client_auth_service import (
    FirebaseClientAuthService
)
from src.infrastructure.persistence.firebase.firebase_app import (
    init_firebase_admin_app
)
from src.infrastructure.persistence.firebase.firebase_rtdb_adapter import (
    FirebaseRtdbAdapter)

# --- INTERFACE ADAPTERS

from src.interface_adapters.controllers.auth_controller import AuthController
from src.interface_adapters.presenters.auth_presenter import AuthPresenter
from src.interface_adapters.controllers.startup_controller import (
    RunStartupUseCasesController,
)


# --- PROGRAM

@dataclass(frozen=True)
class StartupAppContainer:
    auth_controller: AuthController
    auth_presenter: AuthPresenter
    startup_controller: RunStartupUseCasesController


def build_startup_app_container(
        auth_settings,
        read_firebase_node_service: ReadFirebaseNodeService,
) -> StartupAppContainer:
    auth_controller: AuthController = _build_auth_controller(
        auth_settings=auth_settings,
    )

    auth_presenter = AuthPresenter()

    # --- START-UP USE CASE

    lookup_sensor_by_user_uc: LookupSensorByUserInteractor = (
        _lookup_sensor_by_user_use_case(
            read_firebase_node_service=read_firebase_node_service,
        ))

    run_startup_use_cases: RunStartupUseCasesInteractor = (
        RunStartupUseCasesInteractor(
            lookup_sensor_by_user_use_case=lookup_sensor_by_user_uc,
        ))

    # --- CONTROLLER

    run_controller: RunStartupUseCasesController = _build_controller(
        run_startup_use_cases=run_startup_use_cases,
    )

    return StartupAppContainer(
        auth_controller=auth_controller,
        auth_presenter=auth_presenter,
        startup_controller=run_controller,
    )


"""
BUILD AUTHENTICATION
"""


def _build_auth_controller(
        auth_settings,
) -> AuthController:
    firebase_client_auth_service = FirebaseClientAuthService(
        web_config=dict(auth_settings),
    )

    login_user = LoginUser(
        auth_provider=firebase_client_auth_service,
    )
    return AuthController(login_user=login_user)


"""
BUILD CONTROLLER
"""


def _build_controller(
        *,
        run_startup_use_cases: RunStartupUseCasesInteractor,
) -> RunStartupUseCasesController:
    return RunStartupUseCasesController(
        run_startup_use_cases=run_startup_use_cases,
    )


"""
BUILD USE CASES
"""


def _lookup_sensor_by_user_use_case(
        read_firebase_node_service: ReadFirebaseNodeService,
) -> LookupSensorByUserInteractor:
    return LookupSensorByUserUseCase(
        read_firebase_node_service=read_firebase_node_service,
    )


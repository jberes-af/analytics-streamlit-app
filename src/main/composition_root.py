# /src/main/composition_root.py

from dataclasses import dataclass
from pathlib import Path
import logging

# --- APPLICATION

from src.application.auth.login_user import LoginUser
from src.application.ports.firebase_rtdb import FirebaseRtdbPort
# from src.application.ports.aws_appsync_ports import SensorLastSeenPort

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
from src.gui.streamlit.streamlit_settings_loader import (
    StreamlitSecretProvider,
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

# from src.infrastructure.persistence.aws.appsync_last_seen_adapter import (
#     AppSyncLastSeenAdapter,
# )

# --- INTERFACE ADAPTERS

from src.interface_adapters.controllers.auth_controller import AuthController
from src.interface_adapters.presenters.auth_presenter import AuthPresenter
from src.interface_adapters.controllers.startup_controller import (
    RunStartupUseCasesController,
)


# --- PROGRAM

@dataclass(frozen=True)
class StartupAppContainer:
    settings: Settings
    cfg: AppRuntimeConfig
    auth_controller: AuthController
    auth_presenter: AuthPresenter
    startup_controller: RunStartupUseCasesController


def resolve_project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def load_runtime_config() -> tuple[Settings, AppRuntimeConfig]:
    project_root = resolve_project_root()

    logging.info("Project root resolved: %s", project_root)

    secret_provider = _build_secret_provider(
        project_root=project_root,
        use_streamlit_secrets=False,
    )

    settings = load_settings(
        project_root=project_root,
        secret_provider=secret_provider,
    )
    logging.info("Settings loaded")

    cfg = AppConfigLoader.load_from_json(
        settings.config_path,
        project_root=project_root,
    )
    logging.info("Config loaded")

    return settings, cfg


def build_startup_app_container() -> StartupAppContainer:
    settings, cfg = load_runtime_config()

    # --- AUTHENTICATION

    auth_controller: AuthController = _build_auth_controller(
        auth_settings=settings.firebase_web.to_pyrebase_config()
    )

    auth_presenter = AuthPresenter()

    # --- ADAPTERS

    # --- ADAPTERS: Firebase
    # Firebase Admin SDK, used for backend RTDB reads in BOTH modes
    fb_admin_app = init_firebase_admin_app(
        database_url=settings.firebase_admin.database_url,
        service_account_info=settings.firebase_admin.service_account_info,
    )

    rtdb: FirebaseRtdbPort = FirebaseRtdbAdapter(app=fb_admin_app)
    read_firebase_node_service = ReadFirebaseNodeService(rtdb=rtdb)

    logging.info("Infrastructure adapters instantiated")

    # --- ADAPTERS: AWS AppSync
    """
    app_sync_last_seen: SensorLastSeenPort = AppSyncLastSeenAdapter(
        endpoint=settings.appsync_endpoint,
        api_key=settings.appsync_api_key)
    """

    # --- START-UP USE CASE

    lookup_sensor_by_user_uc: LookupSensorByUserInteractor = (
        _lookup_sensor_by_user_use_case(
            read_firebase_node_service=read_firebase_node_service,
            # read_app_sync_last_seen_service=app_sync_last_seen,
        ))

    """
    get_connectivity_uc: LookupSensorsByUserInteractor = (
        _get_sensor_online_status_use_case(
            read_app_sync_last_seen_service=app_sync_last_seen,
        ))
    """

    run_startup_use_cases: RunStartupUseCasesInteractor = (
        RunStartupUseCasesInteractor(
            lookup_sensor_by_user_use_case=lookup_sensor_by_user_uc,
        ))

    # --- CONTROLLER

    run_controller: RunStartupUseCasesController = _build_controller(
        run_startup_use_cases=run_startup_use_cases,
    )

    return StartupAppContainer(
        settings=settings,
        cfg=cfg,
        auth_controller=auth_controller,
        auth_presenter=auth_presenter,
        startup_controller=run_controller,
    )


"""
BUILD SETTINGS
"""


def _build_secret_provider(
        *,
        project_root: Path,
        use_streamlit_secrets: bool,
) -> SecretProvider:
    if use_streamlit_secrets:
        from src.gui.streamlit.streamlit_settings_loader import (
            StreamlitSecretProvider,
        )

        return StreamlitSecretProvider()

    return EnvSecretProvider(
        env_path=project_root / ".env",
    )


"""
BUILD AUTHENTICATION
"""


def _build_auth_controller(
        auth_settings) -> AuthController:
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
        # analyze_movements_use_case: AnalyzeMovementPatternsInteractor,
) -> RunStartupUseCasesController:
    return RunStartupUseCasesController(
        run_startup_use_cases=run_startup_use_cases,
    )


"""
BUILD USE CASES
"""


def _lookup_sensor_by_user_use_case(
        read_firebase_node_service: ReadFirebaseNodeService,
        # read_app_sync_last_seen_service: SensorLastSeenPort,
) -> LookupSensorByUserInteractor:
    return LookupSensorByUserUseCase(
        read_firebase_node_service=read_firebase_node_service,
        # read_app_sync_last_seen_service=read_app_sync_last_seen_service,
    )


"""
def _get_sensor_online_status_use_case(
        read_app_sync_last_seen_service: SensorLastSeenPort,
) -> GetSensorConnectivityStatusInteractor:
    return GetSensorConnectivityStatusUseCase(
        read_app_sync_last_seen_service=read_app_sync_last_seen_service,
    )
"""

startup_app_container = build_startup_app_container()

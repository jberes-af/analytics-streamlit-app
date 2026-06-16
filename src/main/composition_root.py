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

from src.infrastructure.config.settings_model import AppMode

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


from src.main.composition_root_startup import (
    StartupAppContainer,
    build_startup_app_container,
)

from src.main.composition_root_analytics import (
    AnalysisAppContainer,
    build_analysis_app_container,
)


@dataclass(frozen=True)
class StreamlitDependencies:
    startup_app_container: StartupAppContainer
    analytics_app_container: AnalysisAppContainer


def resolve_project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def load_runtime_config(
        app_mode: AppMode,
        user_key: str,
) -> tuple[Settings, AppRuntimeConfig]:
    project_root = resolve_project_root()

    logging.info("Project root resolved: %s", project_root)

    secret_provider = _build_secret_provider(
        project_root=project_root,
        use_streamlit_secrets=False,
    )

    settings = load_settings(
        project_root=project_root,
        secret_provider=secret_provider,
        app_mode=app_mode,
        user_key=user_key,
    )
    logging.info("Settings loaded")

    cfg = AppConfigLoader.load_from_json(
        settings.config_path,
        project_root=project_root,
    )
    logging.info("Config loaded")

    return settings, cfg


def build_app_containers(
        settings: Settings,
):
    # --- ADAPTERS

    # --- Firebase Admin SDK, used for backend RTDB reads in BOTH modes

    fb_admin_app = init_firebase_admin_app(
        database_url=settings.firebase_admin.database_url,
        service_account_info=settings.firebase_admin.service_account_info,
    )

    rtdb: FirebaseRtdbPort = FirebaseRtdbAdapter(app=fb_admin_app)
    read_firebase_node_service = ReadFirebaseNodeService(rtdb=rtdb)

    logging.info("Infrastructure adapters instantiated")

    startup_app_container: StartupAppContainer = build_startup_app_container(
        auth_settings=settings.firebase_web.to_pyrebase_config(),
        read_firebase_node_service=read_firebase_node_service,
    )

    analysis_app_container: AnalysisAppContainer = build_analysis_app_container(
        read_firebase_node_service=read_firebase_node_service,
    )

    return StreamlitDependencies(
        startup_app_container=startup_app_container,
        analytics_app_container=analysis_app_container,
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

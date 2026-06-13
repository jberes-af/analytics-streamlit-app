# infrastructure/config/settings_loader.py

from pathlib import Path
from dotenv import load_dotenv
from typing import cast
import os

from src.infrastructure.config.settings_model import (
    DriveAccessMode,
    FirebaseWebSettings,
    GoogleAccessMode,
    Settings,
)
from src.infrastructure.persistence.google.auth.oauth_scopes import combined_scopes

from src.gui.streamlit.streamlit_settings_loader import (
    streamlit_secrets_available,
    get_secret,
    get_required_secret,
)


class SettingsError(RuntimeError):
    pass

"""
def _getenv_required(name: str) -> str:
    v = os.getenv(name)
    if not v or not v.strip():
        raise SettingsError(f"Missing required environment variable: {name}")
    return v.strip()
"""


def load_settings_from_env(*, project_root: Path) -> Settings:
    project_root: Path = project_root.resolve()

    # --- CHECK IF STREAMLIT ENV IS AVAILABLE

    # load_dotenv(project_root / ".env")
    if not streamlit_secrets_available():
        load_dotenv(project_root / ".env")

    # --- CONFIG JSON PATH

    config_dir: Path = (project_root / "config").resolve()
    app_config_json_path: Path = (config_dir / "config.json").resolve()

    if not app_config_json_path.exists():
        raise SettingsError(f"App config JSON not found: {app_config_json_path}")

    if not app_config_json_path.is_file():
        raise SettingsError(f"App config JSON not found: {app_config_json_path}")

    # --- SHEETS ACCESS MODE

    # sheets_mode_raw = os.getenv("GOOGLE_ACCESS_MODE", "read").strip().lower()
    sheets_mode_raw = get_secret("GOOGLE_ACCESS_MODE", "read").strip().lower()

    if sheets_mode_raw not in ("read", "write"):
        pass
        # raise SettingsError("GOOGLE_ACCESS_MODE must be 'read' or 'write'")
    sheets_mode = cast(GoogleAccessMode, sheets_mode_raw)

    # --- DRIVE ACCESS MODE

    # drive_mode_raw = os.getenv("DRIVE_ACCESS_MODE", "none").strip().lower()
    drive_mode_raw = get_secret("DRIVE_ACCESS_MODE", "none").strip().lower()
    if drive_mode_raw not in ("none", "read", "write", "all"):
        pass
        # raise SettingsError("DRIVE_ACCESS_MODE must be one of: none, read, write, all")
    drive_mode = cast(DriveAccessMode, drive_mode_raw)

    scopes = combined_scopes(sheets_mode=sheets_mode, drive_mode=drive_mode)

    # --- OAUTH SECRETS FILE

    # client_secret_filename = _getenv_required("GOOGLE_CLIENT_SECRET_ACCOUNTING")
    client_secret_filename = get_secret("GOOGLE_CLIENT_SECRET_ACCOUNTING")
    client_secret_json = (project_root / "secrets" / client_secret_filename).resolve()
    if not client_secret_json.exists():
        pass
        # raise SettingsError(f"Client secret not found: {client_secret_json}")

    # --- GOOGLE TOKEN

    state_dir = (project_root / "state").resolve()
    state_dir.mkdir(parents=True, exist_ok=True)

    # raw_token = os.getenv("GOOGLE_TOKEN_JSON")
    raw_token = get_secret("GOOGLE_TOKEN_JSON")
    if raw_token:
        token_path = Path(raw_token)
        token_json = (token_path if token_path.is_absolute() else (project_root / token_path)).resolve()
    else:
        needs_write = (sheets_mode == "write") or (drive_mode in ("write", "all"))
        token_default = "token_write.json" if needs_write else "token_read.json"
        token_json = (state_dir / token_default).resolve()

    spreadsheet_ids_by_file = {
        "model_config": get_secret("SHEET_ID_CONFIG"),
        # "model_config": _getenv_required("SHEET_ID_CONFIG"),
    }

    # GOOGLE DRIVE FOLDER

    # drive_root = os.getenv("GOOGLE_DRIVE_ROOT_FOLDER_ID")
    drive_root = get_secret("GOOGLE_DRIVE_ROOT_FOLDER_ID")
    if drive_mode != "none" and not (drive_root and drive_root.strip()):
        pass
        # raise SettingsError("GOOGLE_DRIVE_ROOT_FOLDER_ID is required when DRIVE_ACCESS_MODE != 'none'")

    # FIREBASE

    """
    firebase_web = FirebaseWebSettings(
        api_key=_getenv_required("FIREBASE_API_KEY"),
        auth_domain=_getenv_required("FIREBASE_AUTH_DOMAIN"),
        database_url=_getenv_required("FIREBASE_DATABASE_URL"),
        project_id=_getenv_required("FIREBASE_PROJECT_ID"),
        storage_bucket=_getenv_required("FIREBASE_STORAGE_BUCKET"),
        messaging_sender_id=_getenv_required("FIREBASE_MESSAGING_SENDER_ID"),
        app_id=_getenv_required("FIREBASE_APP_ID"),
    )
    """

    firebase_web = FirebaseWebSettings(
        api_key=get_required_secret("FIREBASE_API_KEY"),
        auth_domain=get_required_secret("FIREBASE_AUTH_DOMAIN"),
        database_url=get_required_secret("FIREBASE_DATABASE_URL"),
        project_id=get_required_secret("FIREBASE_PROJECT_ID"),
        storage_bucket=get_required_secret("FIREBASE_STORAGE_BUCKET"),
        messaging_sender_id=get_required_secret("FIREBASE_MESSAGING_SENDER_ID"),
        app_id=get_required_secret("FIREBASE_APP_ID"),
    )

    return Settings(
        project_root=project_root,
        config_path=app_config_json_path,
        google_client_secret=client_secret_json,
        google_oauth_token_json=token_json,
        google_scopes=scopes,
        spreadsheet_ids_by_file=spreadsheet_ids_by_file,
        google_access_mode=sheets_mode,
        drive_access_mode=drive_mode,

        firebase_web=firebase_web,
    )

# /src/infrastructure/config/settings_loader.py

from pathlib import Path

from src.infrastructure.config.firebase_settings_loader import (
    load_firebase_admin_settings,
    load_firebase_web_settings,
)
from src.infrastructure.config.google_settings_loader import (
    load_drive_access_mode,
    load_google_access_mode,
    load_google_scopes,
    load_spreadsheet_ids,
    resolve_google_client_secret_path,
    resolve_google_token_path,
    validate_drive_settings,
)
from src.infrastructure.config.path_settings_loader import (
    resolve_config_path,
    resolve_state_dir,
)
from src.infrastructure.config.secret_provider import SecretProvider
from src.infrastructure.config.settings_model import (
    AppMode,
    Settings,
)

USERS: dict[str, str] = {
    "AC+ Carrollton": "ECvBp9PdfagWJdBV2WrGwc4a6Wl1",
    "ARH Clifton Forge": "fI2oxx61iLcdX9EESZHpZCacx4B3",
    "ARH Emporia": "9Aq5EAqls4hWLfuiJSFqruy2mvT2",
    "ARH Lexington": "ssSOQyDrfeh8P7w9TJDFPjhlRuw2",
    "ARH Tappahannock": "KknUjuaVFaZZwsSM9jGf5tuMnYJ2",
    "Barnes": "LDM9dW0TuoZOg9wCtS6wXncud842",
    "Dallas Preserve Katie": "6fTPx9JglJXRB2YWbFgm0AUXfev2",
    "Chattington Manor": "AHcUuyTpTNRGZYLBzVIGZdbOXfq1",
    "Test Carrollton": "9Hajs1JHaHdVLqqnUOvlnbu45BO2",
    "Test Greenville": "7APGmTpXfmTP06FMM9SRoPGt59t1",
    "Dragon Pups": "wVp85WoiDxWesZKNxXuIHmBHfnq1",
}

USER_KEY: str = "Barnes"

def load_settings(
        *,
        project_root: Path,
        secret_provider: SecretProvider,
        app_mode: AppMode = AppMode.DEVELOPMENT,
        user_key: str = "ARH Lexington",
) -> Settings:
    project_root = project_root.resolve()

    config_path = resolve_config_path(project_root)

    state_dir = resolve_state_dir(project_root)

    google_access_mode = load_google_access_mode(secret_provider)
    drive_access_mode = load_drive_access_mode(secret_provider)

    validate_drive_settings(
        secret_provider=secret_provider,
        drive_access_mode=drive_access_mode,
    )

    google_scopes = load_google_scopes(
        google_access_mode=google_access_mode,
        drive_access_mode=drive_access_mode,
    )

    google_client_secret = resolve_google_client_secret_path(
        project_root=project_root,
        secret_provider=secret_provider,
    )

    google_oauth_token_json = resolve_google_token_path(
        project_root=project_root,
        state_dir=state_dir,
        secret_provider=secret_provider,
        google_access_mode=google_access_mode,
        drive_access_mode=drive_access_mode,
    )

    spreadsheet_ids_by_file = load_spreadsheet_ids(secret_provider)

    firebase_web = load_firebase_web_settings(secret_provider)
    firebase_admin = load_firebase_admin_settings(secret_provider)

    dev_user_id: str = USERS[user_key]
    # dev_user_id: str = "ssSOQyDrfeh8P7w9TJDFPjhlRuw2"

    return Settings(
        app_mode=app_mode,
        dev_user_id=dev_user_id,
        project_root=project_root,
        config_path=config_path,
        google_client_secret=google_client_secret,
        google_oauth_token_json=google_oauth_token_json,
        google_scopes=google_scopes,
        spreadsheet_ids_by_file=spreadsheet_ids_by_file,
        google_access_mode=google_access_mode,
        drive_access_mode=drive_access_mode,
        firebase_web=firebase_web,
        firebase_admin=firebase_admin,
    )

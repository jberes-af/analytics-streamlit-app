# /src/infrastructure/config/settings_model.py

from dataclasses import dataclass
from pathlib import Path
from typing import Literal, Mapping, Sequence


GoogleAccessMode = Literal["read", "write"]
DriveAccessMode = Literal["none", "read", "write", "all"]


@dataclass(frozen=True)
class FirebaseWebSettings:
    api_key: str
    auth_domain: str
    database_url: str
    project_id: str
    storage_bucket: str
    messaging_sender_id: str
    app_id: str

    def to_pyrebase_config(self) -> Mapping[str, str]:
        return {
            "apiKey": self.api_key,
            "authDomain": self.auth_domain,
            "databaseURL": self.database_url,
            "projectId": self.project_id,
            "storageBucket": self.storage_bucket,
            "messagingSenderId": self.messaging_sender_id,
            "appId": self.app_id,
        }


@dataclass(frozen=True)
class Settings:
    project_root: Path
    config_path: Path

    google_client_secret: Path
    google_oauth_token_json: Path
    google_scopes: Sequence[str]

    spreadsheet_ids_by_file: Mapping[str, str]
    google_access_mode: GoogleAccessMode
    drive_access_mode: DriveAccessMode

    # google_drive_root_folder_id: str | None = None
    # google_places_api_key: str

    firebase_web: FirebaseWebSettings

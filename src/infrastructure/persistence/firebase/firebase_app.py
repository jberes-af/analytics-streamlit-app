# infrastructure/config/firebase_app.py

from pathlib import Path
from typing import Any

import firebase_admin
from firebase_admin import App, credentials

"""
def init_firebase_app(
        *,
        database_url: str,
        service_account_path: str | Path | None = None,
        service_account_info: dict[str, Any] | None = None,
) -> App:
    try:
        return firebase_admin.get_app()

    except ValueError:
        pass

    if service_account_info is not None:
        cred = credentials.Certificate(service_account_info)

    elif service_account_path is not None:
        cred = credentials.Certificate(str(service_account_path))

    else:
        raise ValueError(
            "Either service_account_info or service_account_path is required."
        )

    return firebase_admin.initialize_app(
        cred,
        {
            "databaseURL": database_url,
        },
    )
"""


def init_firebase_admin_app(
    *,
    database_url: str,
    service_account_info: dict[str, Any],
) -> App:
    try:
        return firebase_admin.get_app()

    except ValueError:
        cred = credentials.Certificate(service_account_info)

        return firebase_admin.initialize_app(
            cred,
            {
                "databaseURL": database_url,
            },
        )
# /src/infrastructure/firebase/firebase_admin_service.py

from typing import Any

import firebase_admin
from firebase_admin import auth, credentials


class FirebaseAdminService:
    """
    Admin Firebase service.

    Uses service account credentials.

    Use for:
    - verifying ID tokens
    - reading user records
    - setting custom claims
    - revoking refresh tokens
    - privileged database/admin operations
    """

    def __init__(
        self,
        service_account_info: dict[str, Any],
        database_url: str | None = None,
        app_name: str = "[DEFAULT]",
    ) -> None:
        self._app = self._initialize_app(
            service_account_info=service_account_info,
            database_url=database_url,
            app_name=app_name,
        )

    @staticmethod
    def _initialize_app(
        service_account_info: dict[str, Any],
        database_url: str | None,
        app_name: str,
    ) -> firebase_admin.App:
        try:
            return firebase_admin.get_app(app_name)
        except ValueError:
            cred = credentials.Certificate(service_account_info)

            options: dict[str, Any] = {}
            if database_url:
                options["databaseURL"] = database_url

            return firebase_admin.initialize_app(
                credential=cred,
                options=options,
                name=app_name,
            )

    def verify_id_token(self, id_token: str) -> dict[str, Any]:
        return auth.verify_id_token(
            id_token,
            app=self._app,
        )

    def get_user(self, uid: str) -> auth.UserRecord:
        return auth.get_user(
            uid,
            app=self._app,
        )

    def set_custom_user_claims(
        self,
        uid: str,
        claims: dict[str, Any],
    ) -> None:
        auth.set_custom_user_claims(
            uid,
            claims,
            app=self._app,
        )

    def revoke_refresh_tokens(self, uid: str) -> None:
        auth.revoke_refresh_tokens(
            uid,
            app=self._app,
        )

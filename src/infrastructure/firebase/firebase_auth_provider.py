# /src/infrastructure/firebase/firebase_auth_provider.py

from src.application.auth.dto import AuthenticatedUserDTO


class FirebaseAuthProvider:
    def __init__(self, pyrebase_config: dict, service_account_info: dict):
        ...

    def authenticate(self, email: str, password: str) -> AuthenticatedUserDTO:
        user = self._py_auth.sign_in_with_email_and_password(email, password)

        return AuthenticatedUserDTO(
            email=user["email"],
            uid=user["localId"],
            display_name=user.get("displayName", ""),
        )

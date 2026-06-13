# firebase/firebase_service.py

"""
usage:
  * for login (firebase-authentication), use pyrebase module (because it's easier...)
"""

from firebase_admin import credentials, get_app
# from firebase_admin import firebase as fba_auth
from firebase_admin import initialize_app as fba_init_app
import pyrebase


def noquote(s):
    return s


import pyrebase


class FirebaseClientAuthService:
    def __init__(self, web_config: dict):
        firebase = pyrebase.initialize_app(web_config)
        self._auth = firebase.auth()

    def sign_in(self, email: str, password: str) -> dict:
        return self._auth.sign_in_with_email_and_password(email, password)


class FirebaseAuthService:
    def __init__(self):
        self._admin_app = None
        self._py_auth: pyrebase.pyrebase.Auth | None = None

    def init_admin_sdk(self,
                       service_account_info: dict[str, any],
                       database_url: str
                       ) -> None:
        """
        Initialize (or retrieve) the Firebase Admin SDK app,
        using the service-account JSON and the databaseURL.
        :param pyrebase_config: dict   # the JS-style one with apiKey, databaseURL, etc.
        :param service_account_info: dict  # the service-account JSON
        """
        try:
            # If already initialized, reuse it
            self._admin_app = get_app()
        except ValueError:
            cred = credentials.Certificate(service_account_info)
            self._admin_app = fba_init_app(
                cred,
                {"databaseURL": database_url},
            )

    def set_config(
            self,
            pyrebase_config: dict[str, str | None],
            service_account_info: dict[str, str | None],
    ) -> None:
        """
        Must call once before authenticate_user.
        - pyrebase_config: your Firebase Web app config (includes databaseURL)
        - service_account_info: your service-account JSON dict
        """
        # 1) init Admin SDK, pulling databaseURL out of your web config
        self.init_admin_sdk(
            service_account_info,
            pyrebase_config["databaseURL"],
        )

        # 2) init Pyrebase firebase data_models_client
        firebase = pyrebase.initialize_app(pyrebase_config)
        self._py_auth = firebase.auth()

    def authenticate_user(self, email: str, password: str) -> dict[str, str]:
        """
        sign-in via Pyrebase and returns the user info dict
        raise HTTPError on bad credentials
        """
        if not self._py_auth:
            raise RuntimeError("FirebaseService not configured! Call set_config first.")
        return self._py_auth.sign_in_with_email_and_password(email, password)

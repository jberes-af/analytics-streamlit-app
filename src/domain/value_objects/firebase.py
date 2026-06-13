# domain/value_objects/firebase_auth.py

from dataclasses import dataclass


@dataclass(frozen=True)
class Uid:
    value: str

    def __post_init__(self) -> None:
        v = self.value.strip()
        if not v:
            raise ValueError("uid must be non-empty")
        object.__setattr__(self, "value", v)


@dataclass(frozen=True)
class FirebasePath:
    value: str

    def __post_init__(self) -> None:
        v = self.value.strip()
        if not v:
            raise ValueError("firebase_auth path must be non-empty")
        if not v.startswith("/"):
            raise ValueError("firebase_auth path must start with '/'")
        if "//" in v:
            raise ValueError("firebase_auth path must not contain '//'")
        object.__setattr__(self, "value", v)

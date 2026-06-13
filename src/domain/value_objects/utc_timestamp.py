
# domain/value_objects/utc_timestamp.py
from dataclasses import dataclass
from datetime import datetime, timezone

@dataclass(frozen=True)
class UtcTimestamp:
    value: datetime

    def __post_init__(self) -> None:
        if not isinstance(self.value, datetime):
            raise TypeError("UtcTimestamp.value must be a datetime")
        if self.value.tzinfo is None or self.value.utcoffset() is None:
            raise ValueError("UtcTimestamp requires timezone-aware datetime")
        if self.value.utcoffset() != timezone.utc.utcoffset(None):
            raise ValueError("UtcTimestamp must be in UTC")

    @classmethod
    def from_datetime(cls, dt: datetime) -> "UtcTimestamp":
        if dt.tzinfo is None or dt.utcoffset() is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return cls(dt.astimezone(timezone.utc))

    @classmethod
    def from_iso(cls, iso_str: str) -> "UtcTimestamp":
        dt = datetime.fromisoformat(iso_str)
        return cls.from_datetime(dt)

    def to_iso(self) -> str:
        return self.value.isoformat()

    def __str__(self) -> str:
        return self.to_iso()

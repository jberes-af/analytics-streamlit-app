# application/ports/clock.py

# Purpose: To allow the application and domain to ask for “current time” without knowing how it is obtained.

from datetime import datetime
from typing import Protocol
# from domain.value_objects.utc_timestamp import UtcTimestamp

class ClockPort(Protocol):
    def now_utc(self) -> datetime:
        ...

# infrastructure/clock/system_clock.py

from datetime import datetime, timezone
from alerta.application.ports.clock import ClockPort
# from domain.value_objects.utc_timestamp import UtcTimestamp


class SystemClock(ClockPort):
    def now_utc(self) -> datetime:  # UtcTimestamp:
        # return UtcTimestamp.from_datetime(datetime.now(timezone.utc))
        return datetime.now(timezone.utc)

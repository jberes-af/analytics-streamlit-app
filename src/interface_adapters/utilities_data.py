# utilities_data.py

# utilities_data.py

from datetime import date, datetime, time, timedelta
from zoneinfo import ZoneInfo

from src.domain.entities.sensor import SensorEvent


def get_start_date_from_end_date_and_days_delta(
    end_date: date,
    days_delta: int,
) -> date:
    return end_date - timedelta(days=days_delta)


def convert_date_to_datetime(
    start_date: date,
    end_date: date,
    local_timezone: str,
) -> tuple[datetime, datetime]:
    local_tz = ZoneInfo(local_timezone)

    start_time = datetime.combine(
        start_date,
        time.min,
        tzinfo=local_tz,
    )

    end_time = datetime.combine(
        end_date,
        time.max,
        tzinfo=local_tz,
    )

    return start_time, end_time


def filter_events_by_time_period(
    events: list[SensorEvent],
    start_time: datetime,
    end_time: datetime,
) -> list[SensorEvent]:
    return [
        event
        for event in events
        if start_time <= event.activated_at_local <= end_time
    ]


def convert_datetime_to_seconds_since_midnight(
    timestamp: datetime,
) -> int:
    return (
        timestamp.hour * 3600
        + timestamp.minute * 60
        + timestamp.second
    )


def get_date_range_in_between_two_dates(
    start_date: date,
    end_date: date,
) -> list[date]:
    if end_date < start_date:
        raise ValueError(
            "end_date must be greater than or equal to start_date"
        )

    days = (end_date - start_date).days

    return [
        start_date + timedelta(days=offset)
        for offset in range(days + 1)
    ]
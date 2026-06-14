# utilities_data.py

from datetime import date, datetime, time, timedelta

from src.domain.entities.sensor import SensorEvent


def get_start_date_from_end_date_and_days_delta(
        end_date: date,
        days_delta: int,
) -> date:
    return end_date - timedelta(days=days_delta)


def convert_date_to_datetime(
        start_date: date,
        end_date: date,
) -> tuple[datetime, datetime]:
    start_time: datetime = datetime.combine(start_date, time.min)
    end_time: datetime = datetime.combine(end_date, time.max)
    return start_time, end_time


def filter_events_by_time_period(
        events: list[SensorEvent],
        start_time: datetime,
        end_time: datetime,
) -> list[SensorEvent]:
    return [
        event
        for event in events
        if start_time <= event.activated_at <= end_time
    ]


def convert_datetime_to_seconds_since_midnight(
    timestamp: datetime,
) -> int:
    return (
        timestamp.hour * 3600
        + timestamp.minute * 60
        + timestamp.second
    )
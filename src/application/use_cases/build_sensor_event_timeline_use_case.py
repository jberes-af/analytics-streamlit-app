# /src/application/use_cases/build_sensor_event_timeline_use_case.py


from datetime import date, datetime, time, timezone
from typing import Any
from zoneinfo import ZoneInfo

from src.application.dto.read_firebase_node_dtos import NodeType

from src.domain.entities.sensor import SensorEvent

from src.application.dto.read_firebase_node_dtos import (
    ReadFirebaseNodeRequestDTO,
    ReadFirebaseNodeResultDTO,
)

from src.application.dto.sensor_timeline_uc_dtos import (
    SensorEventTimelineRequestDTO,
    SensorEventTimelineResultDTO,
)

from src.application.services.read_firebase_node_service import (
    ReadFirebaseNodeService,
)


class BuildSensorEventTimelineUseCase:
    def __init__(
            self,
            read_firebase_node_service: ReadFirebaseNodeService,
    ) -> None:
        self._read_firebase_service = read_firebase_node_service

    def execute(
            self,
            request: SensorEventTimelineRequestDTO,
    ) -> SensorEventTimelineResultDTO:

        sensor_ids: list[str] = request.sensor_ids

        # Get sensor events for sensor IDS -------------------------------

        raw_sensor_events: list[ReadFirebaseNodeResultDTO] = []

        for sensor_id in sensor_ids:
            raw_events_by_sensor_id: ReadFirebaseNodeResultDTO = (
                self._read_firebase_service.read_node(
                    ReadFirebaseNodeRequestDTO(
                        node_id=sensor_id,
                        node_type=NodeType.SENSOR_EVENTS
                    )))
            raw_sensor_events.append(raw_events_by_sensor_id)

        # Convert list of raw sensor events to mapping -------------------

        events_by_sensor_id: dict[str, Any] = {
            events.node_id: events.data
            for events in raw_sensor_events
        }

        local_tz = ZoneInfo(request.local_timezone)

        events: list[SensorEvent] = self._build_sensor_events(
            sensor_ids=sensor_ids,
            events_by_sensor_id=events_by_sensor_id,
            local_timezone=local_tz,
        )

        start_time: datetime
        end_time: datetime
        start_time, end_time = self._convert_date_to_datetime(
            start_date=request.start_date,
            end_date=request.end_date,
            local_timezone=local_tz,
        )

        time_period_events: list[SensorEvent] = (
            self._filter_events_by_time_period(
                events=events,
                start_time=start_time,
                end_time=end_time,
            ))

        # collapsed events: local time from request
        collapsed_events: list[SensorEvent] = (
            self._collapse_consecutive_sensor_events(
                time_period_events
            ))

        return SensorEventTimelineResultDTO(
            start_time=start_time,
            end_time=end_time,
            collapsed_events=collapsed_events,
        )

    @staticmethod
    def _build_sensor_events(
            sensor_ids: list[str],
            events_by_sensor_id: dict[str, Any],
            local_timezone: ZoneInfo  #  str  # e.g. America / New_York
    ) -> list[SensorEvent]:
        events: list[SensorEvent] = []

        for sensor_id in sensor_ids:
            events_by_day = events_by_sensor_id.get(sensor_id, {})

            for timestamps_state in events_by_day.values():
                for timestamp_str, state in timestamps_state.items():
                    activated_at_utc = datetime.strptime(
                        timestamp_str,
                        "%Y%m%d%H%M%S",
                    ).replace(tzinfo=timezone.utc)

                    activated_at_local = activated_at_utc.astimezone(
                        local_timezone
                    )

                    events.append(
                        SensorEvent(
                            sensor_id=sensor_id,
                            activated_at_utc=activated_at_utc,
                            activated_at_local=activated_at_local,
                            sensor_state=state,
                        )
                    )

        return sorted(events, key=lambda event: event.activated_at_utc)

    @staticmethod
    def _collapse_consecutive_sensor_events(
            events: list[SensorEvent],
    ) -> list[SensorEvent]:
        if not events:
            return []

        sorted_events = sorted(
            events,
            key=lambda event: event.activated_at_utc,
        )

        collapsed: list[SensorEvent] = []

        for event in sorted_events:
            if not collapsed:
                collapsed.append(event)
                continue

            previous = collapsed[-1]

            if event.sensor_id == previous.sensor_id:
                # Replace previous with later activation.
                collapsed[-1] = event
            else:
                collapsed.append(event)

        return collapsed

    @staticmethod
    def _convert_date_to_datetime(
            start_date: date,
            end_date: date,
            local_timezone: ZoneInfo,
    ) -> tuple[datetime, datetime]:

        start_time = datetime.combine(
            start_date,
            time.min,
            tzinfo=local_timezone,
        )

        end_time = datetime.combine(
            end_date,
            time.max,
            tzinfo=local_timezone,
        )

        return start_time, end_time

    @staticmethod
    def _filter_events_by_time_period(
            events: list[SensorEvent],
            start_time: datetime,
            end_time: datetime,
    ) -> list[SensorEvent]:
        return [
            event
            for event in events
            if start_time <= event.activated_at_local <= end_time
        ]

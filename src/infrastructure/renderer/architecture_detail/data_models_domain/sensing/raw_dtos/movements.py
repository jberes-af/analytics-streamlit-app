# /src/infrastructure/renderer/architecture_detail/data_models_analytics/data_models_domain/sensing/movements.py


MOVEMENT_DTO: str = """
MovementDTO:
    sensor_start: SensorProfileDTO
    sensor_end: SensorProfileDTO
    time_start: str
    time_end: str
"""

MOVEMENT_PATTERN_REQUEST_DTO: str = """
MovementPatternRequestDTO:
    query_date: str
    query_scope: SensorQueryScopeEnum
    sensor id: str | None = None
    sensor group id: str | None = None
"""

MOVEMENT_PATTERN_RESPONSE_DTO: str = """
MovementPatternResponseDTO:
    query_date: date
    query_scope: SensorQueryScopeEnum
    sensor_id: str | None
    sensor_group_id: str | None
    movements: tuple[MovementDTO, ...]
    timeline_events: tuple[TimelineEventDTO, ...] = ()
"""

MOVEMENT_PATTERN_SERVICE: str = """
class MovementPatternService:
    def build_movements(
        self,
        timeline_events: tuple[TimelineEventDTO, ...],
    ) -> tuple[MovementDTO, ...]:

        sorted_events = sorted(
            timeline_events,
            key=lambda event: event.sensor_event.timestamp,
        )

        unique_events: list[TimelineEventDTO] = []

        for event in sorted_events:
            if not unique_events:
                unique_events.append(event)
                continue

            previous_event = unique_events[-1]

            if event.sensor_profile.sensor_id != previous_event.sensor_profile.sensor_id:
                unique_events.append(event)

        movements: list[MovementDTO] = []

        for start_event, end_event in zip(unique_events, unique_events[1:]):
            movements.append(
                MovementDTO(
                    sensor_start=start_event.sensor_profile,
                    sensor_end=end_event.sensor_profile,
                    time_start=start_event.sensor_event.timestamp,
                    time_end=end_event.sensor_event.timestamp,
                )
            )

        return tuple(movements)
"""

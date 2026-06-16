# /src/application/services/generate_insights_service.py


from datetime import date
from src.domain.entities.sensor import SensorProfile

from src.application.dto.activity_metric_dtos import (
    SensorWeeklyActivityDTO,
)

from src.application.dto.activity_uc_dtos import ActivityAnalysisResultDTO

from src.application.dto.activity_insights_dtos import (
    ActivityInsightDTO,
    ActivityInsightsDTO,
)

from src.application.ports.insights_use_case_ports import (
    ActivityInsightsGeneratorPort,
)


class GenerateInsightsService(ActivityInsightsGeneratorPort):
    def generate(
            self,
            sensor_ids: list[str],
            sensor_profiles: list[SensorProfile],
            analysis_results: ActivityAnalysisResultDTO
    ) -> ActivityInsightsDTO:
        weekly_insights: list[ActivityInsightDTO] = _build_weekly_activity_insights(
            sensor_ids=sensor_ids,
            sensor_profiles=sensor_profiles,
            weekly_analysis_results=analysis_results.weekly_sensor_activity,
        )
        return ActivityInsightsDTO(
            weekly_activity_insights=weekly_insights
        )


def _build_weekly_activity_insights2(
        sensor_ids: list[str],
        sensor_profiles: list[SensorProfile],
        weekly_analysis_results: list[SensorWeeklyActivityDTO],
) -> list[ActivityInsightDTO]:
    """
    """

    allowed_sensor_ids = set(sensor_ids) | {"ALL"}


def _build_weekly_activity_insights(
        sensor_ids: list[str],
        sensor_profiles: list[SensorProfile],
        weekly_analysis_results: list[SensorWeeklyActivityDTO],
) -> list[ActivityInsightDTO]:
    if not weekly_analysis_results:
        return []

    profile_by_id: dict[str, SensorProfile] = {
        profile.sensor_id: profile
        for profile in sensor_profiles
    }

    allowed_sensor_ids = set(sensor_ids) | {"ALL"}

    most_recent_week_end = max(
        item.week_end
        for item in weekly_analysis_results
    )

    results: list[ActivityInsightDTO] = []

    for weekly_result in weekly_analysis_results:
        if weekly_result.sensor_id not in allowed_sensor_ids:
            continue

        if weekly_result.week_end != most_recent_week_end:
            continue

        change_str = _formulate_change_percent_direction_text(
            weekly_result.change_percent
        )

        activations = weekly_result.total_activations_week
        date_str = f"{weekly_result.week_end.strftime('%b')} {weekly_result.week_end.day}"

        sid: str = weekly_result.sensor_id

        if sid == "ALL":
            sensor_name = "All Sensors"
        else:
            user_name = profile_by_id[sid].sensor_name
            location = profile_by_id[sid].sensor_location
            sensor_type = profile_by_id[sid].sensor_type
            sensor_name = f"{user_name} ({location} {sensor_type})"

        message_line_1 = f"Activations were {activations}."
        message_line_2 = change_str

        results.append(
            ActivityInsightDTO(
                sensor_id=weekly_result.sensor_id,
                message_line_1=message_line_1,
                end_date=weekly_result.week_end,
                metric_name="weekly_total_activations",
                current_value=float(activations),
                change_percent=weekly_result.change_percent,
                message_header=sensor_name,
                section_header=f"Week ending: {date_str}",
                message_line_2=message_line_2,
            )
        )

    return results


def _formulate_change_percent_direction_text(
        change_percent: float | None
):
    if change_percent is None:
        return f"percent change value not available."
    elif change_percent < 0:
        return f"↓ {(100 * change_percent):.1f}% lower than the previous week."
    else:
        return f"↑ {(100 * change_percent):.1f}% higher than the previous week."

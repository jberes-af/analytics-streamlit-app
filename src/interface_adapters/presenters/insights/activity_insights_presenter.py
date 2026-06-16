# src/interface_adapters/presenters/activity_insights_presenter.py

from src.application.dto.activity_insights_dtos import (
    ActivityInsightDTO,
)

from src.interface_adapters.view_models.activity_insights_view_models import (
    ActivityInsightViewModel,
    ActivityInsightsViewModel,
)


class ActivityInsightsPresenter:
    def present(
            self,
            activity_insights: list[ActivityInsightDTO],
    ) -> ActivityInsightsViewModel:
        return ActivityInsightsViewModel(
            weekly_activity_insights=[
                self._present_weekly_activity_insight(insight)
                for insight in activity_insights
            ]
        )

    def _present_weekly_activity_insight(
            self,
            insight: ActivityInsightDTO,
    ) -> ActivityInsightViewModel:
        return ActivityInsightViewModel(
            sensor_id=insight.sensor_id,
            message_line_1=insight.message_line_1,
            end_date=insight.end_date,
            end_date_label=self._format_date(insight.end_date),
            metric_name=insight.metric_name,
            current_value=insight.current_value,
            current_value_label=self._format_value(insight.current_value),
            change_percent=insight.change_percent,
            change_percent_label=self._format_change_percent(
                insight.change_percent
            ),
            message_header=insight.message_header,
            section_header=insight.section_header,
            message_line_2=insight.message_line_2,
        )

    @staticmethod
    def _format_date(
            value,
    ) -> str:
        return f'{value.strftime("%b")} {value.day}, {value.strftime("%Y")}'

    @staticmethod
    def _format_value(
            value: float | None,
    ) -> str:
        if value is None:
            return "N/A"

        return f"{value:,.0f}"

    @staticmethod
    def _format_change_percent(
            value: float | None,
    ) -> str:
        if value is None:
            return "N/A"

        direction = "higher" if value >= 0 else "lower"
        return f"{abs(value * 100):.1f}% {direction}"
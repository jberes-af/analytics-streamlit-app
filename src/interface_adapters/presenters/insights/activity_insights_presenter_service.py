# activity_insights_presenter_service.py

from src.application.dto.activity_insights_dtos import ActivityInsightDTO

from src.interface_adapters.presenters.insights.activity_insights_presenter import (
    ActivityInsightsPresenter,
)

from src.interface_adapters.view_models.activity_insights_view_models import (
    ActivityInsightsViewModel)


class InsightsPresenterService:
    def __init__(
            self,
            activity_insights_presenter: ActivityInsightsPresenter,
    ):
        self._activity_insights_presenter = activity_insights_presenter

    def present_weekly_activity_insights(
            self,
            weekly_activity_insights: list[ActivityInsightDTO]
    ) -> ActivityInsightsViewModel:
        insights_view_model: ActivityInsightsViewModel = (
            self._activity_insights_presenter.present(
                activity_insights=weekly_activity_insights))

        return insights_view_model

# /src/interface_adapters/presenters/activity/activity_presenter_service.py

from src.application.use_cases.analyze_activity_levels_use_case import (
    ActivityAnalysisResultDTO,
)

from src.interface_adapters.presenters.activity.activity_metrics_presenter import (
    ActivityAnalysisMetricsPresenter,
)

from src.interface_adapters.presenters.activity.weekly_activity_presenter import (
    WeeklyActivityPresenter,
)

from src.interface_adapters.view_models.activity.activity_metrics_vm import (
    ActivityAnalysisViewModel,
)

from src.interface_adapters.view_models.activity.weekly_activity_vm import (
    WeeklyActivityViewModel,
)


class ActivityPresenterService:
    def __init__(
            self,
            activity_metrics_presenter: ActivityAnalysisMetricsPresenter,
            weekly_activity_presenter: WeeklyActivityPresenter,
    ):
        self._metrics_presenter = activity_metrics_presenter
        self._weekly_presenter = weekly_activity_presenter

    def present_activity_metrics(
            self,
            result: ActivityAnalysisResultDTO | None,
    ) -> ActivityAnalysisViewModel:
        activity_metrics_view_model: ActivityAnalysisViewModel = (
            self._metrics_presenter.present(result))

        return activity_metrics_view_model

    def present_weekly_activity(
            self,
            result: ActivityAnalysisResultDTO | None,
    ) -> WeeklyActivityViewModel:
        if result is None:
            return self._weekly_presenter.present([])

        return self._weekly_presenter.present(
            result.weekly_sensor_activity
        )

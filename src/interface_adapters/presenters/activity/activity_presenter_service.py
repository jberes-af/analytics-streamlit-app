# /src/interface_adapters/presenters/activity/activity_presenter_service.py

from src.application.dto.activity_metric_dtos import (
    SensorTimePeriodStatisticsDTO, ActivityTrendDTO,
)

from src.application.use_cases.analyze_activity_levels_use_case import (
    ActivityAnalysisResultDTO,
)

from src.interface_adapters.presenters.activity.activity_metrics_presenter import (
    ActivityAnalysisMetricsPresenter,
)

from src.interface_adapters.presenters.activity.weekly_activity_presenter import (
    WeeklyActivityPresenter,
)

from src.interface_adapters.presenters.activity.sensor_statistics_presenter import (
    SensorTimePeriodStatisticsPresenter,
)

from src.interface_adapters.presenters.activity.activity_trend_presenter import (
    ActivityTrendPresenter,
)

from src.interface_adapters.view_models.activity.activity_metrics_vm import (
    ActivityAnalysisViewModel,
)

from src.interface_adapters.view_models.activity.weekly_activity_vm import (
    WeeklyActivityViewModel,
)

from src.interface_adapters.view_models.activity.sensor_statistics_vm import (
    SensorTimePeriodStatisticsViewModel,
)

from src.interface_adapters.view_models.activity.activity_trend_vm import (
    ActivityTrendViewModel,
)


class ActivityPresenterService:
    def __init__(
            self,
            activity_metrics_presenter: ActivityAnalysisMetricsPresenter,
            weekly_activity_presenter: WeeklyActivityPresenter,
            sensor_activity_statistics_presenter: SensorTimePeriodStatisticsPresenter,
            activity_trend_presenter: ActivityTrendPresenter,
    ):
        self._metrics_presenter = activity_metrics_presenter
        self._weekly_presenter = weekly_activity_presenter
        self._statistics_presenter = sensor_activity_statistics_presenter
        self._trend_presenter = activity_trend_presenter

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

    def present_time_period_activity_statistics(
            self,
            results: list[SensorTimePeriodStatisticsDTO],
    ) -> SensorTimePeriodStatisticsViewModel:
        return self._statistics_presenter.present(results)

    def present_activity_trend(
            self,
            sensor_ids: list[str],
            trend_results: list[ActivityTrendDTO],
    ) -> ActivityTrendViewModel:
        return self._trend_presenter.present(
            sensor_ids=sensor_ids,
            result=trend_results)

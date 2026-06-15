# /src/interface_adapters/output_handlers/activity/activity_results_handler.py

from datetime import date

from src.domain.entities.sensor import SensorEvent

# --- APPLICATION

from src.application.dto.activity_metric_dtos import (
    ActivityTrendDTO,
    SensorActivityPercentOfTotalDTO,
    SensorTimePeriodStatisticsDTO,
)

from src.application.dto.activity_uc_dtos import (
    DailyActivityBySensorIdDTO,
    ActivityAnalysisResultDTO,
)

# --- INTERFACE ADAPTERS

from src.interface_adapters.output_handlers.activity.results_to_dataframe_adapter import (
    transform_results_to_dataframe,
)

from src.interface_adapters.presenters.activity.activity_presenter_service import (
    ActivityPresenterService,
)

from src.interface_adapters.views.console.console_view_service import (
    ActivityMetricsDataFrames,
    ConsoleViewService,
)

from src.interface_adapters.view_models.activity.activity_metrics_vm import (
    ActivityAnalysisViewModel,
)

from src.interface_adapters.view_models.activity.sensor_statistics_vm import (
    SensorTimePeriodStatisticsViewModel,
)

from src.interface_adapters.views.console.debug_console_view import (
    DebugConsoleView,
)

# --- INFRASTRUCTURE

from src.infrastructure.services.renderers.pandas.pandas_dataframe_renderer import (
    PandasDataFrameRenderer,
)


def handle_result_outputs_activity(
        sensor_events: list[SensorEvent],
        activity_metrics_result: ActivityAnalysisResultDTO,
        activity_presenter_service: ActivityPresenterService,
        dataframe_renderer: PandasDataFrameRenderer,
        sensor_ids: list[str],
        console_view_service: ConsoleViewService,
        start_date: date,
        end_date: date,
) -> None:
    _handle_sensor_summary_outputs(
        sensor_ids=sensor_ids,
        combined_sensor_activity=activity_metrics_result.combined_sensor_activity,
        sensor_by_id_activity=activity_metrics_result.sensor_by_id_by_date_activity,
        start_date=start_date,
        end_date=end_date,
    )

    _handle_weekly_activity_outputs(
        activity_metrics_result=activity_metrics_result,
        presenter_service=activity_presenter_service,
        console_view_service=console_view_service,
    )

    _handle_sensor_trend_outputs(
        sensor_ids=sensor_ids,
        result=activity_metrics_result.activity_trend_by_sensor_id,
    )

    _handle_sensor_activity_time_period_statistics(
        results=activity_metrics_result.sensor_time_period_statistics,
        presenter_service=activity_presenter_service,
    )

    _handle_activity_metrics_outputs(
        activity_metrics_result=activity_metrics_result,
        presenter_service=activity_presenter_service,
        console_view_service=console_view_service,
        dataframe_renderer=dataframe_renderer,
    )


def _handle_activity_metrics_outputs(
        activity_metrics_result: ActivityAnalysisResultDTO,
        presenter_service: ActivityPresenterService,
        console_view_service: ConsoleViewService,
        dataframe_renderer: PandasDataFrameRenderer,
):
    # Get view model(s); show view; write files

    vm: ActivityAnalysisViewModel = (
        presenter_service.present_activity_metrics(
            result=activity_metrics_result,
        ))

    metrics_dataframes: ActivityMetricsDataFrames = (
        transform_results_to_dataframe(
            daily_vm=vm.daily_activity,
            sensor_vm=vm.sensor_activity,
            hourly_vm=vm.hourly_activity,
            rolling_vm=vm.rolling_activity,
            peak_vm=vm.peak_activity,
            inactivity_vm=vm.inactivity_periods,
            dataframe_renderer=dataframe_renderer))

    console_view_service.render_activity_metrics_debug_view(
        metrics_dataframes=metrics_dataframes)


def _handle_weekly_activity_outputs(
        activity_metrics_result: ActivityAnalysisResultDTO,
        presenter_service: ActivityPresenterService,
        console_view_service: ConsoleViewService,
):
    vm = presenter_service.present_weekly_activity(
        result=activity_metrics_result,
    )

    console_view_service.render_weekly_activity_view(vm)


def _handle_sensor_trend_outputs(
        sensor_ids: list[str],
        result: list[ActivityTrendDTO],
):
    DebugConsoleView().render_sensor_trend_result(
        sensor_ids=sensor_ids,
        result=result,
    )


def _handle_sensor_activity_time_period_statistics(
        results: list[SensorTimePeriodStatisticsDTO],
        presenter_service: ActivityPresenterService,
) -> SensorTimePeriodStatisticsViewModel:
    return presenter_service.present_time_period_activity_statistics(
        results=results,
    )


def _handle_sensor_summary_outputs(
        sensor_ids: list[str],
        combined_sensor_activity: list[SensorActivityPercentOfTotalDTO],
        sensor_by_id_activity: list[DailyActivityBySensorIdDTO],
        start_date: date,
        end_date: date,
):
    id_to_record_by_date: dict[str, DailyActivityBySensorIdDTO] = {
        record.sensor_id: record
        for record in sensor_by_id_activity
    }

    for sensor_id in sensor_ids:
        map_date = {}
        if sensor_id in id_to_record_by_date:
            record = id_to_record_by_date[sensor_id]
            map_date[record.date] = record.activation_count

    DebugConsoleView().render_sensor_summary_result(
        sensor_ids=sensor_ids,
        combined_sensor_activity=combined_sensor_activity,
        sensor_by_id_activity=sensor_by_id_activity,
        start_date=start_date,
        end_date=end_date,
    )

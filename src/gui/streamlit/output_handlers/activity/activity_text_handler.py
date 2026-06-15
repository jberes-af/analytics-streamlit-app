# /src/interface_adapters/output_handlers/results_handler.py

from datetime import date

from src.domain.entities.sensor import SensorEvent

# --- APPLICATION

from src.application.dto.run_analysis_use_cases_dtos import (
    RunAnalysisUseCasesResultDTO,
)

from src.application.dto.sensor_timeline_uc_dtos import (
    SensorEventTimelineResultDTO,
)

# --- INTERFACE ADAPTERS

from src.interface_adapters.presenters.activity.activity_presenter_service import (
    ActivityPresenterService,
)

# --- INFRASTRUCTURE

from src.infrastructure.services.renderers.pandas.pandas_dataframe_renderer import (
    PandasDataFrameRenderer,
)

from src.interface_adapters.output_handlers.activity.activity_results_handler import (
    handle_result_outputs_activity,
)

from src.interface_adapters.views.console.console_view_service import (
    ConsoleViewService,
)


def handle_result_outputs_orchestrator(
        *,
        response: RunAnalysisUseCasesResultDTO,
        activity_presenter_service: ActivityPresenterService,
        console_view_service: ConsoleViewService,
        dataframe_renderer: PandasDataFrameRenderer
) -> None:
    sensor_timeline: SensorEventTimelineResultDTO = (
        response.build_sensor_timeline_result)
    sensor_ids: list[str] = response.run_request.sensor_ids
    sensor_events: list[SensorEvent] = sensor_timeline.collapsed_events

    start_date: date = response.run_request.start_date
    end_date: date = response.run_request.end_date

    # --- ACTIVITY

    handle_result_outputs_activity(
        sensor_events=sensor_events,
        activity_metrics_result=response.analyze_activity_result,
        activity_presenter_service=activity_presenter_service,
        dataframe_renderer=dataframe_renderer,
        sensor_ids=sensor_ids,
        console_view_service=console_view_service,
        start_date=start_date,
        end_date=end_date,
    )

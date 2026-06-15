# /src/interface_adapters/output_handlers/shared/shared_results_handler.py

from datetime import datetime

from src.domain.entities.sensor import (
    SensorProfile,
    SensorEvent,
)

# --- APPLICATION

"""
from src.application.dto.sensor_timeline_uc_dtos import (
    SensorLastSeenDTO,
    MostRecentSensorEventDTO,
)
"""

from src.application.dto.run_analysis_use_cases_dtos import (
    RunAnalysisUseCasesRequestDTO,
)

# --- INTERFACE ADAPTERS

from src.interface_adapters.presenters.run_all_config_presenter import (
    RunConfigurationPresenter,
)
from src.interface_adapters.view_models.shared_view_model import RunConfigViewModel

from src.interface_adapters.views.console.console_view_service import (
    ConsoleViewService,
)


# --- INFRASTRUCTURE


def handle_result_outputs_shared(
        run_analysis_request: RunAnalysisUseCasesRequestDTO,
        sensor_ids: list[str],
        # sensor_profiles: list[SensorProfile],
        # sensor_events: list[SensorEvent],
        # most_recent_events: list[MostRecentSensorEventDTO],
        # sensor_online_statuses: list[SensorLastSeenDTO],
        console_view_service: ConsoleViewService,

        # presenter: RunConfigurationPresenter | None = None,
) -> None:
    _handle_run_all_configuration(
        run_all_request=run_analysis_request,
        sensor_ids=sensor_ids,
        sensor_profiles=sensor_profiles,
        most_recent_events=most_recent_events,
        sensor_online_statuses=sensor_online_statuses,
        console_view_service=console_view_service,
    )


def _handle_run_all_configuration(
        run_all_request: RunAllUseCasesRequestDTO,
        sensor_ids: list[str],
        sensor_profiles: list[SensorProfile],
        most_recent_events: list[MostRecentSensorEventDTO],
        sensor_online_statuses: list[SensorLastSeenDTO],
        console_view_service: ConsoleViewService,
) -> None:

    id_to_last_activation: dict[str, datetime | None] = {
        event.sensor_id: event.activated_at_utc
        for event in most_recent_events
    }

    run_configuration_vm = RunConfigurationPresenter().present_timestamp_chart(
        run_all_request,
        sensor_ids,
        sensor_profiles,
        id_to_last_activation,
        sensor_online_statuses,
    )

    console_view_service.render_run_config_info_view(
        run_configuration_vm=run_configuration_vm,
    )

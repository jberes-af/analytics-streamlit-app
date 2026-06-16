# src/main/composition_root.py

from dataclasses import dataclass

# --- DOMAIN

from src.domain.services.movement_analysis.sessionizer import Sessionizer

from src.domain.services.movement_analysis.sequence_counter import SequenceCounter

from src.domain.services.movement_analysis.transition_probability_calculator import (
    TransitionProbabilityCalculator,
)

from src.domain.services.movement_analysis.time_bucket_comparator import (
    TimeBucketComparator,
)

# --- APPLICATION

from src.application.ports.firebase_rtdb import FirebaseRtdbPort

from src.application.ports.aws_appsync_ports import SensorLastSeenPort

from src.application.ports.activity_use_case_ports import (
    ActivityMetricsCalculatorPort,
)

from src.application.services.read_firebase_node_service import (
    ReadFirebaseNodeService,
)

from src.application.services.activity.analyze_metrics_service import (
    ActivityMetricsService,
)

from src.application.use_cases.use_cases_interactor import (
    RunAnalyticsUseCasesInteractor,
    BuildSensorEventTimelineInteractor,
    AnalyzeMovementPatternsInteractor,
    AnalyzeActivityLevelsInteractor,
)

from src.application.use_cases.build_sensor_event_timeline_use_case import (
    BuildSensorEventTimelineUseCase,
)

from src.application.use_cases.analyze_movement_patterns_use_case import (
    AnalyzeMovementPatternsUseCase,
)

from src.application.use_cases.analyze_activity_levels_use_case import (
    AnalyzeActivityLevelsUseCase,
)

# --- INFRASTRUCTURE ADAPTERS

from src.infrastructure.config.settings_loader import Settings
# from src.infrastructure.config.app_config_models import AppRuntimeConfig

from src.infrastructure.persistence.firebase.firebase_app import (
    init_firebase_app)

from src.infrastructure.persistence.firebase.firebase_rtdb_adapter import (
    FirebaseRtdbAdapter)

from src.infrastructure.persistence.aws.appsync_last_seen_adapter import (
    AppSyncLastSeenAdapter,
)

from src.infrastructure.services.analysis.pandas.activity.activity_metrics_calculator import (
    PandasActivityMetricsCalculator,
)

from src.infrastructure.services.analysis.pandas.activity.activity_dataframe_factory import (
    ActivityDataFrameFactory,
)

from src.infrastructure.services.analysis.pandas.activity.daily_activity_calculator import (
    DailyActivityCalculator,
)

from src.infrastructure.services.analysis.pandas.activity.hourly_activity_calculator import (
    HourlyActivityCalculator,
)

from src.infrastructure.services.analysis.pandas.activity.rolling_activity_calculator import (
    RollingActivityCalculator,
)

from src.infrastructure.services.analysis.pandas.activity.sensor_activity_calculator import (
    SensorActivityCalculator,
)

from src.infrastructure.services.analysis.pandas.activity.peak_activity_calculator import (
    PeakActivityCalculator,
)

from src.infrastructure.services.analysis.pandas.activity.inactivity_period_calculator import (
    InactivityPeriodCalculator,
)

from src.infrastructure.services.analysis.pandas.activity.activity_distribution_calculator import (
    ActivityDistributionCalculator,
)

from src.infrastructure.services.analysis.pandas.activity.sensor_activity_trend_calculator import (
    ActivityTrendCalculator,
)
from src.infrastructure.services.analysis.pandas.activity.weekly_activity_calculator import (
    WeeklyActivityCalculator,
)

from src.infrastructure.services.renderers.matplotlib.matplotlib_sensor_week_plotter import (
    MatplotlibSensorWeekPlotter,
)

from src.infrastructure.services.renderers.matplotlib.matplotlib_bar_vertical_chart_renderer import (
    MatplotlibVerticalBarChartPlotter,
)

from src.infrastructure.services.renderers.matplotlib.matplotlib_line_chart_renderer import (
    MatplotlibLineChartPlotter,
)

from src.infrastructure.services.renderers.matplotlib.matplotlib_scatter_chart_renderer import (
    MatplotlibScatterChartPlotter,
)

from src.infrastructure.services.renderers.pandas.pandas_dataframe_renderer import (
    PandasDataFrameRenderer,
)

from src.infrastructure.services.renderers.markdown.movements_markdown_renderer import (
    MovementAnalysisMarkdownRenderer,
)

from src.infrastructure.services.renderers.console.movements_console_renderer import (
    MovementAnalysisConsoleRenderer,
)

# --- INTERFACE ADAPTERS

from src.interface_adapters.controllers.analytics_controller import (
    RunAnalyticsUseCasesController,
)

from src.interface_adapters.presenters.activity.activity_metrics_presenter import (
    ActivityAnalysisMetricsPresenter,
)

from src.interface_adapters.presenters.activity.weekly_activity_presenter import (
    WeeklyActivityPresenter,
)

from src.interface_adapters.presenters.activity.activity_presenter_service import (
    ActivityPresenterService,
)

from src.interface_adapters.presenters.movement.movement_analysis_presenter import (
    MovementAnalysisPresenter)

from src.interface_adapters.presenters.movement.sensor_week_plot_presenter import (
    SensorWeekPlotPresenter,
)

from src.interface_adapters.presenters.charts.charts_presenter_service import (
    ChartsPresenterService,
)

from src.interface_adapters.views.console.debug_console_view import (
    DebugConsoleView,
)

from src.interface_adapters.views.console.weekly_activity_console_view import (
    WeeklyActivityConsoleRenderer,
)

from src.interface_adapters.views.console.console_view_service import (
    ConsoleViewService,
)

# --- MAIN

# from src.main.compo_root_google_sheets_repo import get_sheets_repository_normalize_transactions

import logging

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class AppContainer:
    run_controller: RunAnalyticsUseCasesController

    activity_presenter_service: ActivityPresenterService
    # activity_metrics_presenter: ActivityAnalysisMetricsPresenter

    movements_presenter: MovementAnalysisPresenter
    sensor_week_plot_presenter: SensorWeekPlotPresenter

    charts_presenter_service: ChartsPresenterService

    sensor_week_plotter: MatplotlibSensorWeekPlotter
    line_chart_plotter: MatplotlibLineChartPlotter
    bar_chart_plotter: MatplotlibVerticalBarChartPlotter
    scatter_chart_plotter: MatplotlibScatterChartPlotter

    console_view_service: ConsoleViewService

    movements_console_renderer: MovementAnalysisConsoleRenderer
    movements_markdown_renderer: MovementAnalysisMarkdownRenderer
    dataframe_renderer: PandasDataFrameRenderer
    # table_writer: CsvWriter


def build_analysis_app_container(
        *,
        settings: Settings,
        # cfg: AppRuntimeConfig
) -> AppContainer:
    # --- ADAPTERS



    # --- ADAPTERS: AWS AppSync
    app_sync_last_seen: SensorLastSeenPort = AppSyncLastSeenAdapter(
        endpoint=settings.appsync_endpoint,
        api_key=settings.appsync_api_key)

    # --- USE CASES

    build_sensor_timeline_uc = (
        _build_sensor_connectivity_use_case(
            read_firebase_node_service=read_firebase_node_service,
            read_app_sync_last_seen_service=app_sync_last_seen,
        ))


    run_all_use_cases: RunAnalyticsUseCasesInteractor = RunAnalyticsUseCasesInteractor(
        analyze_movements_use_case=analyze_movements_uc,
        analyze_activity_use_case=analyze_activity_uc,
        build_sensor_event_timeline_use_case=build_sensor_timeline_uc,
    )

    logging.info("Use cases built")

    # --- CONTROLLER

    run_controller: RunAnalyticsUseCasesController = _build_controller(
        run_all_use_cases=run_all_use_cases,
    )

    logging.info("Coordinator controller built")


    # --- APP CONTAINER

    return AppContainer(
        run_controller=run_controller,

        activity_presenter_service=activity_presenter_service,

        movements_presenter=MovementAnalysisPresenter(),
        sensor_week_plot_presenter=SensorWeekPlotPresenter(),

        charts_presenter_service=ChartsPresenterService(),

        sensor_week_plotter=MatplotlibSensorWeekPlotter(),
        line_chart_plotter=MatplotlibLineChartPlotter(),
        bar_chart_plotter=MatplotlibVerticalBarChartPlotter(),
        scatter_chart_plotter=MatplotlibScatterChartPlotter(),

        console_view_service=console_view_service,

        movements_console_renderer=MovementAnalysisConsoleRenderer(),
        movements_markdown_renderer=MovementAnalysisMarkdownRenderer(),
        dataframe_renderer=PandasDataFrameRenderer(),
        # table_writer=CsvWriter()
    )


"""
BUILD CONTROLLER
"""


def _build_controller(
        *,
        run_all_use_cases: RunAnalyticsUseCasesInteractor,
) -> RunSensorConnectivityController:
    return RunSensorConnectivityController(
        run_sensor_connectivity__cases=run_sensor_connectivity_use_cases,
    )


"""
BUILD USE CASES
"""


def _build_sensor_connectivity_use_case(
        read_app_sync_last_seen_service: SensorLastSeenPort,
) -> BuildSensorConnectivityInteractor:
    return BuildSensorConnectivityUseCase(
        read_app_sync_last_seen_service=read_app_sync_last_seen_service,
    )




connectivity_app_container = build_connectivity_app_container()

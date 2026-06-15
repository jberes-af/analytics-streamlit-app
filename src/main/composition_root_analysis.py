# src/main/composition_root.py

from dataclasses import dataclass

# --- DOMAIN


# --- APPLICATION


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
    RunAnalysisUseCasesInteractor,
    BuildSensorEventTimelineInteractor,
    AnalyzeActivityLevelsInteractor,
)

from src.application.use_cases.build_sensor_event_timeline_use_case import (
    BuildSensorEventTimelineUseCase,
)

from src.application.use_cases.analyze_activity_levels_use_case import (
    AnalyzeActivityLevelsUseCase,
)

# --- INFRASTRUCTURE ADAPTERS

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

from src.infrastructure.services.analysis.pandas.activity.sensor_time_period_statistics_calculator import (
    SensorTimePeriodStatisticsCalculator,
)

from src.infrastructure.services.renderers.plotly.line_chart_renderer import (
    PlotlyLineChartRenderer,
)

from src.infrastructure.services.renderers.plotly.bar_vertical_chart_renderer import (
    PlotlyVerticalBarChartRenderer,
)

from src.infrastructure.services.renderers.plotly.bar_horizontal_chart_renderer import (
    PlotlyHorizontalBarChartRenderer,
)

from src.infrastructure.services.renderers.plotly.line_scatter_chart_renderer import (
    PlotlyScatterLineChartRenderer,
)

from src.infrastructure.services.renderers.plotly.scatter_chart_renderer import (
    PlotlyScatterChartRenderer,
)

from src.infrastructure.services.renderers.pandas.pandas_dataframe_renderer import (
    PandasDataFrameRenderer,
)

# --- INTERFACE ADAPTERS

from src.interface_adapters.controllers.analysis_controller import (
    RunAnalysisUseCasesController,
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

from src.interface_adapters.presenters.activity.activity_trend_presenter import (
    ActivityTrendPresenter,
)

from src.interface_adapters.presenters.activity.sensor_statistics_presenter import (
    SensorTimePeriodStatisticsPresenter,
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
class AnalysisAppContainer:
    run_controller: RunAnalysisUseCasesController

    activity_presenter_service: ActivityPresenterService
    # activity_metrics_presenter: ActivityAnalysisMetricsPresenter

    charts_presenter_service: ChartsPresenterService

    # sensor_week_plotter: MatplotlibSensorWeekPlotter
    bar_vertical_chart_plotter: PlotlyVerticalBarChartRenderer
    bar_horizontal_chart_plotter: PlotlyHorizontalBarChartRenderer
    line_chart_renderer: PlotlyLineChartRenderer
    scatter_chart_plotter: PlotlyScatterChartRenderer
    scatter_line_chart_renderer: PlotlyScatterLineChartRenderer

    console_view_service: ConsoleViewService

    # movements_console_renderer: MovementAnalysisConsoleRenderer
    # movements_markdown_renderer: MovementAnalysisMarkdownRenderer
    dataframe_renderer: PandasDataFrameRenderer
    # table_writer: CsvWriter


def build_analysis_app_container(
        *,
        read_firebase_node_service
) -> AnalysisAppContainer:
    # --- USE CASES

    build_sensor_timeline_uc = (
        _build_sensor_event_timeline_use_case(
            read_firebase_node_service=read_firebase_node_service,
        ))

    analyze_activity_uc: AnalyzeActivityLevelsInteractor = (
        _build_analyze_activity_use_case(
        ))

    run_all_use_cases: RunAnalysisUseCasesInteractor = RunAnalysisUseCasesInteractor(
        analyze_activity_use_case=analyze_activity_uc,
        build_sensor_event_timeline_use_case=build_sensor_timeline_uc,
    )

    logging.info("Use cases built")

    # --- CONTROLLER

    run_controller: RunAnalysisUseCasesController = _build_controller(
        run_all_use_cases=run_all_use_cases,
    )

    logging.info("Coordinator controller built")

    # --- PRESENTER

    activity_presenter_service = ActivityPresenterService(
        activity_metrics_presenter=ActivityAnalysisMetricsPresenter(),
        weekly_activity_presenter=WeeklyActivityPresenter(),
        sensor_activity_statistics_presenter=SensorTimePeriodStatisticsPresenter(),
        activity_trend_presenter=ActivityTrendPresenter(),
    )

    # --- VIEWS

    console_view_service = ConsoleViewService(
        activity_metrics_debug_view=DebugConsoleView(),
        weekly_activity_view=WeeklyActivityConsoleRenderer(),
    )

    # --- APP CONTAINER

    return AnalysisAppContainer(
        run_controller=run_controller,

        activity_presenter_service=activity_presenter_service,

        charts_presenter_service=ChartsPresenterService(),

        # sensor_week_plotter=MatplotlibSensorWeekPlotter(),
        bar_vertical_chart_plotter=PlotlyVerticalBarChartRenderer(),
        bar_horizontal_chart_plotter=PlotlyHorizontalBarChartRenderer(),
        line_chart_renderer=PlotlyLineChartRenderer(),
        scatter_chart_plotter=PlotlyScatterChartRenderer(),
        scatter_line_chart_renderer=PlotlyScatterLineChartRenderer(),

        console_view_service=console_view_service,

        # movements_console_renderer=MovementAnalysisConsoleRenderer(),
        # movements_markdown_renderer=MovementAnalysisMarkdownRenderer(),
        dataframe_renderer=PandasDataFrameRenderer(),
    )


"""
BUILD CONTROLLER
"""


def _build_controller(
        *,
        run_all_use_cases: RunAnalysisUseCasesInteractor,
        # analyze_movements_use_case: AnalyzeMovementPatternsInteractor,
) -> RunAnalysisUseCasesController:
    return RunAnalysisUseCasesController(
        run_analysis_use_cases=run_all_use_cases,
    )


"""
BUILD USE CASES
"""


def _build_sensor_event_timeline_use_case(
        read_firebase_node_service: ReadFirebaseNodeService,
) -> BuildSensorEventTimelineInteractor:
    return BuildSensorEventTimelineUseCase(
        read_firebase_node_service=read_firebase_node_service,
    )


def _build_analyze_activity_use_case() -> AnalyzeActivityLevelsInteractor:
    dataframe_factory = ActivityDataFrameFactory()

    daily_calculator = DailyActivityCalculator()
    sensor_calculator = SensorActivityCalculator()
    hourly_calculator = HourlyActivityCalculator()
    rolling_calculator = RollingActivityCalculator()
    peak_calculator = PeakActivityCalculator()
    inactivity_calculator = InactivityPeriodCalculator()
    distribution_calculator = ActivityDistributionCalculator()
    activity_trend_calculator = ActivityTrendCalculator()
    weekly_calculator = WeeklyActivityCalculator()
    time_period_statistics_calculator = SensorTimePeriodStatisticsCalculator()

    activity_calculator: ActivityMetricsCalculatorPort = (
        PandasActivityMetricsCalculator(
            dataframe_factory=dataframe_factory,
            daily_calculator=daily_calculator,
            sensor_calculator=sensor_calculator,
            hourly_calculator=hourly_calculator,
            rolling_calculator=rolling_calculator,
            peak_calculator=peak_calculator,
            inactivity_calculator=inactivity_calculator,
            distribution_calculator=distribution_calculator,
            activity_trend_calculator=activity_trend_calculator,
            weekly_activity_calculator=weekly_calculator,
            time_period_statistics_calculator=time_period_statistics_calculator,
        )
    )

    activity_metrics_service = ActivityMetricsService(
        calculator=activity_calculator,
    )

    return AnalyzeActivityLevelsUseCase(
        activity_metrics_service=activity_metrics_service,
    )

# /src/interface_adapters/output_handlers/results_handler.py

# organize by domain, then by output type (e.g. table, chart, text)

from datetime import date

from src.domain.entities.sensor import SensorEvent

# --- APPLICATION

from src.application.dto.run_analytics_use_cases_dtos import (
    RunAnalyticsUseCasesResultDTO,
)

from src.application.dto.sensor_timeline_uc_dtos import (
    SensorEventTimelineResultDTO,
)

# --- INTERFACE ADAPTERS

#from src.interface_adapters.presenters.movement.movement_analysis_presenter import (
#    MovementAnalysisPresenter,
#)

from src.interface_adapters.presenters.activity.activity_presenter_service import (
    ActivityPresenterService,
)

from src.interface_adapters.presenters.charts.charts_presenter_service import (
    ChartsPresenterService,
)

# from src.interface_adapters.presenters.movement.sensor_week_plot_presenter import (
#    SensorWeekPlotPresenter,
#)

# --- INFRASTRUCTURE

from src.infrastructure.services.renderers.pandas.pandas_dataframe_renderer import (
    PandasDataFrameRenderer,
)

"""
from src.infrastructure.services.renderers.markdown.movements_markdown_renderer import (
    MovementAnalysisMarkdownRenderer,
)

from src.infrastructure.services.renderers.console.movements_console_renderer import (
    MovementAnalysisConsoleRenderer,
)

from src.infrastructure.services.renderers.matplotlib.matplotlib_bar_vertical_chart_renderer import (
    MatplotlibVerticalBarChartPlotter,
)

from src.infrastructure.services.renderers.matplotlib.matplotlib_line_chart_renderer import (
    MatplotlibLineChartPlotter,
)

from src.infrastructure.services.renderers.matplotlib.matplotlib_sensor_week_plotter import (
    MatplotlibSensorWeekPlotter,
)

from src.infrastructure.services.renderers.matplotlib.matplotlib_scatter_chart_renderer import (
    MatplotlibScatterChartPlotter,
)

from src.interface_adapters.output_handlers.movement.movement_results_handler import (
    handle_result_outputs_movements,
)

from src.interface_adapters.output_handlers.shared.shared_results_handler import (
    handle_result_outputs_shared,
)
"""

from src.interface_adapters.output_handlers.activity.activity_results_handler import (
    handle_result_outputs_activity,
)

from src.interface_adapters.views.console.console_view_service import (
    ConsoleViewService,
)


def handle_result_outputs_orchestrator(
        *,
        response: RunAnalyticsUseCasesResultDTO,

        activity_presenter_service: ActivityPresenterService,

        # movements_presenter: MovementAnalysisPresenter,
        # sensor_plot_presenter: SensorWeekPlotPresenter,

        # charts_presenter_service: ChartsPresenterService,

        # sensor_movement_plotter: MatplotlibSensorWeekPlotter,

        # bar_chart_plotter: MatplotlibVerticalBarChartPlotter,
        # line_chart_plotter: MatplotlibLineChartPlotter,
        # scatter_chart_plotter: MatplotlibScatterChartPlotter,

        console_view_service: ConsoleViewService,

        # movements_console_renderer: MovementAnalysisConsoleRenderer,
        # movements_markdown_renderer: MovementAnalysisMarkdownRenderer,
        dataframe_renderer: PandasDataFrameRenderer
) -> None:
    sensor_timeline: SensorEventTimelineResultDTO = (
        response.build_sensor_timeline_result)
    sensor_ids: list[str] = response.run_request.sensor_ids
    sensor_events: list[SensorEvent] = sensor_timeline.collapsed_events

    start_date: date = response.run_request.start_date
    end_date: date = response.run_request.end_date

    # --- SHARED

    """
    handle_result_outputs_shared(
        run_analysis_request=response.run_request,
        sensor_ids=sensor_ids,
        # sensor_profiles=response.run_request.sensor_profiles,
        # sensor_events=sensor_events,
        # most_recent_events=sensor_timeline.most_recent_events,
        # sensor_online_statuses=sensor_timeline.sensor_online_statuses,
        console_view_service=console_view_service,
    )
    """

    # --- MOVEMENTS

    """
    handle_result_outputs_movements(
        sensor_ids=sensor_ids,
        sensor_events=sensor_events,
        start_date=start_date,
        movements_result=response.analyze_movements_result,
        presenter=movements_presenter,
        console_renderer=movements_console_renderer,
        markdown_renderer=movements_markdown_renderer,
        sensor_plot_presenter=sensor_plot_presenter,
        sensor_plotter=sensor_movement_plotter,
    )
    """

    # --- ACTIVITY

    handle_result_outputs_activity(

        sensor_events=sensor_events,

        activity_metrics_result=response.analyze_activity_result,
        activity_presenter_service=activity_presenter_service,
        dataframe_renderer=dataframe_renderer,

        sensor_ids=sensor_ids,
        # charts_presenter_service=charts_presenter_service,

        console_view_service=console_view_service,

        # bar_chart_plotter=bar_chart_plotter,
        # line_chart_plotter=line_chart_plotter,
        # scatter_chart_plotter=scatter_chart_plotter,

        start_date=start_date,
        end_date=end_date,

    )

    """
    handle_chart_outputs(
        sensor_events=sensor_events,
        sensor_ids=sensor_ids,
        sensor_by_id_events=activity_metrics_result.sensor_by_id_activity,
        hourly_activity_results=activity_metrics_result.hourly_activity,
        charts_presenter_service=charts_presenter_service,
        bar_chart_plotter=bar_chart_plotter,
        line_chart_plotter=line_chart_plotter,
        scatter_chart_plotter=scatter_chart_plotter,
        start_date=start_date,
        end_date=end_date,
        path_results=path_results,
    )
    """


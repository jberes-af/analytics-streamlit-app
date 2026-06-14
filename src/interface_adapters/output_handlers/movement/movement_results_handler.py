# /src/interface_adapters/output_handlers/movement/movement_results_handler.py


from datetime import date
from pathlib import Path

from src.domain.entities.sensor import SensorEvent

# --- APPLICATION

from src.application.dto.movement_uc_dtos import MovementAnalysisResultDTO

# --- INTERFACE ADAPTERS

from src.interface_adapters.presenters.movement.movement_analysis_presenter import (
    MovementAnalysisPresenter,
)

from src.interface_adapters.presenters.movement.sensor_week_plot_presenter import (
    SensorWeekPlotPresenter,
    SensorWeekPlotRequest,
)

# --- INFRASTRUCTURE

from src.infrastructure.services.renderers.markdown.movements_markdown_renderer import (
    MovementAnalysisMarkdownRenderer,
)

from src.infrastructure.services.renderers.console.movements_console_renderer import (
    MovementAnalysisConsoleRenderer,
)

from src.infrastructure.services.renderers.matplotlib.matplotlib_sensor_week_plotter import (
    MatplotlibSensorWeekPlotter,
)


def handle_result_outputs_movements(
        sensor_ids: list[str],
        sensor_events: list[SensorEvent],
        start_date: date,
        movements_result: MovementAnalysisResultDTO,
        presenter: MovementAnalysisPresenter,
        console_renderer: MovementAnalysisConsoleRenderer,
        markdown_renderer: MovementAnalysisMarkdownRenderer,
        sensor_plot_presenter: SensorWeekPlotPresenter,
        sensor_plotter: MatplotlibSensorWeekPlotter,
        path_results: Path,

) -> None:
    """
    _handle_movements_analysis_outputs(
        sensor_ids=sensor_ids,
        sensor_events=sensor_events,
        start_date=start_date,
        movements_result=movements_result,
        presenter=presenter,
        console_renderer=console_renderer,
        markdown_renderer=markdown_renderer,
        sensor_plot_presenter=sensor_plot_presenter,
        sensor_plotter=sensor_plotter,
        path_results=path_results,
    )
    """


def _handle_movements_analysis_outputs(
        sensor_ids: list[str],
        sensor_events: list[SensorEvent],
        start_date: date,
        movements_result: MovementAnalysisResultDTO,
        presenter: MovementAnalysisPresenter,
        console_renderer: MovementAnalysisConsoleRenderer,
        markdown_renderer: MovementAnalysisMarkdownRenderer,
        sensor_plot_presenter: SensorWeekPlotPresenter,
        sensor_plotter: MatplotlibSensorWeekPlotter,
        path_results: Path,
) -> None:
    movement_vm = presenter.present(movements_result)

    console_renderer.render(movement_vm)

    markdown_path = path_results / "movement_analysis_report.md"
    markdown_renderer.write(
        view_model=movement_vm,
        output_path=markdown_path,
    )

    path_plots: Path = path_results / "plots" / "sensor_week_plot.png"

    sensor_plot_vm = sensor_plot_presenter.present(
        SensorWeekPlotRequest(
            events=sensor_events,
            sensor_ids=sensor_ids,
            start_day=start_date,
            output_path=path_plots,
        )
    )

    sensor_plotter.plot(sensor_plot_vm)

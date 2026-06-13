# /src/infrastructure/services/renderers/matplotlib/matplotlib_line_chart_renderer.py

from pathlib import Path

import matplotlib.pyplot as plt

from src.interface_adapters.view_models.charts_view_model import (
    LineChartVM,
)


class MatplotlibLineChartPlotter:
    def __init__(
        self,
        dpi: int = 150,
        figsize: tuple[float, float] = (10.0, 5.0),
    ) -> None:
        self.dpi = dpi
        self.figsize = figsize

    def render(
        self,
        chart_vm: LineChartVM,
        output_path: Path,
    ) -> Path:
        output_path.parent.mkdir(parents=True, exist_ok=True)

        fig, ax = plt.subplots(figsize=self.figsize)

        for series in chart_vm.series:
            x_values = [point.x for point in series.points]
            y_values = [point.y for point in series.points]

            ax.plot(
                x_values,
                y_values,
                marker="o",
                linewidth=1.5,
                label=series.name,
            )

        ax.set_title(chart_vm.title)
        ax.set_xlabel(chart_vm.x_axis_label)
        ax.set_ylabel(chart_vm.y_axis_label)

        if chart_vm.x_tick_labels is not None:
            first_series = chart_vm.series[0] if chart_vm.series else None

            if first_series is not None:
                x_values = [point.x for point in first_series.points]

                ax.set_xticks(x_values)
                ax.set_xticklabels(
                    chart_vm.x_tick_labels,
                    rotation=45,
                    ha="right",
                )

        if chart_vm.y_tick_labels is not None:
            ax.set_yticklabels(chart_vm.y_tick_labels)

        if len(chart_vm.series) > 1:
            ax.legend()

        ax.grid(True, alpha=0.3)

        fig.tight_layout()
        fig.savefig(output_path, dpi=self.dpi)
        plt.close(fig)

        return output_path
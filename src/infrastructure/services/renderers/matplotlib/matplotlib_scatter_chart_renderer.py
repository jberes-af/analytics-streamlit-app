# /src/infrastructure/services/renderers/matplotlib/matplotlib_scatter_chart_renderer.py

"""
if chart_vm.show_gridlines:
    ax.grid(
        True,
        axis="y",
        alpha=0.3,
    )
"""

from pathlib import Path

import matplotlib.pyplot as plt

from src.interface_adapters.view_models.charts_view_model import (
    ScatterChartVM,
)


class MatplotlibScatterChartPlotter:
    def __init__(
        self,
        dpi: int = 150,
        figsize: tuple[float, float] = (10.0, 5.0),
        x_tick_rotation: int = 0,
    ) -> None:
        self.dpi = dpi
        self.figsize = figsize
        self.x_tick_rotation = x_tick_rotation

    def render(
        self,
        chart_vm: ScatterChartVM,
        output_path: Path,
    ) -> Path:
        output_path.parent.mkdir(parents=True, exist_ok=True)

        fig, ax = plt.subplots(figsize=self.figsize)

        for series in chart_vm.series:
            x_values = [point.x for point in series.points]
            y_values = [point.y for point in series.points]

            ax.scatter(
                x_values,
                y_values,
                marker="o",
                label=series.name,
                s=12,
                alpha=0.7,
            )

        ax.set_title(chart_vm.title)
        ax.set_xlabel(chart_vm.x_axis_label)
        ax.set_ylabel(chart_vm.y_axis_label)

        if chart_vm.x_tick_coords and chart_vm.x_tick_labels:
            ax.set_xticks(chart_vm.x_tick_coords)
            ax.set_xticklabels(
                chart_vm.x_tick_labels,
                rotation=self.x_tick_rotation,
                ha="center",
            )

        if chart_vm.y_tick_coords and chart_vm.y_tick_labels:
            ax.set_yticks(chart_vm.y_tick_coords)
            ax.set_yticklabels(chart_vm.y_tick_labels)

        ax.set_ylim(0, 24 * 3600)
        ax.grid(True, alpha=0.3)

        fig.tight_layout()
        fig.savefig(output_path, dpi=self.dpi)
        plt.close(fig)

        return output_path

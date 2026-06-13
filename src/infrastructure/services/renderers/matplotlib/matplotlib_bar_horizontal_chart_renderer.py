# /src/infrastructure/services/renderers/matplotlib/matplotlib_bar_horizontal_chart_renderer.py

from pathlib import Path

import matplotlib.pyplot as plt

from src.interface_adapters.view_models.charts_view_model import (
    BarChartVM,
)


class MatplotlibHorizontalBarChartPlotter:
    def __init__(
        self,
        dpi: int = 150,
        figsize: tuple[float, float] = (10.0, 8.0),
    ) -> None:
        self.dpi = dpi
        self.figsize = figsize

    def render(
        self,
        chart_vm: BarChartVM,
        output_path: Path,
    ) -> Path:
        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        fig, ax = plt.subplots(
            figsize=self.figsize,
        )

        y_positions = list(range(len(chart_vm.bars)))

        values = [
            bar.value
            for bar in chart_vm.bars
        ]

        category_labels = [
            bar.category_label
            for bar in chart_vm.bars
        ]

        ax.barh(
            y=y_positions,
            width=values,
        )

        ax.set_title(chart_vm.title)

        ax.set_xlabel(
            chart_vm.x_axis_label
        )

        ax.set_ylabel(
            chart_vm.y_axis_label
        )

        ax.set_yticks(y_positions)

        ax.set_yticklabels(
            category_labels,
        )

        ax.grid(
            True,
            axis="x",
            alpha=0.3,
        )

        fig.tight_layout()

        fig.savefig(
            output_path,
            dpi=self.dpi,
        )

        plt.close(fig)

        return output_path
# /src/infrastructure/services/renderers/matplotlib/matplotlib_bar_vertical_chart_renderer.py

from pathlib import Path

import matplotlib.pyplot as plt

from src.interface_adapters.view_models.charts_view_model import (
    BarChartVM,
)


class MatplotlibVerticalBarChartPlotter:
    def __init__(
        self,
        dpi: int = 150,
        figsize: tuple[float, float] = (10.0, 5.0),
        x_tick_rotation: int = 45,
    ) -> None:
        self.dpi = dpi
        self.figsize = figsize
        self.x_tick_rotation = x_tick_rotation

    def render(
        self,
        chart_vm: BarChartVM,
        output_path: Path,
    ) -> Path:
        output_path.parent.mkdir(parents=True, exist_ok=True)

        fig, ax = plt.subplots(figsize=self.figsize)

        x_positions = list(range(len(chart_vm.bars)))
        values = [bar.value for bar in chart_vm.bars]
        category_labels = [bar.category_label for bar in chart_vm.bars]

        ax.bar(
            x_positions,
            values,
        )

        ax.set_title(chart_vm.title)
        ax.set_xlabel(chart_vm.x_axis_label)
        ax.set_ylabel(chart_vm.y_axis_label)

        ax.set_xticks(x_positions)
        ax.set_xticklabels(
            category_labels,
            rotation=self.x_tick_rotation,
            ha="right",
        )


        """
        if chart_vm.show_gridlines:
            ax.grid(
                True,
                axis="y",
                alpha=0.3,
            )
        """

        fig.tight_layout()
        fig.savefig(output_path, dpi=self.dpi)
        plt.close(fig)

        return output_path
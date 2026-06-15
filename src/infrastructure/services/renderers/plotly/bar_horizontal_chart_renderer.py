# /src/infrastructure/services/renderers/plotly/bar_horizontal_chart_renderer.py

import plotly.graph_objects as go

from src.interface_adapters.view_models.charts_view_model import (
    BarChartVM,
)


class PlotlyHorizontalBarChartRenderer:
    def __init__(
        self,
        height: int = 600,
        show_grid: bool = True,
        bar_text_position: str = "outside",
    ) -> None:
        self.height = height
        self.show_grid = show_grid
        self.bar_text_position = bar_text_position

    def render(
        self,
        chart_vm: BarChartVM,
    ) -> go.Figure:

        category_labels = [
            bar.category_label
            for bar in chart_vm.bars
        ]

        values = [
            bar.value
            for bar in chart_vm.bars
        ]

        value_labels = [
            bar.value_label
            if bar.value != 0 else ""
            for bar in chart_vm.bars
        ]

        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                x=values,
                y=category_labels,
                orientation="h",
                text=value_labels,
                textposition=self.bar_text_position,
                textfont=dict(size=20),            )
        )

        fig.update_layout(
            title="",
            height=self.height,
            showlegend=False,
            margin={
                "l": 120,
                "r": 40,
                "t": 40,
                "b": 60,
            },
        )

        fig.update_xaxes(
            title_text=chart_vm.x_axis_label,
            showgrid=self.show_grid,
            tickfont={"size": 16},
            title_font={"size": 16},
        )

        fig.update_yaxes(
            title_text=chart_vm.y_axis_label,
            showgrid=False,
            tickfont={"size": 16},
            title_font={"size": 16},
            automargin=True,
        )

        fig.update_traces(
            textposition="outside",
            textfont_size=16,
        )

        fig.update_layout(
            uniformtext_minsize=16,
            uniformtext_mode="show",
        )

        return fig
# /src/infrastructure/services/renderers/plotly/bar_vertical_chart_renderer.py

import plotly.graph_objects as go

from src.interface_adapters.view_models.charts_view_model import (
    BarChartVM,
)


class PlotlyVerticalBarChartRenderer:
    def __init__(
            self,
            height: int = 500,
            show_grid: bool = True,
            x_tick_rotation: int = 45,
            show_bar_values: bool = True,
    ) -> None:
        self.height = height
        self.show_grid = show_grid
        self.x_tick_rotation = x_tick_rotation
        self.show_bar_values = show_bar_values

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
            for bar in chart_vm.bars
        ]

        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                x=category_labels,
                y=values,
                text=value_labels if self.show_bar_values else None,
                textposition="outside",
            )
        )

        fig.update_layout(
            title=None,
            height=self.height,
            showlegend=False,
            margin={
                "l": 60,
                "r": 20,
                "t": 40,
                "b": 100,
            },
        )

        fig.update_xaxes(
            title_text=chart_vm.x_axis_label,
            tickangle=self.x_tick_rotation,
            tickfont={"size": 13},
            title_font={"size": 15},
        )

        fig.update_yaxes(
            title_text=chart_vm.y_axis_label,
            showgrid=self.show_grid,
            tickfont={"size": 13},
            title_font={"size": 15},
        )

        return fig

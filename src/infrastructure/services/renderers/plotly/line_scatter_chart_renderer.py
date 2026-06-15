# line_scatter_chart_renderer.py

import plotly.graph_objects as go

from src.interface_adapters.view_models.charts_view_model import (
    ScatterLineChartVM,
)

import math


class PlotlyScatterLineChartRenderer:
    def __init__(
        self,
        height: int = 500,
        show_grid: bool = True,
        scatter_color: str = "#0B3D91",  # dark blue
        line_color: str = "#9CA3AF",     # medium-light gray
        line_width: int = 4,
        marker_size: int = 8,
    ) -> None:
        self.height = height
        self.show_grid = show_grid
        self.scatter_color = scatter_color
        self.line_color = line_color
        self.line_width = line_width
        self.marker_size = marker_size

    def render(self, chart_vm: ScatterLineChartVM) -> go.Figure:
        fig = go.Figure()

        for series in chart_vm.line_series:
            x_values = [
                point.x.isoformat() if hasattr(point.x, "isoformat") else point.x
                for point in series.points
            ]
            y_values = [point.y for point in series.points]

            fig.add_trace(
                go.Scatter(
                    x=x_values,
                    y=y_values,
                    mode="lines",
                    name="Rolling Average",
                    line={
                        "color": self.line_color,
                        "width": self.line_width,
                    },
                )
            )


        for series in chart_vm.scatter_series:
            x_values = [
                point.x.isoformat() if hasattr(point.x, "isoformat") else point.x
                for point in series.points
            ]
            y_values = [point.y for point in series.points]

            fig.add_trace(
                go.Scatter(
                    x=x_values,
                    y=y_values,
                    mode="markers",
                    name="Actual",
                    marker={
                        "color": self.scatter_color,
                        "size": self.marker_size,
                    },
                )
            )

        fig.update_layout(
            title=chart_vm.title,
            xaxis_title=chart_vm.x_axis_label,
            yaxis_title=chart_vm.y_axis_label,
            height=self.height,
            margin={"l": 40, "r": 20, "t": 60, "b": 40},
        )

        fig.update_xaxes(
            showgrid=self.show_grid,
            tickfont=dict(size=16),
        )

        y_max = _get_y_max(chart_vm)

        fig.update_yaxes(
            range=[0, y_max],
            tickmode="array",
            tickvals=[
                0,
                y_max * 0.25,
                y_max * 0.50,
                y_max * 0.75,
                y_max,
            ],
            showgrid=True,
            tickfont=dict(size=16),
        )

        fig.update_layout(
            title="",
            showlegend=True,
            legend=dict(
                orientation="h",
                x=0,
                xanchor="left",
                y=1.05,
                yanchor="bottom",
                font=dict(size=16),
            ),
            margin=dict(
                l=60,
                r=20,
                t=70,
                b=80,
            ),
            height=520,
        )

        step = 7

        if chart_vm.x_tick_labels is not None and chart_vm.line_series:
            tick_values = [
                point.x.isoformat()
                if hasattr(point.x, "isoformat")
                else point.x
                for point in chart_vm.line_series[0].points
            ]

            tick_labels = list(chart_vm.x_tick_labels)

            fig.update_xaxes(
                tickmode="array",
                tickvals=tick_values[::step],
                ticktext=tick_labels[::step],
                tickangle=0,
            )

        fig.update_layout(
            xaxis=dict(
                tickfont=dict(size=16),
            ),
            yaxis=dict(
                tickfont=dict(size=16),
            ),
        )

        return fig



def _get_y_max(
    chart_vm: ScatterLineChartVM,
    minimum_y_max: float = 4.0,
    round_to_nearest: int = 4,
) -> float:
    y_values: list[float] = []

    for series in chart_vm.scatter_series:
        y_values.extend(float(point.y) for point in series.points)

    for series in chart_vm.line_series:
        y_values.extend(float(point.y) for point in series.points)

    if not y_values:
        return minimum_y_max

    raw_max = max(y_values)

    return max(
        minimum_y_max,
        math.ceil(raw_max / round_to_nearest) * round_to_nearest,
    )

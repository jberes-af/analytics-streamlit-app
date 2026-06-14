# plotly_line_scatter_chart_renderer.py

import plotly.graph_objects as go

from src.interface_adapters.view_models.charts_view_model import (
    ScatterLineChartVM,
)


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

        fig.update_xaxes(showgrid=self.show_grid)
        fig.update_yaxes(showgrid=self.show_grid)

        fig.update_layout(
            showlegend=True,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="center",
                x=0.5,
                font=dict(size=16),
            ),
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

        return fig

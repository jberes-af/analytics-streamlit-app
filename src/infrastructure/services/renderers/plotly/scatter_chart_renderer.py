# /src/infrastructure/services/renderers/plotly/scatter_chart_renderer.py

import plotly.graph_objects as go

from src.interface_adapters.view_models.charts_view_model import ScatterChartVM


class PlotlyScatterChartRenderer:
    def __init__(
        self,
        height: int = 500,
        show_grid: bool = True,
        marker_size: int = 8,
        marker_opacity: float = 0.7,
        x_tick_rotation: int = 0,
        y_axis_min: int | float | None = 0,
        y_axis_max: int | float | None = 24 * 3600,
    ) -> None:
        self.height = height
        self.show_grid = show_grid
        self.marker_size = marker_size
        self.marker_opacity = marker_opacity
        self.x_tick_rotation = x_tick_rotation
        self.y_axis_min = y_axis_min
        self.y_axis_max = y_axis_max

    def render(self, chart_vm: ScatterChartVM) -> go.Figure:
        fig = go.Figure()

        for series in chart_vm.series:
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
                    name=series.name,
                    marker={
                        "size": self.marker_size,
                        "opacity": self.marker_opacity,
                    },
                )
            )

        fig.update_layout(
            title=None,
            height=self.height,
            showlegend=len(chart_vm.series) > 1,
            margin={
                "l": 60,
                "r": 20,
                "t": 40,
                "b": 80,
            },
        )

        fig.update_xaxes(
            title_text=chart_vm.x_axis_label,
            showgrid=self.show_grid,
            tickangle=self.x_tick_rotation,
            tickfont={"size": 16},
            title_font={"size": 16},
        )

        fig.update_yaxes(
            title_text=chart_vm.y_axis_label,
            showgrid=self.show_grid,
            tickfont={"size": 16},
            title_font={"size": 16},
            range=[
                self.y_axis_min,
                self.y_axis_max,
            ],
        )

        if chart_vm.x_tick_coords and chart_vm.x_tick_labels:
            fig.update_xaxes(
                tickmode="array",
                tickvals=list(chart_vm.x_tick_coords),
                ticktext=list(chart_vm.x_tick_labels),
            )

        if chart_vm.y_tick_coords and chart_vm.y_tick_labels:
            fig.update_yaxes(
                tickmode="array",
                tickvals=list(chart_vm.y_tick_coords),
                ticktext=list(chart_vm.y_tick_labels),
            )

        return fig
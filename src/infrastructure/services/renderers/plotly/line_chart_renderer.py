# /src/infrastructure/services/renderers/plotly/line_chart_renderer.py

import plotly.graph_objects as go

from src.interface_adapters.view_models.charts_view_model import LineChartVM


class PlotlyLineChartRenderer:
    def __init__(
        self,
        height: int = 500,
        show_grid: bool = True,
    ) -> None:
        self.height = height
        self.show_grid = show_grid

    def render(self, chart_vm: LineChartVM) -> go.Figure:
        fig = go.Figure()

        for series in chart_vm.series:
            x_values = [point.x.isoformat()
                        if hasattr(point.x, "isoformat")
                        else point.x
                        for point in series.points]
            y_values = [point.y for point in series.points]

            fig.add_trace(
                go.Scatter(
                    x=x_values,
                    y=y_values,
                    mode="lines+markers",
                    name=series.name,
                )
            )

        fig.update_layout(
            title=chart_vm.title,
            xaxis_title=chart_vm.x_axis_label,
            yaxis_title=chart_vm.y_axis_label,
            showlegend=len(chart_vm.series) > 1,
        )

        if chart_vm.x_tick_labels is not None and chart_vm.series:
            tick_values = [
                point.x.isoformat() if hasattr(point.x, "isoformat") else point.x
                for point in chart_vm.series[0].points
            ]

            fig.update_xaxes(
                tickmode="array",
                tickvals=tick_values,
                ticktext=list(chart_vm.x_tick_labels),
                tickangle=45,
            )

        return fig
# /src/interface/adapters/presenters/charts/sensor_chart_presenter.py

from datetime import date

from typing import Sequence

from src.interface_adapters.view_models.charts_view_model import (
    PointVM,
    SeriesVM,
    LineChartVM,
)


class SensorActivityLineChartPresenter:

    @staticmethod
    def present(
            *,
            title: str,
            x_axis_label: str,
            y_axis_label: str,
            x_series: Sequence[date | int | float],
            y_series: Sequence[int | float],
    ) -> LineChartVM:
        if len(x_series) != len(y_series):
            raise ValueError(
                f"x and y series must have same length "
                f"{len(x_series)} vs {len(y_series)}"
            )

        points = [
            PointVM(x=x, y=y)
            for x, y in zip(x_series, y_series)
        ]

        x_tick_labels = [
            x.strftime("%m%d") if isinstance(x, date) else str(x)
            for x in x_series
        ]

        return LineChartVM(
            title=title,
            x_axis_label=x_axis_label,
            y_axis_label=y_axis_label,
            x_tick_labels=x_tick_labels,
            y_tick_labels=None,
            series=[
                SeriesVM(
                    name=title.replace(" ", "_").lower(),
                    points=points,
                )
            ],
        )

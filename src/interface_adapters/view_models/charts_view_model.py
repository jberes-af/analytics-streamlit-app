# /src/interface_adapters/view_models/charts_view_model.py

from dataclasses import dataclass
from typing import Sequence

"""
LINE CHART
"""


@dataclass(frozen=True)
class PointVM:
    x: float | int | str
    y: float | int


@dataclass(frozen=True)
class SeriesVM:
    name: str
    points: Sequence[PointVM]


@dataclass(frozen=True)
class LineChartVM:
    title: str
    x_axis_label: str
    y_axis_label: str
    x_tick_labels: Sequence[str] | None
    y_tick_labels: Sequence[str] | None
    series: Sequence[SeriesVM]


"""
BAR CHART
"""


@dataclass(frozen=True)
class BarVM:
    category: str
    value: float | int
    category_label: str
    value_label: str


@dataclass(frozen=True)
class BarChartVM:
    title: str
    x_axis_label: str
    y_axis_label: str
    bars: Sequence[BarVM]


"""
SCATTER CHART
"""


@dataclass(frozen=True)
class ScatterChartVM:
    title: str
    x_axis_label: str
    y_axis_label: str
    x_tick_coords: Sequence[int | float] | None
    y_tick_coords: Sequence[int | float] | None
    x_tick_labels: Sequence[str] | None
    y_tick_labels: Sequence[str] | None
    series: Sequence[SeriesVM]

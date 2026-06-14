# /src/interface_adapters/view_models/activity/weekly_activity_vm.py

from dataclasses import dataclass


@dataclass(frozen=True)
class WeeklyActivityRowVM:
    sensor_id: str

    week_start: str
    week_end: str
    week_label: str

    total_activations_week: int
    total_activations_week_label: str

    maximum_daily_activations: int
    maximum_daily_activations_label: str

    minimum_daily_activations: int
    minimum_daily_activations_label: str

    average_daily_activations: float
    average_daily_activations_label: str

    standard_deviation_daily_activations: float
    standard_deviation_daily_activations_label: str

    coefficient_variation: float
    coefficient_variation_label: str

    change_percent: float | None
    change_percent_label: str


@dataclass(frozen=True)
class WeeklyActivityViewModel:
    title: str
    rows: list[WeeklyActivityRowVM]

    has_data: bool
    empty_message: str | None

# /src/interface_adapters/views/console_view_service.py

from dataclasses import dataclass

from src.interface_adapters.view_models.activity.weekly_activity_vm import (
    WeeklyActivityViewModel,
)

from src.interface_adapters.view_models.shared_view_model import RunConfigViewModel

from src.interface_adapters.views.console.debug_console_view import (
    DebugConsoleView,
)

from src.interface_adapters.views.console.weekly_activity_console_view import (
    WeeklyActivityConsoleRenderer,
)


import pandas as pd


@dataclass(frozen=True)
class ActivityMetricsDataFrames:
    df_daily: pd.DataFrame
    df_sensor: pd.DataFrame
    df_hourly: pd.DataFrame
    df_rolling: pd.DataFrame
    df_peak: pd.DataFrame
    df_inactivity: pd.DataFrame


class ConsoleViewService:
    def __init__(
            self,
            activity_metrics_debug_view: DebugConsoleView,
            weekly_activity_view: WeeklyActivityConsoleRenderer,
    ):
        self._activity_debug_view = activity_metrics_debug_view
        self._weekly_view = weekly_activity_view

    def render_run_config_info_view(
            self,
            run_configuration_vm: RunConfigViewModel
    ):
        self._activity_debug_view.render_run_all_config(
            config_vm=run_configuration_vm,
        )

    def render_activity_metrics_debug_view(
            self,
            metrics_dataframes: ActivityMetricsDataFrames,
    ):
        self._activity_debug_view.render_dataframe(
            "Daily Activity Results",
            df=metrics_dataframes.df_daily,
            show_n_rows=20,
        )

        self._activity_debug_view.render_dataframe(
            "Sensor Activity Results",
            df=metrics_dataframes.df_sensor,
            show_n_rows=20,
        )

        self._activity_debug_view.render_dataframe(
            "Hourly Activity Results",
            df=metrics_dataframes.df_hourly,
            show_n_rows=20,
        )

        self._activity_debug_view.render_dataframe(
            "Rolling Activity Results",
            df=metrics_dataframes.df_rolling,
            show_n_rows=20,
        )

        self._activity_debug_view.render_dataframe(
            "Peak Activity Results",
            df=metrics_dataframes.df_peak,
            show_n_rows=20,
        )

        self._activity_debug_view.render_dataframe(
            "Inactivity Period Results",
            df=metrics_dataframes.df_inactivity,
            show_n_rows=20,
        )

    def render_weekly_activity_view(
            self,
            view_model: WeeklyActivityViewModel,
    ):
        self._weekly_view.render(view_model)

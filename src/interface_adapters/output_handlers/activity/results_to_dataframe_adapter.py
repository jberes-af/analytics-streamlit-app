# /src/interface_adapters/output_handlers/activity/results_to_dataframe_adapter.py

import pandas as pd

from src.infrastructure.services.renderers.pandas.pandas_dataframe_renderer import (
    PandasDataFrameRenderer)

from src.interface_adapters.view_models.activity.activity_metrics_vm import (
    DailyActivityViewModel,
    SensorActivityViewModel,
    HourlyActivityViewModel,
    RollingActivityViewModel,
    PeakActivityViewModel,
    InactivityPeriodsViewModel,
)

from src.interface_adapters.views.console.console_view_service import (
    ActivityMetricsDataFrames,
)


def transform_results_to_dataframe(
        daily_vm: DailyActivityViewModel,
        sensor_vm: SensorActivityViewModel,
        hourly_vm: HourlyActivityViewModel,
        rolling_vm: RollingActivityViewModel,
        peak_vm: PeakActivityViewModel,
        inactivity_vm: InactivityPeriodsViewModel,

        dataframe_renderer: PandasDataFrameRenderer,
) -> ActivityMetricsDataFrames:
    df_daily: pd.DataFrame = dataframe_renderer.to_dataframe_activity_analysis_daily_activity(
        column_headers=[
            x.label
            for x in daily_vm.columns
        ],
        rows=daily_vm.rows,
    )

    df_sensor: pd.DataFrame = (
        dataframe_renderer.to_dataframe_activity_analysis_sensor_activity(
            column_headers=[
                x.label
                for x in sensor_vm.columns
            ],
            rows=sensor_vm.rows,
        ))

    df_hourly: pd.DataFrame = (
        dataframe_renderer.to_dataframe_activity_analysis_hourly_activity(
            column_headers=[
                x.label
                for x in hourly_vm.columns
            ],
            rows=hourly_vm.rows,
        )
    )

    df_rolling: pd.DataFrame = (
        dataframe_renderer.to_dataframe_activity_analysis_rolling_activity(
            column_headers=[
                x.label
                for x in rolling_vm.columns
            ],
            rows=rolling_vm.rows,
        ))

    df_peak: pd.DataFrame = (
        dataframe_renderer.to_dataframe_activity_analysis_peak_activity(
            column_headers=[
                x.label
                for x in peak_vm.columns
            ],
            rows=peak_vm.rows,
        )
    )

    df_inactivity: pd.DataFrame = (
        dataframe_renderer.to_dataframe_activity_analysis_inactivity_periods(
            column_headers=[
                x.label
                for x in inactivity_vm.columns
            ],
            rows=inactivity_vm.rows,
        )
    )

    return ActivityMetricsDataFrames(
        df_daily=df_daily,
        df_sensor=df_sensor,
        df_hourly=df_hourly,
        df_rolling=df_rolling,
        df_peak=df_peak,
        df_inactivity=df_inactivity,
    )

# /src/interface_adapters/views/debug_console_view.py

from datetime import date

from src.application.dto.activity_metric_dtos import (
    ActivityTrendDTO,
    SensorActivityPercentOfTotalDTO,
    DailyActivityBySensorIdDTO,
)

from src.interface_adapters.view_models.shared_view_model import RunConfigViewModel

import pandas as pd


class DebugConsoleView:

    @staticmethod
    def render_run_all_config(
            config_vm: RunConfigViewModel,
    ):
        print(f"\n\n")
        print("=" * 80)
        print(f"\nRUN CONFIGURATION\n----------------------------------")
        print(f"Scenario ID       : {config_vm.scenario_id}")
        print(f"User              : {config_vm.user_reference} ({config_vm.user_id})")
        print(f"Time Period       : {config_vm.time_period}")
        print(f"Sensor Count      : {config_vm.sensor_count}")
        print(f"Sensors           : {config_vm.sensor_ids}")
        print(f"{config_vm.sensor_profiles}")
        print(f"Online Status\n{config_vm.last_seen}")
        print(f"Last Activations\n{config_vm.last_activations}")

    @staticmethod
    def render_dataframe(
            title: str,
            df: pd.DataFrame,
            show_n_rows: int | None = None,
            head_or_tail: str = "tail",
    ) -> None:
        if head_or_tail not in {"head", "tail"}:
            raise ValueError(
                f"head_or_tail must be 'head' or 'tail', got '{head_or_tail}'"
            )

        n_rows = show_n_rows or len(df)

        df_show = (
            df.head(n_rows)
            if head_or_tail == "head"
            else df.tail(n_rows)
        )

        print()
        print("=" * 80)
        print(title)
        print("-" * 60)
        print(f"Rows: {len(df):,}")
        print(f"Columns: {len(df.columns)}")
        print()
        print(df_show)
        print()

    @staticmethod
    def render_sensor_summary_result(
            sensor_ids: list[str],
            combined_sensor_activity: list[SensorActivityPercentOfTotalDTO],
            sensor_by_id_activity: list[DailyActivityBySensorIdDTO],
            start_date: date,
            end_date: date,
    ) -> None:

        title: str = "Sensor Summary"
        days_count: int = (end_date - start_date).days
        print()
        print("=" * 80)
        print(f"\n{title}")
        print("-" * 60)
        print(
            f"Time Period: {start_date.strftime('%b %d')} "
            f"to {end_date.strftime('%b %d')} ({days_count} Days)"
        )
        print()
        print()

    @staticmethod
    def render_sensor_trend_result(
            sensor_ids: list[str],
            result: list[ActivityTrendDTO],
    ) -> None:

        title: str = "Sensor ID Trend Results"
        print()
        print("=" * 80)
        print(f"\n{title}")
        print(f"(Activity Results Handler Trend Outputs)")
        print("-" * 60)

        for sensor_id in sensor_ids:

            print(f"Sensor ID {sensor_id}")

            for record in result:

                if record.sensor_id is None:
                    print(f"No trend record available for sensor ID {sensor_id}\n")
                    continue

                if sensor_id == record.sensor_id:
                    print(f"Metric Name: {record.metric_name}")
                    print(f"Time Period: {record.start_date} to {record.end_date}")
                    print(f"Trend Direction: {record.direction}")
                    print(f"Slope {record.slope_per_day:,.2f} ; Intercept {record.intercept:,.2f}")
                    print()

            print()

        print()
        print()

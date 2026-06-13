# /src/infrastructure/services/renderers/pandas_dataframe_renderer.py

from typing import Any
import pandas as pd

pd.options.display.float_format = '{:,.2f}'.format
pd.options.display.max_rows = None
pd.options.display.max_columns = None
pd.options.display.width = None


class PandasDataFrameRenderer:

    @staticmethod
    def to_dataframe_activity_analysis_daily_activity(
            column_headers: list[str],
            rows: list[Any],
    ) -> pd.DataFrame:
        data: list[list[object]] = []

        for row in rows:
            cell_values: list[object] = []
            cell_values.append(row.date)
            cell_values.append(row.total_activations)
            # cell_values.append(row.total_activations_label)
            cell_values.append(row.first_activation)
            cell_values.append(row.last_activation)
            cell_values.append(row.active_day_length)
            data.append(cell_values)

        return pd.DataFrame(data=data, columns=column_headers)

    @staticmethod
    def to_dataframe_activity_analysis_sensor_activity(
            column_headers: list[str],
            rows: list[Any],
    ) -> pd.DataFrame:
        data: list[list[object]] = []

        for row in rows:
            cell_values: list[object] = []
            cell_values.append(row.sensor_id)
            cell_values.append(row.total_activations)
            # cell_values.append(row.total_activations_label)
            cell_values.append(row.percentage_of_total)
            # cell_values.append(row.percentage_of_total_label)
            data.append(cell_values)

        return pd.DataFrame(data=data, columns=column_headers)

    @staticmethod
    def to_dataframe_activity_analysis_hourly_activity(
            column_headers: list[str],
            rows: list[Any],
    ) -> pd.DataFrame:
        data: list[list[object]] = []

        for row in rows:
            cell_values: list[object] = []
            cell_values.append(row.date)
            cell_values.append(row.hour)
            # cell_values.append(row.hour_label)
            cell_values.append(row.activation_count)
            # cell_values.append(row.activation_count_label)
            data.append(cell_values)

        return pd.DataFrame(data=data, columns=column_headers)

    @staticmethod
    def to_dataframe_activity_analysis_rolling_activity(
            column_headers: list[str],
            rows: list[Any],
    ) -> pd.DataFrame:
        data: list[list[object]] = []

        for row in rows:
            cell_values: list[object] = []
            cell_values.append(row.window_start)
            cell_values.append(row.window_end)
            # cell_values.append(row.window_label)
            cell_values.append(row.activation_count)
            # cell_values.append(row.activation_count_label)
            data.append(cell_values)

        return pd.DataFrame(data=data, columns=column_headers)

    @staticmethod
    def to_dataframe_activity_analysis_peak_activity(
            column_headers: list[str],
            rows: list[Any],
    ) -> pd.DataFrame:
        data: list[list[object]] = []

        for row in rows:
            cell_values: list[object] = []
            cell_values.append(row.rank_label)
            # cell_values.append(row.window_start)
            # cell_values.append(row.window_end)
            cell_values.append(row.window_label)
            cell_values.append(row.activation_count_label)
            # cell_values.append(row.activation_count_label)
            data.append(cell_values)

        return pd.DataFrame(data=data, columns=column_headers)

    @staticmethod
    def to_dataframe_activity_analysis_inactivity_periods(
            column_headers: list[str],
            rows: list[Any],
    ) -> pd.DataFrame:
        data: list[list[object]] = []

        for row in rows:
            cell_values: list[object] = []
            # cell_values.append(row.start_time)
            # cell_values.append(row.end_time)
            cell_values.append(row.period_label)
            cell_values.append(row.duration_label)
            data.append(cell_values)

        return pd.DataFrame(data=data, columns=column_headers)

"""
class TransposedPandasDataFrameRenderer:
    def to_dataframe(
        self,
        table: TableViewModel,
    ) -> pd.DataFrame:
        columns: list[str] = ["Category", *table.column_headers]
        raw_rows: list[list[object]] = [
            [row.row_label, *row.cells.value] for row in table.rows
        ]
        return pd.DataFrame(raw_rows, columns=columns)
"""

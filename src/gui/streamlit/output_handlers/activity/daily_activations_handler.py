# # /src/gui/streamlit/output_handlers/activity_charts_handler.py

from datetime import date

from src.application.dto.activity_metric_dtos import (
    ActivityTrendDTO,
    DailyActivityBySensorIdDTO,
    DailyActivityAllSensorsDTO,
    SensorTimePeriodStatisticsDTO,
)

from src.interface_adapters.presenters.charts.charts_presenter_service import (
    ChartsPresenterService,
)

from src.infrastructure.services.renderers.plotly.line_scatter_chart_renderer import (
    PlotlyScatterLineChartRenderer,
)

from src.interface_adapters.presenters.activity.activity_presenter_service import (
    ActivityPresenterService,
)

from src.interface_adapters.view_models.charts_view_model import (
    ScatterLineChartVM,
)

from src.interface_adapters.view_models.activity.sensor_statistics_vm import (
    SensorTimePeriodStatisticsRowVM,
    SensorTimePeriodStatisticsViewModel,
)

from src.interface_adapters.view_models.activity.activity_trend_vm import (
    ActivityTrendRowVM,
    ActivityTrendViewModel,
)

import streamlit as st


def handle_daily_activation_outputs(
        sensor_ids: list[str],
        daily_activity_by_sensor_id: list[DailyActivityBySensorIdDTO],
        daily_activity_all_sensors: list[DailyActivityAllSensorsDTO],

        trend_all_sensors: list[ActivityTrendDTO],
        trend_by_sensor_id: list[ActivityTrendDTO],

        activity_presenter_service: ActivityPresenterService,

        charts_presenter_service: ChartsPresenterService,

        # line_chart_plotter: PlotlyLineChartRenderer,
        scatter_line_chart_plotter: PlotlyScatterLineChartRenderer,
        start_date: date,
        end_date: date,
        statistics: list[SensorTimePeriodStatisticsDTO],
) -> None:
    chart_options: list[str]
    chart_vms: dict[str, ScatterLineChartVM]
    chart_options, chart_vms = _build_chart_view_models(
        sensor_ids=sensor_ids,
        daily_sum_events_sensor_by_id=daily_activity_by_sensor_id,
        daily_sum_events_all_sensors=daily_activity_all_sensors,
        charts_presenter_service=charts_presenter_service,
    )

    statistics_vms: dict[str, SensorTimePeriodStatisticsRowVM] = (
        _build_statistics_view_models(
            statistics_results=statistics,
            presenter_service=activity_presenter_service,
        ))

    trend_vms: dict[str, dict[str, str]] = (
        _build_trend_view_models(
            sensor_ids=sensor_ids,
            trend_all_sensors=trend_all_sensors,
            trend_by_sensor_id=trend_by_sensor_id,
            presenter_service=activity_presenter_service,
        ))

    _render_output(
        chart_options=chart_options,
        chart_vms=chart_vms,
        trend_vms=trend_vms,
        statistics_vms=statistics_vms,
        scatter_line_chart_plotter=scatter_line_chart_plotter,
        start_date=start_date,
        end_date=end_date,
        statistics=statistics,
    )


def _build_trend_view_models(
        sensor_ids: list[str],
        trend_all_sensors: list[ActivityTrendDTO],
        trend_by_sensor_id: list[ActivityTrendDTO],
        presenter_service: ActivityPresenterService,
) -> dict[str, dict[str, str]]:
    trend_all_sensors.extend(trend_by_sensor_id)

    vm: ActivityTrendViewModel = (
        presenter_service.present_activity_trend(
            sensor_ids=sensor_ids,
            trend_results=trend_all_sensors,
        )
    )

    a: dict[str, str] = {}
    b: dict[str, dict[str, str]] = {}

    for group in vm.sensor_groups:
        for row in group.rows:
            sensor_id = row.sensor_id
            metric = row.metric_name
            trend_direction = row.direction
            print(metric, trend_direction)

            a[metric] = trend_direction
            if sensor_id in b:
                b[sensor_id].update(a)
            else:
                b[sensor_id] = a

    return b


def _build_chart_view_models(
        sensor_ids: list[str],
        daily_sum_events_sensor_by_id: list[DailyActivityBySensorIdDTO],
        daily_sum_events_all_sensors: list[DailyActivityAllSensorsDTO],
        charts_presenter_service: ChartsPresenterService,
) -> tuple[list[str], dict[str, ScatterLineChartVM]]:
    # sensor_to_line_vm_mapping
    # chart_vms: dict[str, LineChartVM] = (
    chart_vms: dict[str, ScatterLineChartVM] = (
        charts_presenter_service.present_sensor_activations_by_date_chart(
            sensor_ids=sensor_ids,
            sensor_by_id_events=daily_sum_events_sensor_by_id,
            all_sensor_events=daily_sum_events_all_sensors,
        )
    )
    chart_options: list[str] = list(chart_vms.keys())
    return chart_options, chart_vms


def _build_statistics_view_models(
        statistics_results: list[SensorTimePeriodStatisticsDTO],
        presenter_service: ActivityPresenterService,
) -> dict[str, SensorTimePeriodStatisticsRowVM]:
    vm: SensorTimePeriodStatisticsViewModel = (
        presenter_service.present_time_period_activity_statistics(
            statistics_results)
    )

    return {
        row.sensor_id: row
        for row in vm.rows
    }


def _render_output(
        chart_options: list[str],
        chart_vms: dict[str, ScatterLineChartVM],
        trend_vms: dict[str, dict[str, str]],
        statistics_vms: dict[str, SensorTimePeriodStatisticsRowVM],
        scatter_line_chart_plotter: PlotlyScatterLineChartRenderer,
        start_date: date,
        end_date: date,
        statistics: list[SensorTimePeriodStatisticsDTO],
) -> None:
    with st.expander(
            "Daily Activations Analysis",
            expanded=False,
    ):

        st.markdown(
            """
            This chart shows actual daily activations and a
            7-day rolling average.
            """
        )

        selected_chart = st.selectbox(
            label="Sensor",
            options=chart_options,
            key="daily_activations_selected_sensor",
            format_func=lambda value: "All Sensors" if value == "ALL" else value,
        )

        selected_chart_vm = chart_vms[selected_chart]
        stats_vm = statistics_vms[selected_chart]
        selected_metrics_trend: dict[str, str] = trend_vms[selected_chart]

        new = {}
        for k, v in selected_metrics_trend.items():
            if "_7_" in k:
                new["7_days"] = v
            elif "_14_" in k:
                new["14_days"] = v


        st.markdown(f"##### {selected_chart_vm.title}")

        try:
            fig = scatter_line_chart_plotter.render(selected_chart_vm)
            # fig = line_chart_plotter.render(selected_vm)

            st.plotly_chart(
                fig,
                width="stretch",
                # key=f"daily_activations_chart_{selected_chart}",
                key=f"daily_activations_chart",
                config={
                    "displayModeBar": False,
                    "responsive": True,
                },
            )

        except Exception as e:
            st.exception(e)

        st.subheader("Period Summary")

        with st.container(border=False):
            st.markdown("##### Summary")

            col1, col2 = st.columns(2)

            col1.metric(
                "Total Activations",
                stats_vm.total_activation_count_label,
            )

            col2.metric(
                "Average / Day",
                stats_vm.average_daily_activation_count_label,
            )
            st.write("")

        with st.container(border=False):
            st.markdown("##### Trends")

            col1, col2 = st.columns(2)

            col1.metric(
                "7-Day Trend",
                new["7_days"],
            )

            col2.metric(
                "14-Day Trend",
                new["14_days"],
            )
            st.write("")

        with st.container(border=False):
            st.markdown("##### Activity")

            col3, col4 = st.columns(2)

            col3.metric(
                "Active Days / Total Days",
                f"{stats_vm.active_day_count_label} / {stats_vm.days_in_period_label}",
            )

            col4.metric(
                "Percent Inactive",
                f"{100. * (stats_vm.inactive_day_count / stats_vm.days_in_period):.1f}%",
            )
            st.write("")

        with st.container(border=False):
            st.markdown("##### Activations Range")

            col5, col6 = st.columns(2)

            col5.metric(
                "Minimum",
                f"{stats_vm.minimum_daily_activation_label}",
            )

            col6.metric(
                "Maximum",
                f"{stats_vm.maximum_daily_activation_label}",
            )
            st.write("")

        with st.container(border=False):
            st.markdown("##### Variation")

            col5, col6 = st.columns(2)

            col5.metric(
                "Coefficient",
                f"{stats_vm.coefficient_variation_label}",
            )

            col6.metric(
                "Standard Deviation",
                f"{stats_vm.standard_deviation_daily_activations_label}",
            )
            st.write("")

        """

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            label="Total Activations",
            value=stats_vm.total_activation_count_label,
        )

        col2.metric(
            label="Avg / Day",
            value=stats_vm.average_daily_activation_count_label,
        )

        col3.metric(
            label="Median / Day",
            value=stats_vm.median_daily_activation_count_label,
        )

        col4.metric(
            label="Active Days",
            value=f"{stats_vm.active_day_count_label} / {stats_vm.days_in_period_label}",
        )
        """

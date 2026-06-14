# /src/interface_adapters/presenters/activity/sensor_statistics_presenter.py

from src.application.dto.activity_metric_dtos import (
    SensorTimePeriodStatisticsDTO,
)

from src.interface_adapters.view_models.activity.sensor_statistics_vm import (
    SENSOR_TIME_PERIOD_STATISTICS_COLUMNS,
    SensorTimePeriodStatisticsRowVM,
    SensorTimePeriodStatisticsViewModel,
)


class SensorTimePeriodStatisticsPresenter:
    def present(
        self,
        data: list[SensorTimePeriodStatisticsDTO],
    ) -> SensorTimePeriodStatisticsViewModel:
        if not data:
            return SensorTimePeriodStatisticsViewModel(
                title="Sensor Time Period Statistics",
                subtitle="Daily activation statistics by sensor",
                columns=SENSOR_TIME_PERIOD_STATISTICS_COLUMNS,
                rows=[],
                has_data=False,
                empty_message="No sensor statistics available.",
            )

        rows = [
            SensorTimePeriodStatisticsRowVM(
                sensor_id=item.sensor_id,

                start_date=item.start_date.isoformat(),
                end_date=item.end_date.isoformat(),
                date_range_label=(
                    f"{item.start_date.strftime('%b %d')} - "
                    f"{item.end_date.strftime('%b %d')}"
                ),

                days_in_period=item.days_in_period,
                days_in_period_label=f"{item.days_in_period:,}",

                total_activation_count=item.total_activation_count,
                total_activation_count_label=f"{item.total_activation_count:,}",

                average_daily_activation_count=item.average_daily_activation_count,
                average_daily_activation_count_label=(
                    f"{item.average_daily_activation_count:.1f}"
                ),

                median_daily_activation_count=item.median_daily_activation_count,
                median_daily_activation_count_label=(
                    f"{item.median_daily_activation_count:.1f}"
                ),

                maximum_daily_activation=item.maximum_daily_activation,
                maximum_daily_activation_label=f"{item.maximum_daily_activation:,}",
                maximum_daily_activation_date=(
                    item.maximum_daily_activation_date.isoformat()
                ),

                minimum_daily_activation=item.minimum_daily_activation,
                minimum_daily_activation_label=f"{item.minimum_daily_activation:,}",
                minimum_daily_activation_date=(
                    item.minimum_daily_activation_date.isoformat()
                ),

                percentile_25_daily_activation_count=(
                    item.percentile_25_daily_activation_count
                ),
                percentile_25_daily_activation_count_label=(
                    f"{item.percentile_25_daily_activation_count:.1f}"
                ),

                percentile_75_daily_activation_count=(
                    item.percentile_75_daily_activation_count
                ),
                percentile_75_daily_activation_count_label=(
                    f"{item.percentile_75_daily_activation_count:.1f}"
                ),

                standard_deviation_daily_activations=(
                    item.standard_deviation_daily_activations
                ),
                standard_deviation_daily_activations_label=(
                    f"{item.standard_deviation_daily_activations:.2f}"
                ),

                coefficient_variation=item.coefficient_variation,
                coefficient_variation_label=f"{item.coefficient_variation:.1%}",

                active_day_count=item.active_day_count,
                active_day_count_label=f"{item.active_day_count:,}",

                inactive_day_count=item.inactive_day_count,
                inactive_day_count_label=f"{item.inactive_day_count:,}",
            )
            for item in sorted(data, key=lambda x: x.sensor_id)
        ]

        return SensorTimePeriodStatisticsViewModel(
            title="Sensor Time Period Statistics",
            subtitle="Daily activation statistics by sensor",
            columns=SENSOR_TIME_PERIOD_STATISTICS_COLUMNS,
            rows=rows,
            has_data=True,
            empty_message=None,
        )

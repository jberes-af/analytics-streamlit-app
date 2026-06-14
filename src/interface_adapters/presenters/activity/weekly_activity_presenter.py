# /src/interface_adapters/presenters/activity/weekly_activity_presenter.py

from src.application.dto.activity_metric_dtos import (
    SensorWeeklyActivityDTO,
)

from src.interface_adapters.view_models.activity.weekly_activity_vm import (
    WeeklyActivityRowVM,
    WeeklyActivityViewModel,
)


class WeeklyActivityPresenter:

    def present(
            self,
            data: list[SensorWeeklyActivityDTO],
    ) -> WeeklyActivityViewModel:

        if not data:
            return WeeklyActivityViewModel(
                title="Weekly Activity Summary",
                rows=[],
                has_data=False,
                empty_message="No weekly activity data available.",
            )

        rows: list[WeeklyActivityRowVM] = []

        for item in data:

            if item.change_percent is None:
                change_label = "N/A"
            else:
                change_label = f"{item.change_percent:.1%}"

            rows.append(
                WeeklyActivityRowVM(
                    sensor_id=item.sensor_id,

                    week_start=item.week_start.isoformat(),
                    week_end=item.week_end.isoformat(),

                    week_label=(
                        f"{item.week_start.strftime('%b %d')} - "
                        f"{item.week_end.strftime('%b %d')}"
                    ),

                    total_activations_week=item.total_activations_week,
                    total_activations_week_label=
                    f"{item.total_activations_week:,}",

                    maximum_daily_activations=
                    item.maximum_daily_activations,
                    maximum_daily_activations_label=
                    f"{item.maximum_daily_activations:,}",

                    minimum_daily_activations=
                    item.minimum_daily_activations,
                    minimum_daily_activations_label=
                    f"{item.minimum_daily_activations:,}",

                    average_daily_activations=
                    item.average_daily_activations,
                    average_daily_activations_label=
                    f"{item.average_daily_activations:.1f}",

                    standard_deviation_daily_activations=
                    item.standard_deviation_daily_activations,
                    standard_deviation_daily_activations_label=
                    f"{item.standard_deviation_daily_activations:.2f}",

                    coefficient_variation=
                    item.coefficient_variation,
                    coefficient_variation_label=
                    f"{item.coefficient_variation:.1%}",

                    change_percent=item.change_percent,
                    change_percent_label=change_label,
                )
            )

        return WeeklyActivityViewModel(
            title="Weekly Activity Summary",
            rows=rows,
            has_data=True,
            empty_message=None,
        )

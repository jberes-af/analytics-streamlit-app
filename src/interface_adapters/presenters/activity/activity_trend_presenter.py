# /src/interface_adapters/presenters/activity/activity_trend_presenter.py

from src.application.dto.activity_metric_dtos import ActivityTrendDTO

from src.interface_adapters.view_models.activity.activity_trend_vm import (
    ACTIVITY_TREND_COLUMNS,
    ActivityTrendRowVM,
    ActivityTrendSensorGroupVM,
    ActivityTrendViewModel,
)


class ActivityTrendPresenter:
    def present(
        self,
        sensor_ids: list[str],
        result: list[ActivityTrendDTO],
    ) -> ActivityTrendViewModel:
        if not result:
            return ActivityTrendViewModel(
                title="Daily Activity Trend Results",
                subtitle="Trend direction by sensor and time period",
                columns=ACTIVITY_TREND_COLUMNS,
                sensor_groups=[],
                has_data=False,
                empty_message="No activity trend results available.",
            )

        rows_by_sensor_id: dict[str, list[ActivityTrendRowVM]] = {
            sensor_id: []
            for sensor_id in sensor_ids
        }

        for item in sorted(
            result,
            key=lambda x: (
                x.sensor_id or "",
                x.start_date,
                x.end_date,
                x.metric_name,
            ),
        ):
            sensor_id = item.sensor_id or "ALL"

            row = ActivityTrendRowVM(
                sensor_id=sensor_id,
                metric_name=item.metric_name,

                start_date=item.start_date.isoformat(),
                end_date=item.end_date.isoformat(),
                period_label=(
                    f"{item.start_date.strftime('%b %d')} - "
                    f"{item.end_date.strftime('%b %d')}"
                ),

                direction=item.direction,
                direction_label=item.direction.title(),

                slope_per_day=item.slope_per_day,
                slope_per_day_label=f"{item.slope_per_day:,.2f}",

                intercept=item.intercept,
                intercept_label=f"{item.intercept:,.2f}",
            )

            rows_by_sensor_id.setdefault(sensor_id, []).append(row)

        sensor_groups: list[ActivityTrendSensorGroupVM] = []

        for sensor_id, rows in rows_by_sensor_id.items():
            sensor_groups.append(
                ActivityTrendSensorGroupVM(
                    sensor_id=sensor_id,
                    title=f"Sensor ID {sensor_id}",
                    rows=rows,
                )
            )

        return ActivityTrendViewModel(
            title="Daily Activity Trend Results",
            subtitle="Trend direction by sensor and time period",
            columns=ACTIVITY_TREND_COLUMNS,
            sensor_groups=sensor_groups,
            has_data=True,
            empty_message=None,
        )

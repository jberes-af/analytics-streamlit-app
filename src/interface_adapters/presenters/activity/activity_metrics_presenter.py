# /src/interface_adapters/presenters/activity/activity_metrics_presenter.py

from datetime import datetime, timedelta

from src.application.use_cases.analyze_activity_levels_use_case import (
    ActivityAnalysisResultDTO,
)

from src.interface_adapters.view_models.activity.activity_metrics_vm import (
    ActivityAnalysisViewModel,
    DailyActivityRowVM,
    HourlyActivityPointVM,
    RollingActivityPointVM,
    SensorActivityRowVM,
    PeakActivityRowVM,
    InactivityPeriodRowVM,
    DailyActivityViewModel,
    SensorActivityViewModel,
    HourlyActivityViewModel,
    RollingActivityViewModel,
    PeakActivityViewModel,
    InactivityPeriodsViewModel,
    ActivityDistributionViewModel,
    DAILY_ACTIVITY_COLUMNS,
    SENSOR_ACTIVITY_COLUMNS,
    HOURLY_ACTIVITY_COLUMNS,
    ROLLING_ACTIVITY_COLUMNS,
    PEAK_ACTIVITY_COLUMNS,
    INACTIVITY_PERIOD_COLUMNS,
)
from src.interface_adapters.view_models.table_view_model import TableColumnVM


class ActivityAnalysisMetricsPresenter:
    def present(
            self,
            result: ActivityAnalysisResultDTO | None,
    ) -> ActivityAnalysisViewModel:
        if result is None:
            return ActivityAnalysisViewModel(
                title="",
                subtitle="",
                summary_text="",
                # user_id="",
                date_range="",
                daily_activity=self._empty_daily_activity(),
                sensor_activity=self._empty_sensor_activity(),
                hourly_activity=self._empty_hourly_activity(),
                rolling_activity=self._empty_rolling_activity(),

                peak_activity=self._empty_peak_activity(),
                inactivity_periods=self._empty_inactivity_periods(),
                activity_distribution=self._empty_activity_distribution(),

                has_data=False,
                empty_message="No activity analysis result was returned.",
            )

        has_data = any(
            [
                result.daily_activity,
                result.combined_sensor_activity,
                result.all_sensors_by_hour_activity,
                result.rolling_activity,
                result.peak_activity,
                result.inactivity_periods,
                result.activity_distribution is not None,
            ]
        )

        daily_activity: DailyActivityViewModel = (
            self._present_daily_activity(result.daily_activity))

        sensor_activity: SensorActivityViewModel = (
            self._present_sensor_activity(result.combined_sensor_activity))

        hourly_activity: HourlyActivityViewModel = (
            self._present_hourly_activity(result.all_sensors_by_hour_activity))

        rolling_activity: RollingActivityViewModel = (
            self._present_rolling_activity(result.rolling_activity))

        peak_activity: PeakActivityViewModel = (
            self._present_peak_activity(result.peak_activity))

        inactivity_periods: InactivityPeriodsViewModel = (
            self._present_inactivity_periods(result.inactivity_periods))

        activity_distribution: ActivityDistributionViewModel = (
            self._present_activity_distribution(result.activity_distribution))

        return ActivityAnalysisViewModel(
            title="Activity Levels Analysis",
            subtitle="Daily, sensor, hourly, and rolling activity metrics",
            summary_text=self._build_summary_text(result),
            # user_id=result.user_id,
            date_range=f"{result.start_date.isoformat()} to {result.end_date.isoformat()}",

            daily_activity=daily_activity,
            sensor_activity=sensor_activity,
            hourly_activity=hourly_activity,
            rolling_activity=rolling_activity,
            peak_activity=peak_activity,
            inactivity_periods=inactivity_periods,
            activity_distribution=activity_distribution,
            has_data=has_data,
            empty_message=None,
        )

    @staticmethod
    def _present_daily_activity(data) -> DailyActivityViewModel:
        columns: list[TableColumnVM] = DAILY_ACTIVITY_COLUMNS

        rows: list[DailyActivityRowVM] = [
            DailyActivityRowVM(
                date=item.date.isoformat(),
                total_activations=int(item.total_activations),
                total_activations_label=f"{item.total_activations:,}",
                first_activation=_format_datetime(item.first_activation),
                last_activation=_format_datetime(item.last_activation),
                active_day_length=_format_timedelta(item.active_day_length),
            )
            for item in sorted(data, key=lambda x: x.date)
        ]

        return DailyActivityViewModel(
            title="Daily Activity Results",
            columns=columns,
            rows=rows,
        )

    @staticmethod
    def _present_sensor_activity(data) -> SensorActivityViewModel:
        columns: list[TableColumnVM] = SENSOR_ACTIVITY_COLUMNS

        rows: list[SensorActivityRowVM] = [
            SensorActivityRowVM(
                sensor_id=item.sensor_id,
                total_activations=int(item.total_activations),
                total_activations_label=f"{item.total_activations:,}",
                percentage_of_total=item.percentage_of_total,
                percentage_of_total_label=f"{item.percentage_of_total:.1%}",
            )
            for item in data
        ]

        return SensorActivityViewModel(
            title="Sensor Activity Results",
            columns=columns,
            rows=rows,
        )

    @staticmethod
    def _present_hourly_activity(data) -> HourlyActivityViewModel:
        columns: list[TableColumnVM] = HOURLY_ACTIVITY_COLUMNS

        rows: list[HourlyActivityPointVM] = [
            HourlyActivityPointVM(
                date=item.date.isoformat(),
                hour=item.hour,
                hour_label=f"{item.hour:02d}:00",
                activation_count=item.activation_count,
                activation_count_label=f"{item.activation_count:,}",
            )
            for item in sorted(data, key=lambda x: x.date)
        ]

        return HourlyActivityViewModel(
            title="Hourly Activity Results",
            columns=columns,
            rows=rows,
        )

    @staticmethod
    def _present_rolling_activity(data) -> RollingActivityViewModel:

        columns: list[TableColumnVM] = ROLLING_ACTIVITY_COLUMNS

        rows: list[RollingActivityPointVM] = []
        for item in sorted(data, key=lambda x: x.window_start):
            window_label = (
                f"{item.window_start.strftime('%I:%M %p')} - "
                f"{item.window_end.strftime('%I:%M %p')}"
            )

            rows.append(RollingActivityPointVM(
                window_start=_format_datetime(item.window_start),
                window_end=_format_datetime(item.window_end),
                window_label=window_label,
                activation_count=item.activation_count,
                activation_count_label=f"{item.activation_count:,}",
            ))

        return RollingActivityViewModel(
            title="Rolling Activity Results",
            columns=columns,
            rows=rows,
        )

    @staticmethod
    def _present_peak_activity(data) -> PeakActivityViewModel:

        columns: list[TableColumnVM] = PEAK_ACTIVITY_COLUMNS

        rows: list[PeakActivityRowVM] = []
        # for item in sorted(data, key=lambda x: x.window_start):
        for item in sorted(data, key=lambda x: x.rank):
            window_label = (
                f"{item.window_start.strftime('%I:%M %p')} - "
                f"{item.window_end.strftime('%I:%M %p')}"
            )

            rows.append(PeakActivityRowVM(
                rank=item.rank,
                rank_label=f"{item.rank:,}",
                window_start=_format_datetime(item.window_start),
                window_end=_format_datetime(item.window_end),
                window_label=window_label,
                activation_count=item.activation_count,
                activation_count_label=f"{item.activation_count:,}",
            ))

        return PeakActivityViewModel(
            title="Peak Activity Results",
            columns=columns,
            rows=rows,
        )

    @staticmethod
    def _present_inactivity_periods(data) -> InactivityPeriodsViewModel:
        rows: list[InactivityPeriodRowVM] = []

        for item in sorted(data, key=lambda x: x.start_time):
            period_label = (
                f"{item.start_time.strftime('%I:%M %p')} - "
                f"{item.end_time.strftime('%I:%M %p')}"
            )

            rows.append(
                InactivityPeriodRowVM(
                    start_time=_format_datetime(item.start_time),
                    end_time=_format_datetime(item.end_time),
                    period_label=period_label,
                    duration_seconds=int(item.duration.total_seconds()),
                    duration_label=_format_timedelta(item.duration),
                )
            )

        return InactivityPeriodsViewModel(
            title="Inactivity Period Results",
            columns=INACTIVITY_PERIOD_COLUMNS,
            rows=rows,
        )

    @staticmethod
    def _present_activity_distribution(data) -> ActivityDistributionViewModel:
        return ActivityDistributionViewModel(
            title="Activity Distribution Results",
            entropy=float(data.entropy),
            entropy_label=f"{data.entropy:.3f}",
            most_active_hour=data.most_active_hour,
            most_active_hour_label=_format_hour(data.most_active_hour),
            least_active_hour=data.least_active_hour,
            least_active_hour_label=_format_hour(data.least_active_hour),
        )

    @staticmethod
    def _build_summary_text(
            result: ActivityAnalysisResultDTO,
    ) -> str:
        total_activations = sum(
            item.total_activations
            for item in result.daily_activity
        )

        total_days = len(result.daily_activity)

        if total_days == 0:
            return "No activity events were found for this period."

        average_daily_activations = total_activations / total_days

        return (
            f"{total_activations:,} total activations across "
            f"{total_days} day(s), averaging "
            f"{average_daily_activations:,.1f} activations per day."
        )

    @staticmethod
    def _empty_daily_activity() -> DailyActivityViewModel:
        return DailyActivityViewModel(
            title="Daily Activity Results",
            columns=DAILY_ACTIVITY_COLUMNS,
            rows=[],
        )

    @staticmethod
    def _empty_sensor_activity() -> SensorActivityViewModel:
        return SensorActivityViewModel(
            title="Sensor Activity Results",
            columns=SENSOR_ACTIVITY_COLUMNS,
            rows=[],
        )

    @staticmethod
    def _empty_hourly_activity() -> HourlyActivityViewModel:
        return HourlyActivityViewModel(
            title="Hourly Activity Results",
            columns=HOURLY_ACTIVITY_COLUMNS,
            rows=[],
        )

    @staticmethod
    def _empty_rolling_activity() -> RollingActivityViewModel:
        return RollingActivityViewModel(
            title="Rolling Activity Results",
            columns=ROLLING_ACTIVITY_COLUMNS,
            rows=[],
        )

    @staticmethod
    def _empty_peak_activity() -> PeakActivityViewModel:
        return PeakActivityViewModel(
            title="Peak Activity Results",
            columns=PEAK_ACTIVITY_COLUMNS,
            rows=[],
        )

    @staticmethod
    def _empty_inactivity_periods() -> InactivityPeriodsViewModel:
        return InactivityPeriodsViewModel(
            title="Inactivity Period Results",
            columns=INACTIVITY_PERIOD_COLUMNS,
            rows=[],
        )

    @staticmethod
    def _empty_activity_distribution() -> ActivityDistributionViewModel:
        return ActivityDistributionViewModel(
            title="Activity Distribution Results",
            entropy=0.0,
            entropy_label="0.000",
            most_active_hour=None,
            most_active_hour_label="N/A",
            least_active_hour=None,
            least_active_hour_label="N/A",
        )


def _format_datetime(value: datetime | None) -> str:
    if value is None:
        return "N/A"

    return value.strftime("%Y-%m-%d %I:%M %p")


def _format_timedelta(value: timedelta | None) -> str:
    if value is None:
        return "N/A"

    total_seconds = int(value.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, _ = divmod(remainder, 60)

    return f"{hours}h {minutes}m"

def _format_hour(value: int | None) -> str:
    if value is None:
        return "N/A"

    return f"{value:02d}:00"
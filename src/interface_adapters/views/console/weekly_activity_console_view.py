# /src/interface_adapters/views/console/weekly_activity_console_view.py

from src.interface_adapters.view_models.activity.weekly_activity_vm import (
    WeeklyActivityViewModel,
)


class WeeklyActivityConsoleRenderer:

    def render(
            self,
            view_model: WeeklyActivityViewModel,
    ) -> None:

        print()
        print(view_model.title)
        print("=" * 80)

        if not view_model.has_data:
            print(view_model.empty_message)
            print()
            return

        current_sensor: str | None = None

        for row in view_model.rows:

            if row.sensor_id != current_sensor:
                current_sensor = row.sensor_id

                print()
                print(f"Sensor: {row.sensor_id}")
                print("-" * 80)

            print(
                f"{row.week_label:<22}"
                f"Total={row.total_activations_week_label:<8}"
                f"Avg={row.average_daily_activations_label:<8}"
                f"Min={row.minimum_daily_activations_label:<6}"
                f"Max={row.maximum_daily_activations_label:<6}"
                f"CV={row.coefficient_variation_label:<8}"
                f"WoW={row.change_percent_label}"
            )

        print()

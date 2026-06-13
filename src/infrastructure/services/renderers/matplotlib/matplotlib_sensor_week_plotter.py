# src/infrastructure/services/matplotlib/matplotlib_sensor_week_plotter.py

from datetime import date

import matplotlib.pyplot as plt

from src.interface_adapters.view_models.movements.sensor_week_plot_view_model import (
    SensorWeekPlotViewModel,
)


class MatplotlibSensorWeekPlotter:
    def plot(
        self,
        view_model: SensorWeekPlotViewModel,
    ) -> None:
        if not view_model.points:
            raise ValueError("No plot points provided.")

        fig, ax = plt.subplots(figsize=(14, 8))

        self._draw_daily_lines(ax, view_model)
        self._draw_points(ax, view_model)

        ax.set_title(view_model.title)
        ax.set_ylabel("Time of day")
        ax.set_xlabel("Day / sensor")

        self._format_x_axis(ax, view_model)
        self._format_y_axis(ax)

        ax.grid(True, axis="y", alpha=0.3)
        fig.tight_layout()

        if view_model.output_path is not None:
            fig.savefig(view_model.output_path, dpi=200)
            plt.close(fig)
        else:
            plt.show()

    def plot2(
        self,
        view_model: SensorWeekPlotViewModel,
    ) -> None:
        if not view_model.points:
            raise ValueError("No plot points provided.")

        x_values = [point.x for point in view_model.points]
        y_values = [point.y_seconds for point in view_model.points]

        fig, ax = plt.subplots(figsize=(14, 8))

        ax.scatter(
            x_values,
            y_values,
            s=12,
            alpha=0.75,
        )

        ax.set_title(view_model.title)
        ax.set_ylabel("Time of day")
        ax.set_xlabel("Day / sensor")

        self._format_x_axis(ax, view_model)
        self._format_y_axis(ax)

        ax.grid(True, axis="y", alpha=0.3)
        fig.tight_layout()

        if view_model.output_path is not None:
            fig.savefig(view_model.output_path, dpi=200)
            plt.close(fig)
        else:
            plt.show()

    @staticmethod
    def _format_x_axis(
        ax,
        view_model: SensorWeekPlotViewModel,
    ) -> None:
        sensor_count = len(view_model.sensor_ids)

        tick_positions: list[int] = []
        tick_labels: list[str] = []

        for day_index in range(view_model.number_of_days):
            current_day = date.fromordinal(
                view_model.start_day.toordinal() + day_index
            )

            for sensor_index, sensor_id in enumerate(view_model.sensor_ids):
                x = day_index * sensor_count + sensor_index
                tick_positions.append(x)
                tick_labels.append(
                    f"{current_day.strftime('%m/%d')}\n{sensor_id}"
                )

        ax.set_xticks(tick_positions)
        ax.set_xticklabels(
            tick_labels,
            rotation=90,
            fontsize=8,
        )

        for day_index in range(1, view_model.number_of_days):
            separator_x = day_index * sensor_count - 0.5
            ax.axvline(separator_x, linestyle="--", alpha=0.25)

    @staticmethod
    def _format_y_axis(ax) -> None:
        ax.set_yticks(
            [
                0,
                6 * 3600,
                12 * 3600,
                18 * 3600,
                24 * 3600,
            ]
        )

        ax.set_yticklabels(
            [
                "12 AM",
                "6 AM",
                "12 PM",
                "6 PM",
                "12 AM",
            ]
        )

        ax.set_ylim(0, 86400)

    @staticmethod
    def _draw_daily_lines(
        ax,
        view_model: SensorWeekPlotViewModel,
    ) -> None:
        for line_group in view_model.line_groups:
            if len(line_group.points) < 2:
                continue

            x_values = [
                point.x
                for point in line_group.points
            ]

            y_values = [
                point.y_seconds
                for point in line_group.points
            ]

            ax.plot(
                x_values,
                y_values,
                linewidth=0.8,
                alpha=0.35,
            )

    @staticmethod
    def _draw_points(
        ax,
        view_model: SensorWeekPlotViewModel,
    ) -> None:
        for marker in sorted({point.marker for point in view_model.points}):
            marker_points = [
                point
                for point in view_model.points
                if point.marker == marker
            ]

            ax.scatter(
                [point.x for point in marker_points],
                [point.y_seconds for point in marker_points],
                c=[point.color for point in marker_points],
                marker=marker,
                s=16,
                alpha=0.75,
                zorder=3,
            )

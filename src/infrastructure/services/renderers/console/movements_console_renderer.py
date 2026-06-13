# /src/infrastructure/services/renderers/movements_console_renderer.py

from dataclasses import asdict

from src.interface_adapters.view_models.movements.movement_analysis_vm import (
    MovementAnalysisViewModel
)

class MovementAnalysisConsoleRenderer:
    def render(
            self,
            view_model: MovementAnalysisViewModel,
    ) -> None:
        print()
        print(view_model.title)
        print("=" * 40)
        print(view_model.summary_text)

        self._render_table_section(view_model.top_sequences.title,
                                   view_model.top_sequences.columns,
                                   view_model.top_sequences.rows)

        self._render_table_section(view_model.transition_probabilities.title,
                                   view_model.transition_probabilities.columns,
                                   view_model.transition_probabilities.rows)

        self._render_table_section(view_model.time_bucket_comparison.title,
                                   view_model.time_bucket_comparison.columns,
                                   view_model.time_bucket_comparison.rows)

    @staticmethod
    def _render_table_section(
            title: str,
            columns,
            rows,
    ) -> None:
        print()
        print(title)
        print("-" * 40)

        if not rows:
            print("No data.")
            return

        headers = [column.label for column in columns]
        keys = [column.key for column in columns]

        print(" | ".join(headers))
        print("-" * 40)

        for row in rows:
            row_dict = asdict(row)
            values = [str(row_dict[key]) for key in keys]
            print(" | ".join(values))


"""
class MovementAnalysisConsoleRenderer:
    def render(
            self,
            view_model: MovementAnalysisViewModel,
    ) -> None:
        print()
        print(view_model.title)
        print("=" * 40)

        if view_model.subtitle:
            print(view_model.subtitle)

        print()
        print(f"Scenario: {view_model.scenario_id}")
        print(f"User: {view_model.user_id}")
        print(f"Period: {view_model.date_range}")

        print()
        print(view_model.summary_text)

        self._print_section(
            title=view_model.top_sequences.title,
            rows=view_model.top_sequences.rows,
        )

        self._print_section(
            title=view_model.transition_probabilities.title,
            rows=view_model.transition_probabilities.rows,
        )

        self._print_section(
            title=view_model.time_bucket_comparison.title,
            rows=view_model.time_bucket_comparison.rows,
        )

    @staticmethod
    def _print_section(
            title: str,
            rows: list,
    ) -> None:
        print()
        print(title)
        print("-" * 40)

        if not rows:
            print("No data.")
            return

        for row in rows:
            print(row)
"""

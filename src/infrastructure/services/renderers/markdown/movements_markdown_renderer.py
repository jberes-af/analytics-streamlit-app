# /src/infrastructure/services/renderers/movements_markdown_renderer.py

from dataclasses import asdict
from pathlib import Path

from src.interface_adapters.view_models.movements.movement_analysis_vm import (
    MovementAnalysisViewModel
)


class MovementAnalysisMarkdownRenderer:
    def write(
        self,
        view_model: MovementAnalysisViewModel,
        output_path: Path,
    ) -> None:
        output_path.parent.mkdir(parents=True, exist_ok=True)

        markdown = self.render(view_model)

        output_path.write_text(markdown, encoding="utf-8")

    def render(
        self,
        view_model: MovementAnalysisViewModel,
    ) -> str:
        lines: list[str] = []

        lines.append(f"# {view_model.title}")

        if view_model.subtitle:
            lines.append("")
            lines.append(view_model.subtitle)

        lines.append("")
        lines.append(f"**Scenario:** {view_model.scenario_id}")
        lines.append(f"**User:** {view_model.user_id}")
        # lines.append(f"**Period:** {view_model.date_range}")

        lines.append("")
        lines.append(view_model.summary_text)

        self._append_table(
            lines,
            title=view_model.top_sequences.title,
            columns=view_model.top_sequences.columns,
            rows=view_model.top_sequences.rows,
        )

        self._append_table(
            lines,
            title=view_model.transition_probabilities.title,
            columns=view_model.transition_probabilities.columns,
            rows=view_model.transition_probabilities.rows,
        )

        self._append_table(
            lines,
            title=view_model.time_bucket_comparison.title,
            columns=view_model.time_bucket_comparison.columns,
            rows=view_model.time_bucket_comparison.rows,
        )

        return "\n".join(lines)

    @staticmethod
    def _append_table(
        lines: list[str],
        title: str,
        columns,
        rows,
    ) -> None:
        lines.append("")
        lines.append(f"## {title}")

        if not rows:
            lines.append("")
            lines.append("No data.")
            return

        headers = [column.label for column in columns]
        keys = [column.key for column in columns]

        lines.append("")
        lines.append("| " + " | ".join(headers) + " |")
        lines.append("| " + " | ".join(["---"] * len(headers)) + " |")

        for row in rows:
            row_dict = asdict(row)
            values = [str(row_dict[key]) for key in keys]
            lines.append("| " + " | ".join(values) + " |")

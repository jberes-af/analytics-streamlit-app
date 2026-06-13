# /src/infrastructure/services/analysis/pandas/activity/activity_distribution_calculator.py

import math

import pandas as pd

from src.application.dto.activity_metric_dtos import ActivityDistributionDTO


class ActivityDistributionCalculator:
    required_columns = {"hour"}

    def calculate_by_hour(
        self,
        df: pd.DataFrame,
    ) -> ActivityDistributionDTO:
        if df.empty:
            return ActivityDistributionDTO(
                entropy=0.0,
                most_active_hour=None,
                least_active_hour=None,
            )

        missing_columns = self.required_columns - set(df.columns)

        if missing_columns:
            raise ValueError(
                f"ActivityDistributionCalculator missing required columns: {missing_columns}"
            )

        hourly_counts = (
            df.groupby("hour")
            .size()
            .reindex(range(24), fill_value=0)
        )

        total_count = int(hourly_counts.sum())

        if total_count == 0:
            return ActivityDistributionDTO(
                entropy=0.0,
                most_active_hour=None,
                least_active_hour=None,
            )

        entropy = self._calculate_entropy(hourly_counts)

        most_active_hour = int(hourly_counts.idxmax())

        # Least active non-zero hour is usually more meaningful than
        # including overnight hours with zero activity.
        nonzero_hourly_counts = hourly_counts[hourly_counts > 0]

        least_active_hour = (
            int(nonzero_hourly_counts.idxmin())
            if not nonzero_hourly_counts.empty
            else None
        )

        return ActivityDistributionDTO(
            entropy=entropy,
            most_active_hour=most_active_hour,
            least_active_hour=least_active_hour,
        )

    @staticmethod
    def _calculate_entropy(
        counts: pd.Series,
    ) -> float:
        total = counts.sum()

        if total == 0:
            return 0.0

        probabilities = counts[counts > 0] / total

        return float(
            -sum(
                probability * math.log(probability)
                for probability in probabilities
            )
        )
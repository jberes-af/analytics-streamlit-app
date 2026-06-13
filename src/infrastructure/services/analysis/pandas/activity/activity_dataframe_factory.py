# /src/infrastructure/services/analysis/pandas/activity/activity_dataframe_factory.py

import pandas as pd

from src.domain.entities.sensor import SensorEvent


class ActivityDataFrameFactory:

    @staticmethod
    def from_events(
        events: list[SensorEvent],
    ) -> pd.DataFrame:

        rows = [
            {
                "sensor_id": event.sensor_id,
                "timestamp": event.activated_at,
                "sensor_state": event.sensor_state,
            }
            for event in events
        ]

        df = pd.DataFrame(rows)

        if df.empty:
            return df

        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df = df.sort_values("timestamp")

        df["date"] = df["timestamp"].dt.date
        df["hour"] = df["timestamp"].dt.hour
        df["weekday"] = df["timestamp"].dt.weekday

        return df
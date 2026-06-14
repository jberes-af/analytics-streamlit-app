# shared_view_model.py

from dataclasses import dataclass


@dataclass(frozen=True)
class RunConfigViewModel:
    scenario_id: str
    user_reference: str
    user_id: str
    time_period: str
    sensor_ids: str
    sensor_count: str
    sensor_profiles: str
    last_activations: str
    last_seen: str



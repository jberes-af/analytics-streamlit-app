# /src/infrastructure/aws/appsync_last_seen_adapter.py

from datetime import datetime, timezone
from zoneinfo import ZoneInfo

from src.application.dto.sensor_timeline_uc_dtos import SensorLastSeenDTO
from src.application.ports.aws_appsync_ports import SensorLastSeenPort

import requests
import traceback


class AppSyncLastSeenAdapter(SensorLastSeenPort):
    GET_DEVICE_CONNECTIVITY = """
    query GetDeviceConnectivity($deviceId: ID!) {
      getDeviceConnectivity(deviceId: $deviceId) {
        deviceId
        connectivityState
        lastSeenAt
        statusAt
      }
    }
    """

    def __init__(self,
                 *,
                 endpoint: str,
                 api_key: str):
        self.endpoint = endpoint
        self.api_key = api_key

    def get_last_seen_utc(self, *, device_id: str) -> SensorLastSeenDTO | None:
        if not self.api_key or not self.api_key.strip():
            print("ERROR: AWS GraphQL API key is missing")
            return None

        payload = {
            "query": self.GET_DEVICE_CONNECTIVITY,
            "variables": {
                "deviceId": device_id,
            },
        }

        response = requests.post(
            self.endpoint,
            headers={
                "Content-Type": "application/json",
                "x-api-key": self.api_key,
            },
            json=payload,
            timeout=10,
        )

        if response.status_code in (401, 403):
            print("ERROR: Unauthorized AWS GraphQL API key.")
            return None

        try:
            response.raise_for_status()
        except requests.HTTPError as exc:
            print(f"ERROR: AWS AppSync request failed: {exc}")
            return None

        result = response.json()

        if "errors" in result:
            print(f"AWS GraphQL errors: {result['errors']}")
            return None

        connectivity = result.get("data", {}).get("getDeviceConnectivity")

        if not connectivity:
            return None

        # device_id_conn = connectivity.get("deviceID")
        last_seen = connectivity.get("lastSeenAt")
        connectivity_state = connectivity.get("connectivityState")
        status_at = connectivity.get("statusAt")

        status_at_utc_dt: datetime = (
            datetime.fromtimestamp(status_at, tz=timezone.utc))
        status_at_cst_dt = status_at_utc_dt.astimezone(ZoneInfo("America/Chicago"))

        try:
            if last_seen is None:
                return None

            last_seen_sec = _normalize_epoch_seconds(last_seen)

            if last_seen_sec is None:
                return None

            utc_dt = datetime.fromtimestamp(last_seen_sec, tz=timezone.utc)
            central_americas_dt = utc_dt.astimezone(ZoneInfo("America/Chicago"))

            """
            print(f"\ndevice ID          : {device_id}; {device_id_conn}")
            print(f"last seen          : {last_seen}")
            print(f"last seen (UTC)    : {utc_dt}")
            print(f"last seen (CST)    : {central_americas_dt}")
            print(f"connectivity state : {connectivity_state}")
            print(f"status at          : {status_at}\n")
            """

            return SensorLastSeenDTO(
                sensor_id=device_id,
                last_seen_time_utc=utc_dt,
                last_seen_time_cst=central_americas_dt,
                connectivity_status=connectivity_state,
                status_timestamp=status_at_cst_dt,
            )

        except Exception:
            """
            print("FAILED values:")
            print("last_seen =", repr(last_seen), type(last_seen))
            print("status_at =", repr(status_at), type(status_at))
            """
            traceback.print_exc()
            return SensorLastSeenDTO(
                sensor_id=device_id,
                last_seen_time_utc="---",
                last_seen_time_cst="---",
                connectivity_status="---",
                status_timestamp=status_at_cst_dt,
            )


def _normalize_epoch_seconds(value: int | float | str | None) -> int | None:
    if value is None:
        return None

    ts = int(value)

    # milliseconds since epoch
    if ts > 10_000_000_000:
        ts = ts // 1000

    return ts

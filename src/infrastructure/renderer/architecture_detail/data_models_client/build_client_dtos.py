# # /src/infrastructure/architecture_detail/data_models_analytics/data_models_client/build_client_dtos.py

from typing import Iterable

from src.domain.mobile_app_types import DataObject, ClientContracts


def build_contract(
        requests: Iterable[DataObject],
        responses: Iterable[DataObject],
) -> ClientContracts:
    return ClientContracts(
        request_dtos=tuple(requests),
        response_dtos=tuple(responses),
        screen_dtos=tuple(responses),
    )

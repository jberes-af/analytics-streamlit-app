# /src/infrastructure/renderer/architecture_detail/data_models_analytics/data_models_backend/build_backen_dtos.py
from typing import Iterable

from src.domain.mobile_app_types import DataObject, DataRead, DataWrite, BackendDataModel


def build_backend_data_model(
        *,
        definitions: Iterable[DataObject] = (),
        persistences: Iterable[DataObject] = (),
        reads: Iterable[DataRead] = (),
        writes: Iterable[DataWrite] = (),
) -> BackendDataModel:
    return BackendDataModel(
        definition_dtos=tuple(definitions),
        persistence_dtos=tuple(persistences),
        data_reads=tuple(reads),
        data_writes=tuple(writes),
    )


def build_dto(
        name: str,
        code: str,
        description: str = "",
) -> DataObject:
    return DataObject(
        name=name,
        description=description,
        code=code.strip(),
    )

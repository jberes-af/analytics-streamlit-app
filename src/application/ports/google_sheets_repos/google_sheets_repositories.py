# application/ports/google_sheets_repository.py

from dataclasses import dataclass
from typing import Protocol

from src.domain.dto.domain_object_dtos import DomainObjectInputsDTO


@dataclass(frozen=True)
class SheetLocator:
    spreadsheet_id: str
    sheet_name: str


class SheetLocatorPort(Protocol):
    def resolve(self, *, table_key: str) -> SheetLocator:
        ...


class ConfigInputsRepositoryPort(Protocol):
    def load_sheets_input_data(self) -> DomainObjectInputsDTO:
        ...
        # Load validated financial model assumptions from an external source.


"""
class SheetWriterPort(Protocol):
    def write_snapshot(
        self,
        *,
        spreadsheet_id: str,
        sheet_name: str,           # destination tab title, e.g. "entities"
        rows: Sequence[EntityRow],
        mode: SnapshotMode = "stage_swap",
    ) -> None:
        ...
    
"""
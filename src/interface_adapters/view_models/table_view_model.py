# /src/interface_adapters/view_models/table_view_model.py

from dataclasses import dataclass


@dataclass(frozen=True)
class TableColumnVM:
    key: str
    label: str

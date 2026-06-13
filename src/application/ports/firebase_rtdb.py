# /src/application/ports/firebase_rtdb.py

from typing import Any, Mapping, Protocol

from src.domain.value_objects.firebase import FirebasePath


class FirebaseRtdbPort(Protocol):

    # def create_node(self, path: FirebasePath, data: Mapping[str, Any]) -> None:
        # ...

    # def delete_node(self, path: FirebasePath) -> None:
        # ...

    def read_node(self, path: FirebasePath) -> Any:
        """Return the value at path (dict/list/scalar) or None if missing."""

    def node_exists(self, path: FirebasePath) -> bool:
        """True if node exists (non-null)."""

    def list_children_keys(self, path: FirebasePath) -> list[str]:
        """Return child keys under a node (e.g., keys of /user)."""

    def update_paths(self, updates: Mapping[str, Any]) -> None:
        """Create or write-to node"""


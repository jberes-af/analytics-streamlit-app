# /src/infrastructure/renderer/architecture_detail/data_models_analytics/data_models_domain/care/raw_priority_item.py


PRIORITY_ITEM_LEVEL_ENUM: str = """
class PriorityItemLevelEnum(StrEnum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
"""




PRIORITY_ITEM_STATUS_ENUM: str = """
class PriorityItemStatusEnum(StrEnum):
    OPEN = "Open"
    RESOLVED = "Resolved"
    CLOSED = "Closed"
    NOTE = "Note"
"""




PRIORITY_ITEM_NOTE_DTO: str = """
@dataclass(frozen=True)
class PriorityItemNoteDTO:
    note_id: str
    user_id: str
    created_at_iso: str
    note: str
"""



PRIORITY_ITEM_RECORD_DTO: str = """
@dataclass(frozen=True)
class PriorityItemRecordDTO:
    item_id: str
    resident_id: str
    item_description: str
    reason_for_priority: str
    priority_level: PriorityItemLevelEnum
    assigned_to: str
    status: PriorityItemStatusEnum
    created_at_iso: str
    created_by_user_id: str
    resolved_at_iso: str | None = None
    closed_at_iso: str | None = None
    item_notes: tuple[PriorityItemNote, ...] = ()
    recommendation_notes: tuple[PriorityItemNote, ...] = ()
"""

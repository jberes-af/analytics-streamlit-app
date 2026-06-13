# /src/infrastructure/renderer/architecture_detail/screens/sensing/movement_patterns.py

from src.domain.mobile_app_types import (
    NavigationRoute,
    ScreenSpec,
)

MOVEMENT_PATTERNS_SCREEN_SPEC = ScreenSpec(
    screen_id="screen.sensing.movement_patterns",
    name="Movement Patterns",
    purpose=(
        "Display sensor-to-sensor notifications."
    ),
    displayed_data=(
        "shift_label",
        "assigned_patient_count",
        "needs_attention_count",
        "patient_cards",
        "priority_level",
        "adl_completion_status",
        "review_signals",
    ),
    user_inputs=(
        "patient_card_selection",
        "review_queue_selection",
        "filter_selection",
    ),
    primary_action="open_patient_summary",
    secondary_actions=(
        "open_review_queue",
        "filter_patients",
        "refresh_dashboard",
    ),
    navigation_in=(
        "app.launch",
        "screen.patient.summary",
        "screen.review.queue",
    ),
    navigation_out=(
        NavigationRoute(
            action="open_patient_summary",
            target_screen_id="screen.patient.summary",
            condition="patient_selected",
        ),
        NavigationRoute(
            action="open_review_queue",
            target_screen_id="screen.review.queue",
        ),
    ),
    loading_state="Loading (grouped) sensor notification data.",
    empty_state="No sensor data available.",
    error_state="Unable to load sensor data.",
)
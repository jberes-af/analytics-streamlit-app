# /src/infrastructure/renderer/architecture_detail/screens/caregiver_adl.py

from src.domain.mobile_app_types import (
    NavigationRoute,
    ScreenSpec,
)

ADL_HOME_SCREEN_SPEC = ScreenSpec(
    screen_id="screen.adl.home",
    name="ADL Home (Shift Dashboard)",
    purpose=(
        "Display assigned patients for the current shift, grouped by priority, "
        "with ADL completion status and review signals."
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
    loading_state="Loading assigned patients and shift status.",
    empty_state="No assigned patients are available for this shift.",
    error_state="Unable to load shift dashboard.",
)

PATIENT_SUMMARY_SCREEN_SPEC = ScreenSpec(
    screen_id="screen.patient.summary",
    name="Patient Summary (Shift Snapshot)",
    purpose=(
        "Provide a patient-specific shift snapshot with ADL status, recent changes, "
        "observations, alerts, tasks, and next actions."
    ),
    displayed_data=(
        "patient_name",
        "location_label",
        "shift_summary",
        "adl_status_cards",
        "recent_observations",
        "active_alerts",
        "open_escalations",
        "actions_required",
    ),
    user_inputs=(
        "adl_card_selection",
        "add_adl_selection",
        "add_observation_selection",
        "history_selection",
        "escalation_selection",
    ),
    primary_action="open_adl_detail_or_entry",
    secondary_actions=(
        "add_observation",
        "open_history",
        "escalate_concern",
        "return_to_home",
    ),
    navigation_in=(
        "screen.adl.home",
        "screen.review.queue.detail",
        "screen.adl.entry",
        "screen.observation.entry",
        "screen.escalate",
        "screen.history",
    ),
    navigation_out=(
        NavigationRoute(
            action="start_adl_entry",
            target_screen_id="screen.adl.entry",
            condition="adl_selected",
        ),
        NavigationRoute(
            action="add_observation",
            target_screen_id="screen.observation.entry",
        ),
        NavigationRoute(
            action="open_history",
            target_screen_id="screen.history",
        ),
        NavigationRoute(
            action="escalate_concern",
            target_screen_id="screen.escalate",
        ),
        NavigationRoute(
            action="back_to_home",
            target_screen_id="screen.adl.home",
        ),
    ),
    loading_state="Loading patient shift snapshot.",
    empty_state="No ADL or observation data is available for this patient.",
    error_state="Unable to load patient summary.",
)

ADL_ENTRY_SCREEN_SPEC = ScreenSpec(
    screen_id="screen.adl.entry",
    name="ADL Entry (Assessment Form)",
    purpose="Enable caregiver to record a structured ADL assessment.",
    displayed_data=(
        "patient_name",
        "location_label",
        "adl_name",
        "adl_description",
        "score_scale",
        "score_definitions",
        "previous_score",
        "baseline_score",
        "comparison_to_previous",
        "comparison_to_baseline",
    ),
    user_inputs=(
        "selected_score",
        "note_text",
        "observed_at",
        "unable_to_assess_selection",
        "refused_selection",
    ),
    primary_action="submit_adl_entry",
    secondary_actions=(
        "cancel_entry",
        "add_related_observation",
        "mark_unable_to_assess",
    ),
    navigation_in=(
        "screen.patient.summary",
        "screen.review.queue.detail",
        "screen.history",
    ),
    navigation_out=(
        NavigationRoute(
            action="submit_adl_entry",
            target_screen_id="screen.patient.summary",
            condition="save_success",
        ),
        NavigationRoute(
            action="cancel_entry",
            target_screen_id="screen.patient.summary",
        ),
        NavigationRoute(
            action="add_related_observation",
            target_screen_id="screen.observation.entry",
        ),
    ),
    validation_rules=(
        "selected_score is required unless unable_to_assess or refused is selected",
        "observed_at is required",
        "observed_at cannot be in the future",
        "note_text is required when score differs from baseline or previous score if policy requires",
    ),
    loading_state="Loading ADL entry context.",
    empty_state="ADL score options are unavailable.",
    error_state="Unable to load ADL entry form.",
)

OBSERVATION_ENTRY_SCREEN_SPEC = ScreenSpec(
    screen_id="screen.observation.entry",
    name="Observation Entry (Narrative Capture)",
    purpose=(
        "Enable caregiver to record a timestamped narrative observation for a patient."
    ),
    displayed_data=(
        "patient_name",
        "location_label",
        "observation_categories",
        "suggested_category",
        "related_adl_context",
    ),
    user_inputs=(
        "selected_category",
        "note_text",
        "observed_at",
    ),
    primary_action="submit_observation",
    secondary_actions=(
        "cancel_entry",
        "link_to_adl",
    ),
    navigation_in=(
        "screen.patient.summary",
        "screen.adl.entry",
        "screen.review.queue.detail",
    ),
    navigation_out=(
        NavigationRoute(
            action="submit_observation",
            target_screen_id="screen.patient.summary",
            condition="save_success",
        ),
        NavigationRoute(
            action="cancel_entry",
            target_screen_id="screen.patient.summary",
        ),
    ),
    validation_rules=(
        "selected_category is required",
        "note_text is required",
        "observed_at is required",
        "observed_at cannot be in the future",
    ),
    loading_state="Loading observation entry context.",
    empty_state="Observation categories are unavailable.",
    error_state="Unable to load observation entry form.",
)

PATIENT_HISTORY_SCREEN_SPEC = ScreenSpec(
    screen_id="screen.history",
    name="Patient History (Timeline & Trends)",
    purpose=(
        "Display historical ADL assessments, observations, escalations, and corrections "
        "with timeline context and ADL trend summaries."
    ),
    displayed_data=(
        "patient_name",
        "date_range",
        "adl_trend_summaries",
        "key_change_summary",
        "timeline_items",
        "filters",
    ),
    user_inputs=(
        "date_range_selection",
        "record_type_filter",
        "adl_type_filter",
        "timeline_item_selection",
        "detailed_trends_selection",
    ),
    primary_action="review_history",
    secondary_actions=(
        "filter_history",
        "open_detailed_trends",
        "correct_entry",
        "return_to_patient_summary",
    ),
    navigation_in=(
        "screen.patient.summary",
        "screen.review.queue.detail",
    ),
    navigation_out=(
        NavigationRoute(
            action="open_detailed_trends",
            target_screen_id="screen.detailed.trends",
            condition="trend_selected",
        ),
        NavigationRoute(
            action="correct_entry",
            target_screen_id="screen.adl.entry",
            condition="editable_entry_selected",
            notes="ADL Entry opens in correction mode when correcting an ADL assessment.",
        ),
        NavigationRoute(
            action="back_to_patient_summary",
            target_screen_id="screen.patient.summary",
        ),
    ),
    validation_rules=(
        "date_range is required",
        "custom date range requires start_at and end_at",
    ),
    loading_state="Loading patient history.",
    empty_state="No history is available for the selected range.",
    error_state="Unable to load patient history.",
)

REVIEW_QUEUE_SCREEN_SPEC = ScreenSpec(
    screen_id="screen.review.queue",
    name="Review Queue (Prioritized Triage List)",
    purpose=(
        "Display prioritized patients or issues requiring review based on ADL declines, "
        "missing ADLs, alerts, observations, or escalations."
    ),
    displayed_data=(
        "queue_counts",
        "priority_filters",
        "queue_items",
        "patient_name",
        "reason_title",
        "reason_summary",
        "priority_level",
        "queue_status",
    ),
    user_inputs=(
        "queue_filter_selection",
        "queue_item_selection",
        "refresh_queue",
    ),
    primary_action="open_review_queue_detail",
    secondary_actions=(
        "filter_queue",
        "refresh_queue",
        "return_to_home",
    ),
    navigation_in=(
        "screen.adl.home",
        "screen.review.queue.detail",
    ),
    navigation_out=(
        NavigationRoute(
            action="open_review_queue_detail",
            target_screen_id="screen.review.queue.detail",
            condition="queue_item_selected",
        ),
        NavigationRoute(
            action="back_to_home",
            target_screen_id="screen.adl.home",
        ),
    ),
    loading_state="Loading review queue.",
    empty_state="No patients or issues currently require review.",
    error_state="Unable to load review queue.",
)

REVIEW_QUEUE_DETAIL_SCREEN_SPEC = ScreenSpec(
    screen_id="screen.review.queue.detail",
    name="Review Detail (Issue Analysis)",
    purpose=(
        "Provide detailed context for a selected review item, including reason, "
        "supporting ADL changes, related observations, and recommended actions."
    ),
    displayed_data=(
        "patient_name",
        "location_label",
        "reason_title",
        "reason_summary",
        "clinical_interpretation",
        "supporting_adl_changes",
        "supporting_observations",
        "related_alerts",
        "related_escalations",
        "recommended_actions",
        "queue_status",
    ),
    user_inputs=(
        "recommended_action_selection",
        "acknowledge_selection",
        "escalation_selection",
        "open_patient_selection",
    ),
    primary_action="open_patient_summary",
    secondary_actions=(
        "acknowledge_review_item",
        "start_adl_entry",
        "escalate_concern",
        "return_to_review_queue",
    ),
    navigation_in=(
        "screen.review.queue",
        "screen.escalate",
    ),
    navigation_out=(
        NavigationRoute(
            action="open_patient_summary",
            target_screen_id="screen.patient.summary",
        ),
        NavigationRoute(
            action="start_adl_entry",
            target_screen_id="screen.adl.entry",
            condition="assessment_recommended",
        ),
        NavigationRoute(
            action="escalate_concern",
            target_screen_id="screen.escalate",
            condition="escalation_recommended",
        ),
        NavigationRoute(
            action="acknowledge_review_item",
            target_screen_id="screen.review.queue",
            condition="status_update_success",
        ),
        NavigationRoute(
            action="back_to_review_queue",
            target_screen_id="screen.review.queue",
        ),
    ),
    validation_rules=(
        "queue_item_id is required",
        "acknowledge action requires valid queue status transition",
    ),
    loading_state="Loading review issue details.",
    empty_state="No supporting data is available for this review item.",
    error_state="Unable to load review issue details.",
)

ESCALATION_SCREEN_SPEC = ScreenSpec(
    screen_id="screen.escalate",
    name="Escalation (Action & Assignment)",
    purpose=(
        "Enable caregiver to create a structured escalation for a patient concern, "
        "assign it for follow-up, set priority, and optionally notify recipients."
    ),
    displayed_data=(
        "patient_name",
        "location_label",
        "default_reason",
        "auto_summary",
        "supporting_adl_changes",
        "supporting_observations",
        "related_alerts",
        "assignable_recipients",
        "priority_options",
        "classification_options",
        "follow_up_options",
    ),
    user_inputs=(
        "reason_code",
        "caregiver_note",
        "priority",
        "classifications",
        "assigned_recipients",
        "expected_follow_up",
        "notification_channels",
        "requires_real_time_interaction",
    ),
    primary_action="submit_escalation",
    secondary_actions=(
        "cancel_escalation",
        "view_supporting_data",
    ),
    navigation_in=(
        "screen.patient.summary",
        "screen.review.queue.detail",
    ),
    navigation_out=(
        NavigationRoute(
            action="submit_escalation",
            target_screen_id="screen.patient.summary",
            condition="submit_success",
        ),
        NavigationRoute(
            action="cancel_escalation",
            target_screen_id="screen.patient.summary",
        ),
        NavigationRoute(
            action="view_supporting_data",
            target_screen_id="screen.history",
        ),
    ),
    validation_rules=(
        "reason_code is required",
        "priority is required",
        "at least one assigned recipient or role is required",
        "expected_follow_up is required when priority is high",
    ),
    loading_state="Loading escalation context.",
    empty_state="No supporting escalation context is available.",
    error_state="Unable to load escalation screen.",
)

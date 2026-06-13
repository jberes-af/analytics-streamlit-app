# /src/infrastructure/renderer/architecture_detail/data_models_analytics/data_models_domain/care/raw_adl.py


ADL_ASSESSMENT_CATEGORY_ENUM: str = """
class AdlAssessmentCategoryEnum(StrEnum):
    BATHING = "Bathing"
    CONTINENCE = "Continence"
    DRESSING = "Dressing"
    EATING = "Eating"
    TOILETING = "Toileting"
    TRANSFERRING = "Transferring"
"""

ADL_OBSERVATION_CATEGORY_ENUM: str = """
class AdlObservationCategoryEnum(StrEnum):
    APPETITE_AND_INTAKE = "Appetite and Intake"
    SLEEP_AND_REST = "Sleep and Rest"
    ENGAGEMENT_AND_INTERACTION = "Engagement and Interaction"
    MOOD_AND_AFFECT = "Mood and Affect"
    MOBILITY = "Mobility"
    COMFORT_AND_WELL-BEING = "Comfort and Well-Being"
    ROUTINE_CHANGES = "Routine Changes"
    OTHER = "Other"
"""

ADL_CATEGORY_DEFINITIONS_LOOKUP: str = """
ADL_CATEGORY_DEFINITIONS_LOOKUP = {
    "bathing": "Washing the body, including showering or sponge bathing. Includes getting in and out of the bath or shower, washing, and drying.",
    "continence": "Bladder and bowel control; includes control, frequency of episodes, use of continence aids.",
    "dressing": "Selecting clothes, putting on and removing upper and lower body garments, and manipulating fasteners (buttons, zippers).",
    "eating": "Eating and drinking; includes bringing food to mouth, chewing/swallowing, use of adaptive utensils.",
    "toileting": "Using the toilet; includes transfer to/from toilet, clothing management, hygiene after elimination.",
    "transferring": "Moving between surfaces, for example bed to chair, chair to standing position, wheelchair transfers.",
}
"""

ADL_SCORE_DEFINITIONS_BATHING_LOOKUP: str = """
ADL_SCORE_DEFINITIONS_BATHING_LOOKUP = {
    "0": "Bathes safely without assistance",
    "1": "Supplies or environment prepared",
    "2": "Verbal reminders, staff on standby for safety",
    "3": "Assistance with some body areas",
    "4": "Assistance with most bathing tasks",
    "5": "Staff performs bathing",
    "8": "Activity did not occur",
}
"""

ADL_SCORE_DEFINITIONS_CONTINENCE_LOOKUP: str = """
ADL_SCORE_DEFINITIONS_CONTINENCE_LOOKUP = {
    "0": "Able to control bladder and bowel.",
    "1": "Infrequent episodes",
    "2": "Regular episodes",
    "3": "Insufficient voluntary control",
    "4": "Uses briefs, catheter, or aids",
    "8": "Activity did not occur",
}
"""

ADL_SCORE_DEFINITIONS_DRESSING_LOOKUP: str = """
ADL_SCORE_DEFINITIONS_DRESSING_LOOKUP = {
    "0": "Dresses self completely",
    "1": "Clothes laid out",
    "2": "Verbal cueing only",
    "3": "Help with come garments (e.g. socks)",
    "4": "Help with most clothing",
    "5": "Fully dressed by staff",
    "8": "Activity did not occur",
}
"""

ADL_SCORE_DEFINITIONS_EATING_LOOKUP: str = """
ADL_SCORE_DEFINITIONS_EATING_LOOKUP = {
    "0": "Eats without help",
    "1": "Tray prepared, food cut",
    "2": "Cueing to continue",
    "3": "Occasional physical help",
    "4": "Staff feeds most bites",
    "5": "Fully fed by staff",
    "8": "Activity did not occur",
}
"""

ADL_SCORE_DEFINITIONS_TOILETING_LOOKUP: str = """
ADL_SCORE_DEFINITIONS_TOILETING_LOOKUP = {
    "0": "Completes all steps",
    "2": "Staff on standby for safety",
    "3": "Help with clothing",
    "4": "Help with hygiene and transfer",
    "5": "Staff performs entire task",
    "8": "Activity did not occur",
}
"""

ADL_SCORE_DEFINITIONS_TRANSFERRING_LOOKUP: str = """
ADL_SCORE_DEFINITIONS_TRANSFERRING_LOOKUP = {
    "0": "Transfers safely along",
    "2": "Staff on standby for safety",
    "3": "One-person assist",
    "4": "Two-person assist",
    "5": "Full mechanical lift",
    "8": "Activity did not occur",
}
"""

ADL_OBSERVATION_CATEGORY_DEFINITIONS_LOOKUP: str = """
ADL_OBSERVATION_CATEGORY_DEFINITIONS_LOOKUP = {
    "appetite_and_intake": "Note any observations about eating or drinking, such as amount consumed, interest in food, or changes from usual patterns.",
    "sleep_and_rest": "Note sleep quality or rest patterns, including difficulty falling asleep, frequent waking, or daytime drowsiness.",
    "engagement_and_interaction": "Note participation in activities, social interaction, or changes in engagement with others.",
    "mood_and_affect": "Note observed emotional state or behavior, such as calmness, irritability, or changes from usual demeanor.",
    "mobility": "Note observations related to movement, steadiness, hesitation, or changes in usual mobility.",
    "comfort_and_well-being": "Note signs of comfort or discomfort, such as restlessness, positioning needs, or visible distress.",
    "routine_changes": "Note deviations from the usual routine, including schedule changes, visitors, or altered activities.",
    "other": "Note any additional observations that do not fit the categories above.",
}
"""

ADL_SCORE_LABELS_BATHING_LOOKUP: str = """
ADL_SCORE_LABELS_BATHING_LOOKUP = {
    "0": "Independent",
    "1": "Setup Assistance",
    "2": "Supervision",
    "3": "Limited Assist",
    "4": "Extensive Assist",
    "5": "Dependent",
    "8": "N/A",
}
"""

ADL_SCORE_LABELS_CONTINENCE_LOOKUP: str = """
ADL_SCORE_LABELS_CONTINENCE_LOOKUP = {
    "0": "Continent",
    "1": "Occasional Incontinence",
    "2": "Frequent Incontinence",
    "3": "Incontinent",
    "4": "Managed with Device",
    "8": "N/A",
}
"""

ADL_SCORE_LABELS_DRESSING_LOOKUP: str = """
ADL_SCORE_LABELS_DRESSING_LOOKUP = {
    "0": "Independent",
    "1": "Setup",
    "2": "Supervision",
    "3": "Limited Assist",
    "4": "Extensive Assist",
    "5": "Dependent",
    "8": "N/A",
}
"""

ADL_SCORE_LABELS_EATING_LOOKUP: str = """
ADL_SCORE_LABELS_EATING_LOOKUP = {
    "0": "Independent",
    "1": "Setup",
    "2": "Supervision",
    "3": "Limited Assist",
    "4": "Extensive Assist",
    "5": "Dependent",
    "8": "N/A",
}
"""

ADL_SCORE_LABELS_TOILETING_LOOKUP: str = """
ADL_SCORE_LABELS_TOILETING_LOOKUP = {
    "0": "Independent",
    "2": "Supervision",
    "3": "Limited Assist",
    "4": "Extensive Assist",
    "5": "Dependent",
    "8": "N/A",
}
"""

ADL_SCORE_LABELS_TRANSFERRING_LOOKUP: str = """
ADL_SCORE_LABELS_TRANSFERRING_LOOKUP = {
    "0": "Independent",
    "2": "Supervision",
    "3": "Limited Assist",
    "4": "Extensive Assist",
    "5": "Dependent",
    "8": "N/A",
}
"""

ADL_SCORE_DEFINITION_ENTITY_DTO: str = """
@dataclass(frozen=True)
class AdlScoreDefinitionEntityDTO:
    adl_category: AdlCategoryEnum
    numeric_value: int
    score_label: AdlScoreLabelLookupService
    score_definition: AdlScoreDefinitionLookupService
"""

ADL_ASSESSMENT_RECORD_DTO: str = """
@dataclass(frozen=True)
class AdlAssessmentRecordDTO:
    assessment_id: str
    resident_id: str
    adl_category: AdlCategoryEnum
    adl_category_definitions: AdlCategoryDefinitionLookupService
    score_value: AdlScoreDefinitionEntity
    observed_at_iso: str
    recorded_at_iso: str
    recorded_by_user_id: str
    assessment_note: str | None = None
"""

ADL_OBSERVATION_RECORD_DTO: str = """
@dataclass(frozen=True)
class AdlObservationRecordDTO:
    observation_id: str
    resident_id: str
    category: AdlObservationCategoryEnum
    category_definition: AdlObservationCategoryLookupService
    observation_note: str
    observed_at_iso: str
    recorded_at_iso: str
    recorded_by_user_id: str
"""

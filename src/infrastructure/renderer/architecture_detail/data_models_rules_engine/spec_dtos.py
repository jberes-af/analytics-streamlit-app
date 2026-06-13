# /src/infrastructure/architecture_detail/data_models_analytics/data_models_rules_engine/spec_dtos.py

from src.domain.mobile_app_types import (
    RulesEngineSpec,
)

ADL_ENTRY_RULES_ENGINE = RulesEngineSpec(
    engines=(
        "Clinical Interpretation Engine",
        "Workflow Decision Engine",
    ),
    rules_purpose=(
        "Validate score against scale",
        "Interpret score in context",
        "Trigger downstream workflow signals",
    ),
)

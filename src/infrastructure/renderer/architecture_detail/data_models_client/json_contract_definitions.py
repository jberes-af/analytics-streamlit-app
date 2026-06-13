# # /src/infrastructure/flow_diagram/json_contract_definitions.py


SUBMIT_ADL_ASSESSMENT_REQUEST_JSON: str = """
{
  "adl_code": "bathing",
  "score_value": 3,
  "note": "Needed help",
  "observed_at": "2025-06-23T23:15:00Z"
}
"""

SUBMIT_ADL_ASSESSMENT_RESPONSE_JSON: str = """
{
  "assessment_id": "adl_001",
  "status": "created"
}
"""

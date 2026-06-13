# /src/gui/streamlit/components/node_content_to_diagram_ui_adapter

from dataclasses import asdict
from typing import Any

from src.domain.mobile_app_types import (
    DataObject,
    DataRead,
    DataWrite,
    NavigationRoute,
)
from src.application.flow_diagram.flow_diagram_types import FlowNode


def _data_object_to_ui(dto: DataObject) -> dict[str, Any]:
    return {
        "name": dto.name,
        "description": dto.description,
        "code": dto.code,
        "json_example": dto.json_example,
    }


def _data_read_to_ui(read: DataRead) -> dict[str, Any]:
    return {
        "name": read.name,
        "source_dtos": list(read.source_dtos),
        "output_dto": read.output_dto,
        "description": read.description,
    }


def _data_write_to_ui(write: DataWrite) -> dict[str, Any]:
    return {
        "name": write.name,
        "target_dtos": list(write.target_dtos),
        "description": write.description,
    }


def _navigation_route_to_ui(route: NavigationRoute) -> dict[str, str]:
    return {
        "action": route.action,
        "target_screen_id": route.target_screen_id,
        "condition": route.condition,
        "notes": route.notes,
    }


def _permission_to_ui(permission) -> dict[str, str]:
    return {
        "domain": str(permission.domain.value),
        "action": str(permission.action.value),
    }


def _use_case_to_ui(use_case) -> dict[str, Any]:
    return {
        "id": use_case.use_case_id,
        "name": use_case.name,
        "description": use_case.description,
        "types": [t.value for t in use_case.use_case_types],
        "outcome": use_case.outcome,
        "user_goal": use_case.user_goal,
        "business_goal": use_case.business_goal,
    }


def _workflow_to_ui(workflow) -> dict[str, Any]:
    return {
        "id": workflow.workflow_id,
        "name": workflow.name,
        "description": workflow.description,
        "goal": workflow.goal,
        "trigger": workflow.trigger,
        "success_outcome": workflow.success_outcome,
        "entry_conditions": list(workflow.entry_conditions),
        "exit_conditions": list(workflow.exit_conditions),
        "flow": [
            {
                "sequence": step.sequence,
                "actor": step.actor,
                "action": step.action,
                "system_response": step.system_response,
            }
            for step in workflow.flow
        ],
    }


def flow_node_to_node_info(node: FlowNode) -> dict[str, Any]:
    screen = node.screen_spec
    backend = node.backend_data_model
    client = node.client_contracts
    rules = node.rules_engine

    return {
        "title": node.title,
        "label": node.label,
        "description": node.description,
        "class_name": str(node.class_name.value),

        "screen_images": list(node.screen_images),

        "screen_spec": {
            "screen_id": screen.screen_id,
            "name": screen.name,
            "purpose": screen.purpose,
            "displayed_data": list(screen.displayed_data),
            "user_inputs": list(screen.user_inputs),
            "primary_action": screen.primary_action,
            "secondary_actions": list(screen.secondary_actions),
            "validation_rules": list(screen.validation_rules),
            "navigation_in": list(screen.navigation_in),
            "navigation_out": [
                _navigation_route_to_ui(route)
                for route in screen.navigation_out
            ],
            "states": {
                "empty_state": screen.empty_state,
                "loading_state": screen.loading_state,
                "error_state": screen.error_state,
            },
        },

        "required_permissions": [
            _permission_to_ui(permission)
            for permission in node.required_permissions
        ],

        "use_cases": [
            _use_case_to_ui(use_case)
            for use_case in node.related_use_cases
        ],

        "workflows": [
            _workflow_to_ui(workflow)
            for workflow in node.related_workflows
        ],

        "feature_groups": list(node.feature_groups),

        "client_contracts": {
            "request_dtos": [
                _data_object_to_ui(dto)
                for dto in client.request_dtos
            ],
            "response_dtos": [
                _data_object_to_ui(dto)
                for dto in client.response_dtos
            ],
            "screen_dtos": [
                _data_object_to_ui(dto)
                for dto in client.screen_dtos
            ],
        },

        "backend_data_model": {
            "definition_dtos": [
                _data_object_to_ui(dto)
                for dto in backend.definition_dtos
            ],
            "persistence_dtos": [
                _data_object_to_ui(dto)
                for dto in backend.persistence_dtos
            ],
            "data_reads": [
                _data_read_to_ui(read)
                for read in backend.data_reads
            ],
            "data_writes": [
                _data_write_to_ui(write)
                for write in backend.data_writes
            ],
        },

        "data_models_rules_engine": {
            "engines": list(rules.engines) if rules else [],
            "rules_purpose": list(rules.rules_purpose) if rules else [],
            "output_dtos": [
                _data_object_to_ui(dto)
                for dto in rules.output_dtos
            ] if rules else [],
        },

        "open_questions": list(node.open_questions),
    }

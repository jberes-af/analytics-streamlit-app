# /src/application/flow_diagram/flow_diagram_types.py

from dataclasses import dataclass, field
from enum import Enum

from src.domain.mobile_app_types import (
    BackendDataModel,
    ClientContracts,
    PermissionRequirement,
    RulesEngineSpec,
    ScreenSpec,
    UseCase,
    UserDefinition,
    Workflow,
)


class NodeClassName(str, Enum):
    ACTION = "action"
    FORM = "form"
    PAGE = "page"
    QUEUE = "queue"
    UTILITY = "utility"


"""
SCREEN / FLOW DIAGRAM NODE
"""


@dataclass(frozen=True)
class FlowNode:
    title: str
    label: str
    class_name: NodeClassName

    screen_spec: ScreenSpec | None = field(default_factory=ScreenSpec)
    screen_images: tuple[str, ...] = field(default_factory=tuple)
    # users: tuple[UserDefinition, ...] = field(default_factory=tuple)
    # required_permissions: tuple[PermissionRequirement, ...] = field(default_factory=tuple())
    # primary_actions: tuple[str, ...] = field(default_factory=tuple)

    required_permissions: tuple[PermissionRequirement, ...] = field(default_factory=tuple)

    use_cases: tuple[UseCase, ...] = field(default_factory=tuple)
    workflows: tuple[Workflow, ...] = field(default_factory=tuple)

    # feature_groups: tuple[str, ...] = field(default_factory=tuple)

    client_contracts: ClientContracts  | None  = field(default_factory=ClientContracts)
    backend_data_model: BackendDataModel  | None = field(default_factory=BackendDataModel)
    rules_engine: RulesEngineSpec | None = field(default_factory=RulesEngineSpec)

    # validation_rules: tuple[str, ...] = field(default_factory=tuple)
    open_questions: tuple[str, ...] = field(default_factory=tuple)
    description: str = ""


@dataclass(frozen=True)
class FlowEdge:
    source: str
    target: str
    action_label: str | None = None

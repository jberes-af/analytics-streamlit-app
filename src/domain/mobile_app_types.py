# /src/domain/mobile_app_types.py

from dataclasses import dataclass, field

from src.domain.mobile_app_enums import (
    Role,
    UserResponsibility,

    Action,
    DomainObject,
    Scope,

    UseCaseType,

    WorkflowComplexity,
    Severity,
)

"""
SCREEN
"""


@dataclass(frozen=True)
class NavigationRoute:
    action: str
    target_screen_id: str
    condition: str = ""
    notes: str = ""


@dataclass(frozen=True)
class PermissionRequirement:
    domain: DomainObject
    action: Action


@dataclass(frozen=True)
class ScreenSpec:
    screen_id: str  # "screen.<domain>.<purpose>"
    name: str
    purpose: str

    # --- What is shown
    displayed_data: tuple[str, ...] = field(default_factory=tuple)

    # --- What user can do
    user_inputs: tuple[str, ...] = field(default_factory=tuple)
    primary_action: str = ""
    secondary_actions: tuple[str, ...] = field(default_factory=tuple)

    # --- How screen behaves
    navigation_in: tuple[str, ...] = field(default_factory=tuple)
    navigation_out: tuple[NavigationRoute, ...] = field(default_factory=tuple)

    validation_rules: tuple[str, ...] = field(default_factory=tuple)

    # --- States
    empty_state: str = ""
    loading_state: str = ""
    error_state: str = ""


"""
USER
"""


@dataclass(frozen=True)
class PermissionRule:
    domain: DomainObject
    action: Action
    allowed: bool
    scope: Scope = Scope.ASSIGNED_PATIENT
    notes: str = ""


@dataclass(frozen=True)
class RoleDefinition:
    role: Role
    name: str
    description: str = ""
    responsibilities: tuple[UserResponsibility, ...] = field(default_factory=tuple)
    permissions: tuple[PermissionRule, ...] = field(default_factory=tuple)


# runtime user
@dataclass(frozen=True)
class UserDefinition:
    user_id: str = "firebase_auth_user_id"
    display_name: str = "<user_name>"
    role: Role | None = None
    is_active: bool = True


"""
USE CASE
"""


@dataclass(frozen=True)
class UseCase:
    name: str
    use_case_id: str

    use_case_types: tuple[UseCaseType, ...] = field(default_factory=tuple)
    description: str = ""

    primary_actors: tuple[Role, ...] = field(default_factory=tuple)
    supporting_actors: tuple[Role, ...] = field(default_factory=tuple)

    user_goal: str = ""
    business_goal: str = ""
    outcome: str = ""

    preconditions: tuple[str, ...] = field(default_factory=tuple)
    post_conditions: tuple[str, ...] = field(default_factory=tuple)

    related_workflows: tuple[str, ...] = field(default_factory=tuple)
    related_screens: tuple[str, ...] = field(default_factory=tuple)
    related_data_objects: tuple[str, ...] = field(default_factory=tuple)

    # priority: str = ""
    # status: str = ""
    assumptions: tuple[str, ...] = field(default_factory=tuple)
    open_questions: tuple[str, ...] = field(default_factory=tuple)


"""
WORKFLOWS
"""


@dataclass(frozen=True)
class FlowStep:
    sequence: int
    actor: str
    action: str
    system_response: str = ""


@dataclass(frozen=True)
class SystemBehavior:
    description: str
    component: str = ""
    related_state: str = ""


@dataclass(frozen=True)
class EdgeCase:
    condition: str
    expected_behavior: str
    severity: Severity = Severity.WARNING


@dataclass(frozen=True)
class DataState:
    name: str
    required: bool = True
    description: str = ""


@dataclass(frozen=True)
class AuditRule:
    event_name: str
    required: bool = True
    compliance_relevant: bool = False
    notes: str = ""


@dataclass(frozen=True)
class Workflow:
    workflow_id: str
    name: str
    primary_actor: str
    goal: str
    trigger: str
    entry_conditions: tuple[str, ...]
    exit_conditions: tuple[str, ...]
    success_outcome: str
    complexity: WorkflowComplexity = WorkflowComplexity.L2
    description: str = ""

    flow: tuple[FlowStep, ...] = field(default_factory=tuple)
    system_behaviors: tuple[SystemBehavior, ...] = field(default_factory=tuple)
    edge_cases: tuple[EdgeCase, ...] = field(default_factory=tuple)
    data_state: tuple[DataState, ...] = field(default_factory=tuple)
    audit_rules: tuple[AuditRule, ...] = field(default_factory=tuple)
    open_questions: tuple[str, ...] = field(default_factory=tuple)

    related_use_case: str = ""
    related_screens: tuple[str, ...] = field(default_factory=tuple)
    related_backend_contracts: tuple[str, ...] = field(default_factory=tuple)


"""
DATA MODELS
"""


@dataclass(frozen=True)
class DataObject:
    name: str
    description: str = ""
    code: str = ""
    json_example: str = ""

@dataclass(frozen=True)
class DataRead:
    name: str
    source_dtos: tuple[str, ...] = ()
    output_dto: str = ""
    description: str = ""


@dataclass(frozen=True)
class DataWrite:
    name: str
    target_dtos: tuple[str, ...] = ()
    description: str = ""


@dataclass(frozen=True)
class ClientContracts:
    request_dtos: tuple[DataObject, ...] = ()
    response_dtos: tuple[DataObject, ...] = ()
    screen_dtos: tuple[DataObject, ...] = ()


@dataclass(frozen=True)
class BackendDataModel:
    definition_dtos: tuple[DataObject, ...] = ()
    persistence_dtos: tuple[DataObject, ...] = ()
    data_reads: tuple[DataRead, ...] = ()
    data_writes: tuple[DataWrite, ...] = ()


@dataclass(frozen=True)
class RulesEngineSpec:
    engines: tuple[str, ...] = ()
    rules_purpose: tuple[str, ...] = ()
    output_dtos: tuple[DataObject, ...] = ()

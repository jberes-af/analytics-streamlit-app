# priority_item_diagram_node_definitions

from src.application.flow_diagram.flow_diagram_types import (
    FlowNode,
    NodeClassName,
)

from src.infrastructure.renderer.architecture_detail.data_models_domain.care.priority_item_domain_dtos import (
    CREATE_PRIORITY_ITEM_BACKEND_DTOS,
    PRIORITY_ITEM_DASHBOARD_BACKEND_DTOS,
    PRIORITY_ITEM_RECORD_BACKEND_DTOS,
    UPDATE_PRIORITY_ITEM_BACKEND_DTOS,
)

PRIORITY_ITEMS_NODE = FlowNode(
    title="Priority Items",
    label="Priority Items",
    class_name=NodeClassName.PAGE,
    screen_spec=None,
    screen_images=tuple([
        "care/priority_item/PI01-priority-item-list-01.png"
    ]),

    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=PRIORITY_ITEM_DASHBOARD_BACKEND_DTOS,
    rules_engine=None,
    description="",
)

PRIORITY_ITEM_RECORD_NODE = FlowNode(
    title="Priority Item Record",
    label="Priority Item Record",
    class_name=NodeClassName.PAGE,
    screen_spec=None,
    screen_images=tuple([
        "care/priority_item/PI02-priority-item-record.png"
    ]),

    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=PRIORITY_ITEM_RECORD_BACKEND_DTOS,
    rules_engine=None,
    description="",
)

CREATE_PRIORITY_ITEM_NODE = FlowNode(
    title="Create Priority Item",
    label="Create Priority Item",
    class_name=NodeClassName.FORM,
    screen_spec=None,
    screen_images=tuple([
        "care/priority_item/PI03-create-priority-item-01.png"
    ]),

    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=CREATE_PRIORITY_ITEM_BACKEND_DTOS,
    rules_engine=None,
    description="",
)

UPDATE_PRIORITY_ITEM_NODE = FlowNode(
    title="Update Priority Item",
    label="Update Priority Item",
    class_name=NodeClassName.FORM,
    screen_spec=None,
    screen_images=tuple([
        "care/priority_item/PI03-create-priority-item-01.png"
    ]),
    required_permissions=tuple(),
    use_cases=tuple(),
    workflows=tuple(),
    client_contracts=None,
    backend_data_model=UPDATE_PRIORITY_ITEM_BACKEND_DTOS,
    rules_engine=None,
    description="",
)

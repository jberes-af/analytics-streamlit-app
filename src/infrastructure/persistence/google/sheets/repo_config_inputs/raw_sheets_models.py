# /src/infrastructure/google/sheets/repo_config_inputs/raw_sheets_models.py

from dataclasses import dataclass

"""
TIME HORIZON
"""


@dataclass(frozen=True)
class TimeHorizonRaw:
    start_month: str
    period_duration_months: str


"""
REVENUES
"""


@dataclass(frozen=True)
class SalesSegmentInputsRaw:
    segment_percent_b2b: str
    segment_percent_b2c: str


@dataclass(frozen=True)
class CustomerQuantityRaw:
    month_index: str
    quantity_kits: str
    subscribers_new: str
    subscribers_active_start: str
    subscribers_active_end: str
    subscriber_churn: str


@dataclass(frozen=True)
class PriceInputsRaw:
    kit_price_b2b: str
    subscription_price_b2b: str
    kit_price_b2c: str
    subscription_price_b2c: str


"""
PERSONNEL COST MAPS
"""


@dataclass(frozen=True)
class PersonnelRoleMapRaw:
    role_name: str
    function: str
    cost_account: str
    account: str
    sub_account: str


@dataclass(frozen=True)
class PersonnelCompensationScheduleRaw:
    role_name: str
    month_start: str
    month_end: str
    cost_per_month: str


"""
NON-PERSONNEL COSTS - COST RULES - DYNAMIC 
"""


@dataclass(frozen=True)
class CostRuleRaw:
    cost_name: str
    cost_account: str
    account: str
    sub_account: str
    amount: str
    month_start: str
    month_end: str
    driver_name: str
    driver_factor: str


"""
NON-PERSONNEL COSTS - EXPLICIT COSTS 
"""


@dataclass(frozen=True)
class ExplicitNonPersonnelExpensesRaw:
    month_index: str
    cost_account: str
    account: str
    sub_account: str
    amount: str


"""
PERSONNEL COSTS - COST RULES - DYNAMIC
"""


@dataclass(frozen=True)
class PersonnelDriverRuleRaw:
    role_name: str
    driver_name: str
    units_per_head: str
    month_start: str
    month_end: str
    minimum_headcount: str


"""
PERSONNEL COSTS - EXPLICIT COSTS
"""


@dataclass(frozen=True)
class ExplicitPersonnelHeadcountRaw:
    month_index: str
    role_name: str
    headcount: str


"""
CAPITAL EXPENDITURES: DYNAMIC & EXPLICIT
"""


@dataclass(frozen=True)
class CapExRuleRaw:
    project_name: str
    project_type: str
    project_scope: str
    amount: str
    month_start: str
    month_end: str


@dataclass(frozen=True)
class ExplicitCapExRaw:
    month_index: str
    project_name: str
    project_type: str
    project_scope: str
    amount: str

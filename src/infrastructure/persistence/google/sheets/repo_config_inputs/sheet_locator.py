# /src/infrastructure/persistence/google/sheets/repo_config_inputs/sheet_locator.py

from dataclasses import dataclass


@dataclass(frozen=True)
class GoogleSheetLocator:
    spreadsheet_id: str
    worksheet_name: str
    worksheet_range: str


@dataclass(frozen=True)
class FinancialModelSheetLocators:
    time_horizon: GoogleSheetLocator
    sales_segments: GoogleSheetLocator
    sales_quantities: GoogleSheetLocator
    sales_prices: GoogleSheetLocator

    cogs_cost_rules: GoogleSheetLocator
    cogs_personnel_explicit: GoogleSheetLocator
    cogs_personnel_driver_rules: GoogleSheetLocator

    personnel_roles: GoogleSheetLocator
    personnel_compensation: GoogleSheetLocator

    sales_cost_explicit: GoogleSheetLocator
    sales_cost_rules: GoogleSheetLocator
    sales_personnel_explicit: GoogleSheetLocator
    sales_personnel_driver_rules: GoogleSheetLocator

    general_cost_explicit: GoogleSheetLocator
    general_cost_rules: GoogleSheetLocator
    general_personnel_explicit: GoogleSheetLocator
    general_personnel_driver_rules: GoogleSheetLocator

    capital_projects_driver_rules: GoogleSheetLocator
    capital_projects_explicit: GoogleSheetLocator





# /src/infrastructure/persistence/google/sheets/repo_config_inputs/config_repo_adapter.py

"""
Column-oriented read → parse → map:
sheet values
→ read returns:    list[dict[str, str]]
→ parse returns:   list[RawDTO]
→ map:             domain DTOs

Row-oriented read → parse → map:
sheet values
→ read returns:    list[dict[str, str]]
→ parse step #1:   dict[str, str]
→ parse returns:   RawDTO
→ map:             domain DTO

"""

from dataclasses import dataclass

from src.application.ports.google_sheets_repos.google_sheets_repositories import (
    ConfigInputsRepositoryPort,
)
from src.domain.dto.build_model.assumptions_dto import FinancialModelAssumptionsDTO
from src.infrastructure.persistence.google.sheets.sheets_query_service import (
    GoogleSheetsQueryService,
)
from src.infrastructure.persistence.google.sheets.repo_config_inputs.sheet_locator import (
    GoogleSheetLocator,
    FinancialModelSheetLocators,
)
from src.infrastructure.persistence.google.sheets.repo_config_inputs.raw_sheets_models import (
    CapExRuleRaw,
    CostRuleRaw,
    ExplicitCapExRaw,
    ExplicitPersonnelHeadcountRaw,
    ExplicitNonPersonnelExpensesRaw,
    CustomerQuantityRaw,
    PersonnelCompensationScheduleRaw,
    PersonnelDriverRuleRaw,
    PersonnelRoleMapRaw,
    PriceInputsRaw,
    SalesSegmentInputsRaw,
    TimeHorizonRaw,
)

from src.infrastructure.services.mappers.config_repo_to_domain_mapper import (
    RawSheetToDomainMapper,
)
from src.infrastructure.services.worksheet_parsing_utils import (
    records_to_key_value_map,
    require_key,
    require_value,
)


@dataclass
class ConfigInputsGoogleSheetsRepository(ConfigInputsRepositoryPort):
    query_service: GoogleSheetsQueryService
    locators: FinancialModelSheetLocators
    mapper: RawSheetToDomainMapper

    # _cache: dict[str, list[dict[str, str]]]

    def load_financial_model_assumptions(self) -> FinancialModelAssumptionsDTO:
        """
        Load raw data tables from Google Sheets
        Transform data: raw tables -> raw Sheets DTOs -> domain assumption DTOs
        """
        # --- TIME HORIZON

        rows_time_horizon: list[dict[str, str]] = self._get_table(
            name="time_horizon",
            locator=self.locators.time_horizon,
        )

        # --- REVENUE

        rows_segments: list[dict[str, str]] = self._get_table(
            name="sales_segments",
            locator=self.locators.sales_segments,
        )
        rows_quantities: list[dict[str, str]] = self._get_table(
            name="sales_quantities",
            locator=self.locators.sales_quantities,
        )
        rows_prices = self._get_table(
            name="sales_prices",
            locator=self.locators.sales_prices,
        )

        # --- COST OF GOODS

        rows_cogs_cost_rules = self._get_table(
            name="cogs_cost_rules",
            locator=self.locators.cogs_cost_rules,
        )

        rows_cogs_explicit_personnel = self._get_table(
            name="cogs_personnel_explicit",
            locator=self.locators.cogs_personnel_explicit,
        )
        rows_cogs_personnel_driver_rules = self._get_table(
            name="cogs_personnel_driver_rules",
            locator=self.locators.cogs_personnel_driver_rules,
        )

        # --- SALES EXPENSES

        rows_sales_cost_explicit = self._get_table(
            name="sales_expenses_non_personnel_explicit",
            locator=self.locators.sales_cost_explicit,
        )

        rows_sales_cost_rules = self._get_table(
            name="sales_expenses_non_personnel_cost_rules",
            locator=self.locators.sales_cost_rules,
        )

        rows_sales_explicit_personnel = self._get_table(
            name="sales_expenses_personnel_explicit",
            locator=self.locators.sales_personnel_explicit,
        )
        rows_sales_personnel_driver_rules = self._get_table(
            name="sales_expenses_personnel_driver_rules",
            locator=self.locators.sales_personnel_driver_rules,
        )

        # --- GENERAL EXPENSES

        rows_general_cost_explicit = self._get_table(
            name="general_expenses_non_personnel_explicit",
            locator=self.locators.general_cost_explicit,
        )

        rows_general_cost_rules = self._get_table(
            name="general_expenses_non_personnel_cost_rules",
            locator=self.locators.general_cost_rules,
        )

        rows_general_explicit_personnel = self._get_table(
            name="general_expenses_personnel_explicit",
            locator=self.locators.general_personnel_explicit,
        )
        rows_general_personnel_driver_rules = self._get_table(
            name="general_expenses_personnel_driver_rules",
            locator=self.locators.general_personnel_driver_rules,
        )

        # --- PERSONNEL MAPS

        rows_personnel_roles = self._get_table(
            name="personnel_roles",
            locator=self.locators.personnel_roles,
        )
        rows_personnel_comp = self._get_table(
            name="personnel_compensation",
            locator=self.locators.personnel_compensation,
        )

        # --- CAPITAL EXPENDITURES

        rows_capex_rules = self._get_table(
            name="capital_projects_dynamic",
            locator=self.locators.capital_projects_driver_rules,
        )
        rows_capex_explicit = self._get_table(
            name="capital_projects_explicit",
            locator=self.locators.capital_projects_explicit,
        )

        """
        PARSER CALLS
        """

        raw_time_horizon: TimeHorizonRaw = self._parse_table_time_horizon(
            rows=rows_time_horizon)

        # --- REVENUE

        raw_segments: SalesSegmentInputsRaw = self._parse_table_segments(
            rows=rows_segments)

        raw_quantities: list[CustomerQuantityRaw] = self._parse_table_volumes(
            rows=rows_quantities)

        raw_prices: PriceInputsRaw = self._parse_table_prices(
            rows=rows_prices)

        # --- PERSONNEL MAPS

        raw_role_map: list[PersonnelRoleMapRaw] = (
            self._parse_table_personnel_roles(
                rows=rows_personnel_roles))

        raw_compensation: list[PersonnelCompensationScheduleRaw] = (
            self._parse_table_personnel_compensation(
                rows=rows_personnel_comp))

        # --- COST OF GOODS

        xformed_cogs = _explicit_personnel_pre_parser(
            rows_cogs_explicit_personnel)

        raw_cogs_personnel_explicit: list[ExplicitPersonnelHeadcountRaw] = (
            self._parse_table_explicit_personnel(
                # rows=rows_cogs_explicit_personnel))
                rows=xformed_cogs))

        raw_cogs_personnel_driver_rule: list[PersonnelDriverRuleRaw] = (
            self._parse_table_personnel_driver_rules(
                rows=rows_cogs_personnel_driver_rules))

        raw_cogs_cost_rule: list[CostRuleRaw] = self._parse_table_cost_rules(
            rows=rows_cogs_cost_rules)

        # --- SALES EXPENSES

        xformed_sales = _explicit_personnel_pre_parser(
            rows_sales_explicit_personnel)

        raw_sales_personnel_explicit: list[ExplicitPersonnelHeadcountRaw] = (
            self._parse_table_explicit_personnel(
                rows=xformed_sales))

        raw_sales_personnel_driver_rule: list[PersonnelDriverRuleRaw] = (
            self._parse_table_personnel_driver_rules(
                rows=rows_sales_personnel_driver_rules))

        raw_sales_expenses_explicit: list[ExplicitNonPersonnelExpensesRaw] = (
            self._parse_table_explicit_non_personnel(
                rows=rows_sales_cost_explicit))

        raw_sales_cost_rule: list[CostRuleRaw] = self._parse_table_cost_rules(
            rows=rows_sales_cost_rules)

        # --- GENERAL EXPENSES

        xformed_general = _explicit_personnel_pre_parser(
            rows_general_explicit_personnel)

        raw_general_personnel_explicit: list[ExplicitPersonnelHeadcountRaw] = (
            self._parse_table_explicit_personnel(
                rows=xformed_general))

        raw_general_personnel_driver_rule: list[PersonnelDriverRuleRaw] = (
            self._parse_table_personnel_driver_rules(
                rows=rows_general_personnel_driver_rules))

        raw_general_expenses_explicit: list[ExplicitNonPersonnelExpensesRaw] = (
            self._parse_table_explicit_non_personnel(
                rows=rows_general_cost_explicit))

        raw_general_cost_rule: list[CostRuleRaw] = self._parse_table_cost_rules(
            rows=rows_general_cost_rules)

        # --- CAPITAL EXPENDITURES

        capex_rule_raw_items: list[CapExRuleRaw] = (
            self._parse_table_capex_driver_rules(
                rows=rows_capex_rules))
        capex_explicit_raw_items: list[ExplicitCapExRaw] = (
            self._parse_table_explicit_capex(
                rows=rows_capex_explicit))

        # --- RETURN

        return self.mapper.to_financial_model_assumptions(
            time_horizon_raw=raw_time_horizon,
            segments_raw=raw_segments,
            quantity_raw_items=raw_quantities,
            price_raw=raw_prices,

            cogs_cost_rule_raw_items=raw_cogs_cost_rule,
            cogs_explicit_personnel_raw_items=raw_cogs_personnel_explicit,
            cogs_personnel_driver_rule_raw_items=raw_cogs_personnel_driver_rule,

            sales_cost_rule_raw_items=raw_sales_cost_rule,
            sales_costs_explicit_raw_items=raw_sales_expenses_explicit,
            sales_explicit_personnel_raw_items=raw_sales_personnel_explicit,
            sales_personnel_driver_rule_raw_items=raw_sales_personnel_driver_rule,

            general_cost_rule_raw_items=raw_general_cost_rule,
            general_costs_explicit_raw_items=raw_general_expenses_explicit,
            general_explicit_personnel_raw_items=raw_general_personnel_explicit,
            general_personnel_driver_rule_raw_items=raw_general_personnel_driver_rule,

            role_map_raw_items=raw_role_map,
            compensation_raw_items=raw_compensation,

            capex_rule_raw_items=capex_rule_raw_items,
            capex_explicit_raw_items=capex_explicit_raw_items,
        )

    def _get_table(
            self,
            *,
            name: str,
            locator: GoogleSheetLocator,
    ) -> list[dict[str, str]]:
        spreadsheet_id: str = locator.spreadsheet_id
        if not spreadsheet_id:
            raise KeyError(f"No spreadsheet_id configured for worksheet '{name}'.")

        tab_name: str = locator.worksheet_name
        worksheet_range: str = locator.worksheet_range
        range_a1: str = f"{tab_name}!{worksheet_range}"

        values: list[dict[str, str]] = self.query_service.read_values(
            spreadsheet_id=spreadsheet_id,
            range_a1=range_a1,
        )

        return values

    """
    PARSE COLUMN-ORIENTED & ROW-ORIENTED TABLES
    """

    @staticmethod
    def _parse_table_time_horizon(
            *,
            rows: list[dict[str, str]],
    ) -> TimeHorizonRaw:
        key_values: dict[str, str] = records_to_key_value_map(
            rows,
            key_field="category",
            value_field="value",
        )

        return TimeHorizonRaw(
            start_month=require_value(key_values, "start_month"),
            period_duration_months=require_value(
                key_values,
                "period_duration_months",
            ),
        )

    @staticmethod
    def _parse_table_segments(
            *,
            rows: list[dict[str, str]],
    ) -> SalesSegmentInputsRaw:
        key_values: dict[str, str] = records_to_key_value_map(
            rows,
            key_field="category",
            value_field="value",
        )

        return SalesSegmentInputsRaw(
            segment_percent_b2b=require_value(
                key_values,
                "segment_percent_b2b",
            ),
            segment_percent_b2c=require_value(
                key_values,
                "segment_percent_b2c",
            ),
        )

    @staticmethod
    def _parse_table_volumes(
            *,
            rows: list[dict[str, str]],
    ) -> list[CustomerQuantityRaw]:
        return [
            CustomerQuantityRaw(
                month_index=require_key(record=row, key="month_index"),
                quantity_kits=require_key(record=row, key="quantity_kits"),
                subscribers_new=require_key(record=row, key="subscribers_new"),
                subscribers_active_start=require_key(record=row, key="subscribers_active_start"),
                subscribers_active_end=require_key(record=row, key="subscribers_active_end"),
                subscriber_churn=require_key(record=row, key="subscriber_churn"),
            )
            for row in rows
        ]

    @staticmethod
    def _parse_table_prices(
            *,
            rows: list[dict[str, str]],
    ) -> PriceInputsRaw:
        key_values: dict[str, str] = records_to_key_value_map(
            rows,
            key_field="category",
            value_field="value",
        )

        return PriceInputsRaw(
            kit_price_b2b=require_value(key_values, "kit_price_b2b"),
            subscription_price_b2b=require_value(
                key_values,
                "subscription_price_b2b",
            ),
            kit_price_b2c=require_value(key_values, "kit_price_b2c"),
            subscription_price_b2c=require_value(
                key_values,
                "subscription_price_b2c",
            ),
        )

    @staticmethod
    def _parse_table_cost_rules(
            *,
            rows: list[dict[str, str]],
    ) -> list[CostRuleRaw]:
        return [
            CostRuleRaw(
                cost_name=require_key(record=row, key="cost_name"),
                cost_account=require_key(record=row, key="cost_account"),
                account=require_key(record=row, key="account"),
                sub_account=require_key(record=row, key="sub_account"),
                amount=require_key(record=row, key="amount"),
                month_start=require_key(record=row, key="month_start"),
                month_end=require_key(record=row, key="month_end"),
                driver_name=str(row.get("driver_name", "")).strip(),
                driver_factor=require_key(record=row, key="driver_factor"),
            )
            for row in rows
        ]

    @staticmethod
    def _parse_table_personnel_roles(
            *,
            rows: list[dict[str, str]],
    ) -> list[PersonnelRoleMapRaw]:
        return [
            PersonnelRoleMapRaw(
                role_name=require_key(record=row, key="role_name"),
                function=require_key(record=row, key="function"),
                cost_account=require_key(record=row, key="cost_account"),
                account=require_key(record=row, key="account"),
                sub_account=require_key(record=row, key="sub_account"),
            )
            for row in rows
        ]

    @staticmethod
    def _parse_table_personnel_compensation(
            *,
            rows: list[dict[str, str]],
    ) -> list[PersonnelCompensationScheduleRaw]:
        return [
            PersonnelCompensationScheduleRaw(
                role_name=require_key(record=row, key="role_name"),
                month_start=require_key(record=row, key="month_start"),
                month_end=require_key(record=row, key="month_end"),
                cost_per_month=require_key(record=row, key="cost_per_month"),
            )
            for row in rows
        ]

    @staticmethod
    def _parse_table_explicit_personnel(
            *,
            rows: list[dict[str, str]],
    ) -> list[ExplicitPersonnelHeadcountRaw]:
        return [
            ExplicitPersonnelHeadcountRaw(
                month_index=require_key(record=row, key="month_index"),
                role_name=require_key(record=row, key="role_name"),
                headcount=require_key(record=row, key="headcount"),
            )
            for row in rows
        ]

    @staticmethod
    def _parse_table_explicit_non_personnel(
            *,
            rows: list[dict[str, str]],
    ) -> list[ExplicitNonPersonnelExpensesRaw]:
        return [
            ExplicitNonPersonnelExpensesRaw(
                month_index=require_key(record=row, key="month_index"),
                cost_account=require_key(record=row, key="cost_account"),
                account=require_key(record=row, key="account"),
                sub_account=require_key(record=row, key="sub_account"),
                amount=require_key(record=row, key="amount"),
            )
            for row in rows
        ]

    @staticmethod
    def _parse_table_personnel_driver_rules(
            *,
            rows: list[dict[str, str]],
    ) -> list[PersonnelDriverRuleRaw]:
        return [
            PersonnelDriverRuleRaw(
                role_name=require_key(record=row, key="role_name"),
                driver_name=require_key(record=row, key="driver_name"),
                units_per_head=require_key(record=row, key="units_per_head"),
                month_start=require_key(record=row, key="month_start"),
                month_end=require_key(record=row, key="month_end"),
                minimum_headcount=require_key(record=row, key="minimum_headcount"),
            )
            for row in rows
        ]

    @staticmethod
    def _parse_table_explicit_capex(
            *,
            rows: list[dict[str, str]],
    ) -> list[ExplicitCapExRaw]:

        return [
            ExplicitCapExRaw(
                month_index=require_key(record=row, key="month_index"),
                project_name=require_key(record=row, key="project_name"),
                project_type=require_key(record=row, key="project_type"),
                project_scope=require_key(record=row, key="project_scope"),
                amount=require_key(record=row, key="amount"),
            )
            for row in rows
        ]

    @staticmethod
    def _parse_table_capex_driver_rules(
            *,
            rows: list[dict[str, str]],
    ) -> list[CapExRuleRaw]:
        return [
            CapExRuleRaw(
                project_name=require_key(record=row, key="project_name"),
                project_type=require_key(record=row, key="project_type"),
                project_scope=require_key(record=row, key="project_scope"),
                amount=require_key(record=row, key="amount"),
                month_start=require_key(record=row, key="month_start"),
                month_end=require_key(record=row, key="month_end"),
            )
            for row in rows
        ]


def _explicit_personnel_pre_parser(
        rows: list[dict[str, str]],
) -> list[dict[str, str]]:
    """
    Convert:
      [{'month_index': '1', 'Production Lead': '1', 'Production Technician': '2'}, ...]
    To:
      [{'month_index': '1', 'role_name': 'Production Lead', 'headcount': '1'},
       {'month_index': '1', 'role_name': 'Production Technician', 'headcount': '2'}, ...]
    """

    xformed: list[dict[str, str]] = []

    for d in rows:

        mi = d["month_index"]

        for k, v in d.items():
            d2: dict[str, str] = {}

            if k != "month_index":
                d2["role_name"] = k
                d2["headcount"] = v
                d2["month_index"] = mi
                xformed.append(d2)

    return xformed

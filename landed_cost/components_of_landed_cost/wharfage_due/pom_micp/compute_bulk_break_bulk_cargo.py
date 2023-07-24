import sys

from customs_tax import WDBulkBreakBulkCargoImport, WDBulkBreakBulkCargoExport
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class WDBulkBreakBulkCargo:
    def __init__(self, type_of_ton: float, total_metric_or_revenue_tons: float) -> None:
        self.type_of_ton = type_of_ton
        self.total_metric_or_revenue_tons = total_metric_or_revenue_tons

    def get_bulk_break_bulk_cargo_values(self) -> tuple[float, float]:
        self.type_of_ton = ErrorandInput.get_input(prompt_var.prompt_type_of_ton)
        self.total_metric_or_revenue_tons = ErrorandInput.get_input(prompt_var.prompt_total_metric_or_revenue_tons)
        return self.type_of_ton, self.total_metric_or_revenue_tons


class WDComputeBulkBreakBulkCargoImport(WDBulkBreakBulkCargo):
    def __init__(self, type_of_ton, total_metric_or_revenue_tons) -> None:
        super().__init__(type_of_ton, total_metric_or_revenue_tons)

    def get_bulk_break_bulk_cargo_import_values(self) -> tuple[float, float]:
        sys.stdout.write(prompt_var.prompt_lcl_import_wd_intro)
        return self.get_bulk_break_bulk_cargo_values()

    def compute_bulk_break_bulk_cargo_import(self) -> None:
        values = self.get_bulk_break_bulk_cargo_import_values()
        total_arrastre_charge = WDBulkBreakBulkCargoImport(*values)
        total_arrastre_charge = total_arrastre_charge.calculate_lcl_import()
        sys.stdout.write(f'Total Wharfage Due: P{total_arrastre_charge}\n')
        return


class WDComputeBulkBreakBulkCargoExport(WDBulkBreakBulkCargo):
    def __init__(self, type_of_ton, total_metric_or_revenue_tons) -> None:
        super().__init__(type_of_ton, total_metric_or_revenue_tons)

    def get_bulk_break_bulk_cargo_export_values(self) -> tuple[float, float]:
        sys.stdout.write(prompt_var.prompt_lcl_import_wd_intro)
        return self.get_bulk_break_bulk_cargo_values()

    def compute_bulk_break_bulk_cargo_export(self) -> None:
        values = self.get_bulk_break_bulk_cargo_export_values()
        total_arrastre_charge = WDBulkBreakBulkCargoExport(*values)
        total_arrastre_charge = total_arrastre_charge.calculate_lcl_export()
        sys.stdout.write(f'Total Wharfage Due: P{total_arrastre_charge}\n')
        return

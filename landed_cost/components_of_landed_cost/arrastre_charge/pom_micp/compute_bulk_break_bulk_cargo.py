import sys

from customs_tax import ACBulkBreakBulkCargoImport, ACBulkBreakBulkCargoExport
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class ACBulkBreakBulkCargo:
    def __init__(self, type_of_cargo: float, total_metric_or_revenue_tons: float) -> None:
        self.type_of_cargo = type_of_cargo
        self.total_metric_or_revenue_tons = total_metric_or_revenue_tons

    def get_bulk_break_bulk_cargo_values(self) -> tuple[float, float]:
        self.type_of_cargo = ErrorandInput.get_input(prompt_var.prompt_type_of_cargo)
        self.total_metric_or_revenue_tons = ErrorandInput.get_input(prompt_var.prompt_total_metric_or_revenue_tons)
        return self.type_of_cargo, self.total_metric_or_revenue_tons


class ACComputeBulkBreakBulkCargoImport(ACBulkBreakBulkCargo):
    def __init__(self, type_of_cargo: float, total_metric_or_revenue_tons: float) -> None:
        super().__init__(type_of_cargo, total_metric_or_revenue_tons)

    def get_bulk_break_bulk_cargo_import_values(self) -> tuple[float, float]:
        sys.stdout.write(prompt_var.prompt_lcl_intro_ac_intro)
        return self.get_bulk_break_bulk_cargo_values()

    def compute_bulk_break_bulk_cargo_import(self) -> None:
        values = self.get_bulk_break_bulk_cargo_import_values()
        total_arrastre_charge = ACBulkBreakBulkCargoImport(*values)
        total_arrastre_charge = total_arrastre_charge.calculate_bulk_break_bulk_cargo_import()
        sys.stdout.write(f'Total Arrastre Charge: P{total_arrastre_charge}\n')
        return


class ACComputeBulkBreakBulkCargoExport(ACBulkBreakBulkCargo):
    def __init__(self, type_of_cargo: float, total_metric_or_revenue_tons: float) -> None:
        super().__init__(type_of_cargo, total_metric_or_revenue_tons)

    def get_bulk_break_bulk_cargo_export_values(self) -> tuple[float, float]:
        sys.stdout.write(prompt_var.prompt_lcl_intro_ac_intro)
        return self.get_bulk_break_bulk_cargo_values()

    def compute_bulk_break_bulk_cargo_export(self) -> None:
        values = self.get_bulk_break_bulk_cargo_export_values()
        total_arrastre_charge = ACBulkBreakBulkCargoExport(*values)
        total_arrastre_charge = total_arrastre_charge.calculate_bulk_break_bulk_cargo_export()
        sys.stdout.write(f'Total Arrastre Charge: P{total_arrastre_charge}\n')
        return

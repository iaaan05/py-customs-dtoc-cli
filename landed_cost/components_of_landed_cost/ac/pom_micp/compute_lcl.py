import sys

from customs_dtoc import ACBulkBreakBulkCargoImport, ACBulkBreakBulkCargoExport
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class ACBulkBreakBulkCargo:
    def __init__(self, type_of_cargo: float, total_mt_or_rt: float) -> None:
        self.type_of_cargo = type_of_cargo
        self.total_mt_or_rt = total_mt_or_rt

    def get_lcl_values(self) -> tuple[float, float]:
        self.type_of_cargo = ErrorandInput.get_input(prompt_var.prompt_type_of_cargo)
        self.total_mt_or_rt = ErrorandInput.get_input(prompt_var.prompt_total_mt_or_rt)
        return self.type_of_cargo, self.total_mt_or_rt


class ACComputeLCLImport(ACBulkBreakBulkCargo):
    def get_lcl_import_values(self) -> tuple[float, float]:
        sys.stdout.write(prompt_var.prompt_ac_lcl_intro)
        return self.get_lcl_values()

    def compute_lcl_import(self) -> None:
        values = self.get_lcl_import_values()
        total_ac = ACBulkBreakBulkCargoImport(*values)
        total_ac = total_ac.calculate_lcl_import()
        sys.stdout.write(f'Total Arrastre Charge: P{total_ac}\n')
        return


class ACComputeLCLExport(ACBulkBreakBulkCargo):
    def get_lcl_export_values(self) -> tuple[float, float]:
        sys.stdout.write(prompt_var.prompt_ac_lcl_intro)
        return self.get_lcl_values()

    def compute_lcl_export(self) -> None:
        values = self.get_lcl_export_values()
        total_ac = ACBulkBreakBulkCargoExport(*values)
        total_ac = total_ac.calculate_lcl_export()
        sys.stdout.write(f'Total Arrastre Charge: P{total_ac}\n')
        return

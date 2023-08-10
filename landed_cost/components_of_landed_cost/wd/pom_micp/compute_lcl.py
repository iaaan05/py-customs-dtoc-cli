import sys

from customs_dtoc import WDBulkBreakBulkCargoImport, WDBulkBreakBulkCargoExport
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class WDBulkBreakBulkCargo:
    def __init__(self, type_of_ton: float, total_mt_or_rt: float) -> None:
        self.type_of_ton = type_of_ton
        self.total_mt_or_rt = total_mt_or_rt

    def get_lcl_values(self) -> tuple[float, float]:
        self.type_of_ton = ErrorandInput.get_input(prompt_var.prompt_type_of_ton)
        self.total_mt_or_rt = ErrorandInput.get_input(prompt_var.prompt_total_mt_or_rt)
        return self.type_of_ton, self.total_mt_or_rt


class WDComputeLCLImport(WDBulkBreakBulkCargo):
    def get_lcl_import_values(self) -> tuple[float, float]:
        sys.stdout.write(prompt_var.prompt_wd_lcl_import_intro)
        return self.get_lcl_values()

    def compute_lcl_import(self) -> None:
        values = self.get_lcl_import_values()
        total_wd = WDBulkBreakBulkCargoImport(*values)
        total_wd = total_wd.calculate_lcl_import()
        sys.stdout.write(f'Total Wharfage Due: P{total_wd}\n')
        return


class WDComputeLCLExport(WDBulkBreakBulkCargo):
    def get_lcl_export_values(self) -> tuple[float, float]:
        sys.stdout.write(prompt_var.prompt_wd_lcl_import_intro)
        return self.get_lcl_values()

    def compute_lcl_export(self) -> None:
        values = self.get_lcl_export_values()
        total_wd = WDBulkBreakBulkCargoExport(*values)
        total_wd = total_wd.calculate_lcl_export()
        sys.stdout.write(f'Total Wharfage Due: P{total_wd}\n')
        return

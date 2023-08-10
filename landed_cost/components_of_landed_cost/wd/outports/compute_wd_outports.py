import sys

from customs_dtoc import WDOutportsViaShipside, WDOutportsViaPierside
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class WharfageDueOutports:
    def __init__(self, total_mt: float) -> None:
        self.total_mt = total_mt

    def get_wd_values(self) -> float:
        self.total_mt = ErrorandInput.get_input(prompt_var.prompt_mt)
        return self.total_mt


class ComputeWDViaShipside(WharfageDueOutports):
    def get_wd_via_shipside_values(self) -> float:
        sys.stdout.write(prompt_var.prompt_wd_shipside)
        return self.get_wd_values()

    def compute_wd_due_via_shipside(self) -> None:
        values = self.get_wd_via_shipside_values()
        total_wd = WDOutportsViaShipside(values)
        total_wd = total_wd.calculate_wd_outport_via_shipside()
        sys.stdout.write(f'Total Wharfage Due: P{total_wd}\n')
        return


class ComputeWDViaPierside(WharfageDueOutports):
    def get_wd_via_pierside_values(self) -> float:
        sys.stdout.write(prompt_var.prompt_wd_pierside)
        return self.get_wd_values()

    def compute_wd_due_via_pierside(self) -> None:
        values = self.get_wd_via_pierside_values()
        total_wd = WDOutportsViaPierside(values)
        total_wd = total_wd.calculate_wd_outport_via_pierside()
        sys.stdout.write(f'Total Wharfage Due: P{total_wd}\n')
        return

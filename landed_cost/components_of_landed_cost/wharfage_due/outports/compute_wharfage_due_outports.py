import sys

from customs_tax import WharfageDueOutportsViaShipside, WharfageDueOutportsViaPierside
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class WharfageDueOutports:
    def __init__(self, total_metric_ton: float) -> None:
        self.total_metric_ton = total_metric_ton

    def get_wharfage_due_values(self) -> float:
        self.total_metric_ton = ErrorandInput.get_input(prompt_var.prompt_metric_ton)
        return self.total_metric_ton


class ComputeWharfageDueViaShipside(WharfageDueOutports):
    def __init__(self, total_metric_ton) -> None:
        super().__init__(total_metric_ton)

    def get_wharfage_due_via_shipside_values(self) -> float:
        sys.stdout.write(prompt_var.prompt_wd_shipside)
        return self.get_wharfage_due_values()

    def compute_total_wharfage_due_via_shipside(self) -> None:
        values = self.get_wharfage_due_via_shipside_values()
        total_wharfage_due_via_shipside = WharfageDueOutportsViaShipside(values)
        total_wharfage_due_via_shipside = total_wharfage_due_via_shipside.\
            calculate_wharfage_due_outport_via_shipside()
        sys.stdout.write(f'Total Wharfage Due: P{total_wharfage_due_via_shipside}\n')
        return


class ComputeWharfageDueViaPierside(WharfageDueOutports):
    def __init__(self, total_metric_ton) -> None:
        super().__init__(total_metric_ton)

    def get_wharfage_due_via_pierside_values(self) -> float:
        sys.stdout.write(prompt_var.prompt_wd_pierside)
        return self.get_wharfage_due_values()

    def compute_total_wharfage_due_via_pierside(self) -> None:
        values = self.get_wharfage_due_via_pierside_values()
        total_wharfage_due_via_pierside = WharfageDueOutportsViaPierside(values)
        total_wharfage_due_via_pierside = total_wharfage_due_via_pierside.\
            calculate_wharfage_due_outport_via_pierside()
        sys.stdout.write(f'Total Wharfage Due: P{total_wharfage_due_via_pierside}\n')
        return

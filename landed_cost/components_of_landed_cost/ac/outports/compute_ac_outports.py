import sys

from customs_dtoc import ACOutportsViaShipside, ACOutportsViaPierside
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class ArrastreChargeOutports:
    def __init__(self, total_mt: float) -> None:
        self.total_mt = total_mt

    def get_ac_values(self) -> float:
        self.total_mt = ErrorandInput.get_input(prompt_var.prompt_mt)
        return self.total_mt


class ComputeACViaShipside(ArrastreChargeOutports):
    def get_ac_via_values(self) -> float:
        sys.stdout.write(prompt_var.prompt_ac_shipside)
        return self.get_ac_values()

    def compute_ac_via_shipside(self) -> None:
        values = self.get_ac_via_values()
        total_ac = ACOutportsViaShipside(values)
        total_ac = total_ac.calculate_ac_outport_via_shipside()
        sys.stdout.write(f'Total Arrastre Charge: P{total_ac}\n')
        return


class ComputeACViaPierside(ArrastreChargeOutports):
    def get_ac_via_values(self) -> float:
        sys.stdout.write(prompt_var.prompt_ac_pierside)
        return self.get_ac_values()

    def compute_ac_via_pierside(self) -> None:
        values = self.get_ac_via_values()
        total_ac = ACOutportsViaPierside(values)
        total_ac = total_ac.calculate_ac_outport_via_pierside()
        sys.stdout.write(f'Total Arrastre Charge: P{total_ac}\n')
        return

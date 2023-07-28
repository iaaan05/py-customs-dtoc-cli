import sys

from customs_tax import ArrastreChargeOutportsViaShipside, ArrastreChargeOutportsViaPierside
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class ArrastreChargeOutports:
    def __init__(self, total_metric_ton: float) -> None:
        self.total_metric_ton = total_metric_ton

    def get_arrastre_charge_values(self) -> float:
        self.total_metric_ton = ErrorandInput.get_input(prompt_var.prompt_metric_ton)
        return self.total_metric_ton


class ComputeArrastreChargeViaShipside(ArrastreChargeOutports):
    def __init__(self, total_metric_ton) -> None:
        super().__init__(total_metric_ton)

    def get_arrastre_charge_via_shipside_values(self) -> float:
        sys.stdout.write(prompt_var.prompt_ac_shipside)
        return self.get_arrastre_charge_values()

    def compute_total_arrastre_charge_via_shipside(self) -> None:
        values = self.get_arrastre_charge_via_shipside_values()
        total_arrastre_charge_via_shipside = ArrastreChargeOutportsViaShipside(values)
        total_arrastre_charge_via_shipside = total_arrastre_charge_via_shipside. \
            calculate_arrastre_charge_outport_via_shipside()
        sys.stdout.write(f'Total Arrastre Charge: P{total_arrastre_charge_via_shipside}\n')
        return


class ComputeArrastreChargeViaPierside(ArrastreChargeOutports):
    def __init__(self, total_metric_ton) -> None:
        super().__init__(total_metric_ton)

    def get_arrastre_charge_via_pierside_values(self) -> float:
        sys.stdout.write(prompt_var.prompt_ac_pierside)
        return self.get_arrastre_charge_values()

    def compute_total_arrastre_charge_via_pierside(self) -> None:
        values = self.get_arrastre_charge_via_pierside_values()
        total_arrastre_charge_via_pierside = ArrastreChargeOutportsViaPierside(values)
        total_arrastre_charge_via_pierside = total_arrastre_charge_via_pierside. \
            calculate_arrastre_charge_outport_via_pierside()
        sys.stdout.write(f'Total Arrastre Charge: P{total_arrastre_charge_via_pierside}\n')
        return

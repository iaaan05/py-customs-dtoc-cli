import sys

from utils.error_handling_and_input_validation import ErrorandInput
from customs_dtoc import VatExciseTax, VatNonExciseTax
from utils import prompt_var


class ValueAddedTax:
    def __init__(self, landed_cost: float) -> None:
        self.landed_cost = landed_cost


class ComputeVATExciseTax(ValueAddedTax):
    def __init__(self, landed_cost: float) -> None:
        super().__init__(landed_cost)
        self.excise_tax = float

    def get_vat_values(self) -> tuple[float, float]:
        sys.stdout.write(prompt_var.prompt_vat_et)
        self.landed_cost = ErrorandInput.get_input(prompt_var.prompt_total_lc)
        self.excise_tax = ErrorandInput.get_input(prompt_var.prompt_excise_tax)
        return self.landed_cost, self.excise_tax

    def compute_vat(self) -> None:
        values = self.get_vat_values()
        total_vat = VatExciseTax(*values)
        total_vat = total_vat.calculate_vat_with_et()
        sys.stdout.write(f'Total Value-Added Tax: P{total_vat}\n')
        return


class ComputeVATNonExciseTax(ValueAddedTax):
    def __init__(self, landed_cost: float) -> None:
        super().__init__(landed_cost)
        self.landed_cost = landed_cost

    def get_vat_non_excise_tax_values(self) -> float:
        sys.stdout.write(prompt_var.prompt_vat_non_et)
        self.landed_cost = ErrorandInput.get_input(prompt_var.prompt_total_lc)
        return self.landed_cost

    def compute_vat_non_excise_tax(self) -> None:
        values = self.get_vat_non_excise_tax_values()
        total_vat = VatNonExciseTax(values)
        total_vat = total_vat.calculate_vat_non_excise_tax()
        sys.stdout.write(f'Total Value-Added Tax: P{total_vat}\n')
        return

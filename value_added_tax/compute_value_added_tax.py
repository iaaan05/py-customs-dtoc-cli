import sys

from customs_tax import VatExciseTax, VatNonExciseTax
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class ValueAddedTax:
    def __init__(self, landed_cost: float) -> None:
        self.landed_cost = landed_cost


class ComputeValueAddedTaxExciseTax(ValueAddedTax):
    def __init__(self, landed_cost: float) -> None:
        super().__init__(landed_cost)
        self.excise_tax = float

    def get_value_added_tax_values(self) -> tuple[float, float]:
        sys.stdout.write(prompt_var.prompt_vat_et)
        self.landed_cost = ErrorandInput.get_input(prompt_var.prompt_total_landed_cost)
        self.excise_tax = ErrorandInput.get_input(prompt_var.prompt_excise_tax)
        return self.landed_cost, self.excise_tax

    def compute_value_added_tax(self) -> None:
        values = self.get_value_added_tax_values()
        total_value_added_tax = VatExciseTax(*values)
        total_value_added_tax = total_value_added_tax.calculate_vat()
        sys.stdout.write(f'Total Value-Added Tax: P{total_value_added_tax}\n')
        return


class ComputeValueAddedTaxNonExciseTax(ValueAddedTax):
    def __init__(self, landed_cost: float) -> None:
        super().__init__(landed_cost)
        self.landed_cost = landed_cost

    def get_value_added_tax_non_excise_tax_values(self) -> float:
        sys.stdout.write(prompt_var.prompt_vat_non_et)
        self.landed_cost = ErrorandInput.get_input(prompt_var.prompt_total_landed_cost)
        return self.landed_cost

    def compute_value_added_tax_non_excise_tax(self) -> None:
        values = self.get_value_added_tax_non_excise_tax_values()
        total_value_added_tax = VatNonExciseTax(values)
        total_value_added_tax = total_value_added_tax.calculate_vat_non_excise_tax()
        sys.stdout.write(f'Total Value-Added Tax: P{total_value_added_tax}\n')
        return

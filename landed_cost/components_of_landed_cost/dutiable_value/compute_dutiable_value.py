import sys

from utils.error_handling_and_input_validation import ErrorandInput
from customs_tax import DutiableValueBySea, DutiableValueByAir
from utils import prompt_var


class DutiableValue:
    def __init__(self, dutiable_insurance: float, dutiable_freight: float, rate_of_exchange: float):
        self.dutiable_insurance = dutiable_insurance
        self.dutiable_freight = dutiable_freight
        self.rate_of_exchange = rate_of_exchange


class ComputeDutiableValueBySea(DutiableValue):
    def __init__(self, dutiable_insurance: float, dutiable_freight: float, rate_of_exchange: float) -> None:
        super().__init__(dutiable_insurance, dutiable_freight, rate_of_exchange)
        self.freight_on_board = float

    def get_dutiable_value_by_sea_values(self):
        sys.stdout.write(prompt_var.prompt_dv_sea)
        self.freight_on_board = ErrorandInput.get_input(prompt_var.prompt_total_fob)
        self.dutiable_insurance = ErrorandInput.get_input(prompt_var.prompt_dutiable_insurance)
        self.dutiable_freight = ErrorandInput.get_input(prompt_var.prompt_dutiable_freight)
        self.rate_of_exchange = ErrorandInput.get_input(prompt_var.prompt_rate_of_exchange)
        return self.freight_on_board, self.dutiable_insurance, self.dutiable_freight, self.rate_of_exchange

    def compute_total_dutiable_value_by_sea(self):
        values = self.get_dutiable_value_by_sea_values()
        total_dutiable_value_by_sea = DutiableValueBySea(*values)
        total_dutiable_value_by_sea = total_dutiable_value_by_sea.calculate_dutiable_value_by_sea()
        sys.stdout.write(f'Total Dutiable Value: P{total_dutiable_value_by_sea}\n')
        return


class ComputeDutiableValueByAir(DutiableValue):
    def __init__(self, dutiable_insurance: float, dutiable_freight: float,
                 rate_of_exchange: float) -> None:
        super().__init__(dutiable_insurance, dutiable_freight, rate_of_exchange)
        self.free_carrier = float

    def get_dutiable_value_by_air_values(self):
        sys.stdout.write(prompt_var.prompt_dv_air)
        self.free_carrier = ErrorandInput.get_input(prompt_var.prompt_free_carrier)
        self.dutiable_insurance = ErrorandInput.get_input(prompt_var.prompt_dutiable_insurance)
        self.dutiable_freight = ErrorandInput.get_input(prompt_var.prompt_dutiable_freight)
        self.rate_of_exchange = ErrorandInput.get_input(prompt_var.prompt_rate_of_exchange)
        return self.free_carrier, self.dutiable_insurance, self.dutiable_freight, self.rate_of_exchange

    def compute_total_dutiable_value_by_air(self):
        values = self.get_dutiable_value_by_air_values()
        total_dutiable_value_by_air = DutiableValueByAir(*values)
        total_dutiable_value_by_air = total_dutiable_value_by_air.calculate_dutiable_value_by_air()
        sys.stdout.write(f'Total Dutiable Value: P{total_dutiable_value_by_air}\n')
        return

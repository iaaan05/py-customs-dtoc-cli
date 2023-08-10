import sys

from utils.error_handling_and_input_validation import ErrorandInput
from customs_dtoc import DutiableValueBySea, DutiableValueByAir
from utils import prompt_var


class DutiableValue:
    def __init__(self, dutiable_ins: float, dutiable_frt: float, rate_of_exchange: float) -> None:
        self.dutiable_ins = dutiable_ins
        self.dutiable_frt = dutiable_frt
        self.rate_of_exchange = rate_of_exchange


class ComputeDVViaSea(DutiableValue):
    def __init__(self, dutiable_ins: float, dutiable_frt: float, rate_of_exchange: float) -> None:
        super().__init__(dutiable_ins, dutiable_frt, rate_of_exchange)
        self.fob = float

    def get_dv_values(self) -> tuple[float, float, float, float]:
        sys.stdout.write(prompt_var.prompt_dv_sea)
        self.fob = ErrorandInput.get_input(prompt_var.prompt_total_fob)
        self.dutiable_ins = ErrorandInput.get_input(prompt_var.prompt_dutiable_ins)
        self.dutiable_frt = ErrorandInput.get_input(prompt_var.prompt_dutiable_frt)
        self.rate_of_exchange = ErrorandInput.get_input(prompt_var.prompt_rate_of_exchange)
        return self.fob, self.dutiable_ins, self.dutiable_frt, self.rate_of_exchange

    def compute_dv_via_sea(self) -> None:
        values = self.get_dv_values()
        total_dv = DutiableValueBySea(*values)
        total_dv = total_dv.calculate_dutiable_value_by_sea()
        sys.stdout.write(f'Total Dutiable Value: P{total_dv}\n')
        return


class ComputeDVViaAir(DutiableValue):
    def __init__(self, dutiable_ins: float, dutiable_frt: float, rate_of_exchange: float) -> None:
        super().__init__(dutiable_ins, dutiable_frt, rate_of_exchange)
        self.fca = float

    def get_dv_values(self):
        sys.stdout.write(prompt_var.prompt_dv_air)
        self.fca = ErrorandInput.get_input(prompt_var.prompt_fca)
        self.dutiable_ins = ErrorandInput.get_input(prompt_var.prompt_dutiable_ins)
        self.dutiable_frt = ErrorandInput.get_input(prompt_var.prompt_dutiable_frt)
        self.rate_of_exchange = ErrorandInput.get_input(prompt_var.prompt_rate_of_exchange)
        return self.fca, self.dutiable_ins, self.dutiable_frt, self.rate_of_exchange

    def compute_dv_by_air(self):
        values = self.get_dv_values()
        total_dv = DutiableValueByAir(*values)
        total_dv = total_dv.calculate_dutiable_value_by_air()
        sys.stdout.write(f'Total Dutiable Value: P{total_dv}\n')
        return

import sys

from utils.operations.lc.components_of_lc.dv_type import DutiableValueType
from utils.error_handling_and_input_validation import ErrorandInput
from customs_dtoc import CustomsDuty
from utils import prompt_var


class ComputeCUD:
    def __init__(self, total_dv: float, rod: float, dutiable_frt: float,
                 dutiable_ins: float, rate_of_exchange: float) -> None:
        self.dutiable_frt = dutiable_frt
        self.dutiable_ins = dutiable_ins
        self.rate_of_exchange = rate_of_exchange
        self.total_dv = total_dv
        self.rod = rod

    def get_user_confirmation(self) -> None:
        valid_user_inputs = {
            1.0: self.redirect_dv_type,
            2.0: self.redirect_cud,
            3.0: self.terminate_program
        }

        sys.stdout.write(prompt_var.prompt_dv_intro)
        while True:
            user_input = ErrorandInput.get_input('Enter here:\n-> ')
            if user_input in valid_user_inputs:
                action = valid_user_inputs[user_input]
                action()
                return

            else:
                sys.stdout.write(prompt_var.prompt_invalid_input_1_to_3)

    @staticmethod
    def terminate_program() -> None:
        sys.stdout.write(prompt_var.prompt_terminate_program)
        sys.exit()

    def redirect_dv_type(self) -> None:
        sys.stdout.write(prompt_var.prompt_dv_type_redirect)
        DutiableValueType(
            self.dutiable_frt, self.dutiable_ins, self.rate_of_exchange
        ).get_type_of_dutiable_value()
        return

    def redirect_cud(self) -> None:
        sys.stdout.write(prompt_var.prompt_cud_redirect)
        ComputeCUD(
            self.total_dv, self.rod, self.dutiable_frt, self.dutiable_ins, self.rate_of_exchange
        ).compute_cud()
        return

    def get_cud_values(self) -> tuple[float, float]:
        sys.stdout.write(prompt_var.prompt_cud_intro)
        self.total_dv = ErrorandInput.get_input(prompt_var.prompt_dv)
        self.rod = ErrorandInput.get_input(prompt_var.prompt_rate_of_duty_percent)
        return self.total_dv, self.rod

    def compute_cud(self) -> None:
        values = self.get_cud_values()
        total_cud = CustomsDuty(*values)
        total_cud = total_cud.calculate_cud()
        sys.stdout.write(f'Total Customs Duty: P{total_cud}\n')
        return

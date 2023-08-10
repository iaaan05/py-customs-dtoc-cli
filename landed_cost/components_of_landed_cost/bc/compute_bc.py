import sys

from utils.operations.lc.components_of_lc.dv_type import DutiableValueType
from utils.error_handling_and_input_validation import ErrorandInput
from customs_dtoc import BankCharge
from utils import prompt_var


class ComputeBC:
    def __init__(self, total_dv: float, dutiable_frt: float, dutiable_ins: float,
                 rate_of_exchange: float) -> None:
        self.dutiable_frt = dutiable_frt
        self.dutiable_ins = dutiable_ins
        self.rate_of_exchange = rate_of_exchange
        self.total_dv = total_dv

    def get_user_confirmation(self) -> None:
        valid_user_inputs = {
            1.0: self.redirect_dv_type,
            2.0: self.redirect_bc,
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

    def redirect_bc(self) -> None:
        sys.stdout.write(prompt_var.prompt_bc_redirect)
        ComputeBC(
            self.total_dv, self.dutiable_frt, self.dutiable_ins, self.rate_of_exchange
        ).compute_bc()
        return

    def get_bc_values(self) -> float:
        sys.stdout.write(prompt_var.prompt_bc_intro)
        self.total_dv = ErrorandInput.get_input(prompt_var.prompt_dv)
        return self.total_dv

    def compute_bc(self) -> None:
        values = self.get_bc_values()
        total_bc = BankCharge(values)
        total_bc = total_bc.calculate_bc()
        sys.stdout.write(f'Total Bank Charge: P{total_bc}\n')
        return

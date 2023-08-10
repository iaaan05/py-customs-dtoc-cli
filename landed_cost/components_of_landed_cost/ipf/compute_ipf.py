import sys

from utils.operations.lc.components_of_lc.dv_type import DutiableValueType
from utils.error_handling_and_input_validation import ErrorandInput
from customs_dtoc import ImportProcessingFee
from utils import prompt_var


class ComputeIPF:
    def __init__(self, total_dv: float, dutiable_frt: float, dutiable_ins: float, rate_of_exchange: float) -> None:
        self.dutiable_frt = dutiable_frt
        self.dutiable_ins = dutiable_ins
        self.rate_of_exchange = rate_of_exchange
        self.total_dv = total_dv

    def get_user_confirmation(self) -> None:
        valid_user_inputs = {
            1.0: self.redirect_dv_type,
            2.0: self.redirect_ipf,
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

    def redirect_ipf(self) -> None:
        sys.stdout.write(prompt_var.prompt_ipf_redirect)
        ComputeIPF(
            self.total_dv, self.dutiable_frt, self.dutiable_ins, self.rate_of_exchange
        ).compute_ipf()
        return

    def get_ipf_values(self) -> float:
        sys.stdout.write(prompt_var.prompt_ipf_intro)
        self.total_dv = ErrorandInput.get_input(prompt_var.prompt_dv)
        return self.total_dv

    def compute_ipf(self) -> None:
        values = self.get_ipf_values()
        total_ipf = ImportProcessingFee(values)
        total_ipf = total_ipf.calculate_dv_to_ipf()
        sys.stdout.write(f'Import Processing Fee : P{total_ipf}\n')
        return

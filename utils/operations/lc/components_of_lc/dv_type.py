import sys

from landed_cost.components_of_landed_cost.dv.compute_dv import ComputeDVViaSea, \
    ComputeDVViaAir
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class DutiableValueType:
    def __init__(self, dutiable_frt: float, dutiable_ins: float, rate_of_exchange: float) -> None:
        self.dutiable_frt = dutiable_frt
        self.dutiable_ins = dutiable_ins
        self.rate_of_exchange = rate_of_exchange

    def get_type_of_dutiable_value(self):
        valid_user_inputs = {
            1.0: self.redirect_dv_via_sea,
            2.0: self.redirect_dv_via_air,
            3.0: self.terminate_program
        }

        sys.stdout.write(prompt_var.prompt_dv_type_intro)
        while True:
            user_input = ErrorandInput.get_input('Enter here:\n-> ')
            if user_input in valid_user_inputs:
                action = valid_user_inputs[user_input]
                action()
                return

            else:
                sys.stdout.write(prompt_var.prompt_invalid_input_1_to_4)

    @staticmethod
    def terminate_program() -> None:
        sys.stdout.write(prompt_var.prompt_terminate_program)
        sys.exit()

    def redirect_dv_via_sea(self):
        sys.stdout.write(prompt_var.prompt_dv_sea_redirect)
        ComputeDVViaSea(
            self.dutiable_ins, self.dutiable_frt, self.rate_of_exchange
        ).compute_dv_via_sea()
        return

    def redirect_dv_via_air(self):
        sys.stdout.write(prompt_var.prompt_dv_sea_or_air_redirect)
        ComputeDVViaAir(
            self.dutiable_ins, self.dutiable_frt, self.rate_of_exchange
        ).compute_dv_by_air()
        return

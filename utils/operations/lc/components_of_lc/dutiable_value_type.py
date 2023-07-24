import sys

from landed_cost.components_of_landed_cost.dutiable_value.compute_dutiable_value import ComputeDutiableValueBySea, \
    ComputeDutiableValueByAir
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class DutiableValueType:
    def __init__(self) -> None:
        self.sea = 1
        self.air = 2
        self.terminate_program = 3

    def get_type_of_dutiable_value(self):
        dutiable_insurance = 0
        dutiable_freight = 0
        rate_of_exchange = 0

        valid_user_inputs = (self.sea, self.air, self.terminate_program)
        while True:
            sys.stdout.write(prompt_var.prompt_dv_type_intro)
            user_input = ErrorandInput.get_input('Enter here:\n-> ')
            if user_input in valid_user_inputs:

                if user_input == self.terminate_program:
                    sys.stdout.write(prompt_var.prompt_terminate_program)
                    sys.exit()

                elif user_input == self.sea:
                    sys.stdout.write(prompt_var.prompt_dv_sea_redirect)
                    ComputeDutiableValueBySea(
                        dutiable_insurance, dutiable_freight, rate_of_exchange
                    ).compute_total_dutiable_value_by_sea()
                    return

                elif user_input == self.air:
                    sys.stdout.write(prompt_var.prompt_dv_sea_or_air_redirect)
                    ComputeDutiableValueByAir(
                        dutiable_insurance, dutiable_freight, rate_of_exchange
                    ).compute_total_dutiable_value_by_air()
                    return

            else:
                sys.stdout.write(prompt_var.prompt_invalid_input_1_to_4)

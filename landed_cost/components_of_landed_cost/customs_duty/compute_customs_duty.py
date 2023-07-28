import sys

from utils.operations.lc.components_of_lc.dutiable_value_type import DutiableValueType
from utils.error_handling_and_input_validation import ErrorandInput
from customs_tax import CustomsDuty
from utils import prompt_var


class ComputeCustomsDuty:
    def __init__(self, total_dutiable_value: float, rate_of_duty: float) -> None:
        self.total_dutiable_value = total_dutiable_value
        self.rate_of_duty = rate_of_duty
        self.dutiable_value = 1
        self.customs_duty = 2
        self.terminate_program = 3

    def get_user_confirmation_customs_duty(self) -> None:
        total_dutiable_value = 0
        rate_of_duty = 0

        sys.stdout.write(prompt_var.prompt_dv_intro)
        user_input = ErrorandInput.get_input('Enter here:\n-> ')

        valid_user_inputs = (self.dutiable_value, self.customs_duty, self.terminate_program)
        if user_input in valid_user_inputs:

            if user_input == self.terminate_program:
                sys.stdout.write(prompt_var.prompt_terminate_program)
                sys.exit()

            elif user_input == self.dutiable_value:
                sys.stdout.write(prompt_var.prompt_dutiable_value_type_redirect)
                DutiableValueType().get_type_of_dutiable_value()
                return

            elif user_input == self.customs_duty:
                sys.stdout.write(prompt_var.prompt_cud_redirect)
                ComputeCustomsDuty(
                    total_dutiable_value, rate_of_duty
                ).compute_customs_duty()
                return

        else:
            sys.stdout.write(prompt_var.prompt_invalid_input_1_to_3)

    def get_customs_duty_values(self) -> tuple[float, float]:
        sys.stdout.write(prompt_var.prompt_cud_intro)
        self.total_dutiable_value = ErrorandInput.get_input(prompt_var.prompt_dutiable_value)
        self.rate_of_duty = ErrorandInput.get_input(prompt_var.prompt_rate_of_duty_percent)
        return self.total_dutiable_value, self.rate_of_duty

    def compute_customs_duty(self) -> None:
        values = self.get_customs_duty_values()
        total_customs_duty = CustomsDuty(*values)
        total_customs_duty = total_customs_duty.calculate_cud()
        sys.stdout.write(f'Total Customs Duty: P{total_customs_duty}\n')
        return

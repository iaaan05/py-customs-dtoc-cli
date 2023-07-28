import sys

from utils.operations.lc.components_of_lc.dutiable_value_type import DutiableValueType
from utils.error_handling_and_input_validation import ErrorandInput
from customs_tax import BrokerageFeeFormalEntry
from utils import prompt_var


class ComputeBrokerageFeeFormalEntry:
    def __init__(self, total_dutiable_value: float) -> None:
        self.total_dutiable_value = total_dutiable_value
        self.dutiable_value = 1
        self.brokerage_fee = 2
        self.terminate_program = 3

    def get_user_confirmation_brokerage_fee_formal_entry(self) -> None:
        total_dutiable_value = 0

        sys.stdout.write(prompt_var.prompt_dv_intro)
        user_input = ErrorandInput.get_input('Enter here:\n-> ')

        valid_user_inputs = (self.dutiable_value, self.brokerage_fee, self.terminate_program)
        if user_input in valid_user_inputs:

            if user_input == self.terminate_program:
                sys.stdout.write(prompt_var.prompt_terminate_program)
                sys.exit()

            elif user_input == 1:
                sys.stdout.write(prompt_var.prompt_dutiable_value_type_redirect)
                DutiableValueType().get_type_of_dutiable_value()
                return

            elif user_input == 2:
                sys.stdout.write(prompt_var.prompt_bf_redirect)
                ComputeBrokerageFeeFormalEntry(
                    total_dutiable_value
                ).compute_brokerage_fee_formal_entry()
                return

        else:
            sys.stdout.write(prompt_var.prompt_invalid_input_1_to_3)

    def get_brokerage_fee_formal_values(self) -> float:
        sys.stdout.write(prompt_var.prompt_bf_intro)
        self.total_dutiable_value = ErrorandInput.get_input(prompt_var.prompt_dutiable_value)
        return self.total_dutiable_value

    def compute_brokerage_fee_formal_entry(self) -> None:
        values = self.get_brokerage_fee_formal_values()
        total_brokerage_fee = BrokerageFeeFormalEntry(values)
        total_brokerage_fee = total_brokerage_fee.calculate_dutiable_value_to_brokerage_fee_formal()
        sys.stdout.write(f'Total Brokerage Fee: P{total_brokerage_fee}\n')
        return

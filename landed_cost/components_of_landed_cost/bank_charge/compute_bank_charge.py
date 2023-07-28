import sys

from utils.operations.lc.components_of_lc.dutiable_value_type import DutiableValueType
from utils.error_handling_and_input_validation import ErrorandInput
from customs_tax import BankCharge
from utils import prompt_var


class ComputeBankCharge:
    def __init__(self, total_dutiable_value: float) -> None:
        self.total_dutiable_value = total_dutiable_value
        self.dutiable_value = 1
        self.bank_charge = 2
        self.terminate_program = 3

    def get_user_confirmation_bank_charge(self) -> None:
        total_dutiable_value = 0

        bc_valid_user_inputs = (self.bank_charge, self.dutiable_value, self.terminate_program)
        sys.stdout.write(prompt_var.prompt_dv_intro)
        bc_user_input = ErrorandInput.get_input('Enter here:\n-> ')
        if bc_user_input in bc_valid_user_inputs:

            if bc_user_input == self.terminate_program:
                sys.stdout.write(prompt_var.prompt_terminate_program)
                sys.exit()

            if bc_user_input == self.dutiable_value:
                sys.stdout.write(prompt_var.prompt_dutiable_value_type_redirect)
                DutiableValueType().get_type_of_dutiable_value()
                return

            elif bc_user_input == self.bank_charge:
                sys.stdout.write(prompt_var.prompt_bc_redirect)
                ComputeBankCharge(
                    total_dutiable_value
                ).compute_bank_charge()
                return

        else:
            sys.stdout.write(prompt_var.prompt_invalid_input_1_to_3)

    def get_bank_charge_values(self) -> float:
        sys.stdout.write(prompt_var.prompt_bc_intro)
        self.total_dutiable_value = ErrorandInput.get_input(prompt_var.prompt_dutiable_value)
        return self.total_dutiable_value

    def compute_bank_charge(self) -> None:
        values = self.get_bank_charge_values()
        total_bank_charge = BankCharge(values)
        total_bank_charge = total_bank_charge.calculate_bank_charge()
        sys.stdout.write(f'Total Bank Charge: P{total_bank_charge}\n')
        return

import sys

from value_added_tax.compute_value_added_tax import ComputeValueAddedTaxExciseTax, ComputeValueAddedTaxNonExciseTax
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class ValueAddedTaxType:
    def __init__(self) -> None:
        self.vat_excise_tax = 1
        self.vat_non_excise_tax = 2
        self.terminate_program = 3

    def get_type_of_vat(self) -> None:
        landed_cost_vat = 0

        valid_user_inputs = (self.vat_excise_tax, self.vat_non_excise_tax, self.terminate_program)
        while True:
            sys.stdout.write(prompt_var.prompt_vat_intro)
            user_input = ErrorandInput.get_input('Enter here:\n-> ')
            if user_input in valid_user_inputs:

                if user_input == self.terminate_program:
                    sys.stdout.write(prompt_var.prompt_terminate_program)
                    sys.exit()

                if user_input == self.vat_excise_tax:
                    sys.stdout.write(prompt_var.prompt_vat_excise_tax_redirect)
                    ComputeValueAddedTaxExciseTax(
                        landed_cost_vat
                    ).compute_value_added_tax()
                    return

                elif user_input == self.vat_non_excise_tax:
                    sys.stdout.write(prompt_var.prompt_vat_non_excise_tax_redirect)
                    ComputeValueAddedTaxNonExciseTax(
                        landed_cost_vat
                    ).compute_value_added_tax_non_excise_tax()
                    return

            else:
                sys.stdout.write(prompt_var.prompt_invalid_input_1_to_3)

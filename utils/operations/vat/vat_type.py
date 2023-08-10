import sys

from vat.compute_vat import ComputeVATExciseTax, ComputeVATNonExciseTax
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class VATType:
    def __init__(self, landed_cost_vat: float) -> None:
        self.landed_cost_vat = landed_cost_vat

    def get_type_of_vat(self) -> None:
        valid_user_inputs = {
            1.0: self.redirect_vat_with_et,
            2.0: self.redirect_vat_non_et,
            3.0: self.terminate_program
        }

        sys.stdout.write(prompt_var.prompt_vat_intro)
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

    def redirect_vat_with_et(self):
        sys.stdout.write(prompt_var.prompt_vat_excise_tax_redirect)
        ComputeVATExciseTax(
            self.landed_cost_vat
        ).compute_vat()
        return

    def redirect_vat_non_et(self):
        sys.stdout.write(prompt_var.prompt_vat_non_excise_tax_redirect)
        ComputeVATNonExciseTax(
            self.landed_cost_vat
        ).compute_vat_non_excise_tax()
        return

import sys

from utils.operations.lc.landed_cost_or_components import LandedCostOrComponents
from utils.operations.sop.summary_of_payments_type import SummaryOfPaymentsType
from utils.operations.vat.value_added_tax_type import ValueAddedTaxType
from utils.error_handling_and_input_validation import ErrorandInput
from utils.operations.pro_rata.pro_rata_type import ProRataType
from utils.operations.csf.container_type import ContainerType
from utils import prompt_var


class CustomsTaxCalculator:
    def __init__(self) -> None:
        self.landed_cost = 1
        self.value_added_tax = 2
        self.summary_of_payments = 3
        self.container_security_fee = 4
        self.pro_rata = 5
        self.terminate_program = 6

    def get_user_input(self):

        valid_user_inputs = (self.landed_cost, self.value_added_tax, self.summary_of_payments,
                             self.container_security_fee, self.pro_rata, self.terminate_program)
        while True:
            sys.stdout.write(prompt_var.prompt_main_intro)
            user_input = ErrorandInput.get_input('Enter here:\n-> ')
            if user_input in valid_user_inputs:

                if user_input == self.terminate_program:
                    sys.stdout.write(prompt_var.prompt_terminate_program)
                    sys.exit()

                elif user_input == self.landed_cost:
                    sys.stdout.write(prompt_var.prompt_lc_confirmation_redirect)
                    LandedCostOrComponents().get_to_compute()
                    return

                elif user_input == self.value_added_tax:
                    sys.stdout.write(prompt_var.prompt_vat_type_redirect)
                    ValueAddedTaxType().get_type_of_vat()
                    return

                elif user_input == self.summary_of_payments:
                    sys.stdout.write(prompt_var.prompt_sop_type_redirect)
                    SummaryOfPaymentsType().get_type_of_sop()
                    return

                elif user_input == self.container_security_fee:
                    sys.stdout.write(prompt_var.prompt_csf_type_redirect)
                    ContainerType().get_type_of_container()
                    return

                elif user_input == self.pro_rata:
                    sys.stdout.write(prompt_var.prompt_pro_rata_type_redirect)
                    ProRataType().get_type_of_pro_rata()
                    return

            else:
                sys.stdout.write(prompt_var.prompt_invalid_input_1_to_6)


if __name__ == '__main__':
    app = CustomsTaxCalculator()
    app.get_user_input()

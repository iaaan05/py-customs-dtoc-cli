import sys

from container_security_fee.compute_container_security_fee import ComputeCSF20Footer, ComputeCSF40Footer
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class ContainerType:
    def __init__(self) -> None:
        self.container_20_ft = 1
        self.container_40_ft = 2
        self.terminate_program = 3

    def get_type_of_container(self) -> None:
        number_of_containers = 0
        rate_of_exchange = 0

        valid_user_inputs = (self.container_20_ft, self.container_40_ft, self.terminate_program)
        while True:
            sys.stdout.write(prompt_var.prompt_csf_intro)
            user_input = ErrorandInput.get_input('Enter here:\n-> ')
            if user_input in valid_user_inputs:

                if user_input == self.terminate_program:
                    sys.stdout.write(prompt_var.prompt_terminate_program)
                    sys.exit()

                elif user_input == self.container_20_ft:
                    sys.stdout.write(prompt_var.prompt_csf_20_footer_redirect)
                    ComputeCSF20Footer(
                        number_of_containers, rate_of_exchange
                    ).compute_csf_20_footer(
                        number_of_containers, rate_of_exchange
                    )
                    return

                elif user_input == self.container_40_ft:
                    sys.stdout.write(prompt_var.prompt_csf_40_footer_redirect)
                    ComputeCSF40Footer(
                        number_of_containers, rate_of_exchange
                    ).compute_csf_40_footer(
                        number_of_containers, rate_of_exchange
                    )
                    return

            else:
                sys.stdout.write(prompt_var.prompt_invalid_input_1_to_3)

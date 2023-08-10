import sys

from csf.compute_csf import ComputeCSF20Footer, ComputeCSF40Footer
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class ContainerType:
    def __init__(self, number_of_containers: float, rate_of_exchange: float) -> None:
        self.number_of_containers = number_of_containers
        self.rate_of_exchange = rate_of_exchange

    def get_type_of_container(self) -> None:
        valid_user_inputs = {
            1.0: self.redirect_compute_csf_20,
            2.0: self.redirect_compute_csf_40,
            3.0: self.terminate_program
        }

        sys.stdout.write(prompt_var.prompt_csf_intro)
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

    def redirect_compute_csf_20(self) -> None:
        sys.stdout.write(prompt_var.prompt_csf_20_footer_redirect)
        ComputeCSF20Footer(
            self.number_of_containers, self.rate_of_exchange
        ).compute_csf_20_footer(
            self.number_of_containers, self.rate_of_exchange
        )

    def redirect_compute_csf_40(self) -> None:
        sys.stdout.write(prompt_var.prompt_csf_40_footer_redirect)
        ComputeCSF40Footer(
            self.number_of_containers, self.rate_of_exchange
        ).compute_csf_40_footer(
            self.number_of_containers, self.rate_of_exchange
        )
        return

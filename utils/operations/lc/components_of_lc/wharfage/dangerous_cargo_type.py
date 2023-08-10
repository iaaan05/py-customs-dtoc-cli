import sys

from landed_cost.components_of_landed_cost.wd.pom_micp.compute_containerized_dangerous_cargo import \
    WDComputeDangerousCargo20Footer, WDComputeDangerousCargo40Footer
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class WDDangerousCargoType:
    def __init__(self, number_of_containers: float) -> None:
        self.number_of_containers = number_of_containers

    def get_type_of_dangerous_cargo(self):
        valid_user_inputs = {
            1.0: self.redirect_dangerous_cargo_20,
            2.0: self.redirect_dangerous_cargo_40,
            3.0: self.terminate_program
        }

        sys.stdout.write(prompt_var.prompt_dangerous_intro)
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

    def redirect_dangerous_cargo_20(self):
        sys.stdout.write(prompt_var.prompt_dangerous_cargo_20_footer_redirect)
        WDComputeDangerousCargo20Footer(
            self.number_of_containers
        ).compute_dangerous_cargo_20_footer()
        return

    def redirect_dangerous_cargo_40(self):
        sys.stdout.write(prompt_var.prompt_dangerous_cargo_40_footer_redirect)
        WDComputeDangerousCargo40Footer(
            self.number_of_containers
        ).compute_dangerous_cargo_40_footer()
        return

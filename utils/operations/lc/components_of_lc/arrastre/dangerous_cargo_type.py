import sys

from landed_cost.components_of_landed_cost.arrastre_charge.pom_micp.compute_containerized_dangerous_cargo import \
    ACComputeContainerizedDangerousCargo20Footer, ACComputeContainerizedDangerousCargo40Footer
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class ACDangerousCargoType:
    def __init__(self) -> None:
        self.dangerous_cargo_20_footer = 1
        self.dangerous_cargo_40_footer = 2
        self.terminate_program = 3

    def get_type_of_dangerous_cargo(self):
        classification_of_dangerous_cargo = 0
        total_number_of_containers = 0

        valid_user_input = (self.dangerous_cargo_20_footer, self.dangerous_cargo_40_footer, self.terminate_program)
        while True:
            sys.stdout.write(prompt_var.prompt_dangerous_intro)
            user_input = ErrorandInput.get_input('Enter here:\n-> ')
            if user_input in valid_user_input:

                if user_input == self.terminate_program:
                    sys.stdout.write(prompt_var.prompt_terminate_program)
                    sys.exit()

                elif user_input == self.dangerous_cargo_20_footer:
                    sys.stdout.write(prompt_var.prompt_dangerous_cargo_20_footer_redirect)
                    ACComputeContainerizedDangerousCargo20Footer(
                        classification_of_dangerous_cargo, total_number_of_containers
                    ).compute_containerized_dangerous_cargo_20_footer()
                    return

                elif user_input == self.dangerous_cargo_40_footer:
                    sys.stdout.write(prompt_var.prompt_dangerous_cargo_40_footer_redirect)
                    ACComputeContainerizedDangerousCargo40Footer(
                        classification_of_dangerous_cargo, total_number_of_containers
                    ).compute_containerized_dangerous_cargo_40_footer()
                    return

            else:
                sys.stdout.write(prompt_var.prompt_invalid_input_1_to_3)

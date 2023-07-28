import sys

from utils.operations.lc.components_of_lc.arrastre.dangerous_cargo_type import ACDangerousCargoType
from utils.operations.lc.components_of_lc.arrastre.fcl_type import ACFCLType
from utils.operations.lc.components_of_lc.arrastre.lcl_type import ACLCLType
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class ACCargoType:
    def __init__(self) -> None:
        self.containerized_cargo = 1
        self.bulk_break_bulk_cargo = 2
        self.dangerous_cargo = 3
        self.terminate_program = 4

    def get_type_of_cargo(self) -> None:
        valid_user_input = (self.containerized_cargo, self.bulk_break_bulk_cargo, self.dangerous_cargo,
                            self.terminate_program)
        while True:
            sys.stdout.write(prompt_var.prompt_pom_micp_discharge_intro)
            user_input = ErrorandInput.get_input('Enter here:\n-> ')
            if user_input in valid_user_input:

                if user_input == self.containerized_cargo:
                    sys.stdout.write(prompt_var.prompt_containerized_cargo_type_redirect)
                    ACFCLType().get_type_of_fcl()
                    return

                elif user_input == self.bulk_break_bulk_cargo:
                    sys.stdout.write(prompt_var.prompt_bulk_break_bulk_cargo_type_redirect)
                    ACLCLType().get_type_of_lcl()
                    return

                elif user_input == self.dangerous_cargo:
                    sys.stdout.write(prompt_var.prompt_dangerous_cargo_type_redirect)
                    ACDangerousCargoType().get_type_of_dangerous_cargo()
                    return

                else:
                    sys.stdout.write(prompt_var.prompt_terminate_program)
                    sys.exit()

            else:
                sys.stdout.write(prompt_var.prompt_invalid_input_1_to_4)

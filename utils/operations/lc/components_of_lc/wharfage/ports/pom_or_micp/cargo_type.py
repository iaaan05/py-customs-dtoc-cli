import sys

from utils.operations.lc.components_of_lc.wharfage.dangerous_cargo_type import WDDangerousCargoType
from utils.operations.lc.components_of_lc.wharfage.fcl_type import WDFCLType
from utils.operations.lc.components_of_lc.wharfage.lcl_type import WDLCLType
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class WDCargoType:
    def __init__(self) -> None:
        self.containerized_cargo = 1
        self.bulk_break_bulk_cargo = 2
        self.dangerous_cargo = 3
        self.terminate_program = 4

    def get_type_of_cargo(self):
        valid_user_inputs = (self.containerized_cargo, self.bulk_break_bulk_cargo, self.dangerous_cargo,
                             self.terminate_program)
        while True:
            sys.stdout.write(prompt_var.prompt_pom_micp_discharge_intro)
            user_input = ErrorandInput.get_input('Enter here:\n-> ')
            if user_input in valid_user_inputs:

                if user_input == self.terminate_program:
                    sys.stdout.write(prompt_var.prompt_terminate_program)
                    sys.exit()

                elif user_input == self.containerized_cargo:
                    sys.stdout.write(prompt_var.prompt_containerized_cargo_type_redirect)
                    WDFCLType().get_type_of_fcl()
                    return

                elif user_input == self.bulk_break_bulk_cargo:
                    sys.stdout.write(prompt_var.prompt_bulk_break_bulk_cargo_type_redirect)
                    WDLCLType().get_type_of_lcl()
                    return

                elif user_input == self.dangerous_cargo:
                    sys.stdout.write(prompt_var.prompt_dangerous_cargo_type_redirect)
                    WDDangerousCargoType().get_type_of_dangerous_cargo()
                    return

            else:
                sys.stdout.write(prompt_var.prompt_invalid_input_1_to_4)

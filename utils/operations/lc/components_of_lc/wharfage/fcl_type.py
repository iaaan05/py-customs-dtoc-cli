import sys

from landed_cost.components_of_landed_cost.wharfage_due.pom_micp.compute_full_containerized_cargo import \
    WDComputeContainerizedCargoImport, WDComputeContainerizedCargoExport
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class WDFCLType:
    def __init__(self) -> None:
        self.fcl_import = 1
        self.fcl_export = 2
        self.terminate_program = 3

    def get_type_of_fcl(self):
        size_of_container = 0
        total_number_of_containers = 0

        valid_user_input = (self.fcl_import, self.fcl_export, self.terminate_program)
        while True:
            sys.stdout.write(prompt_var.prompt_wd_fcl_intro)
            user_input = ErrorandInput.get_input('Enter here:\n-> ')
            if user_input in valid_user_input:

                if user_input == self.terminate_program:
                    sys.stdout.write(prompt_var.prompt_terminate_program)
                    sys.exit()

                elif user_input == self.fcl_import:
                    sys.stdout.write(prompt_var.prompt_fcl_import)
                    WDComputeContainerizedCargoImport(
                        size_of_container, total_number_of_containers
                    ).compute_containerized_cargo_import()
                    return

                elif user_input == self.fcl_export:
                    sys.stdout.write(prompt_var.prompt_fcl_export)
                    WDComputeContainerizedCargoExport(
                        size_of_container, total_number_of_containers
                    ).compute_containerized_cargo_export()
                    return

            else:
                sys.stdout.write(prompt_var.prompt_invalid_input_1_to_3)

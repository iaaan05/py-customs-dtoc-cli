import sys

from landed_cost.components_of_landed_cost.arrastre_charge.pom_micp.compute_full_containerized_cargo import \
    ACComputeContainerizedCargoImport, ACComputeContainerizedCargoExport, ACComputeContainerizedCargoShutOutExport
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class ACFCLType:
    def __init__(self) -> None:
        self.fcl_import = 1
        self.fcl_export = 2
        self.shut_out_export = 3
        self.terminate_program = 4

    def get_type_of_fcl(self):
        size_of_container = 0
        total_number_of_containers = 0
        type_of_shutout_export_container = 0

        valid_user_input = (self.fcl_import, self.fcl_export, self.shut_out_export, self.terminate_program)
        while True:
            sys.stdout.write(prompt_var.prompt_ac_fcl_intro)
            user_input = ErrorandInput.get_input('Enter here:\n-> ')
            if user_input in valid_user_input:

                if user_input == self.terminate_program:
                    sys.stdout.write(prompt_var.prompt_terminate_program)
                    sys.exit()

                elif user_input == self.fcl_import:
                    sys.stdout.write(prompt_var.prompt_fcl_import)
                    ACComputeContainerizedCargoImport(
                        size_of_container, total_number_of_containers
                    ).compute_containerized_cargo_import()
                    return

                elif user_input == self.fcl_export:
                    sys.stdout.write(prompt_var.prompt_fcl_export)
                    ACComputeContainerizedCargoExport(
                        size_of_container, total_number_of_containers
                    ).compute_containerized_cargo_export()
                    return

                elif user_input == self.shut_out_export:
                    sys.stdout.write(prompt_var.prompt_ac_fcl_shut_out_export_redirect)
                    ACComputeContainerizedCargoShutOutExport(
                        type_of_shutout_export_container, total_number_of_containers
                    ).compute_containerized_cargo_shutout_export()
                    return

            else:
                sys.stdout.write(prompt_var.prompt_invalid_input_1_to_4)

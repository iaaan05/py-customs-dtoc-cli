import sys

from landed_cost.components_of_landed_cost.ac.pom_micp.compute_fcl import \
    ACComputeFCLImport, ACComputeFCLExport, ACComputeFCLShutOutExport
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class ACFCLType:
    def __init__(self, size_of_container: float, number_of_containers: float, type_of_shutout_export_container: float
                 ) -> None:
        self.size_of_container = size_of_container
        self.number_of_containers = number_of_containers
        self.type_of_shutout_export_container = type_of_shutout_export_container

    def get_type_of_fcl(self):
        valid_user_inputs = {
            1.0: self.redirect_fcl_import,
            2.0: self.redirect_fcl_export,
            3.0: self.redirect_shutout_export,
            4.0: self.terminate_program
        }

        sys.stdout.write(prompt_var.prompt_ac_fcl_intro)
        while True:
            user_input = ErrorandInput.get_input('Enter here:\n-> ')
            if user_input in valid_user_inputs:
                action = valid_user_inputs[user_input]
                action()
                return

            else:
                sys.stdout.write(prompt_var.prompt_invalid_input_1_to_4)

    @staticmethod
    def terminate_program() -> None:
        sys.stdout.write(prompt_var.prompt_terminate_program)
        sys.exit()

    def redirect_fcl_import(self):
        sys.stdout.write(prompt_var.prompt_fcl_import)
        ACComputeFCLImport(
            self.size_of_container, self.number_of_containers
        ).compute_fcl_import()
        return

    def redirect_fcl_export(self):
        sys.stdout.write(prompt_var.prompt_fcl_export)
        ACComputeFCLExport(
            self.size_of_container, self.number_of_containers
        ).compute_fcl_export()
        return

    def redirect_shutout_export(self):
        sys.stdout.write(prompt_var.prompt_ac_fcl_shut_out_export_redirect)
        ACComputeFCLShutOutExport(
            self.type_of_shutout_export_container, self.number_of_containers
        ).compute_fcl_shutout_export()
        return

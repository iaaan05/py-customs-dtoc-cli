import sys

from landed_cost.components_of_landed_cost.ac.pom_micp.compute_lcl import \
    ACComputeLCLImport, ACComputeLCLExport
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class ACLCLType:
    def __init__(self, type_of_cargo: float, total_mt_or_rt: float) -> None:
        self.type_of_cargo = type_of_cargo
        self.total_mt_or_rt = total_mt_or_rt

    def get_type_of_lcl(self) -> None:
        valid_user_inputs = {
            1.0: self.redirect_lcl_import,
            2.0: self.redirect_lcl_export,
            3.0: self.terminate_program
        }

        sys.stdout.write(prompt_var.prompt_lcl_intro)
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

    def redirect_lcl_import(self):
        sys.stdout.write(prompt_var.prompt_lcl_import_redirect)
        ACComputeLCLImport(
            self.type_of_cargo, self.total_mt_or_rt
        ).compute_lcl_import()
        return

    def redirect_lcl_export(self):
        sys.stdout.write(prompt_var.prompt_lcl_export_redirect)
        ACComputeLCLExport(
            self.type_of_cargo, self.total_mt_or_rt
        ).compute_lcl_export()
        return

import sys

from utils.operations.lc.components_of_lc.wharfage.dangerous_cargo_type import WDDangerousCargoType
from utils.operations.lc.components_of_lc.wharfage.fcl_type import WDFCLType
from utils.operations.lc.components_of_lc.wharfage.lcl_type import WDLCLType
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class WDCargoType:
    def __init__(self, type_of_ton: float, total_mt_or_rt: float, size_of_container: float, number_of_containers: float
                 ) -> None:
        self.type_of_ton = type_of_ton
        self.total_mt_or_rt = total_mt_or_rt
        self.size_of_container = size_of_container
        self.number_of_containers = number_of_containers

    def get_type_of_cargo(self):
        valid_user_inputs = {
            1.0: self.redirect_fcl_type,
            2.0: self.redirect_lcl_type,
            3.0: self.redirect_dangerous_cargo_type,
            4.0: self.terminate_program
        }

        sys.stdout.write(prompt_var.prompt_pom_micp_discharge_intro)
        while True:
            user_input = ErrorandInput.get_input('Enter here:\n-> ')
            if user_input in valid_user_inputs:
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

    def redirect_fcl_type(self):
        sys.stdout.write(prompt_var.prompt_containerized_cargo_type_redirect)
        WDFCLType(
            self.size_of_container, self.number_of_containers
        ).get_type_of_fcl()
        return

    def redirect_lcl_type(self):
        sys.stdout.write(prompt_var.prompt_lcl_type_redirect)
        WDLCLType(
            self.type_of_ton, self.total_mt_or_rt
        ).get_type_of_lcl()
        return

    def redirect_dangerous_cargo_type(self):
        sys.stdout.write(prompt_var.prompt_dangerous_cargo_type_redirect)
        WDDangerousCargoType(
            self.number_of_containers
        ).get_type_of_dangerous_cargo()
        return

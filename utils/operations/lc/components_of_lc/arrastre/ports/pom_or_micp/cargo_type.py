import sys

from utils.operations.lc.components_of_lc.arrastre.dangerous_cargo_type import ACDangerousCargoType
from utils.operations.lc.components_of_lc.arrastre.fcl_type import ACFCLType
from utils.operations.lc.components_of_lc.arrastre.lcl_type import ACLCLType
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class ACCargoType:
    def __init__(self, size_of_container: float, number_of_containers: float, type_of_shutout_export_container: float,
                 classification_of_dangerous_cargo: float) -> None:
        self.size_of_container = size_of_container
        self.number_of_containers = number_of_containers
        self.type_of_shutout_export_container = type_of_shutout_export_container
        self.classification_of_dangerous_cargo = classification_of_dangerous_cargo

    def get_type_of_cargo(self) -> None:
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
        ACFCLType(
            self.size_of_container, self.number_of_containers, self.type_of_shutout_export_container
        ).get_type_of_fcl()
        return

    def redirect_lcl_type(self):
        sys.stdout.write(prompt_var.prompt_lcl_type_redirect)
        ACLCLType(
            self.size_of_container, self.number_of_containers
        ).get_type_of_lcl()
        return

    def redirect_dangerous_cargo_type(self):
        sys.stdout.write(prompt_var.prompt_dangerous_cargo_type_redirect)
        ACDangerousCargoType(
            self.classification_of_dangerous_cargo, self.number_of_containers
        ).get_type_of_dangerous_cargo()
        return

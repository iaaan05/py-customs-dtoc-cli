import sys

from utils.operations.lc.components_of_lc.arrastre.ports.out_ports.discharge_type import ACDischargeType
from utils.operations.lc.components_of_lc.wharfage.ports.out_ports.discharge_type import WDDischargeType
from utils.operations.lc.components_of_lc.arrastre.ports.pom_or_micp.cargo_type import ACCargoType
from utils.operations.lc.components_of_lc.wharfage.ports.pom_or_micp.cargo_type import WDCargoType
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class PortofDischarge:
    def __init__(self) -> None:
        self.outport = 1
        self.port_of_manila_or_micp = 2
        self.terminate_program = 3

    def get_port_of_discharge_in_arrastre(self) -> None:
        valid_user_inputs = (self.outport, self.port_of_manila_or_micp, self.terminate_program)
        while True:
            sys.stdout.write(prompt_var.prompt_port_of_discharge_intro)
            user_input = ErrorandInput.get_input('Enter Here:\n-> ')
            if user_input in valid_user_inputs:

                if user_input == self.terminate_program:
                    sys.stdout.write(prompt_var.prompt_invalid_input_1_to_3)
                    sys.exit()

                elif user_input == self.outport:
                    sys.stdout.write(prompt_var.prompt_ac_outport_type_redirect)
                    ACDischargeType().get_type_of_discharge()
                    return

                elif user_input == self.port_of_manila_or_micp:
                    sys.stdout.write(prompt_var.prompt_ac_pom_or_micp_type_redirect)
                    ACCargoType().get_type_of_cargo()
                    return

            else:
                sys.stdout.write(prompt_var.prompt_invalid_input_1_to_3)

    def get_port_of_discharge_in_wharfage(self) -> None:
        valid_user_inputs = (self.outport, self.port_of_manila_or_micp, self.terminate_program)
        while True:
            sys.stdout.write(prompt_var.prompt_port_of_discharge_intro)
            user_input = ErrorandInput.get_input('Enter Here:\n-> ')
            if user_input in valid_user_inputs:

                if user_input == self.terminate_program:
                    sys.stdout.write(prompt_var.prompt_invalid_input_1_to_3)
                    sys.exit()

                elif user_input == self.outport:
                    sys.stdout.write(prompt_var.prompt_wd_outport_type_redirect)
                    WDDischargeType().get_type_of_discharge()
                    return

                elif user_input == self.port_of_manila_or_micp:
                    sys.stdout.write(prompt_var.prompt_wd_pom_or_micp_type_redirect)
                    WDCargoType().get_type_of_cargo()
                    return

            else:
                sys.stdout.write(prompt_var.prompt_invalid_input_1_to_3)

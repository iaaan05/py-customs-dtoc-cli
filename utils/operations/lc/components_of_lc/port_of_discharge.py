import sys

from utils.operations.lc.components_of_lc.arrastre.ports.out_ports.discharge_type import ACDischargeType
from utils.operations.lc.components_of_lc.wharfage.ports.out_ports.discharge_type import WDDischargeType
from utils.operations.lc.components_of_lc.arrastre.ports.pom_or_micp.cargo_type import ACCargoType
from utils.operations.lc.components_of_lc.wharfage.ports.pom_or_micp.cargo_type import WDCargoType
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class PortofDischarge:
    def __init__(self, total_mt: float, size_of_container: float, number_of_containers: float,
                 type_of_shutout_export_container: float, classification_of_dangerous_cargo: float, type_of_ton: float,
                 total_mt_or_rt: float) -> None:
        self.type_of_ton = type_of_ton
        self.total_mt_or_rt = total_mt_or_rt
        self.total_mt = total_mt
        self.size_of_container = size_of_container
        self.number_of_containers = number_of_containers
        self.type_of_shutout_export_container = type_of_shutout_export_container
        self.classification_of_dangerous_cargo = classification_of_dangerous_cargo

    def get_port_of_discharge_in_arrastre(self) -> None:
        valid_user_inputs = {
            1.0: self.redirect_ac_outport_discharge,
            2.0: self.redirect_ac_pom_micp_discharge,
            3.0: self.terminate_program
        }

        sys.stdout.write(prompt_var.prompt_port_of_discharge_intro)
        while True:
            user_input = ErrorandInput.get_input('Enter Here:\n-> ')
            if user_input in valid_user_inputs:
                action = valid_user_inputs[user_input]
                action()
                return

            else:
                sys.stdout.write(prompt_var.prompt_invalid_input_1_to_3)

    def redirect_ac_outport_discharge(self):
        sys.stdout.write(prompt_var.prompt_ac_outport_type_redirect)
        ACDischargeType(
            self.total_mt
        ).get_type_of_discharge()
        return

    def redirect_ac_pom_micp_discharge(self):
        sys.stdout.write(prompt_var.prompt_ac_pom_or_micp_type_redirect)
        ACCargoType(
            self.size_of_container, self.number_of_containers, self.type_of_shutout_export_container,
            self.classification_of_dangerous_cargo
        ).get_type_of_cargo()
        return

    def get_port_of_discharge_in_wharfage(self) -> None:
        valid_user_inputs = {
            1.0: self.redirect_wd_outport_discharge,
            2.0: self.redirect_wd_pom_micp_discharge,
            3.0: self.terminate_program
        }

        sys.stdout.write(prompt_var.prompt_port_of_discharge_intro)
        while True:
            user_input = ErrorandInput.get_input('Enter Here:\n-> ')
            if user_input in valid_user_inputs:
                action = valid_user_inputs[user_input]
                action()
                return

            else:
                sys.stdout.write(prompt_var.prompt_invalid_input_1_to_3)

    def redirect_wd_outport_discharge(self):
        sys.stdout.write(prompt_var.prompt_wd_outport_type_redirect)
        WDDischargeType(
            self.total_mt
        ).get_type_of_discharge()
        return

    def redirect_wd_pom_micp_discharge(self):
        sys.stdout.write(prompt_var.prompt_wd_pom_or_micp_type_redirect)
        WDCargoType(
            self.type_of_ton, self.total_mt_or_rt, self.size_of_container, self.number_of_containers
        ).get_type_of_cargo()
        return

    @staticmethod
    def terminate_program() -> None:
        sys.stdout.write(prompt_var.prompt_terminate_program)
        sys.exit()

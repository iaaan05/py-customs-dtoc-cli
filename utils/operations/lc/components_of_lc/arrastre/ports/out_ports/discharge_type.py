import sys

from landed_cost.components_of_landed_cost.arrastre_charge.outports.compute_arrastre_charge_outports import \
    ComputeArrastreChargeViaShipside, ComputeArrastreChargeViaPierside
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class ACDischargeType:
    def __init__(self) -> None:
        self.shipside_discharge = 1
        self.pierside_discharge = 2
        self.terminate_program = 3
        self.total_metric_ton = 0

    def get_type_of_discharge(self) -> None:
        valid_user_inputs = (self.shipside_discharge, self.pierside_discharge, self.terminate_program)
        while True:
            sys.stdout.write(prompt_var.prompt_outport_discharge_intro)
            user_input = ErrorandInput.get_input('Enter Here:\n-> ')
            if user_input in valid_user_inputs:

                if user_input == self.terminate_program:
                    sys.stdout.write(prompt_var.prompt_terminate_program)
                    sys.exit()

                elif user_input == self.shipside_discharge:
                    sys.stdout.write(prompt_var.prompt_ac_outport_shipside_discharge_redirect)
                    ComputeArrastreChargeViaShipside(
                        self.total_metric_ton
                    ).compute_total_arrastre_charge_via_shipside()
                    return

                elif user_input == self.pierside_discharge:
                    sys.stdout.write(prompt_var.prompt_ac_outport_pierside_discharge_redirect)
                    ComputeArrastreChargeViaPierside(
                        self.total_metric_ton
                    ).compute_total_arrastre_charge_via_pierside()
                    return

            else:
                sys.stdout.write(prompt_var.prompt_invalid_input_1_to_3)

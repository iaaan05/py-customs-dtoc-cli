import sys

from landed_cost.components_of_landed_cost.wd.outports.compute_wd_outports import \
    ComputeWDViaShipside, ComputeWDViaPierside
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class WDDischargeType:
    def __init__(self, total_mt: float) -> None:
        self.total_mt = total_mt

    def get_type_of_discharge(self) -> None:
        valid_user_inputs = {
            1.0: self.redirect_wd_shipside_discharge,
            2.0: self.redirect_wd_pierside_discharge,
            3.0: self.terminate_program
        }

        sys.stdout.write(prompt_var.prompt_outport_discharge_intro)
        while True:
            user_input = ErrorandInput.get_input('Enter Here:\n-> ')
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

    def redirect_wd_shipside_discharge(self):
        sys.stdout.write(prompt_var.prompt_wd_outport_shipside_discharge_redirect)
        ComputeWDViaShipside(
            self.total_mt
        ).compute_wd_due_via_shipside()
        return

    def redirect_wd_pierside_discharge(self):
        sys.stdout.write(prompt_var.prompt_wd_outport_pierside_discharge_redirect)
        ComputeWDViaPierside(
            self.total_mt
        ).compute_wd_due_via_pierside()
        return

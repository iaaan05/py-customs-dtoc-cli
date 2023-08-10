import sys

from pro_rata.compute_pro_rata import ComputeProRataFreight, ComputeProRataInsurance, \
    ComputeProRataDutiableValue, ComputeProRataMiscExpenses
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class ProRataType:
    def __init__(self, individual_fob: float, total_fob: float) -> None:
        self.individual_fob = individual_fob
        self.total_fob = total_fob

    def get_type_of_pro_rata(self) -> None:
        valid_user_inputs = {
            1.0: self.redirect_compute_pro_rata_frt,
            2.0: self.redirect_compute_pro_rata_ins,
            3.0: self.redirect_compute_pro_rata_dv,
            4.0: self.redirect_compute_pro_rata_misc,
            5.0: self.terminate_program
        }

        sys.stdout.write(prompt_var.prompt_pro_rata_intro)
        while True:
            user_input = ErrorandInput.get_input('Enter here:\n-> ')
            if user_input in valid_user_inputs:
                action = valid_user_inputs[user_input]
                action()
                return

            else:
                sys.stdout.write(prompt_var.prompt_invalid_input_1_to_5)

    @staticmethod
    def terminate_program() -> None:
        sys.stdout.write(prompt_var.prompt_terminate_program)
        sys.exit()

    def redirect_compute_pro_rata_frt(self) -> None:
        sys.stdout.write(prompt_var.prompt_individual_frt_redirect)
        ComputeProRataFreight(
            self.individual_fob, self.total_fob
        ).compute_pro_rata_frt()
        return

    def redirect_compute_pro_rata_ins(self) -> None:
        sys.stdout.write(prompt_var.prompt_individual_ins_redirect)
        ComputeProRataInsurance(
            self.individual_fob, self.total_fob
        ).compute_pro_rata_ins()
        return

    def redirect_compute_pro_rata_dv(self) -> None:
        sys.stdout.write(prompt_var.prompt_individual_dv_redirect)
        ComputeProRataDutiableValue(
            self.individual_fob, self.total_fob
        ).compute_pro_rata_dv()
        return

    def redirect_compute_pro_rata_misc(self) -> None:
        sys.stdout.write(prompt_var.prompt_individual_me_redirect)
        ComputeProRataMiscExpenses(
            self.individual_fob, self.total_fob
        ).compute_pro_rata_misc_expenses()
        return

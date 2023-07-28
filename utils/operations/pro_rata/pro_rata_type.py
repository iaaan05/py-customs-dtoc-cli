import sys

from pro_rata.compute_pro_rata_individual import ComputeProRataIndividualFreight, ComputeProRataIndividualInsurance, \
    ComputeProRataIndividualDutiableValue, ComputeProRataIndividualMiscExpenses
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class ProRataType:
    def __init__(self) -> None:
        self.individual_frt = 1
        self.individual_ins = 2
        self.individual_dutiable_value = 3
        self.individual_misc_expenses = 4
        self.terminate_program = 5

    def get_type_of_pro_rata(self) -> None:
        individual_fob = 0
        total_fob = 0

        valid_user_inputs = (self.individual_frt, self.individual_ins, self.individual_dutiable_value,
                             self.individual_misc_expenses, self.terminate_program)
        while True:
            sys.stdout.write(prompt_var.prompt_pro_rata_intro)
            user_input = ErrorandInput.get_input('Enter here:\n-> ')
            if user_input in valid_user_inputs:

                if user_input == self.terminate_program:
                    sys.stdout.write(prompt_var.prompt_terminate_program)
                    sys.exit()

                elif user_input == self.individual_frt:
                    sys.stdout.write(prompt_var.prompt_individual_frt_redirect)
                    ComputeProRataIndividualFreight(
                        individual_fob, total_fob
                    ).compute_pro_rata_individual_freight()
                    return

                elif user_input == self.individual_ins:
                    sys.stdout.write(prompt_var.prompt_individual_ins_redirect)
                    ComputeProRataIndividualInsurance(
                        individual_fob, total_fob
                    ).compute_pro_rata_individual_insurance()
                    return

                elif user_input == self.individual_dutiable_value:
                    sys.stdout.write(prompt_var.prompt_individual_dv_redirect)
                    ComputeProRataIndividualDutiableValue(
                        individual_fob, total_fob
                    ).compute_pro_rata_individual_dutiable_value()
                    return

                elif user_input == self.individual_misc_expenses:
                    sys.stdout.write(prompt_var.prompt_individual_me_redirect)
                    ComputeProRataIndividualMiscExpenses(
                        individual_fob, total_fob
                    ).compute_pro_rata_individual_misc_expenses()
                    return

            else:
                sys.stdout.write(prompt_var.prompt_invalid_input_1_to_5)

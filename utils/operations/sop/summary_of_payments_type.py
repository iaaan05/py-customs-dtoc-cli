import sys

from summary_of_payments.compute_sop import ComputeSummaryOfPaymentsWithLetterOfCredit, \
    ComputeSummaryOfPaymentsNonLetterOfCredit, ComputeSummaryOfPaymentsWithInformalEntry
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class SummaryOfPaymentsType:
    def __init__(self) -> None:
        self.letter_of_credit = 1
        self.non_letter_of_credit = 2
        self.informal_entry = 3
        self.terminate_program = 4

    def get_type_of_sop(self) -> None:
        customs_duty = 0
        value_added_tax_sop = 0
        excise_tax = 0
        import_processing_fee = 0
        customs_documentary_stamps = 0
        container_security_fee_sop = 0
        advance_deposit = 0

        valid_user_inputs = (self.letter_of_credit, self.non_letter_of_credit, self.informal_entry,
                             self.terminate_program)
        while True:
            sys.stdout.write(prompt_var.prompt_sop_intro)
            user_input = ErrorandInput.get_input('Enter here:\n-> ')
            if user_input in valid_user_inputs:

                if user_input == self.terminate_program:
                    sys.stdout.write(prompt_var.prompt_terminate_program)
                    sys.exit()

                elif user_input == self.letter_of_credit:
                    sys.stdout.write(prompt_var.prompt_letter_of_credit_redirect)
                    ComputeSummaryOfPaymentsWithLetterOfCredit(
                        customs_duty, value_added_tax_sop, excise_tax, import_processing_fee,
                        customs_documentary_stamps, container_security_fee_sop, advance_deposit
                    ).compute_sop_with_letter_of_credit()
                    return

                elif user_input == self.non_letter_of_credit:
                    sys.stdout.write(prompt_var.prompt_non_letter_of_credit_redirect)
                    ComputeSummaryOfPaymentsNonLetterOfCredit(
                        customs_duty, value_added_tax_sop, excise_tax, import_processing_fee,
                        customs_documentary_stamps, container_security_fee_sop
                    ).compute_sop_with_non_letter_of_credit()
                    return

                elif user_input == self.informal_entry:
                    sys.stdout.write(prompt_var.prompt_lc_informal_entry_redirect)
                    ComputeSummaryOfPaymentsWithInformalEntry(
                        customs_duty, value_added_tax_sop, excise_tax, import_processing_fee
                    ).compute_sop_with_informal_entry()
                    return

            else:
                sys.stdout.write(prompt_var.prompt_invalid_input_1_to_4)

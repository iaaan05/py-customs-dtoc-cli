import sys

from sop.compute_sop import ComputeSOPWithLetterOfCredit, \
    ComputeSOPNonLetterOfCredit, ComputeSOPWithInformalEntry
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class SummaryOfPaymentsType:
    def __init__(self, cud: float, vat: float, excise_tax: float, ipf: float, cds: float, csf: float,
                 advance_deposit: float) -> None:
        self.cud = cud
        self.vat = vat
        self.excise_tax = excise_tax
        self.ipf = ipf
        self.cds = cds
        self.csf = csf
        self.advance_deposit = advance_deposit

    def get_type_of_sop(self) -> None:
        valid_user_inputs = {
            1.0: self.redirect_sop_with_lc,
            2.0: self.redirect_sop_non_lc,
            3.0: self.redirect_sop_informal_entry,
            4.0: self.terminate_program
        }

        sys.stdout.write(prompt_var.prompt_sop_intro)
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

    def redirect_sop_with_lc(self) -> None:
        sys.stdout.write(prompt_var.prompt_sop_with_lc_redirect)
        ComputeSOPWithLetterOfCredit(
            self.cud, self.vat, self.excise_tax, self.ipf, self.cds, self.csf, self.advance_deposit
        ).compute_sop_with_lc()
        return

    def redirect_sop_non_lc(self) -> None:
        sys.stdout.write(prompt_var.prompt_sop_non_lc_redirect)
        ComputeSOPNonLetterOfCredit(
            self.cud, self.vat, self.excise_tax, self.ipf, self.cds, self.csf
        ).compute_sop_non_lc()
        return

    def redirect_sop_informal_entry(self) -> None:
        sys.stdout.write(prompt_var.prompt_sop_informal_entry_redirect)
        ComputeSOPWithInformalEntry(
            self.cud, self.vat, self.excise_tax, self.ipf
        ).compute_sop_with_informal_entry()
        return

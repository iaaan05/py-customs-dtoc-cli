import sys

from landed_cost.entry_type.compute_informal_lc import ComputeLCViaInformalEntry
from utils.operations.lc.entry_type.formal_entry_type import FormalEntryType
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class EntryType:
    def __init__(self, dv: float, cud: float, bc: float, bf: float, ac: float, wd: float, ipf: float, cds: float
                 ) -> None:
        self.dv = dv
        self.cud = cud
        self.bc = bc
        self.bf = bf
        self.ac = ac
        self.wd = wd
        self.ipf = ipf
        self.cds = cds

    def get_type_of_entry(self):
        valid_user_inputs = {
            1.0: self.redirect_lc_via_formal_entry,
            2.0: self.redirect_lc_via_informal_entry,
            3.0: self.terminate_program
        }

        sys.stdout.write(prompt_var.prompt_entry_input_intro)
        while True:
            user_input = ErrorandInput.get_input('Enter here:\n-> ')
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

    def redirect_lc_via_formal_entry(self):
        sys.stdout.write(prompt_var.prompt_lc_formal_entry_type_redirect)
        FormalEntryType(
            self.dv, self.cud, self.bc, self.bf, self.ac, self.wd, self.ipf, self.cds
        ).get_type_of_formal_entry()
        return

    def redirect_lc_via_informal_entry(self):
        sys.stdout.write(prompt_var.prompt_lc_informal_entry_redirect)
        ComputeLCViaInformalEntry(
            self.dv, self.cud, self.bf, self.cds
        ).compute_lc_via_informal_entry()
        return

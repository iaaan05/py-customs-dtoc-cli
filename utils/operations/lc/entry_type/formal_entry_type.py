import sys

from landed_cost.entry_type.compute_formal_lc import ComputeLCViaSea, ComputeLCViaAir
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class FormalEntryType:
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

    def get_type_of_formal_entry(self) -> None:
        valid_user_inputs = {
            1.0: self.redirect_lc_via_sea,
            2.0: self.redirect_lc_via_air,
            3.0: self.terminate_program
        }

        sys.stdout.write(prompt_var.prompt_formal_entry_intro)
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

    def redirect_lc_via_sea(self):
        sys.stdout.write(prompt_var.prompt_lc_formal_sea_redirect)
        ComputeLCViaSea(
            self.dv, self.cud, self.bc, self.bf, self.ac, self.wd, self.ipf, self.cds
        ).compute_lc_via_sea()
        return

    def redirect_lc_via_air(self):
        sys.stdout.write(prompt_var.prompt_lc_formal_air_redirect)
        ComputeLCViaAir(
            self.dv, self.cud, self.bc, self.bf, self.ipf, self.cds
        ).compute_lc_via_air()
        return

import sys

from utils.operations.lc.components_of_lc.components_of_lc import ComponentsOfLandedCost
from utils.operations.lc.entry_type.entry_type import EntryType
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class LandedCostOrComponents:
    def __init__(self, dv: float, cud: float, bc: float, bf: float, ac: float, wd: float, ipf: float, cds: float,
                 rod: float, total_dv: float, type_of_entry: float, dutiable_frt: float, dutiable_ins: float,
                 rate_of_exchange: float, total_mt: float, size_of_container: float, number_of_containers: float,
                 type_of_shutout_export_container: float, classification_of_dangerous_cargo: float, type_of_ton: float,
                 total_mt_or_rt: float) -> None:
        self.dv = dv
        self.cud = cud
        self.bc = bc
        self.bf = bf
        self.ac = ac
        self.wd = wd
        self.ipf = ipf
        self.cds = cds
        self.dutiable_frt = dutiable_frt
        self.dutiable_ins = dutiable_ins
        self.rate_of_exchange = rate_of_exchange
        self.total_dv = total_dv
        self.rod = rod
        self.type_of_entry = type_of_entry
        self.type_of_ton = type_of_ton
        self.total_mt_or_rt = total_mt_or_rt
        self.total_mt = total_mt
        self.size_of_container = size_of_container
        self.number_of_containers = number_of_containers
        self.type_of_shutout_export_container = type_of_shutout_export_container
        self.classification_of_dangerous_cargo = classification_of_dangerous_cargo

    def get_to_compute(self):
        valid_user_inputs = {
            1.0: self.redirect_lc_entry_type,
            2.0: self.redirect_components_of_lc,
            3.0: self.terminate_program
        }

        sys.stdout.write(prompt_var.prompt_lc_or_components_intro)
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

    def redirect_lc_entry_type(self):
        sys.stdout.write(prompt_var.prompt_type_of_lc_entry_redirect)
        EntryType(
            self.dv, self.cud, self.bc, self.bf, self.ac, self.wd, self.ipf, self.cds
        ).get_type_of_entry()
        return

    def redirect_components_of_lc(self):
        sys.stdout.write(prompt_var.prompt_components_of_lc_redirect)
        ComponentsOfLandedCost(
            self.dutiable_frt, self.dutiable_ins, self.rate_of_exchange, self.total_dv, self.rod, self.type_of_entry,
            self.total_mt, self.size_of_container, self.number_of_containers, self.type_of_shutout_export_container,
            self.classification_of_dangerous_cargo, self.type_of_ton, self.total_mt_or_rt
        ).get_component_of_landed_cost()
        return

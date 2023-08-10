import sys

from utils.operations.lc.landed_cost_or_components import LandedCostOrComponents
from utils.operations.sop.sop_type import SummaryOfPaymentsType
from utils.operations.vat.vat_type import VATType
from utils.error_handling_and_input_validation import ErrorandInput
from utils.operations.pro_rata.pro_rata_type import ProRataType
from utils.operations.csf.container_type import ContainerType
from utils import prompt_var


class CustomsCalculator:
    def __init__(self, dv: float, cud: float, bc: float, bf: float, ac: float, wd: float, ipf: float, cds: float,
                 rod: float, total_dv: float, type_of_entry: float, dutiable_frt: float, dutiable_ins: float,
                 rate_of_exchange: float, total_mt: float, size_of_container: float, number_of_containers: float,
                 type_of_shutout_export_container: float, classification_of_dangerous_cargo: float,
                 landed_cost_vat: float, vat: float, excise_tax: float, csf: float, advance_deposit: float,
                 individual_fob: float, total_fob: float, type_of_ton: float, total_mt_or_rt: float) -> None:
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
        self.rate_of_duty = rod
        self.type_of_entry = type_of_entry
        self.type_of_ton = type_of_ton
        self.total_mt_or_rt = total_mt_or_rt
        self.total_mt = total_mt
        self.size_of_container = size_of_container
        self.number_of_containers = number_of_containers
        self.type_of_shutout_export_container = type_of_shutout_export_container
        self.classification_of_dangerous_cargo = classification_of_dangerous_cargo
        self.landed_cost_vat = landed_cost_vat
        self.vat = vat
        self.excise_tax = excise_tax
        self.csf = csf
        self.advance_deposit = advance_deposit
        self.individual_fob = individual_fob
        self.total_fob = total_fob

    def get_user_input(self) -> None:
        valid_user_inputs = {
            1.0: self.redirect_lc_or_components_of_lc,
            2.0: self.redirect_vat,
            3.0: self.redirect_sop,
            4.0: self.redirect_csf,
            5.0: self.redirect_pro_rata,
            6.0: self.terminate_program
        }

        sys.stdout.write(prompt_var.prompt_main_intro)
        while True:
            user_input = ErrorandInput.get_input('Enter here:\n-> ')
            if user_input in valid_user_inputs:
                action = valid_user_inputs[user_input]
                action()
                return

            else:
                sys.stdout.write(prompt_var.prompt_invalid_input_1_to_6)

    @staticmethod
    def terminate_program() -> None:
        sys.stdout.write(prompt_var.prompt_terminate_program)
        sys.exit()

    def redirect_lc_or_components_of_lc(self) -> None:
        sys.stdout.write(prompt_var.prompt_lc_confirmation_redirect)
        LandedCostOrComponents(
            self.dv, self.cud, self.bc, self.bf, self.ac, self.wd, self.ipf, self.cds, self.dutiable_frt,
            self.dutiable_ins, self.rate_of_exchange, self.total_dv, self.rate_of_duty, self.type_of_entry,
            self.total_mt, self.size_of_container, self.number_of_containers, self.type_of_shutout_export_container,
            self.classification_of_dangerous_cargo, self.type_of_ton, self.total_mt_or_rt
        ).get_to_compute()
        return

    def redirect_vat(self) -> None:
        sys.stdout.write(prompt_var.prompt_vat_type_redirect)
        VATType(
            self.landed_cost_vat
        ).get_type_of_vat()
        return

    def redirect_sop(self) -> None:
        sys.stdout.write(prompt_var.prompt_sop_type_redirect)
        SummaryOfPaymentsType(
            self.cud, self.vat, self.excise_tax, self.ipf,
            self.cds, self.csf, self.advance_deposit
        ).get_type_of_sop()
        return

    def redirect_csf(self) -> None:
        sys.stdout.write(prompt_var.prompt_csf_type_redirect)
        ContainerType(
            self.number_of_containers, self.rate_of_exchange
        ).get_type_of_container()
        return

    def redirect_pro_rata(self) -> None:
        sys.stdout.write(prompt_var.prompt_pro_rata_type_redirect)
        ProRataType(
            self.individual_fob, self.total_fob
        ).get_type_of_pro_rata()
        return

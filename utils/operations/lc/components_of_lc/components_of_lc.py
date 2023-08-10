import sys

from landed_cost.components_of_landed_cost.bf.compute_bf import ComputeBFFormalEntry
from utils.operations.lc.components_of_lc.dv_type import DutiableValueType
from utils.operations.lc.components_of_lc.port_of_discharge import PortofDischarge
from landed_cost.components_of_landed_cost.cds.compute_cds import ComputeCDS
from landed_cost.components_of_landed_cost.ipf.compute_ipf import ComputeIPF
from landed_cost.components_of_landed_cost.cud.compute_cud import ComputeCUD
from landed_cost.components_of_landed_cost.bc.compute_bc import ComputeBC
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class ComponentsOfLandedCost:
    def __init__(self, rod: float, total_dv: float, type_of_entry: float, dutiable_frt: float, dutiable_ins: float,
                 rate_of_exchange: float, total_mt: float, size_of_container: float, number_of_containers: float,
                 type_of_shutout_export_container: float, classification_of_dangerous_cargo: float, type_of_ton: float,
                 total_mt_or_rt: float) -> None:
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

    def get_component_of_landed_cost(self):
        valid_user_inputs = {
            1.0: self.redirect_dutiable_value,
            2.0: self.redirect_customs_duty,
            3.0: self.redirect_bank_charge,
            4.0: self.redirect_brokerage_fee,
            5.0: self.redirect_arrastre_charge,
            6.0: self.redirect_wharfage_due,
            7.0: self.redirect_import_processing_fee,
            8.0: self.redirect_customs_documentary_stamp,
            9.0: self.terminate_program
        }

        sys.stdout.write(prompt_var.prompt_components_lc_intro)
        while True:
            user_input = ErrorandInput.get_input("Enter here:\n-> ")
            if user_input in valid_user_inputs:
                action = valid_user_inputs[user_input]
                action()
                return

            else:
                sys.stdout.write(prompt_var.prompt_invalid_input_1_to_9)

    @staticmethod
    def terminate_program() -> None:
        sys.stdout.write(prompt_var.prompt_terminate_program)
        sys.exit()

    def redirect_dutiable_value(self):
        sys.stdout.write(prompt_var.prompt_dv)
        DutiableValueType(
            self.dutiable_frt, self.dutiable_ins, self.rate_of_exchange
        ).get_type_of_dutiable_value()
        return

    def redirect_customs_duty(self):
        sys.stdout.write(prompt_var.prompt_cud_confirmation_redirect)
        ComputeCUD(
            self.dutiable_frt, self.dutiable_ins, self.rate_of_exchange, self.rod, self.total_dv
        ).get_user_confirmation()
        return

    def redirect_bank_charge(self):
        sys.stdout.write(prompt_var.prompt_bc_redirect)
        ComputeBC(
            self.dutiable_frt, self.dutiable_ins, self.rate_of_exchange, self.total_dv
        ).get_user_confirmation()
        return

    def redirect_brokerage_fee(self):
        sys.stdout.write(prompt_var.prompt_bf_redirect)
        ComputeBFFormalEntry(
            self.dutiable_frt, self.dutiable_ins, self.rate_of_exchange, self.total_dv
        ).get_user_confirmation()
        return

    def redirect_arrastre_charge(self):
        sys.stdout.write(prompt_var.prompt_port_of_discharge_type_redirect)
        PortofDischarge(
            self.total_mt, self.size_of_container, self.number_of_containers, self.type_of_shutout_export_container,
            self.classification_of_dangerous_cargo, self.type_of_ton, self.total_mt_or_rt
        ).get_port_of_discharge_in_arrastre()
        return

    def redirect_wharfage_due(self):
        sys.stdout.write(prompt_var.prompt_port_of_discharge_type_redirect)
        PortofDischarge(
            self.total_mt, self.size_of_container, self.number_of_containers, self.type_of_shutout_export_container,
            self.classification_of_dangerous_cargo, self.type_of_ton, self.total_mt_or_rt
        ).get_port_of_discharge_in_wharfage()
        return

    def redirect_import_processing_fee(self):
        sys.stdout.write(prompt_var.prompt_ipf_confirmation_redirect)
        ComputeIPF(
            self.dutiable_frt, self.dutiable_ins, self.rate_of_exchange, self.total_dv
        ).get_user_confirmation()
        return

    def redirect_customs_documentary_stamp(self):
        sys.stdout.write(prompt_var.prompt_cds_type_redirect)
        ComputeCDS(
            self.type_of_entry
        ).compute_cds()
        return

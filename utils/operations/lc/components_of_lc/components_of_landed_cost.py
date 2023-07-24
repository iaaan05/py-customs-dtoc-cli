import sys

from landed_cost.components_of_landed_cost.customs_documentary_stamp.compute_customs_documentary_stamp import \
    ComputeCustomsDocumentaryStamp
from landed_cost.components_of_landed_cost.import_processing_fee.compute_import_processing_fee import \
    ComputeImportProcessingFee
from landed_cost.components_of_landed_cost.brokerage_fee.compute_brokerage_fee import ComputeBrokerageFeeFormalEntry
from landed_cost.components_of_landed_cost.customs_duty.compute_customs_duty import ComputeCustomsDuty
from landed_cost.components_of_landed_cost.bank_charge.compute_bank_charge import ComputeBankCharge
from utils.operations.lc.components_of_lc.dutiable_value_type import DutiableValueType
from utils.operations.lc.components_of_lc.port_of_discharge import PortofDischarge
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class ComponentsOfLandedCost:
    def __init__(self) -> None:
        self.dutiable_value = 1
        self.customs_duty = 2
        self.bank_charge = 3
        self.brokerage_fee = 4
        self.arrastre_charge = 5
        self.wharfage_due = 6
        self.import_processing_fee = 7
        self.customs_documentary_stamp = 8
        self.terminate_program = 9

    def get_component_of_landed_cost(self):
        rate_of_duty = 0
        total_dutiable_value = 0
        type_of_entry = 0

        valid_user_inputs = (self.dutiable_value, self.customs_duty, self.bank_charge,
                             self.brokerage_fee, self.arrastre_charge, self.wharfage_due,
                             self.import_processing_fee, self.customs_documentary_stamp,
                             self.terminate_program)
        while True:
            sys.stdout.write(prompt_var.prompt_components_lc_intro)
            user_input = ErrorandInput.get_input("Enter here:\n-> ")
            if user_input in valid_user_inputs:

                if user_input == self.terminate_program:
                    sys.stdout.write(prompt_var.prompt_terminate_program)
                    sys.exit()

                if user_input == self.dutiable_value:
                    sys.stdout.write(prompt_var.prompt_dutiable_value)
                    DutiableValueType().get_type_of_dutiable_value()
                    return

                elif user_input == self.customs_duty:
                    sys.stdout.write(prompt_var.prompt_cud_confirmation_redirect)
                    ComputeCustomsDuty(
                        rate_of_duty, total_dutiable_value
                    ).get_user_confirmation_customs_duty()
                    return

                elif user_input == self.bank_charge:
                    sys.stdout.write(prompt_var.prompt_bc_redirect)
                    ComputeBankCharge(
                        total_dutiable_value
                    ).get_user_confirmation_bank_charge()
                    return

                elif user_input == self.brokerage_fee:
                    sys.stdout.write(prompt_var.prompt_bf_redirect)
                    ComputeBrokerageFeeFormalEntry(
                        total_dutiable_value
                    ).get_user_confirmation_brokerage_fee_formal_entry()
                    return

                elif user_input == self.arrastre_charge:
                    sys.stdout.write(prompt_var.prompt_port_of_discharge_type_redirect)
                    PortofDischarge().get_port_of_discharge_in_arrastre()
                    return

                elif user_input == self.wharfage_due:
                    sys.stdout.write(prompt_var.prompt_port_of_discharge_type_redirect)
                    PortofDischarge().get_port_of_discharge_in_wharfage()
                    return

                elif user_input == self.import_processing_fee:
                    sys.stdout.write(prompt_var.prompt_ipf_confirmation_redirect)
                    ComputeImportProcessingFee(
                        total_dutiable_value
                    ).get_user_confirmation_import_processing_fee()
                    return

                elif user_input == self.customs_documentary_stamp:
                    sys.stdout.write(prompt_var.prompt_cds_type_redirect)
                    ComputeCustomsDocumentaryStamp(
                        type_of_entry
                    ).compute_customs_documentary_stamp()
                    return

            else:
                sys.stdout.write(prompt_var.prompt_invalid_input_1_to_9)

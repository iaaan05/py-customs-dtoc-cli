import sys

from customs_tax import SummaryOfPaymentsNonLetterOfCredit, SummaryOfPaymentsWithLetterOfCredit, \
    SummaryOfPaymentsWithInformalEntry
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class ComputeSummaryOfPaymentsWithLetterOfCredit:
    def __init__(self, customs_duty: float, value_added_tax: float, excise_tax: float,
                 import_processing_fee: float, customs_documentary_stamps: float, container_security_fee: float,
                 advance_deposit: float) -> None:
        self.customs_duty = customs_duty
        self.value_added_tax = value_added_tax
        self.excise_tax = excise_tax
        self.import_processing_fee = import_processing_fee
        self.customs_documentary_stamps = customs_documentary_stamps
        self.container_security_fee = container_security_fee
        self.advance_deposit = advance_deposit

    def get_sop_with_letter_of_credit_values(self) -> tuple[float, float, float, float, float, float, float]:
        sys.stdout.write(prompt_var.prompt_sop_lc)
        self.customs_duty = ErrorandInput.get_input(prompt_var.prompt_customs_duty)
        self.value_added_tax = ErrorandInput.get_input(prompt_var.prompt_value_added_tax)
        self.excise_tax = ErrorandInput.get_input(prompt_var.prompt_excise_tax)
        self.import_processing_fee = ErrorandInput.get_input(prompt_var.prompt_import_processing_fee)
        self.customs_documentary_stamps = ErrorandInput.get_input(prompt_var.prompt_customs_documentary_stamps)
        self.container_security_fee = ErrorandInput.get_input(prompt_var.prompt_container_security_fee)
        self.advance_deposit = ErrorandInput.get_input(prompt_var.prompt_advance_deposit)
        return self.customs_duty, self.value_added_tax, self.excise_tax, self.import_processing_fee, \
            self.customs_documentary_stamps, self.container_security_fee, self.advance_deposit

    def compute_sop_with_letter_of_credit(self) -> None:
        values = self.get_sop_with_letter_of_credit_values()
        total_net_amount_payable = SummaryOfPaymentsWithLetterOfCredit(*values)
        total_net_amount_payable = total_net_amount_payable. \
            calculate_sop_with_letter_of_credit()
        sys.stdout.write(f'Total Net Amount Payable: P{total_net_amount_payable}\n')
        return


class ComputeSummaryOfPaymentsNonLetterOfCredit:
    def __init__(self, customs_duty: float, value_added_tax: float, excise_tax: float,
                 import_processing_fee: float, customs_documentary_stamps: float,
                 container_security_fee: float) -> None:
        self.customs_duty = customs_duty
        self.value_added_tax = value_added_tax
        self.excise_tax = excise_tax
        self.import_processing_fee = import_processing_fee
        self.customs_documentary_stamps = customs_documentary_stamps
        self.container_security_fee = container_security_fee

    def get_sop_with_non_letter_of_credit_values(self) -> tuple[float, float, float, float, float, float]:
        sys.stdout.write(prompt_var.prompt_sop_non_lc)
        self.customs_duty = ErrorandInput.get_input(prompt_var.prompt_customs_duty)
        self.value_added_tax = ErrorandInput.get_input(prompt_var.prompt_value_added_tax)
        self.excise_tax = ErrorandInput.get_input(prompt_var.prompt_excise_tax)
        self.import_processing_fee = ErrorandInput.get_input(prompt_var.prompt_import_processing_fee)
        self.customs_documentary_stamps = ErrorandInput.get_input(prompt_var.prompt_customs_documentary_stamps)
        self.container_security_fee = ErrorandInput.get_input(prompt_var.prompt_container_security_fee)
        return self.customs_duty, self.value_added_tax, self.excise_tax, self.import_processing_fee, \
            self.customs_documentary_stamps, self.container_security_fee,

    def compute_sop_with_non_letter_of_credit(self) -> None:
        values = self.get_sop_with_non_letter_of_credit_values()
        total_duties_taxes_other_charges = SummaryOfPaymentsNonLetterOfCredit(*values)
        total_duties_taxes_other_charges = total_duties_taxes_other_charges. \
            calculate_sop_non_letter_of_credit()
        sys.stdout.write(f'Total Duties, Taxes and Other Charges: P{total_duties_taxes_other_charges}\n')
        return


class ComputeSummaryOfPaymentsWithInformalEntry:
    def __init__(self, customs_duty: float, value_added_tax: float, excise_tax: float,
                 customs_documentary_stamps: float) -> None:
        self.customs_duty = customs_duty
        self.value_added_tax = value_added_tax
        self.excise_tax = excise_tax
        self.customs_documentary_stamps = customs_documentary_stamps

    def get_sop_with_informal_entry_values(self) -> tuple[float, float, float, float]:
        sys.stdout.write(prompt_var.prompt_sop_informal_entry)
        self.customs_duty = ErrorandInput.get_input(prompt_var.prompt_customs_duty)
        self.value_added_tax = ErrorandInput.get_input(prompt_var.prompt_value_added_tax)
        self.excise_tax = ErrorandInput.get_input(prompt_var.prompt_excise_tax)
        self.customs_documentary_stamps = ErrorandInput.get_input(prompt_var.prompt_customs_documentary_stamps)
        return self.customs_duty, self.value_added_tax, self.excise_tax, self.customs_documentary_stamps,

    def compute_sop_with_informal_entry(self) -> None:
        values = self.get_sop_with_informal_entry_values()
        total_duties_taxes_other_charges = SummaryOfPaymentsWithInformalEntry(*values)
        total_duties_taxes_other_charges = total_duties_taxes_other_charges. \
            calculate_sop_with_informal_entry()
        sys.stdout.write(f'Total Duties, Taxes and Other Charges: P{total_duties_taxes_other_charges}\n')
        return

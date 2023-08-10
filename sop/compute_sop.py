import sys

from customs_dtoc import SummaryOfPaymentsNonLetterOfCredit, SummaryOfPaymentsWithLetterOfCredit, \
    SummaryOfPaymentsWithInformalEntry
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class ComputeSOPWithLetterOfCredit:
    def __init__(self, cud: float, vat: float, excise_tax: float, ipf: float, cds: float, csf: float,
                 advance_deposit: float) -> None:
        self.cud = cud
        self.vat = vat
        self.excise_tax = excise_tax
        self.ipf = ipf
        self.cds = cds
        self.csf = csf
        self.advance_deposit = advance_deposit

    def get_sop_with_lc_values(self) -> tuple[float, float, float, float, float, float, float]:
        sys.stdout.write(prompt_var.prompt_sop_lc)
        self.cud = ErrorandInput.get_input(prompt_var.prompt_cud)
        self.vat = ErrorandInput.get_input(prompt_var.prompt_vat)
        self.excise_tax = ErrorandInput.get_input(prompt_var.prompt_excise_tax)
        self.ipf = ErrorandInput.get_input(prompt_var.prompt_ipf)
        self.cds = ErrorandInput.get_input(prompt_var.prompt_cds)
        self.csf = ErrorandInput.get_input(prompt_var.prompt_csf)
        self.advance_deposit = ErrorandInput.get_input(prompt_var.prompt_advance_deposit)
        return self.cud, self.vat, self.excise_tax, self.ipf, self.cds, self.csf, self.advance_deposit

    def compute_sop_with_lc(self) -> None:
        values = self.get_sop_with_lc_values()
        total_net_amount_payable = SummaryOfPaymentsWithLetterOfCredit(*values)
        total_net_amount_payable = total_net_amount_payable.calculate_sop_with_letter_of_credit()
        sys.stdout.write(f'Total Net Amount Payable: P{total_net_amount_payable}\n')
        return


class ComputeSOPNonLetterOfCredit:
    def __init__(self, cud: float, vat: float, excise_tax: float, ipf: float, cds: float, csf: float) -> None:
        self.cud = cud
        self.vat = vat
        self.excise_tax = excise_tax
        self.ipf = ipf
        self.cds = cds
        self.csf = csf

    def get_sop_non_lc_values(self) -> tuple[float, float, float, float, float, float]:
        sys.stdout.write(prompt_var.prompt_sop_non_lc)
        self.cud = ErrorandInput.get_input(prompt_var.prompt_cud)
        self.vat = ErrorandInput.get_input(prompt_var.prompt_vat)
        self.excise_tax = ErrorandInput.get_input(prompt_var.prompt_excise_tax)
        self.ipf = ErrorandInput.get_input(prompt_var.prompt_ipf)
        self.cds = ErrorandInput.get_input(prompt_var.prompt_cds)
        self.csf = ErrorandInput.get_input(prompt_var.prompt_csf)
        return self.cud, self.vat, self.excise_tax, self.ipf, self.cds, self.csf,

    def compute_sop_non_lc(self) -> None:
        values = self.get_sop_non_lc_values()
        total_duties_taxes_other_charges = SummaryOfPaymentsNonLetterOfCredit(*values)
        total_duties_taxes_other_charges = total_duties_taxes_other_charges.calculate_sop_non_letter_of_credit()
        sys.stdout.write(f'Total Duties, Taxes and Other Charges: P{total_duties_taxes_other_charges}\n')
        return


class ComputeSOPWithInformalEntry:
    def __init__(self, cud: float, vat: float, excise_tax: float, cds: float) -> None:
        self.cud = cud
        self.vat = vat
        self.excise_tax = excise_tax
        self.cds = cds

    def get_sop_with_informal_entry_values(self) -> tuple[float, float, float, float]:
        sys.stdout.write(prompt_var.prompt_sop_informal_entry)
        self.cud = ErrorandInput.get_input(prompt_var.prompt_cud)
        self.vat = ErrorandInput.get_input(prompt_var.prompt_vat)
        self.excise_tax = ErrorandInput.get_input(prompt_var.prompt_excise_tax)
        self.cds = ErrorandInput.get_input(prompt_var.prompt_cds)
        return self.cud, self.vat, self.excise_tax, self.cds,

    def compute_sop_with_informal_entry(self) -> None:
        values = self.get_sop_with_informal_entry_values()
        total_duties_taxes_other_charges = SummaryOfPaymentsWithInformalEntry(*values)
        total_duties_taxes_other_charges = total_duties_taxes_other_charges.calculate_sop_with_informal_entry()
        sys.stdout.write(f'Total Duties, Taxes and Other Charges: P{total_duties_taxes_other_charges}\n')
        return

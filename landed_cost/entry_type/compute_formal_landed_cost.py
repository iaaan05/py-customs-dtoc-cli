import sys

from customs_tax import LandedCostBySeaViaFormalEntry, LandedCostByAirViaFormalEntry
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class ComputeLandedCostBySea:
    def __init__(self, dutiable_value: float, customs_duty: float, bank_charge: float, brokerage_fee: float,
                 arrastre_charge: float, wharfage_due: float, import_processing_fee: float,
                 customs_documentary_stamps: float) -> None:
        self.dutiable_value = dutiable_value
        self.customs_duty = customs_duty
        self.bank_charge = bank_charge
        self.brokerage_fee = brokerage_fee
        self.arrastre_charge = arrastre_charge
        self.wharfage_due = wharfage_due
        self.import_processing_fee = import_processing_fee
        self.customs_documentary_stamps = customs_documentary_stamps

    def get_landed_cost_by_sea_values(self) -> tuple[float, float, float, float, float, float, float, float]:
        sys.stdout.write(prompt_var.prompt_lc_formal_sea)
        self.dutiable_value = ErrorandInput.get_input(prompt_var.prompt_dutiable_value)
        self.customs_duty = ErrorandInput.get_input(prompt_var.prompt_customs_duty)
        self.bank_charge = ErrorandInput.get_input(prompt_var.prompt_bank_charge)
        self.brokerage_fee = ErrorandInput.get_input(prompt_var.prompt_brokerage_fee)
        self.arrastre_charge = ErrorandInput.get_input(prompt_var.prompt_arrastre_charge)
        self.wharfage_due = ErrorandInput.get_input(prompt_var.prompt_wharfage_due)
        self.import_processing_fee = ErrorandInput.get_input(prompt_var.prompt_import_processing_fee)
        self.customs_documentary_stamps = ErrorandInput.get_input(prompt_var.prompt_customs_documentary_stamps)
        return self.dutiable_value, self.customs_duty, self.bank_charge, self.brokerage_fee, self.arrastre_charge, \
            self.wharfage_due, self.import_processing_fee, self.customs_documentary_stamps

    def compute_landed_cost_by_sea(self) -> None:
        values = self.get_landed_cost_by_sea_values()
        total_landed_cost_by_sea_formal = LandedCostBySeaViaFormalEntry(*values)
        total_landed_cost_by_sea_formal = total_landed_cost_by_sea_formal.calculate_landed_cost_by_sea()
        sys.stdout.write(f'Total Landed Cost: P{total_landed_cost_by_sea_formal}\n')
        return


class ComputeLandedCostByAir:
    def __init__(self, dutiable_value: float, customs_duty: float, bank_charge: float, brokerage_fee: float,
                 import_processing_fee: float, customs_documentary_stamps: float) -> None:
        self.dutiable_value = dutiable_value
        self.customs_duty = customs_duty
        self.bank_charge = bank_charge
        self.brokerage_fee = brokerage_fee
        self.import_processing_fee = import_processing_fee
        self.customs_documentary_stamps = customs_documentary_stamps

    def get_landed_cost_by_air_values(self) -> tuple[float, float, float, float, float, float]:
        sys.stdout.write(prompt_var.prompt_lc_formal_air)
        self.dutiable_value = ErrorandInput.get_input(prompt_var.prompt_dutiable_value)
        self.customs_duty = ErrorandInput.get_input(prompt_var.prompt_customs_duty)
        self.bank_charge = ErrorandInput.get_input(prompt_var.prompt_bank_charge)
        self.brokerage_fee = ErrorandInput.get_input(prompt_var.prompt_brokerage_fee)
        self.import_processing_fee = ErrorandInput.get_input(prompt_var.prompt_import_processing_fee)
        self.customs_documentary_stamps = ErrorandInput.get_input(prompt_var.prompt_customs_documentary_stamps)
        return self.dutiable_value, self.customs_duty, self.bank_charge, self.brokerage_fee, \
            self.import_processing_fee, self.customs_documentary_stamps

    def compute_landed_cost_by_air(self) -> None:
        values = self.get_landed_cost_by_air_values()
        total_landed_cost_by_air_formal = LandedCostByAirViaFormalEntry(*values)
        total_landed_cost_by_air_formal = total_landed_cost_by_air_formal.calculate_landed_cost_by_air()
        sys.stdout.write(f'Total Landed Cost: P{total_landed_cost_by_air_formal}\n')
        return

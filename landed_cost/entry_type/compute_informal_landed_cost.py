import sys

from customs_tax import LandedCostViaInformalEntry
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class ComputeLandedCostViaInformalEntry:
    def __init__(self, dutiable_value: float, customs_duty: float, brokerage_fee: float,
                 customs_documentary_stamps: float) -> None:
        self.dutiable_value = dutiable_value
        self.customs_duty = customs_duty
        self.brokerage_fee = brokerage_fee
        self.customs_documentary_stamps = customs_documentary_stamps

    def get_landed_cost_via_informal_entry_values(self) -> tuple[float, float, float, float]:
        sys.stdout.write(prompt_var.prompt_lc_informal)
        self.dutiable_value = ErrorandInput.get_input(prompt_var.prompt_dutiable_value)
        self.customs_duty = ErrorandInput.get_input(prompt_var.prompt_customs_duty)
        self.brokerage_fee = ErrorandInput.get_input(prompt_var.prompt_brokerage_fee)
        self.customs_documentary_stamps = ErrorandInput.get_input(prompt_var.prompt_customs_documentary_stamps)
        return self.dutiable_value, self.customs_duty, self.brokerage_fee, self.customs_documentary_stamps

    def compute_landed_cost_via_informal_entry(self) -> None:
        values = self.get_landed_cost_via_informal_entry_values()
        total_landed_cost_informal = LandedCostViaInformalEntry(*values)
        total_landed_cost_informal = total_landed_cost_informal.calculate_landed_cost_via_informal_entry()
        sys.stdout.write(f'Total Landed Cost: P{total_landed_cost_informal}\n')
        return

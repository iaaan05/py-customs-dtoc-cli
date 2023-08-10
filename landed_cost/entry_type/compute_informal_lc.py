import sys

from utils.error_handling_and_input_validation import ErrorandInput
from customs_dtoc import LandedCostViaInformalEntry
from utils import prompt_var


class ComputeLCViaInformalEntry:
    def __init__(self, dv: float, cud: float, bf: float, cds: float) -> None:
        self.dv = dv
        self.cud = cud
        self.bf = bf
        self.cds = cds

    def get_lc_via_informal_entry_values(self) -> tuple[float, float, float, float]:
        sys.stdout.write(prompt_var.prompt_lc_informal)
        self.dv = ErrorandInput.get_input(prompt_var.prompt_dv)
        self.cud = ErrorandInput.get_input(prompt_var.prompt_cud)
        self.bf = ErrorandInput.get_input(prompt_var.prompt_bf)
        self.cds = ErrorandInput.get_input(prompt_var.prompt_cds)
        return self.dv, self.cud, self.bf, self.cds

    def compute_lc_via_informal_entry(self) -> None:
        values = self.get_lc_via_informal_entry_values()
        total_lc = LandedCostViaInformalEntry(*values)
        total_lc = total_lc.calculate_landed_cost_via_informal_entry()
        sys.stdout.write(f'Total Landed Cost: P{total_lc}\n')
        return

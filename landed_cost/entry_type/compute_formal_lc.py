import sys

from customs_dtoc import LandedCostBySeaViaFormalEntry, LandedCostByAirViaFormalEntry
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class ComputeLCViaSea:
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

    def get_lc_via_sea_values(self) -> tuple[float, float, float, float, float, float, float, float]:
        sys.stdout.write(prompt_var.prompt_lc_formal_sea)
        self.dv = ErrorandInput.get_input(prompt_var.prompt_dv)
        self.cud = ErrorandInput.get_input(prompt_var.prompt_cud)
        self.bc = ErrorandInput.get_input(prompt_var.prompt_bc)
        self.bf = ErrorandInput.get_input(prompt_var.prompt_bf)
        self.ac = ErrorandInput.get_input(prompt_var.prompt_ac)
        self.wd = ErrorandInput.get_input(prompt_var.prompt_wd)
        self.ipf = ErrorandInput.get_input(prompt_var.prompt_ipf)
        self.cds = ErrorandInput.get_input(prompt_var.prompt_cds)
        return self.dv, self.cud, self.bc, self.bf, self.ac, self.wd, self.ipf, self.cds

    def compute_lc_via_sea(self) -> None:
        values = self.get_lc_via_sea_values()
        total_lc = LandedCostBySeaViaFormalEntry(*values)
        total_lc = total_lc.calculate_landed_cost_by_sea()
        sys.stdout.write(f'Total Landed Cost: P{total_lc}\n')
        return


class ComputeLCViaAir:
    def __init__(self, dv: float, cud: float, bc: float, bf: float, ipf: float, cds: float) -> None:
        self.dv = dv
        self.cud = cud
        self.bc = bc
        self.bf = bf
        self.ipf = ipf
        self.cds = cds

    def get_lc_via_air_values(self) -> tuple[float, float, float, float, float, float]:
        sys.stdout.write(prompt_var.prompt_lc_formal_air)
        self.dv = ErrorandInput.get_input(prompt_var.prompt_dv)
        self.cud = ErrorandInput.get_input(prompt_var.prompt_cud)
        self.bc = ErrorandInput.get_input(prompt_var.prompt_bc)
        self.bf = ErrorandInput.get_input(prompt_var.prompt_bf)
        self.ipf = ErrorandInput.get_input(prompt_var.prompt_ipf)
        self.cds = ErrorandInput.get_input(prompt_var.prompt_cds)
        return self.dv, self.cud, self.bc, self.bf, self.ipf, self.cds

    def compute_lc_via_air(self) -> None:
        values = self.get_lc_via_air_values()
        total_lc = LandedCostByAirViaFormalEntry(*values)
        total_lc = total_lc.calculate_landed_cost_by_air()
        sys.stdout.write(f'Total Landed Cost: P{total_lc}\n')
        return

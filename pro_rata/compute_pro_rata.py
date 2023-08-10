import sys

from customs_dtoc import ProRataIndividualFreight, ProRataIndividualInsurance, ProRataIndividualDutiableValue, \
    ProRataIndividualMiscExpenses
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class ComputeProRataIndividual:
    def __init__(self, individual_fob: float, total_fob: float) -> None:
        self.individual_fob = individual_fob
        self.total_fob = total_fob


class ComputeProRataFreight(ComputeProRataIndividual):
    def __init__(self, individual_fob: float, total_fob: float) -> None:
        super().__init__(individual_fob, total_fob)
        self.total_frt = float

    def get_pro_rata_frt_values(self) -> tuple[float, float, float]:
        sys.stdout.write(prompt_var.prompt_frt_pro_rata)
        self.individual_fob = ErrorandInput.get_input(prompt_var.prompt_individual_fob)
        self.total_fob = ErrorandInput.get_input(prompt_var.prompt_total_fob)
        self.total_frt = ErrorandInput.get_input(prompt_var.prompt_total_frt)
        return self.individual_fob, self.total_fob, self.total_frt

    def compute_pro_rata_frt(self) -> None:
        values = self.get_pro_rata_frt_values()
        pro_rata_frt = ProRataIndividualFreight(*values)
        pro_rata_frt = pro_rata_frt.calculate_pro_rata_individual_freight()
        sys.stdout.write(f'Individual Freight: ${pro_rata_frt}\n')
        return


class ComputeProRataInsurance(ComputeProRataIndividual):
    def __init__(self, individual_fob: float, total_fob: float) -> None:
        super().__init__(individual_fob, total_fob)
        self.total_ins = float

    def get_pro_rata_ins_values(self) -> tuple[float, float, float]:
        sys.stdout.write(prompt_var.prompt_ins_pro_rata)
        self.individual_fob = ErrorandInput.get_input(prompt_var.prompt_individual_fob)
        self.total_fob = ErrorandInput.get_input(prompt_var.prompt_total_fob)
        self.total_ins = ErrorandInput.get_input(prompt_var.prompt_total_ins)
        return self.individual_fob, self.total_fob, self.total_ins

    def compute_pro_rata_ins(self) -> None:
        values = self.get_pro_rata_ins_values()
        pro_rata_ins = ProRataIndividualInsurance(*values)
        pro_rata_ins = pro_rata_ins.calculate_pro_rata_individual_insurance()
        sys.stdout.write(f'Individual Insurance: ${pro_rata_ins}\n')
        return


class ComputeProRataDutiableValue(ComputeProRataIndividual):
    def __init__(self, individual_fob: float, total_fob: float) -> None:
        super().__init__(individual_fob, total_fob)
        self.total_dutiable_value = float

    def get_pro_rata_dv_values(self) -> tuple[float, float, float]:
        sys.stdout.write(prompt_var.prompt_dv_pro_rata)
        self.individual_fob = ErrorandInput.get_input(prompt_var.prompt_individual_fob)
        self.total_fob = ErrorandInput.get_input(prompt_var.prompt_total_fob)
        self.total_dutiable_value = ErrorandInput.get_input(prompt_var.prompt_total_dv)
        return self.individual_fob, self.total_fob, self.total_dutiable_value

    def compute_pro_rata_dv(self) -> None:
        values = self.get_pro_rata_dv_values()
        pro_rata_dv = ProRataIndividualDutiableValue(*values)
        pro_rata_dv = pro_rata_dv.calculate_pro_rata_individual_dutiable_value()
        sys.stdout.write(f'Individual Dutiable Value: P{pro_rata_dv}\n')
        return


class ComputeProRataMiscExpenses(ComputeProRataIndividual):
    def __init__(self, individual_fob: float, total_fob: float) -> None:
        super().__init__(individual_fob, total_fob)
        self.total_misc_expenses = float

    def get_pro_rata_misc_expenses_values(self) -> tuple[float, float, float]:
        sys.stdout.write(prompt_var.prompt_me_pro_rata)
        self.individual_fob = ErrorandInput.get_input(prompt_var.prompt_individual_fob)
        self.total_fob = ErrorandInput.get_input(prompt_var.prompt_total_fob)
        self.total_misc_expenses = ErrorandInput.get_input(prompt_var.prompt_total_misc_expenses)
        return self.individual_fob, self.total_fob, self.total_misc_expenses

    def compute_pro_rata_misc_expenses(self) -> None:
        values = self.get_pro_rata_misc_expenses_values()
        pro_rata_misc_expenses = ProRataIndividualMiscExpenses(*values)
        pro_rata_misc_expenses = pro_rata_misc_expenses.calculate_pro_rata_individual_misc_expenses()
        sys.stdout.write(f'Individual Miscellaneous Expenses: P{pro_rata_misc_expenses}\n')
        return

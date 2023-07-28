import sys

from customs_tax import ProRataIndividualFreight, ProRataIndividualInsurance, ProRataIndividualDutiableValue, \
    ProRataIndividualMiscExpenses
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class ComputeProRataIndividual:
    def __init__(self, individual_fob: float, total_fob: float) -> None:
        self.individual_fob = individual_fob
        self.total_fob = total_fob


class ComputeProRataIndividualFreight(ComputeProRataIndividual):
    def __init__(self, individual_fob: float, total_fob: float) -> None:
        super().__init__(individual_fob, total_fob)
        self.total_frt = float

    def get_pro_rata_individual_freight_values(self) -> tuple[float, float, float]:
        sys.stdout.write(prompt_var.prompt_frt_pro_rata)
        self.individual_fob = ErrorandInput.get_input(prompt_var.prompt_individual_fob)
        self.total_fob = ErrorandInput.get_input(prompt_var.prompt_total_fob)
        self.total_frt = ErrorandInput.get_input(prompt_var.prompt_total_frt)
        return self.individual_fob, self.total_fob, self.total_frt

    def compute_pro_rata_individual_freight(self) -> None:
        values = self.get_pro_rata_individual_freight_values()
        pro_rata_individual_freight = ProRataIndividualFreight(*values)
        pro_rata_individual_freight = pro_rata_individual_freight.calculate_pro_rata_individual_freight()
        sys.stdout.write(f'Individual Freight: ${pro_rata_individual_freight}\n')
        return


class ComputeProRataIndividualInsurance(ComputeProRataIndividual):
    def __init__(self, individual_fob: float, total_fob: float) -> None:
        super().__init__(individual_fob, total_fob)
        self.total_ins = float

    def get_pro_rata_individual_insurance_values(self) -> tuple[float, float, float]:
        sys.stdout.write(prompt_var.prompt_ins_pro_rata)
        self.individual_fob = ErrorandInput.get_input(prompt_var.prompt_individual_fob)
        self.total_fob = ErrorandInput.get_input(prompt_var.prompt_total_fob)
        self.total_ins = ErrorandInput.get_input(prompt_var.prompt_total_ins)
        return self.individual_fob, self.total_fob, self.total_ins

    def compute_pro_rata_individual_insurance(self) -> None:
        values = self.get_pro_rata_individual_insurance_values()
        pro_rata_individual_insurance = ProRataIndividualInsurance(*values)
        pro_rata_individual_insurance = pro_rata_individual_insurance.calculate_pro_rata_individual_insurance()
        sys.stdout.write(f'Individual Insurance: ${pro_rata_individual_insurance}\n')
        return


class ComputeProRataIndividualDutiableValue(ComputeProRataIndividual):
    def __init__(self, individual_fob: float, total_fob: float) -> None:
        super().__init__(individual_fob, total_fob)
        self.total_dutiable_value = float

    def get_pro_rata_individual_dutiable_value_values(self) -> tuple[float, float, float]:
        sys.stdout.write(prompt_var.prompt_dv_pro_rata)
        self.individual_fob = ErrorandInput.get_input(prompt_var.prompt_individual_fob)
        self.total_fob = ErrorandInput.get_input(prompt_var.prompt_total_fob)
        self.total_dutiable_value = ErrorandInput.get_input(prompt_var.prompt_total_dutiable_value)
        return self.individual_fob, self.total_fob, self.total_dutiable_value

    def compute_pro_rata_individual_dutiable_value(self) -> None:
        values = self.get_pro_rata_individual_dutiable_value_values()
        pro_rata_individual_dutiable_value = ProRataIndividualDutiableValue(*values)
        pro_rata_individual_dutiable_value = pro_rata_individual_dutiable_value. \
            calculate_pro_rata_individual_dutiable_value()
        sys.stdout.write(f'Individual Dutiable Value: P{pro_rata_individual_dutiable_value}\n')
        return


class ComputeProRataIndividualMiscExpenses(ComputeProRataIndividual):
    def __init__(self, individual_fob: float, total_fob: float) -> None:
        super().__init__(individual_fob, total_fob)
        self.total_misc_expenses = float

    def get_pro_rata_individual_misc_expenses_values(self) -> tuple[float, float, float]:
        sys.stdout.write(prompt_var.prompt_me_pro_rata)
        self.individual_fob = ErrorandInput.get_input(prompt_var.prompt_individual_fob)
        self.total_fob = ErrorandInput.get_input(prompt_var.prompt_total_fob)
        self.total_misc_expenses = ErrorandInput.get_input(prompt_var.prompt_total_misc_expenses)
        return self.individual_fob, self.total_fob, self.total_misc_expenses

    def compute_pro_rata_individual_misc_expenses(self) -> None:
        values = self.get_pro_rata_individual_misc_expenses_values()
        pro_rata_individual_misc_expenses = ProRataIndividualMiscExpenses(*values)
        pro_rata_individual_misc_expenses = pro_rata_individual_misc_expenses. \
            calculate_pro_rata_individual_misc_expenses()
        sys.stdout.write(f'Individual Miscellaneous Expenses: P{pro_rata_individual_misc_expenses}\n')
        return

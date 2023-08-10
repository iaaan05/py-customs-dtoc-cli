import sys

from utils.error_handling_and_input_validation import ErrorandInput
from customs_dtoc import CSF20Footer, CSF40Footer
from utils import prompt_var


class ContainerSecurityFee:
    def __init__(self, number_of_containers: float, rate_of_exchange: float) -> None:
        self.number_of_containers = number_of_containers
        self.rate_of_exchange = rate_of_exchange

    def get_csf_values(self) -> tuple[float, float]:
        self.number_of_containers = ErrorandInput.get_input(prompt_var.prompt_number_of_containers)
        self.rate_of_exchange = ErrorandInput.get_input(prompt_var.prompt_rate_of_exchange)
        return self.number_of_containers, self.rate_of_exchange


class ComputeCSF20Footer(ContainerSecurityFee):
    def compute_csf_20_footer(self, number_of_containers: float, rate_of_exchange: float) -> None:
        super().__init__(number_of_containers, rate_of_exchange)

        sys.stdout.write(prompt_var.prompt_csf_20)
        values = self.get_csf_values()
        total_csf = CSF20Footer(*values)
        total_csf = total_csf.calculate_csf_20_footer()
        sys.stdout.write(f'Total Container Security Fee: P{total_csf}\n')
        return


class ComputeCSF40Footer(ContainerSecurityFee):
    def compute_csf_40_footer(self, number_of_containers: float, rate_of_exchange: float) -> None:
        super().__init__(number_of_containers, rate_of_exchange)

        sys.stdout.write(prompt_var.prompt_csf_40)
        values = self.get_csf_values()
        total_csf = CSF40Footer(*values)
        total_csf = total_csf.calculate_csf_40_footer()
        sys.stdout.write(f'Total Container Security Fee: P{total_csf}\n')
        return

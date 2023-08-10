import sys

from customs_dtoc import WDContainerizedDangerousCargo20Footer, WDContainerizedDangerousCargo40Footer
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class WDContainerizedDangerousCargo:
    def __init__(self, number_of_containers: float) -> None:
        self.number_of_containers = number_of_containers

    def get_dangerous_cargo_footer_values(self) -> float:
        self.number_of_containers = ErrorandInput.get_input(prompt_var.prompt_number_of_containers)
        return self.number_of_containers


class WDComputeDangerousCargo20Footer(WDContainerizedDangerousCargo):
    def get_dangerous_cargo_20_footer_values(self) -> float:
        sys.stdout.write(prompt_var.prompt_wd_dangerous_20_footer)
        return self.get_dangerous_cargo_footer_values()

    def compute_dangerous_cargo_20_footer(self) -> None:
        values = self.get_dangerous_cargo_20_footer_values()
        total_wd = WDContainerizedDangerousCargo20Footer(values)
        total_wd = total_wd.calculate_containerized_dangerous_cargo_20_footer()
        sys.stdout.write(f'Total Wharfage Due: P{total_wd}\n')
        return


class WDComputeDangerousCargo40Footer(WDContainerizedDangerousCargo):
    def get_dangerous_cargo_40_footer_values(self) -> float:
        sys.stdout.write(prompt_var.prompt_wd_dangerous_40_footer)
        return self.get_dangerous_cargo_footer_values()

    def compute_dangerous_cargo_40_footer(self) -> None:
        values = self.get_dangerous_cargo_40_footer_values()
        total_wd = WDContainerizedDangerousCargo40Footer(values)
        total_wd = total_wd.calculate_containerized_dangerous_cargo_40_footer()
        sys.stdout.write(f'Total Wharfage Due: P{total_wd}\n')
        return

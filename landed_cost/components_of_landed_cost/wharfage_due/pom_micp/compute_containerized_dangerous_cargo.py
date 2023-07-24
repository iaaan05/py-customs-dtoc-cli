import sys

from customs_tax import WDContainerizedDangerousCargo20Footer, WDContainerizedDangerousCargo40Footer
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class WDContainerizedDangerousCargo:
    def __init__(self, total_number_of_containers: float) -> None:
        self.total_number_of_containers = total_number_of_containers

    def get_fcl_footer_values(self) -> float:
        self.total_number_of_containers = ErrorandInput.get_input(prompt_var.prompt_number_of_containers)
        return self.total_number_of_containers


class WDComputeContainerizedDangerousCargo20Footer(WDContainerizedDangerousCargo):
    def __init__(self, total_number_of_containers) -> None:
        super().__init__(total_number_of_containers)
        self.total_number_of_containers = total_number_of_containers

    def get_containerized_dangerous_cargo_20_footer_values(self) -> float:
        sys.stdout.write(prompt_var.prompt_wd_dangerous_20_footer)
        return self.get_fcl_footer_values()

    def compute_containerized_dangerous_cargo_20_footer(self) -> None:
        values = self.get_containerized_dangerous_cargo_20_footer_values()
        total_wharfage_due = WDContainerizedDangerousCargo20Footer(values)
        total_wharfage_due = total_wharfage_due.calculate_containerized_dangerous_cargo_20_footer()
        sys.stdout.write(f'Total Wharfage Due: P{total_wharfage_due}\n')
        return


class WDComputeContainerizedDangerousCargo40Footer(WDContainerizedDangerousCargo):
    def __init__(self, total_number_of_containers) -> None:
        super().__init__(total_number_of_containers)
        self.total_number_of_containers = total_number_of_containers

    def get_containerized_dangerous_cargo_40_footer_values(self) -> float:
        sys.stdout.write(prompt_var.prompt_wd_dangerous_40_footer)
        return self.get_fcl_footer_values()

    def compute_containerized_dangerous_cargo_40_footer(self) -> None:
        values = self.get_containerized_dangerous_cargo_40_footer_values()
        total_wharfage_due = WDContainerizedDangerousCargo40Footer(values)
        total_wharfage_due = total_wharfage_due.calculate_containerized_dangerous_cargo_40_footer()
        sys.stdout.write(f'Total Wharfage Due: P{total_wharfage_due}\n')
        return

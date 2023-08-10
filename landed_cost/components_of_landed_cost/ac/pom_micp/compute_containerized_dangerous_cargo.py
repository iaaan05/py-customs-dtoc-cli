import sys

from customs_dtoc import ACContainerizedDangerousCargo20Footer, ACContainerizedDangerousCargo40Footer
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class ACContainerizedDangerousCargo:
    def __init__(self, classification_of_dangerous_cargo: float, number_of_containers: float) -> None:
        self.classification_of_dangerous_cargo = classification_of_dangerous_cargo
        self.number_of_containers = number_of_containers

    def get_containerized_dangerous_values(self) -> tuple[float, float]:
        self.classification_of_dangerous_cargo = ErrorandInput.get_input(prompt_var.prompt_ac_class_cargo)
        self.number_of_containers = ErrorandInput.get_input(prompt_var.prompt_number_of_containers)
        return self.classification_of_dangerous_cargo, self.number_of_containers


class ACComputeDangerousCargo20Footer(ACContainerizedDangerousCargo):
    def get_dangerous_cargo_20_footer_values(self) -> tuple[float, float]:
        sys.stdout.write(prompt_var.prompt_ac_dangerous_intro)
        return self.get_containerized_dangerous_values()

    def compute_dangerous_cargo_20_footer(self) -> None:
        values = self.get_dangerous_cargo_20_footer_values()
        total_ac = ACContainerizedDangerousCargo20Footer(*values)
        total_ac = total_ac.calculate_fcl_20_footer()
        sys.stdout.write(f'Total Arrastre Charge: P{total_ac}\n')
        return


class ACComputeDangerousCargo40Footer(ACContainerizedDangerousCargo):
    def get_dangerous_cargo_40_footer_values(self) -> tuple[float, float]:
        sys.stdout.write(prompt_var.prompt_ac_dangerous_intro)
        return self.get_containerized_dangerous_values()

    def compute_dangerous_cargo_40_footer(self) -> None:
        values = self.get_dangerous_cargo_40_footer_values()
        total_ac = ACContainerizedDangerousCargo40Footer(*values)
        total_ac = total_ac.calculate_fcl_40_footer()
        sys.stdout.write(f'Total Arrastre Charge: P{total_ac}\n')
        return

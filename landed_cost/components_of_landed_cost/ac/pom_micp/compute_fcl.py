import sys

from customs_dtoc import ACContainerizedCargoImport, ACContainerizedCargoExport, \
    ACContainerizedCargoShutOutExport
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class ACContainerizedCargo:
    def __init__(self, size_of_container: float, number_of_containers: float) -> None:
        self.size_of_container = size_of_container
        self.number_of_containers = number_of_containers

    def get_fcl_values(self) -> tuple[float, float]:
        self.size_of_container = ErrorandInput.get_input(prompt_var.prompt_size_of_container)
        self.number_of_containers = ErrorandInput.get_input(prompt_var.prompt_number_of_containers)
        return self.size_of_container, self.number_of_containers


class ACComputeFCLImport(ACContainerizedCargo):
    def get_fcl_import_values(self) -> tuple[float, float]:
        sys.stdout.write(prompt_var.prompt_fcl_import)
        return self.get_fcl_values()

    def compute_fcl_import(self) -> None:
        values = self.get_fcl_import_values()
        total_ac = ACContainerizedCargoImport(*values)
        total_ac = total_ac.calculate_fcl_import()
        sys.stdout.write(f'Total Arrastre Charge: P{total_ac}\n')
        return


class ACComputeFCLExport(ACContainerizedCargo):
    def get_fcl_export_values(self) -> tuple[float, float]:
        sys.stdout.write(prompt_var.prompt_fcl_export)
        return self.get_fcl_values()

    def compute_fcl_export(self) -> None:
        values = self.get_fcl_export_values()
        total_ac = ACContainerizedCargoExport(*values)
        total_ac = total_ac.calculate_fcl_export()
        sys.stdout.write(f'Total Arrastre Charge: P{total_ac}\n')
        return


class ACComputeFCLShutOutExport:
    def __init__(self, type_of_shutout_export_container: float, number_of_containers: float) -> None:
        self.type_of_shutout_export_container = type_of_shutout_export_container
        self.number_of_containers = number_of_containers

    def get_fcl_shutout_export_values(self) -> tuple[float, float]:
        sys.stdout.write(prompt_var.prompt_fcl_shutout_export_intro)
        self.type_of_shutout_export_container = ErrorandInput.get_input(
            prompt_var.prompt_type_of_shutout_export_container
        )
        self.number_of_containers = ErrorandInput.get_input(
            prompt_var.prompt_number_of_containers
        )
        return self.type_of_shutout_export_container, self.number_of_containers

    def compute_fcl_shutout_export(self) -> None:
        values = self.get_fcl_shutout_export_values()
        total_ac = ACContainerizedCargoShutOutExport(*values)
        total_ac = total_ac.calculate_fcl_shutout_export()
        sys.stdout.write(f'Total Arrastre Charge: P{total_ac}\n')
        return

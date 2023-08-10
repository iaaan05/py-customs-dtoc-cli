import sys

from customs_dtoc import WDContainerizedCargoImport, WDContainerizedCargoExport
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class WDContainerizedCargo:
    def __init__(self, size_of_container: float, total_number_of_containers: float) -> None:
        self.size_of_container = size_of_container
        self.number_of_containers = total_number_of_containers

    def get_fcl_values(self) -> tuple[float, float]:
        self.size_of_container = ErrorandInput.get_input(prompt_var.prompt_size_of_container)
        self.number_of_containers = ErrorandInput.get_input(prompt_var.prompt_number_of_containers)
        return self.size_of_container, self.number_of_containers


class WDComputeFCLImport(WDContainerizedCargo):
    def get_fcl_import_values(self) -> tuple[float, float]:
        sys.stdout.write(prompt_var.prompt_fcl_import)
        return self.get_fcl_values()

    def compute_fcl_import(self) -> None:
        values = self.get_fcl_import_values()
        total_wd = WDContainerizedCargoImport(*values)
        total_wd = total_wd.calculate_fcl_import()
        sys.stdout.write(f'Total Wharfage Due: P{total_wd}\n')
        return


class WDComputeFCLExport(WDContainerizedCargo):
    def get_fcl_export_values(self) -> tuple[float, float]:
        sys.stdout.write(prompt_var.prompt_fcl_export)
        return self.get_fcl_values()

    def compute_fcl_export(self) -> None:
        values = self.get_fcl_export_values()
        total_wd = WDContainerizedCargoExport(*values)
        total_wd = total_wd.calculate_fcl_export()
        sys.stdout.write(f'Total Wharfage Due: P{total_wd}\n')
        return

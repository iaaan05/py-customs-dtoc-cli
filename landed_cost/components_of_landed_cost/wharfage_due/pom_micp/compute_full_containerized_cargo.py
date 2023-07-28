import sys

from customs_tax import WDContainerizedCargoImport, WDContainerizedCargoExport
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class WDContainerizedCargo:
    def __init__(self, size_of_container: float, total_number_of_containers: float) -> None:
        self.size_of_container = size_of_container
        self.total_number_of_containers = total_number_of_containers

    def get_containerized_cargo_values(self) -> tuple[float, float]:
        self.size_of_container = ErrorandInput.get_input(prompt_var.prompt_size_of_container)
        self.total_number_of_containers = ErrorandInput.get_input(prompt_var.prompt_number_of_containers)
        return self.size_of_container, self.total_number_of_containers


class WDComputeContainerizedCargoImport(WDContainerizedCargo):
    def __init__(self, size_of_container, total_number_of_containers) -> None:
        super().__init__(size_of_container, total_number_of_containers)

    def get_containerized_cargo_import_values(self) -> tuple[float, float]:
        sys.stdout.write(prompt_var.prompt_fcl_import)
        return self.get_containerized_cargo_values()

    def compute_containerized_cargo_import(self) -> None:
        values = self.get_containerized_cargo_import_values()
        total_wharfage_due = WDContainerizedCargoImport(*values)
        total_wharfage_due = total_wharfage_due.calculate_fcl_import()
        sys.stdout.write(f'Total Wharfage Due: P{total_wharfage_due}\n')
        return


class WDComputeContainerizedCargoExport(WDContainerizedCargo):
    def __init__(self, size_of_container, total_number_of_containers) -> None:
        super().__init__(size_of_container, total_number_of_containers)

    def get_containerized_cargo_export_values(self) -> tuple[float, float]:
        sys.stdout.write(prompt_var.prompt_fcl_export)
        return self.get_containerized_cargo_values()

    def compute_containerized_cargo_export(self) -> None:
        values = self.get_containerized_cargo_export_values()
        total_wharfage_due = WDContainerizedCargoExport(*values)
        total_wharfage_due = total_wharfage_due.calculate_fcl_export()
        sys.stdout.write(f'Total Wharfage Due: P{total_wharfage_due}\n')
        return

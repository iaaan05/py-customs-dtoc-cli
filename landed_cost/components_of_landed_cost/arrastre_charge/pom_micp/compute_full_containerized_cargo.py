import sys

from customs_tax import ACContainerizedCargoImport, ACContainerizedCargoExport, \
    ACContainerizedCargoShutOutExport
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class ACContainerizedCargo:
    def __init__(self, size_of_container: float, total_number_of_containers: float) -> None:
        self.size_of_container = size_of_container
        self.total_number_of_containers = total_number_of_containers

    def get_containerized_cargo_values(self) -> tuple[float, float]:
        self.size_of_container = ErrorandInput.get_input(prompt_var.prompt_size_of_container)
        self.total_number_of_containers = ErrorandInput.get_input(prompt_var.prompt_number_of_containers)
        return self.size_of_container, self.total_number_of_containers


class ACComputeContainerizedCargoImport(ACContainerizedCargo):
    def __init__(self, size_of_container: float, total_number_of_containers: float) -> None:
        super().__init__(size_of_container, total_number_of_containers)

    def get_containerized_cargo_import_values(self) -> tuple[float, float]:
        sys.stdout.write(prompt_var.prompt_fcl_import)
        return self.get_containerized_cargo_values()

    def compute_containerized_cargo_import(self) -> None:
        values = self.get_containerized_cargo_import_values()
        total_arrastre_charge = ACContainerizedCargoImport(*values)
        total_arrastre_charge = total_arrastre_charge.calculate_containerized_cargo_import()
        sys.stdout.write(f'Total Arrastre Charge: P{total_arrastre_charge}\n')
        return


class ACComputeContainerizedCargoExport(ACContainerizedCargo):
    def __init__(self, size_of_container: float, total_number_of_containers: float) -> None:
        super().__init__(size_of_container, total_number_of_containers)

    def get_containerized_cargo_export_values(self) -> tuple[float, float]:
        sys.stdout.write(prompt_var.prompt_fcl_export)
        return self.get_containerized_cargo_values()

    def compute_containerized_cargo_export(self) -> None:
        values = self.get_containerized_cargo_export_values()
        total_arrastre_charge = ACContainerizedCargoExport(*values)
        total_arrastre_charge = total_arrastre_charge.calculate_containerized_cargo_export()
        sys.stdout.write(f'Total Arrastre Charge: P{total_arrastre_charge}\n')
        return


class ACComputeContainerizedCargoShutOutExport:
    def __init__(self, type_of_shutout_export_container: float, total_number_of_containers: float) -> None:
        self.type_of_shutout_export_container = type_of_shutout_export_container
        self.total_number_of_containers = total_number_of_containers

    def get_containerized_cargo_shutout_export_values(self) -> tuple[float, float]:
        sys.stdout.write(prompt_var.prompt_fcl_shutout_export_intro)
        self.type_of_shutout_export_container = ErrorandInput.get_input(
            prompt_var.prompt_type_of_shutout_export_container
        )
        self.total_number_of_containers = ErrorandInput.get_input(
            prompt_var.prompt_number_of_containers
        )
        return self.type_of_shutout_export_container, self.total_number_of_containers

    def compute_containerized_cargo_shutout_export(self) -> None:
        values = self.get_containerized_cargo_shutout_export_values()
        total_arrastre_charge = ACContainerizedCargoShutOutExport(*values)
        total_arrastre_charge = total_arrastre_charge.calculate_containerized_cargo_shutout_export()
        sys.stdout.write(f'Total Arrastre Charge: P{total_arrastre_charge}\n')
        return
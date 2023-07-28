import sys

from landed_cost.components_of_landed_cost.arrastre_charge.pom_micp.compute_bulk_break_bulk_cargo import \
    ACComputeBulkBreakBulkCargoImport, ACComputeBulkBreakBulkCargoExport
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class ACLCLType:
    def __init__(self) -> None:
        self.lcl_import = 1
        self.lcl_export = 2
        self.terminate_program = 3

    def get_type_of_lcl(self) -> None:
        type_of_cargo = 0
        total_metric_or_revenue_tons = 0

        valid_user_input = (self.lcl_import, self.lcl_export, self.terminate_program)
        while True:
            sys.stdout.write(prompt_var.prompt_lcl_intro)
            user_input = ErrorandInput.get_input('Enter here:\n-> ')
            if user_input in valid_user_input:

                if user_input == self.terminate_program:
                    sys.stdout.write(prompt_var.prompt_terminate_program)
                    sys.exit()

                if user_input == self.lcl_import:
                    sys.stdout.write(prompt_var.prompt_lcl_import_redirect)
                    ACComputeBulkBreakBulkCargoImport(
                        type_of_cargo, total_metric_or_revenue_tons
                    ).compute_bulk_break_bulk_cargo_import()
                    return

                elif user_input == self.lcl_export:
                    sys.stdout.write(prompt_var.prompt_lcl_export_redirect)
                    ACComputeBulkBreakBulkCargoExport(
                        type_of_cargo, total_metric_or_revenue_tons
                    ).compute_bulk_break_bulk_cargo_export()
                    return

            else:
                sys.stdout.write(prompt_var.prompt_invalid_input_1_to_3)

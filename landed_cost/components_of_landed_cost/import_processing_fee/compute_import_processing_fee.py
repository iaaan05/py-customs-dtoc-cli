import sys

from utils.operations.lc.components_of_lc.dutiable_value_type import DutiableValueType
from utils.error_handling_and_input_validation import ErrorandInput
from customs_tax import ImportProcessingFee
from utils import prompt_var


class ComputeImportProcessingFee:
    def __init__(self, total_dutiable_value: float) -> None:
        self.total_dutiable_value = total_dutiable_value
        self.dutiable_value = 1
        self.import_processing_fee = 2
        self.terminate_program = 3

    def get_user_confirmation_import_processing_fee(self) -> None:

        total_dutiable_value = 0

        valid_user_inputs = (self.import_processing_fee, self.dutiable_value, self.terminate_program)
        while True:
            sys.stdout.write(prompt_var.prompt_dv_intro)
            user_input = input('Enter here:\n-> ')
            if user_input in valid_user_inputs:

                if user_input == self.terminate_program:
                    sys.stdout.write(prompt_var.prompt_terminate_program)
                    sys.exit()

                if user_input == self.dutiable_value:
                    sys.stdout.write(prompt_var.prompt_dutiable_value_type_redirect)
                    DutiableValueType().get_type_of_dutiable_value()
                    return

                elif user_input == self.import_processing_fee:
                    sys.stdout.write(prompt_var.prompt_ipf_redirect)
                    ComputeImportProcessingFee(
                        total_dutiable_value
                    ).compute_import_processing_fee()
                    return

            else:
                sys.stdout.write(prompt_var.prompt_invalid_input_1_to_3)

    def compute_import_processing_fee(self) -> None:
        sys.stdout.write(prompt_var.prompt_ipf_intro)
        self.total_dutiable_value = ErrorandInput.get_input(prompt_var.prompt_dutiable_value)
        total_import_processing_fee = ImportProcessingFee(self.total_dutiable_value)
        total_import_processing_fee = total_import_processing_fee.calculate_dutiable_value_to_import_processing_fee()
        sys.stdout.write(f'Import Processing Fee : P{total_import_processing_fee}\n')
        return

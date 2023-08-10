import sys

from utils.error_handling_and_input_validation import ErrorandInput
from customs_dtoc import CustomsDocumentaryStamp
from utils import prompt_var


class ComputeCDS:
    def __init__(self, type_of_entry: float) -> None:
        self.type_of_entry = type_of_entry

    def compute_cds(self) -> None:
        sys.stdout.write(prompt_var.prompt_cds_intro)
        self.type_of_entry = ErrorandInput.get_input(prompt_var.prompt_entry_type)
        total_cds = CustomsDocumentaryStamp(self.type_of_entry)
        total_cds = total_cds.calculate_cds()
        sys.stdout.write(f'Customs Documentary Stamp: P{total_cds}\n')
        return

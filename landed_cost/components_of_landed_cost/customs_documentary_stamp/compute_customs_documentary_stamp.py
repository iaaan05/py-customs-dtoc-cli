import sys

from utils.error_handling_and_input_validation import ErrorandInput
from customs_tax import CustomsDocumentaryStamp
from utils import prompt_var


class ComputeCustomsDocumentaryStamp:
    def __init__(self, type_of_entry: float) -> None:
        self.type_of_entry = type_of_entry

    def compute_customs_documentary_stamp(self) -> None:
        sys.stdout.write(prompt_var.prompt_cds_intro)
        self.type_of_entry = ErrorandInput.get_input(prompt_var.prompt_entry_type)
        total_customs_documentary_stamp = CustomsDocumentaryStamp(self.type_of_entry)
        total_customs_documentary_stamp = total_customs_documentary_stamp.calculate_customs_documentary_stamp()
        sys.stdout.write(f'Customs Documentary Stamp: P{total_customs_documentary_stamp}\n')
        return

import sys

from landed_cost.entry_type.compute_informal_landed_cost import ComputeLandedCostViaInformalEntry
from utils.operations.lc.entry_type.formal_entry_type import FormalEntryType
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class EntryType:
    def __init__(self) -> None:
        self.formal_entry = 1
        self.informal_entry = 2
        self.terminate_program = 3

    def get_type_of_entry(self):
        dutiable_value = 0
        customs_duty = 0
        brokerage_fee = 0
        customs_documentary_stamp = 0

        valid_user_inputs = (self.formal_entry, self.informal_entry, self.terminate_program)
        while True:
            sys.stdout.write(prompt_var.prompt_entry_input_intro)
            user_input = ErrorandInput.get_input('Enter here:\n-> ')
            if user_input in valid_user_inputs:

                if user_input == self.terminate_program:
                    sys.stdout.write(prompt_var.prompt_terminate_program)
                    sys.exit()

                elif user_input == self.formal_entry:
                    sys.stdout.write(prompt_var.prompt_formal_entry_type_redirect)
                    FormalEntryType().get_type_of_formal_entry()
                    return

                elif user_input == self.informal_entry:
                    sys.stdout.write(prompt_var.prompt_informal_entry_redirect)
                    ComputeLandedCostViaInformalEntry(
                        dutiable_value, customs_duty, brokerage_fee, customs_documentary_stamp
                    ).compute_landed_cost_via_informal_entry()
                    return

            else:
                sys.stdout.write(prompt_var.prompt_invalid_input_1_to_3)

import sys

from utils.operations.lc.components_of_lc.components_of_landed_cost import ComponentsOfLandedCost
from utils.operations.lc.entry_type.entry_type import EntryType
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class LandedCostOrComponents:
    def __init__(self) -> None:
        self.type_of_landed_cost_entry = 1
        self.components_of_landed_cost = 2
        self.terminate_program = 3

    def get_to_compute(self):
        valid_user_inputs = (self.type_of_landed_cost_entry, self.components_of_landed_cost, self.terminate_program)
        while True:
            sys.stdout.write(prompt_var.prompt_lc_or_components_intro)
            user_input = ErrorandInput.get_input('Enter here:\n-> ')
            if user_input in valid_user_inputs:

                if user_input == self.terminate_program:
                    sys.stdout.write(prompt_var.prompt_terminate_program)
                    sys.exit()

                if user_input == self.type_of_landed_cost_entry:
                    sys.stdout.write(prompt_var.prompt_type_of_landed_cost_entry_redirect)
                    EntryType().get_type_of_entry()
                    return

                elif user_input == self.components_of_landed_cost:
                    sys.stdout.write(prompt_var.prompt_components_of_landed_cost_redirect)
                    ComponentsOfLandedCost().get_component_of_landed_cost()
                    return

            else:
                sys.stdout.write(prompt_var.prompt_invalid_input_1_to_3)

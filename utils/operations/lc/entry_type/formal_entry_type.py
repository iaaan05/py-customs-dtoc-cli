import sys

from landed_cost.entry_type.compute_formal_landed_cost import ComputeLandedCostBySea, ComputeLandedCostByAir
from utils.error_handling_and_input_validation import ErrorandInput
from utils import prompt_var


class FormalEntryType:
    def __init__(self) -> None:
        self.sea = 1
        self.air = 2
        self.terminate_program = 3

    def get_type_of_formal_entry(self) -> None:
        dutiable_value = 0
        customs_duty = 0
        bank_charge = 0
        brokerage_fee = 0
        arrastre_charge = 0
        wharfage_due = 0
        import_processing_fee = 0
        customs_documentary_stamp = 0

        valid_user_inputs = (self.sea, self.air, self.terminate_program)
        while True:
            sys.stdout.write(prompt_var.prompt_formal_entry_intro)
            user_input = ErrorandInput.get_input('Enter here:\n-> ')
            if user_input in valid_user_inputs:

                if user_input == self.terminate_program:
                    sys.stdout.write(prompt_var.prompt_terminate_program)
                    sys.exit()

                elif user_input == self.sea:
                    sys.stdout.write(prompt_var.prompt_lc_formal_sea_redirect)
                    ComputeLandedCostBySea(
                        dutiable_value, customs_duty, bank_charge, brokerage_fee, arrastre_charge, wharfage_due,
                        import_processing_fee, customs_documentary_stamp
                    ).compute_landed_cost_by_sea()
                    return

                elif user_input == self.air:
                    sys.stdout.write(prompt_var.prompt_lc_formal_air_redirect)
                    ComputeLandedCostByAir(
                        dutiable_value, customs_duty, bank_charge, brokerage_fee,
                        import_processing_fee, customs_documentary_stamp
                    ).compute_landed_cost_by_air()
                    return

            else:
                sys.stdout.write(prompt_var.prompt_invalid_input_1_to_3)

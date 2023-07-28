import sys


class ErrorandInput:
    @staticmethod
    def get_input(prompt) -> float:
        while True:
            try:
                value = float(input(prompt))
                if value < 0:
                    sys.stdout.write('\nINVALID INPUT: Please enter a non-negative value.\n')
                else:
                    return value
            except ValueError:
                sys.stdout.write('\nINVALID INPUT: Please enter a valid numeric value.\n')

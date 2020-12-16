"""
Used to ask for the user input and check if the input
is within the list of acceptable inputs
"""

from classes.parameters.messages import BAD_INPUT, BAD_NUMBER_INPUT


class UserInputs():
    """
    Used to ask for the user input and check if the input
    is within the list of acceptable inputs
    """

    def __init__(self, accepted_values):
        self.correct_input = False
        while not self.correct_input:
            self.user_input = input("\nPlease enter one of the item numbers"
                                    " to indicate your choice\n")
            self.verif_input(self.user_input, accepted_values)

    def verif_input(self, user_input, accepted_values):
        """
        Verification of the input of the user regarding the possible values

        Keyword arguments:
        user_input -- value entered by the user
        accepted_values -- accepted values to be compared to the user input
        """
        if user_input.isdigit():
            if int(self.user_input) in accepted_values:
                self.correct_input = True
                self.validated_input = int(self.user_input)
            else:
                print(BAD_NUMBER_INPUT)
        else:
            print(BAD_INPUT)


if __name__ == "__main__":
    a = [1, 2, 3, 4]
    u = UserInputs(a)

import messages_displayed as MSG
import parameters.constants as CONST


class User_inputs():
    def __init__(self, accepted_values):
        self.correct_input = False
        while self.correct_input == False:
            self.user_input = input("\nPlease enter one of the item numbers"
                                    " to indicate your choice\n")
            self.verif_input(self.user_input, accepted_values)

    def verif_input(self, user_input, accepted_values):
        if user_input.isdigit():
            if int(self.user_input) in accepted_values:
                self.correct_input = True
                self.validated_input = int(self.user_input)
            else:
                print(MSG.bad_number_input)
        else:
            print(MSG.bad_input)


if __name__ == "__main__":
    a = [1, 2, 3, 4]
    u = User_inputs(a)
    pass

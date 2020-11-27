from messages_displayed import Messages_displayed
from os import system


class Menu:
    input_error = Messages_displayed.bad_input
    disclaimer = Messages_displayed.disclaimer
    input_error = Messages_displayed.bad_input
    list_menu = Messages_displayed.menu
    input_number_error = Messages_displayed.bad_number_input

    def __init__(self):
        # system('cls')
        print(self.disclaimer)
        print(self.list_menu)
        user_choice = self.ask_user_input()
        keep_run = True
        while keep_run == True:
            if user_choice == 1:
                # alt_product()
                print("\nyou selected {}\n".format(user_choice))
            elif user_choice == 2:
                # display_alt()
                print("\nyou selected {}\n".format(user_choice))
            elif user_choice == 3:
                # reset_DB()
                print("\nyou selected {}\n".format(user_choice))
            elif user_choice == 4:
                keep_run = False
            if keep_run == True:
                user_choice = self.ask_user_input()
        print("Thank you, have a nice day!")
        quit()

    def ask_user_input(self):
        user_input = input("\nPlease enter one of the line numbers "
                           "to indicate your choice\n")
        if user_input.isdigit():
            if user_input in ('1', '2', '3', '4'):
                return int(user_input)
            else:
                print(self.input_number_error)
        else:
            print(self.input_error)


menu = Menu()

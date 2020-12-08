import messages_displayed as MSG
from os import system
import database
import off_api
import parameters.constants as CONST
import time


class Menu:
    api = off_api.Off_api_data()

    def __init__(self):
        # system('cls')
        if init == True:
            print("Please wait while the required data is loaded")
            DB = database.Database()
            DB.load_sql_file()
            self.api.fetch_data()
            init == False
            # print(MSG.disclaimer)
            # print(MSG.menu)
            # user_choice = self.ask_user_input_main_menu
            # init == False
        keep_run = True
        return_menu = False
        while keep_run == True:
            if return_menu == True:
                print("\nYou've been redirected to the main menu\n")
            # if return_menu == False:
            #     return_menu == True
            print(MSG.menu)
            user_menu_choice = self.ask_user_input_main_menu()
            if user_menu_choice == 1:
                # self.api.fetch_data()
                self.display_cat()
                self.display_prod_from_cat()
                DB.display_prod_from_cat(self.selected_cat)
                user_choice = self.ask_user_input()
                # print("selected_cat:{}".format(self.selected_cat))
                # print("self.dict_cat:{}".format(self.dict_cat))
                # selected_cat_name = self.dict_cat[user_choice]
                # print("selected cat name:{}".format(selected_cat_name))
                DB.find_better_nutri(
                    user_choice, self.selected_cat)
                DB.save_alternative(user_choice, DB.id_alternative_product)
                return_menu = True
            elif user_menu_choice == 2:
                # display_alt()
                print("\nyou selected {}\n".format(user_choice))
                return_menu = True
            elif user_menu_choice == 3:
                print("\nBeginning reset process\n")
                DB.load_sql_file()
                self.api = off_api.Off_api_data()
                self.api.fetch_data()
                print("\nDatabase reset succesfull\n")
                return_menu = True
            elif user_menu_choice == 4:
                keep_run = False
            # if keep_run == True:
            #     user_choice = self.ask_user_input()
        print("Thank you, have a nice day!")
        quit()

    def ask_user_input_main_menu(self):
        user_input = input("\nPlease enter one of the line numbers "
                           "to indicate your choice\n")
        if user_input.isdigit():
            if user_input in ('1', '2', '3', '4'):
                return int(user_input)
            else:
                print(MSG.bad_number_input)
        else:
            print(MSG.bad_input)

    def ask_user_input(self):
        user_input = input("\nPlease enter one of the item numbers "
                           "to indicate your choice\n")
        if user_input.isdigit():
            if int(user_input) > 0 and int(user_input) <= CONST.MAX_PROD_ID:
                return int(user_input)
            else:
                print(MSG.bad_number_input)
        else:
            print(MSG.bad_input)

    def display_cat(self):
        categories = self.api.cat_list
        i = 1
        self.dict_cat = {}
        for cat in categories:
            add = {i: cat}
            self.dict_cat.update(add)
            print("\nCATEGORY {}: {}".format(i, cat))
            i = i+1
        return (self.dict_cat)

    def display_prod_from_cat(self):
        self.cat_selected_nbr = self.ask_user_input()
        self.selected_cat = self.dict_cat[self.cat_selected_nbr]


if __name__ != "main":
    init = True
    menu = Menu()

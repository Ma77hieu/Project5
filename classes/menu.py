import messages_displayed as MSG
from os import system
from database import Database as DB
import off_api
import parameters.constants as CONST
import time
from user_inputs import User_inputs as check_input


class Menu:

    def __init__(self):
        # system('cls')
        self.api = off_api.Off_api_data()
        self.db = DB()
        self.return_menu = False
        self.keep_run = True
        self.menu_launch()

    def menu_launch(self):
        if self.api.data_loaded == False:
            print("\n##########\n\n"
                  "No data have been retrieved,"
                  "please use menu choice 3\n\n"
                  "##########")
        while self.keep_run == True:
            if self.return_menu == True:
                print("\nYou've been redirected to the main menu\n")
            print(MSG.menu)
            self.user_menu_choice = self.ask_user_input_main_menu()
            if self.user_menu_choice == 1 and self.api.data_loaded == True:
                self.menu_1_alternative()
            # elif self.user_menu_choice == 2: and (
            #         (self.api.data_loaded == True) and (
            #         self.db.alt_saved == True)):
            elif self.user_menu_choice == 2 and self.api.data_loaded == True:
                if self.db.alt_saved == True:
                    self.menu_2_display_alt()
                else:
                    print(
                        "You have to save alternative products before you can review them")
            elif self.user_menu_choice == 3:
                self.menu_3_load_db()
            elif self.user_menu_choice == 4:
                self.keep_run = False
            else:
                print("please initalise the database first, menu choice 3")
        print("Thank you, have a nice day!")
        quit()

    def menu_1_alternative(self):
        self.display_cat()
        self.display_prod_from_cat(self.list_cat_nbr)
        self.db.display_prod_from_cat(self.selected_cat)
        self.select_prod_from_cat(self.db.selectionnable_prod)
        self.db.find_better_nutri(
            self.selected_prod, self.selected_cat)
        self.db.save_alternative(
            self.selected_prod, self.db.id_alternative_product)
        self.return_menu = True

    def menu_2_display_alt(self):
        self.db.display_alternative()
        self.return_menu = True

    def menu_3_load_db(self):
        print("\nBeginning loading data\n")
        self.db.load_sql_file()
        self.api.fetch_data()
        print("\nDatabase loaded\n")
        init == False
        self.return_menu = True

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
        self.list_cat_nbr = []
        for cat in categories:
            add = {i: cat}
            self.dict_cat.update(add)
            print("\nCATEGORY {}: {}".format(i, cat))
            self.list_cat_nbr.append(i)
            i = i+1
        return (self.dict_cat)

    def display_prod_from_cat(self, list_cat_nbr):
        self.checked_input = check_input(self.list_cat_nbr)
        self.selected_cat = self.dict_cat[self.checked_input.validated_input]

    def select_prod_from_cat(self, selectionnable_prod):
        self.checked_input = check_input(self.db.selectionnable_prod)
        self.selected_prod = self.checked_input.validated_input


if __name__ != "main":
    init = True
    menu = Menu()

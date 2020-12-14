"""
The menu of this program
"""

import os
import sys
import classes.messages_displayed as MSG
from classes.database import Database as DB
import classes.off_api
from classes.user_inputs import UserInputs as check_input


class Menu:
    """
    The menu of this program
    """

    def __init__(self):
        self.cls()
        self.api = classes.off_api.OffApiData()
        self.db = DB()
        self.return_menu = False
        self.keep_run = True
        self.menu_launch()
        self.dict_cat = None
        self.list_cat_nbr = None
        self.checked_input = None
        self.selected_cat = None
        self.selected_prod = None

    def menu_launch(self):
        """
        Initializes the menu and execute actions based on user input
        """
        if not self.api.data_loaded:
            print("\n##########\n\n"
                  "No data have been retrieved,"
                  "please use menu choice 3\n\n"
                  "##########")
        while self.keep_run:
            if self.return_menu:
                print("\nYou've been redirected to the main menu\n")
            print(MSG.MENU)
            checked_input = check_input([1, 2, 3, 4])
            self.user_menu_choice = checked_input.validated_input
            if self.user_menu_choice == 1 and self.api.data_loaded:
                self.menu_1_alternative()
            elif self.user_menu_choice == 2 and self.api.data_loaded:
                if self.db.alt_saved:
                    self.menu_2_display_alt()
                else:
                    print(
                        "You have to save alternative products before you can review them")
            elif self.user_menu_choice == 3:
                self.menu_3_load_db()
            elif self.user_menu_choice == 4:
                self.keep_run = False
            else:
                print("\nPlease initalise the database first, menu choice 3")
        print("Thank you, have a nice day!")
        sys.exit()

    def menu_1_alternative(self):
        """
        Menu choice 1: find an alternative with a
        better nutrition grade and save it in DB
        """
        self.display_cat()
        self.display_prod_from_cat()
        self.db.display_prod_from_cat(self.selected_cat)
        self.select_prod_from_cat()
        self.db.find_better_nutri(
            self.selected_prod, self.selected_cat)
        if self.db.available_alt is not None:
            self.db.save_alternative(
                self.selected_prod, self.db.id_alternative_product)
        self.return_menu = True

    def menu_2_display_alt(self):
        """
        Menu choice 2: Display the saved alternatives
        """
        self.db.display_alternative()
        self.return_menu = True

    def menu_3_load_db(self):
        """
        Menu choice 3: Load or reset the database
        """
        print("\nBeginning loading data\n")
        self.db.load_sql_file()
        self.api.fetch_data()
        print("\nDatabase loaded\n")
        self.return_menu = True

    def display_cat(self):
        """
        Display the name of the category received from the API
        """
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
        return self.dict_cat

    def display_prod_from_cat(self):
        """
        Display the products from a defined category

        Keyword arguments:
        list_cat_nbr -- number corresponding to the chosen category
        (assigned by the "fetch data" function of the off_api module)
        """
        self.checked_input = check_input(self.list_cat_nbr)
        self.selected_cat = self.dict_cat[self.checked_input.validated_input]

    def select_prod_from_cat(self):
        """
        User selection of one of the product of the category

        Keyword arguments:
        selectionnable_prod -- list of the products ID corresponding to
        the selected category
        """
        self.checked_input = check_input(self.db.selectionnable_prod)
        self.selected_prod = self.checked_input.validated_input

    def cls(self):
        """
        Used to clear the screen of the terminal
        """
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ != "main":
    menu = Menu()

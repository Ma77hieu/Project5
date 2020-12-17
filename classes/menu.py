"""
The menu of this program
"""

import os
import sys
from classes.parameters.messages import (DISCLAIMER, MENU,
                                         INIT_NO_LOAD, LOAD_FIRST,
                                         SAVE_ALT_FIRST, MENU_RETURN)
from classes.database import Database as DB
from classes.category import Category
from classes.product import Product
from classes.substitute import Substitute
from classes.off_api import OffApiData
from classes.user_inputs import UserInputs as check_input


class Menu:
    """
    The menu of this program
    """

    def __init__(self):
        self.cls()
        self.api = OffApiData()
        self.database = DB()
        self.category = Category()
        self.product = Product()
        self.substitute = Substitute()
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
        print(DISCLAIMER)
        if not self.api.data_loaded:
            print(INIT_NO_LOAD)
        while self.keep_run:
            if self.return_menu:
                print(MENU_RETURN)
                input()
                self.cls()
            print(MENU)
            checked_input = check_input([1, 2, 3, 4])
            self.user_menu_choice = checked_input.validated_input
            if self.user_menu_choice == 1 and self.api.data_loaded:
                self.menu_1_alternative()
            elif self.user_menu_choice == 2 and self.api.data_loaded:
                if self.substitute.alt_saved:
                    self.menu_2_display_alt()
                else:
                    print(SAVE_ALT_FIRST)
            elif self.user_menu_choice == 3:
                self.menu_3_load_db()
            elif self.user_menu_choice == 4:
                self.keep_run = False
            else:
                print(LOAD_FIRST)
        print("Thank you, have a nice day!")
        sys.exit()

    def menu_1_alternative(self):
        """
        Menu choice 1: find an alternative with a
        better nutrition grade and save it in DB
        """
        self.category.display_categories()
        print("\nPlease choose one category of product to find a substitute")
        self.category.ask_choose_cat()
        self.category.display_prod_from_cat(self.category.selected_cat_name)
        print("Please choose one product you wish to replace.")
        self.product.ask_choose_prod(self.category.selectionnable_prod)
        self.product.find_better_nutri(
            self.product.selected_prod_id, self.category.selected_cat_name)
        if self.product.available_alt is not None:
            self.substitute.save_alternative(
                self.product.selected_prod_id,
                self.product.id_alternative_product)
        self.return_menu = True

    def menu_2_display_alt(self):
        """
        Menu choice 2: Display the saved alternatives
        """
        self.substitute.display_alternative()
        self.return_menu = True

    def menu_3_load_db(self):
        """
        Menu choice 3: Load or reset the database
        """
        print("\nBeginning loading data\n")
        self.database.load_sql_file()
        self.api.get_info()
        print("\nDatabase loaded\n")
        self.return_menu = True

    @staticmethod
    def cls():
        """
        Used to clear the screen of the terminal
        """
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ != "main":
    menu = Menu()

"""
Messages to be displayed to the user
"""

BAD_INPUT = ("\n##########\nINFO:\n"
             "The input you entered is not an integer.\n"
             "Please use one of the listed numbers\n##########")

MENU = ("\n###################################\n"
        "############## MENU ###############\n"
        "###################################\n\n"
        "1/ Find an alternative to a product\n"
        "2/ Display the saved alternatives\n"
        "3/ Initialise or reset database\n"
        "4/ Exit\n")

DISCLAIMER = ("\nWelcome!\n\n"
              "This program will help you find substitutes"
              " for your favorite food products.\n"
              "This program's data is based "
              "on the open food fact initiative, "
              "the information provided need therefore"
              " to be used with caution.\n"
              "For more information please refer to:"
              " https://fr.openfoodfacts.org/\n")

BAD_NUMBER_INPUT = ("\n##########\nINFO:\n"
                    "The number you entered is not in "
                    "the above list, please try again.\n##########")

INIT_NO_LOAD = ("\n##########\nINFO:\n"
                "No data have been retrieved yet"
                " from the open food fact API.\n"
                "Please use menu choice 3 to initialize "
                "the database\n##########")

LOAD_FIRST = ("\n##########\nINFO:\n"
              "Please initalise the database first, menu choice 3\n"
              "##########")

SAVE_ALT_FIRST = ("\n##########\nINFO:\n"
                  "You have to save alternative products "
                  "before you can review them\n"
                  "##########")

MENU_RETURN = ("\n##########\nINFO:\n"
               "Press enter to be redirected to the main menu\n"
               "##########")

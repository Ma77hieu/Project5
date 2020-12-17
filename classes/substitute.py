from classes.database import Database
from classes.product import Product
from classes.category import Category
from classes.user_inputs import UserInputs as check_input


class Substitute():
    """
    The class representing a substitute to a food product,
    corresponding to the table substituts in our database
    """

    def __init__(self):
        self.database = Database()
        self.product = Product()
        self.category = Category()
        self.alt_saved = None

    def save_alternative(self, prod_id, alt_id):
        """
        Save a product inside the substituts table of our DB

        Keyword arguments:
        prod_id -- Id of the product the user wishes to find
        an alternative for
        alt_id -- Id of the altenrative product
        """
        repeat = True
        while repeat:
            print(
                "\nWould you like to save this alternative aliment?"
                "\n1.YES\n2.NO")
            checked_input = check_input([1, 2])
            need_save = checked_input.validated_input

            if need_save == 1:
                with self.database.connection.cursor(buffered=True) as cursor:
                    cursor.execute(
                        """INSERT INTO substituts (aliments_id,substitut_id)
                        VALUES(%s,%s)""", (prod_id, alt_id))
                    print("\n##########\nINFO:\nSubstitute SAVED"
                          "\n##########")
                self.alt_saved = True
                self.database.connection.commit()
            if need_save == 2:
                print("\n##########\nINFO:\nSubstitute NOT saved"
                      "\n##########")
            repeat = False

    def display_alternative(self):
        """
        Display the products from the same category
         with a better nutrition grade
        """
        with self.database.connection.cursor(buffered=True) as cursor:
            cursor.execute(
                """SELECT name,nutrition_grade,stores,categories_id,substitut_id
                FROM aliments
                JOIN substituts
                ON aliments.id=substituts.aliments_id""")
            all_info = cursor.fetchall()
            for row in all_info:
                prod_name = row[0]
                print(
                    "\n######\nThe product:"
                    "\n{}\ncan be replaced by:".format(prod_name))
                substitut_id = row[4]
                cursor.execute(
                    """SELECT name,nutrition_grade,stores,categories_id
                    FROM aliments
                    WHERE id=%s""", (substitut_id,))
                substitute_info = cursor.fetchone()
                substitut_name = substitute_info[0]
                print("{}\n######".format(substitut_name))

        self.database.connection.commit()

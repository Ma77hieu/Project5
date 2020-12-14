"""
Creation of the database plus various operations like
inserting a product
display of the products of a category
find a product with a better nutriscore
save a substitution product in the database
"""

import mysql.connector
import classes.parameters.sqlCredentials as CRED
from classes.user_inputs import UserInputs as check_input


class Database ():
    """
    The class represeintg our database
    """

    def __init__(self):

        self.connection = mysql.connector.connect(
            host=CRED.HOST,
            database=CRED.DATABASE,
            user=CRED.USER,
            passwd=CRED.PASSWD
        )
        self.alt_saved = False
        self.selectionnable_prod = []
        self.available_alt = None
        self.id_alternative_product = None

    def load_sql_file(self):
        """
        Creates database from SQL file stored in SQL folder
        """
        with open('SQLmywb/substitution_aliments.sql', 'r') as file:
            with self.connection.cursor() as cursor:
                for _ in cursor.execute(file.read(), multi=True):
                    pass
            self.connection.commit()

    def insert_product(self, product_name, nutrition_grade,
                       stores, url, cat_name):
        """
        Save the products and their characteristics in DB

        Keyword arguments:
        product_name -- Name of the product to be inserted in DB
        nutrition_grade -- Nutrition grade of the product
        stores -- stores where user can buy the product
        url -- url of the open food fact webpage of the product
        cat_name -- name of the category related to the product
        """
        with self.connection.cursor() as cursor:
            cursor.execute("""INSERT INTO aliments
                    (name,nutrition_grade,stores,url,categories_id)
                    VALUES (%s,%s,%s,%s,%s)""",
                           (product_name, nutrition_grade,
                            stores, url, cat_name))
        self.connection.commit()

    def display_prod_from_cat(self, cat):
        """
        Display the products from a category

        Keyword arguments:
        cat -- Category from which we want to display the products
        """
        with self.connection.cursor() as cursor:
            cursor.execute(
                """SELECT id,name,nutrition_grade FROM aliments
                WHERE categories_id=%s""", (cat,))
            result = cursor.fetchall()
            print("\n#####\n\nProducts from the chosen category\n"
                  " ID | NAME | Nutriscore")

            for row in result:
                print(" {} | {} | {} ".format(
                    row[0], row[1], row[2]))
                self.selectionnable_prod.append(row[0])
        self.connection.commit()

    def find_better_nutri(self, prod_id, cat_id):
        """
        Find a product from the same category with a better nutrition grade

        Keyword arguments:
        prod_id -- Id of the product the user wishes to find
         an alternative for
        cat_id -- Name of the category of the product
        """
        print("Category: {}".format(cat_id))
        with self.connection.cursor(buffered=True) as cursor:
            cursor.execute(
                """SELECT nutrition_grade FROM aliments
                WHERE id=%s""", (prod_id,))
            nutri_chosen_product = str(cursor.fetchall())[3]
            print("Nutriscore chosen product: {}".format(
                nutri_chosen_product))
            cursor.execute(
                """SELECT id FROM aliments
                WHERE id!=%s AND nutrition_grade<=%s AND categories_id=%s""",
                (prod_id, nutri_chosen_product, cat_id,))
            self.available_alt = cursor.fetchone()
            if self.available_alt is None:
                print(
                    "\nThere are no products within the same"
                    " category with a better nutriscore in the extracted data")
            else:
                self.id_alternative_product = str(self.available_alt)[1]
                cursor.execute(
                    """SELECT id,name,nutrition_grade FROM aliments
                    WHERE id=%s """, (self.id_alternative_product,))
                alt = cursor.fetchone()
                print("#####\nAlternative product found:"
                      "\n ID | NAME | Nutriscore")
                print(" {} | {} | {} ".format(
                    alt[0], alt[1], alt[2]))

        self.connection.commit()

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
                with self.connection.cursor(buffered=True) as cursor:
                    cursor.execute(
                        """INSERT INTO substituts (aliments_id,substitut_id)
                        VALUES(%s,%s)""",  (prod_id, alt_id))
                    print("\n##########\nINFO:\nSubstitute SAVED"
                          "\n##########")
                self.alt_saved = True
                self.connection.commit()
            if need_save == 2:
                print("\n##########\nINFO:\nSubstitute NOT saved"
                      "\n##########")
            repeat = False

    def display_alternative(self):
        """
        Display the products from the same category
         with a better nutrition grade
        """
        with self.connection.cursor(buffered=True) as cursor:
            cursor.execute(
                """SELECT name,nutrition_grade,stores,categories_id,substitut_id
                FROM aliments
                RIGHT OUTER JOIN substituts
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

        self.connection.commit()


if __name__ == "__main__":
    database = Database()
    # database.load_sql_file()
    # database.find_better_nutri(7, "Snacks")

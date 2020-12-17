from classes.category import Category
from classes.database import Database
from classes.user_inputs import UserInputs as check_input


class Product():
    """
    The class representing a food product, corresponding to
    the table aliments in our database
    """

    def __init__(self, product_id=None, product_name=None,
                 nutrition_grade=None, stores=None, url=None,
                 cat_name=None, ):
        self.database = Database()
        self.product_id = product_id
        self.product_name = product_name
        self.nutrition_grade = nutrition_grade
        self.stores = stores
        self.url = url
        self.cat_name = cat_name
        self.category = Category()
        self.data_loaded = None
        self.checked_input = None
        self.selected_prod_id = None
        self.available_alt = None
        self.id_alternative_product = None

    def insert_product(self, product_name, nutrition_grade,
                       stores, url, cat_name):
        """
        Insert one new line in aliments table of the database
        """
        with self.database.connection.cursor() as cursor:
            cursor.execute("""INSERT INTO aliments
                    (name,nutrition_grade,stores,url,categories_id)
                    VALUES (%s,%s,%s,%s,%s)""",
                           (product_name, nutrition_grade,
                            stores, url, cat_name))
        self.database.connection.commit()
        self.data_loaded = True

    def ask_choose_prod(self, selectionnable_prod):
        """
        Asks for the user to choose a product from a category
        """
        self.checked_input = check_input(selectionnable_prod)
        self.selected_prod_id = self.checked_input.validated_input

    def find_better_nutri(self, prod_id, cat_id):
        """
        Find a product from the same category with a better nutrition grade

        Keyword arguments:
        prod_id -- Id of the product the user wishes to find
         an alternative for
        cat_id -- Name of the category of the product
        """
        with self.database.connection.cursor(buffered=True) as cursor:
            cursor.execute(
                """SELECT nutrition_grade FROM aliments
                WHERE id=%s""", (self.selected_prod_id,))
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
                    """SELECT id,name,nutrition_grade,stores,url FROM aliments
                    WHERE id=%s """, (self.id_alternative_product,))
                alt = cursor.fetchone()
                print("#####\nAlternative product found:"
                      "\n ID | NAME | Nutriscore | store | url")
                print(" {} | {} | {} | {} | {} ".format(
                    alt[0], alt[1], alt[2], alt[3], alt[4]))
        self.database.connection.commit()

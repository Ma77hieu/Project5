from classes.model import Model
from classes.database import Database
from classes.user_inputs import UserInputs as check_input


# class Category(Model):

#     def __init__(self, category_id=None, name):
#         # check la syntaxe du super_init
#         super.__init__()
#         self.category_id = category_id
#         self.name = name


class Category():
    def __init__(self):
        self.database = Database()
        self.cat_name = str

        self.list_cat_ids = []
        self.list_cat_names = []

    def insert_cat(self, cat_name):
        with self.database.connection.cursor() as cursor:
            cursor.execute(
                """INSERT INTO categories (name) VALUES (%s)""", (cat_name,))
        self.database.connection.commit()

    def display_categories(self):
        """
        Display the name of the category received from the API
        """
        with self.database.connection.cursor(buffered=True) as cursor:
            cursor.execute(
                """SELECT id,name FROM categories
                """)
            result = cursor.fetchall()

            for row in result:
                print(" CATEGORY {} : {} ".format(
                    row[0], row[1]))
                self.list_cat_ids.append(row[0])
                self.list_cat_names.append(row[1])
        self.database.connection.commit()

    def ask_choose_cat(self):
        """
        Asks for the user to choose a category
        """
        self.checked_input = check_input(self.list_cat_ids)
        self.selected_cat_id = self.checked_input.validated_input
        with self.database.connection.cursor(buffered=True) as cursor:
            cursor.execute(
                """SELECT name FROM categories
                WHERE id=%s""", (self.selected_cat_id,)
            )
            result = cursor.fetchone()
            self.selected_cat_name = result[0]
            print("selected category : {}".format(self.selected_cat_name))
        self.database.connection.commit()

    def display_prod_from_cat(self, cat_name):
        """
        Display the products from a defined category

        Keyword arguments:
        list_cat_nbr -- number corresponding to the chosen category
        (assigned by the "fetch data" function of the off_api module)
        """
        self.selectionnable_prod = []
        with self.database.connection.cursor() as cursor:
            cursor.execute(
                """SELECT id,name,nutrition_grade FROM aliments
                WHERE categories_id=%s""", (cat_name,))
            result = cursor.fetchall()
            print("\n#####\n\nProducts from the chosen category\n"
                  " ID | NAME | Nutriscore")
            for row in result:
                print(" {} | {} | {} ".format(
                    row[0], row[1], row[2]))
                self.selectionnable_prod.append(row[0])
        self.database.connection.commit()
        print("selectionnable IDs:{}".format(self.selectionnable_prod))

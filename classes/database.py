import sqlite3
import json
from messages_displayed import Messages_displayed


class Database ():
    input_error = Messages_displayed.bad_input
    disclaimer = Messages_displayed.disclaimer
    input_error = Messages_displayed.bad_input
    list_menu = Messages_displayed.menu
    input_number_error = Messages_displayed.bad_number_input
    category_list = []
    products_list = []
    NOMBRE_CATEGORIES = 5
    NOMBRE_PRODUITS = 5

    def __init__(self):
        """
        Creates database from SQL file stored in SQL folder
        """
        self.connection = sqlite3.connect(
            "SQLmywb/substitution_aliments.db")
        self.cursor = self.connection.cursor()
        sql_file = open(
            "SQLmywb/Substitution_aliments.sql")
        sql_as_string = sql_file.read()
        self.cursor.executescript(sql_as_string)

    # b/Import data from the OFF databse => see off_api.Py

    def insert_values(self):
        """
        Populates the Database with the following data:
        - name of the product
        - nutriscore of the product
        - stores in which the product ius available
        - url of the product page
        """

        for each_cat in range(0, self.NOMBRE_CATEGORIES):
            with open("JSON/categories_list_OFF_API.json") as f:
                categories_json = json.load(f)
            category_name = categories_json["tags"][each_cat]["name"]
            # print('#######\nCAT:{}\nname:{}\n'.format(
            #     each_cat+1, category_name))
            self.cursor.execute("""INSERT INTO categories
                (name)
                VALUES (?)""", (category_name,))
            self.connection.commit()
            self.category_list.append(category_name)
            # print(self.category_list)
            for each_product in range(0, self.NOMBRE_PRODUITS):
                products_from_one_cat = []
                with open("JSON/CAT{}_OFF_API.json".format(each_cat+1)) as f:
                    products_json = json.load(f)
                product_name = products_json["products"][each_product]["product_name_fr"]
                nutriscore = products_json["products"][each_product]["nutriscore_grade"]
                stores = products_json["products"][each_product]["stores"]
                url = products_json["products"][each_product]["url"]
                # print('CAT:{}\nProduct number:{}\nname:{}\nnutri:{}\nstores:{}\nurl:{}\n'.format(
                #     each_cat+1, each_product+1, product_name, nutriscore, stores, url))
                self.cursor.execute("""INSERT INTO aliments
                        (name,nutrition_grade,stores,url,categories_id)
                        VALUES (?, ?, ?, ?,?)""", (product_name, nutriscore, stores, url, each_cat+1))
                self.connection.commit()
                # print("Product name:{}".format(product_name))
                products_from_one_cat.append(product_name)
                self.products_list.append(products_from_one_cat)
                # print('\n Product list:{}'.format(self.products_list))

    def print_DB(self):
        """
        Prints the database final state
        """
        for row in self.cursor.execute("SELECT * FROM aliments"):
            print(row)
        for row in self.cursor.execute("SELECT * FROM categories"):
            print(row)

    def substitute_product(self):
        """
        User chooses  one category, then one product
        for which he wants asubstitute.
        """
        print("\nPlease find below the available categories:")
        for cat_number in range(0, self.NOMBRE_CATEGORIES):
            print('Category n {}: {}'.format(
                cat_number+1, self.category_list[cat_number]))
        cat_user_input = input(
            "\nPlease enter one of the categories "
            "number to indicate your choice\n")
        print("\nPlease find below the aliments from the selected category:")
        if cat_user_input.isdigit():
            if int(cat_user_input) <= self.NOMBRE_CATEGORIES:
                for product_display in range(0, self.NOMBRE_PRODUITS):
                    print('product n {}: {}'.format(product_display+1, self.products_list[
                        (int(cat_user_input)-1)*self.NOMBRE_PRODUITS+product_display]))
            else:
                print(self.input_number_error)
        else:
            print(self.input_error)
        product_user_input = input(
            "\nPlease enter one of the product "
            "so we can offer a substitute\n")
        selected_product_name = self.products_list[
            (int(cat_user_input)-1)*self.NOMBRE_PRODUITS+(int(product_user_input)-1)]

        print("You selected {}".format(selected_product_name))


database = Database()
database.insert_values()
# database.print_DB()
database.substitute_product()

# d/display categories and ask for selection
# e/display products in categories and ask for selection
# f/offer save the product
# g/insert the substitute id in DB


# for row in cursor.execute("SELECT * FROM airports"):
#     print(row)

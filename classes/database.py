
import json
import mysql.connector
import parameters.SQL_credentials as CRED
import pprint
import string
import messages_displayed as MSG


class Database ():

    def __init__(self):

        self.connection = mysql.connector.connect(
            host=CRED.host,
            user=CRED.user,
            passwd=CRED.passwd
        )

    def load_sql_file(self):
        """
        Creates database from SQL file stored in SQL folder
        """
        with open('SQLmywb/substitution_aliments.sql', 'r') as f:
            with self.connection.cursor() as cursor:
                for _ in cursor.execute(f.read(), multi=True):
                    pass
            self.connection.commit()

    def insert_product(self, product_name, nutrition_grade, stores, url, cat_name):
        with self.connection.cursor() as cursor:
            cursor.execute("""USE substitution_aliments;""")
            cursor.execute("""INSERT INTO aliments
                    (name,nutrition_grade,stores,url,categories_id)
                    VALUES (%s,%s,%s,%s,%s)""", (product_name, nutrition_grade, stores, url, cat_name))
        self.connection.commit()

    def display_prod_from_cat(self, cat):
        with self.connection.cursor() as cursor:
            cursor.execute("""USE substitution_aliments;""")
            cursor.execute(
                """SELECT id,name,nutrition_grade FROM aliments
                WHERE categories_id=%s""", (cat,))
            result = cursor.fetchall()
            print("\n#####\n\nProducts from the chosen category\n ID | NAME | Nutriscore")
            for row in result:
                print(" {} | {} | {} ".format(
                    row[0], row[1], row[2]))
            # pprint.pprint(result, indent=1)
        self.connection.commit()

    def find_better_nutri(self, id, cat_id):
        print("cat_id:{}".format(cat_id))
        with self.connection.cursor(buffered=True) as cursor:
            cursor.execute("""USE substitution_aliments;""")
            cursor.execute(
                """SELECT nutrition_grade FROM aliments
                WHERE id=%s""", (id,))
            nutri_chosen_product = str(cursor.fetchall())[3]
            print("\nnutriscore chosen product:{}".format(nutri_chosen_product))
            cursor.execute(
                """SELECT id FROM aliments
                WHERE id!=%s AND nutrition_grade<=%s AND categories_id=%s""", (id, nutri_chosen_product, cat_id,))
            # retour = cursor.fetchall()
            # for row in retour:
            #     print("retour {} ".format(
            #         row[0]))
            # print("retour:{}".format(retour))
            self.id_alternative_product = str(cursor.fetchone())[1]
            # print("id_alternative:{}".format(id_alternative_product))
            cursor.execute(
                """SELECT id,name,nutrition_grade FROM aliments
                WHERE id=%s """, (self.id_alternative_product,))
            alt = cursor.fetchone()
            print("\n#####\n\nAlternative product found:\n ID | NAME | Nutriscore")

            print(" {} | {} | {} ".format(
                alt[0], alt[1], alt[2]))
            # print("id alternative product:{}".format(id_alternative_product))
        self.connection.commit()

    def save_alternative(self, prod_id, alt_id):
        repeat = True
        while repeat == True:
            need_save = input(
                "\nWould you like to save this alternative aliment?\n1.YES\n2.NO\n")
            if need_save.isdigit():
                if int(need_save) == 1:
                    with self.connection.cursor(buffered=True) as cursor:
                        cursor.execute(
                            """INSERT INTO substituts (aliments_id,substitut_id)
                            VALUES(%s,%s)""",  (prod_id, alt_id))
                        print("Substitute SAVED")
                    self.connection.commit()
                if int(need_save) == 2:
                    print("Substitute NOT saved")
                repeat = False
            else:
                print("Wrong input, please type '1' or '2'\n")
                pass


if __name__ != "main":
    database = Database()
    # database.load_sql_file()
    # database.find_better_nutri(7, "Snacks")


# d/display categories and ask for selection
# e/display products in categories and ask for selection
# f/display substitutes for selected product
# g/ask user choice for substitute
# h/ask if user wants to save substitute
# g/insert the substitute id in DB

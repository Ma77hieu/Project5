"""
Creation of the database plus various operations like
inserting a product
display of the products of a category
find a product with a better nutriscore
save a substitution product in the database
"""

import mysql.connector
from classes.parameters.connexion import HOST, DATABASE, USER, PASSWD


class Database ():
    """
    The class representing our database
    """

    def __init__(self):

        self.connection = mysql.connector.connect(
            host=HOST,
            database=DATABASE,
            user=USER,
            passwd=PASSWD
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


if __name__ == "__main__":
    database = Database()
    # database.load_sql_file()
    # database.find_better_nutri(7, "Snacks")

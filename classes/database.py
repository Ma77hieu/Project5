import sqlite3
import json

# a/Create database from SQL file
connection = sqlite3.connect(
    "SQLmywb/substitution_aliments.db")
cursor = connection.cursor()
sql_file = open(
    "SQLmywb/Substitution_aliments.sql")
sql_as_string = sql_file.read()
cursor.executescript(sql_as_string)

# b/Import data from the OFF databse => see off_api.Py
# c/Insert values in database
NOMBRE_CATEGORIES = 8
NOMBRE_PRODUITS = 8
for each_cat in range(1, NOMBRE_CATEGORIES+1):
    for each_product in range(0, NOMBRE_PRODUITS):
        with open("JSON/CAT{}_OFF_API.json".format(each_cat)) as f:
            products_json = json.load(f)
        name = products_json["products"][each_product]["product_name_fr"]
        nutriscore = products_json["products"][each_product]["nutriscore_grade"]
        stores = products_json["products"][each_product]["stores"]
        url = products_json["products"][each_product]["url"]
        print('CAT:{}\nProduct number:{}\nname:{}\nnutri:{}\nstores:{}\nurl:{}\n'.format(
            each_cat, each_product+1, name, nutriscore, stores, url))
        cursor.execute("""INSERT INTO aliments
                (name,nutrition_grade,stores,url,categories_id)
                VALUES (?, ?, ?, ?,?)""", (name, nutriscore, stores, url, each_cat+1))
        connection.commit()


for row in cursor.execute("SELECT * FROM aliments"):
    print(row)
# d/display categories and ask for selection
# e/display products in categories and ask for selection
# f/offer save the product
# g/insert the substitute id in DB


# for row in cursor.execute("SELECT * FROM airports"):
#     print(row)

import sqlite3

# a/Create database from SQL file
connection = sqlite3.connect(
    "C:/Users/matthieu/GitHub/Project5/SQLmywb/substitution_aliments.db")
cursor = connection.cursor()
sql_file = open(
    "C:/Users/matthieu/GitHub/Project5/"
    "SQLmywb/Substitution_aliments.sql")
sql_as_string = sql_file.read()
cursor.executescript(sql_as_string)

# b/Import data from the OFF databse => see off_api.Py
# c/Insert values in database
cursor.execute("INSERT INTO aliments"
               "(name,nutrition_grade,stores,url,categories_id) "
               "VALUES ('noodle','c','',"
               "'https://static.openfoodfacts.org/images/products/073/762/806/4502/nutrition_en.12.400.jpg',"
               "7)")
connection.commit()
for row in cursor.execute("SELECT * FROM aliments"):
    print(row)
# d/display categories and ask for selection
# e/display products in categories and ask for selection
# f/offer save the product
# g/insert the substitute id in DB


# for row in cursor.execute("SELECT * FROM airports"):
#     print(row)

import json
import requests
import mysql.connector
import parameters.SQL_credentials as CRED
import parameters.constants as CONST
import database


class Off_api_data():

    def __init__(self):
        pass

    def fetch_all_data(self):
        url_req_categories = (
            'https://fr.openfoodfacts.org/categories.json&limit='
            + str(CONST.NBR_CAT+1)
        )
        categories = requests.get(url_req_categories)
        categories_json = json.loads(categories.content.decode('utf-8'))
        self.all_data = []
        for each_cat in range(0, CONST.NBR_CAT):
            cat_name = categories_json["tags"][each_cat]["name"]
            for each_product in range(0, CONST.NBR_PROD):
                products_url = (
                    'https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0='
                    + cat_name
                    + '&json=true&page_size='
                    + str(CONST.NBR_PROD)
                    + '&page=1'
                )
                products = requests.get(products_url)
                products_json = json.loads(products.content.decode('utf-8'))
                product_name = products_json["products"][each_product]["product_name_fr"]
                nutriscore = products_json["products"][each_product]["nutriscore_grade"]
                stores = products_json["products"][each_product]["stores"]
                url = products_json["products"][each_product]["url"]
                # print("product_name:{}\n nutriscore: {}\n stores: {}\n url:{}\ncategory{}\n".format(
                #     product_name, nutriscore, stores, url, cat_name))
                DB = database.Database()
                DB.insert_product(product_name, nutriscore,
                                  stores, url, cat_name)


if __name__ != "main":
    data = Off_api_data()
    data.fetch_all_data()

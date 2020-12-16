"""
Extraction of the data from the Open food fact (OFF) API
"""

import json
import requests
import classes.parameters.constants as CONST
import classes.database
from classes.category import Category
from classes.product import Product


class OffApiData():

    """
    This class represents the data extracted from the OFF API
    """

    def __init__(self):
        self.data_loaded = False
        self.category = Category()
        self.product = Product()

    def get_info(self):
        self.get_categories()
        self.get_products()
        # for each_cat in range(0, CONST.NBR_CAT):
        #     print("loading CATEGORY {} ".format(each_cat+1))
        #     cat_name = categories_json["tags"][each_cat]["name"]
        #     self.cat_list.append(cat_name)
        #     DB = classes.database.Database()
        #     DB.insert_cat(cat_name)
        #     self.get_product
        #     DB.insert_product(self.product_name, self.nutriscore,
        #                       self.stores, self.url, cat_name)
        # print(self.cat_list)

    def get_categories(self):
        self.cat_list = []
        url_req_categories = (
            'https://fr.openfoodfacts.org/categories.json&limit='
            + str(CONST.NBR_CAT+1)
        )
        self.categories = requests.get(url_req_categories)
        categories_json = json.loads(
            self.categories.content.decode('utf-8'))
        for each_cat in range(0, CONST.NBR_CAT):
            print("loading CATEGORY {} ".format(each_cat+1))
            cat_name = categories_json["tags"][each_cat]["name"]
            self.cat_list.append(cat_name)
            self.category.insert_cat(cat_name)
        print(self.cat_list)

    def get_products(self):
        """
        Retrieve data from the open food fact API
        """
        for cat_name in self.cat_list:
            for each_product in range(0, CONST.NBR_PROD):
                products_url = (
                    "https://fr.openfoodfacts.org/cgi/search.pl"
                    "?action=process&tagtype_0=categories&tag_contains_0"
                    "=contains&tag_0="
                    + cat_name
                    + '&json=true&page_size='
                    + str(CONST.NBR_PROD)
                    + '&page=1'
                )
                products = requests.get(products_url)
                products_json = json.loads(products.content.decode('utf-8'))
                self.product_name = products_json["products"][each_product]["product_name_fr"]
                self.nutriscore = products_json["products"][each_product]["nutriscore_grade"]
                self.stores = products_json["products"][each_product]["stores"]
                self.url = products_json["products"][each_product]["url"]
                self.product.insert_product(self.product_name, self.nutriscore,
                                            self.stores, self.url, cat_name)
        self.data_loaded = True


if __name__ == "__main__":
    data = OffApiData()
    data.get_categories()
    # data.fetch_data()

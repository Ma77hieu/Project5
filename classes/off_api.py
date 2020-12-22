"""
Extraction of the data from the Open food fact (OFF) API
"""

import json
import requests
import classes.parameters.constants as CONST
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
        self.cat_list = None
        self.categories = None
        self.product_name = None
        self.nutriscore = None
        self.stores = None
        self.url = None

    def get_info(self):
        """
        Get the information we need from the OFF API
        """
        self.get_categories()
        self.get_products()

    def get_categories(self):
        """
        Sends a request to the OFF API to receive a list of categories
        """
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

    def get_products(self):
        """
        Sends a request to the OFF API to receive a list of products
        within a specific category
        """
        elem = str
        for cat_name in self.cat_list:
            for prod in range(0, CONST.NBR_PROD):
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
                p_json = json.loads(products.content.decode('utf-8'))
                self.product_name = p_json["products"][prod]["product_name_fr"]
                if "nutriscore_grade" in p_json["products"][prod]:
                    self.nutriscore = p_json["products"][prod]["nutriscore_grade"]
                self.stores = p_json["products"][prod]["stores"]
                self.url = p_json["products"][prod]["url"]
                self.product.insert_product(self.product_name, self.nutriscore,
                                            self.stores, self.url, cat_name)
        self.data_loaded = True


if __name__ == "__main__":
    data = OffApiData()
    data.get_categories()
    # data.fetch_data()

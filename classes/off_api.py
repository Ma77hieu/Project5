"""
Extraction of the data from the Open food fact (OFF) API
"""

import json
import requests
import classes.parameters.constants as CONST
import classes.database


class OffApiData():

    """
    This class represents the data extracted from the OFF API
    """

    def __init__(self):
        url_req_categories = (
            'https://fr.openfoodfacts.org/categories.json&limit='
            + str(CONST.NBR_CAT+1)
        )
        self.categories = requests.get(url_req_categories)
        self.data_loaded = False
        self.cat_list = []

    def fetch_data(self):
        """
        Retrieve data from the open food fact API
        """

        for each_cat in range(0, CONST.NBR_CAT):
            print("loading CATEGORY {} ".format(each_cat+1))
            categories_json = json.loads(
                self.categories.content.decode('utf-8'))
            cat_name = categories_json["tags"][each_cat]["name"]
            self.cat_list.append(cat_name)
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
                product_name = products_json["products"][each_product]["product_name_fr"]
                nutriscore = products_json["products"][each_product]["nutriscore_grade"]
                stores = products_json["products"][each_product]["stores"]
                url = products_json["products"][each_product]["url"]
                DB = classes.database.Database()
                DB.insert_product(product_name, nutriscore,
                                  stores, url, cat_name)
        self.data_loaded = True


# if __name__ != __main__:
#     data = Off_api_data()
#     data.fetch_data()

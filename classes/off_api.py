import json
import requests

NOMBRE_CATEGORIES = 8
NOMBRE_PRODUITS = 8
url_req_categories = (
    'https://fr.openfoodfacts.org/categories.json&limit='
    + str(NOMBRE_CATEGORIES+1)
)
categories = requests.get(url_req_categories)
categories_json = json.loads(categories.content.decode('utf-8'))
categories_file = open(
    "JSON/categories_list_OFF_API.json", "w")
json.dump(categories_json, categories_file, indent=4)
for each_cat in range(0, NOMBRE_CATEGORIES):
    nom_categorie = categories_json["tags"][each_cat]["name"]
    print(categories_json["tags"][each_cat]["name"])
    for each_product in range(0, NOMBRE_PRODUITS):
        products_url = (
            'https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0='
            + nom_categorie
            + '&json=true&page_size='
            + str(NOMBRE_PRODUITS)
            + '&page=1'
        )
        products = requests.get(products_url)
        products_json = json.loads(products.content.decode('utf-8'))
        products_file = open(
            "JSON/CAT{}_OFF_API.json".format(
                each_cat+1), "w"
        )
        json.dump(products_json, products_file, indent=4)
        print(products_json["products"][each_product]["code"])

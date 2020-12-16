from classes.database import Database


class Model:

    def __init__(self):
        self.database = Database()

    def show(self):
        to_print = []
        # parcours tous les attributs
        for attr, value in self.__dict__.items():
            print(attr, value)
            to_print.append(value)
            # print(" {} | {} | {} ".format(
    #                  self.product_id, self.product_name, self.nutrition_grade))
            print(to_print)


if __name__ == "__main__":
    model = Model()

from Exercise.ex_4_Restaurant.product import Product


class Beverage(Product):

    def __init__(self, name: str, price: float,milliliters: float ):
        self.__milliliters = milliliters
        super().__init__(name, price)

    @property
    def milliliters(self):
        return self.__milliliters

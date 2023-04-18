from ex_5_Shop.product import Product
class ProductRepository:

    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        try:
            match = [product for product in self.products if product.name == product_name][0]
            return match
        except IndexError:
            pass

    def remove(self, product_name):
        try:
            match = [product for product in self.products if product.name == product_name][0]
            self.products.remove(match)
        except IndexError:
            pass

    def __repr__(self):
        return '\n'.join(f"{product.name}: {product.quantity}" for product in self.products)

class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        print("Available Products:")
        for product in self.products:
            print(product)

shop = Shop()

shop.add_product("Laptop")
shop.add_product("Mouse")
shop.add_product("Keyboard")

shop.list_products()
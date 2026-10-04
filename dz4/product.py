class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.category = category
        self.price = price

    def price_change(self, new_price):
        self.price = new_price


class Warehouse:
    def __init__(self, name):
        self.name = name
        self.stock = {}

    def change_quantity(self, product, quantity):
        self.stock[product] = quantity

    def get_quantity(self, product):
        return self.stock.get(product,0)


class Customer:
    def __init__(self, name, mail):
        self.name = name
        self.mail = mail
        self.list_orders = []

    def add_order(self, order):
        self.list_orders.append(order)


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append((product, quantity))

    def get_total(self):
        total = 0
        for product, quantity in self.items:
            total += quantity*product.price
        return total


class Shop:
    def __init__(self):
        self.products = {}
        self.customers = []
        self.warehouse = Warehouse("Главний склад")

    def from_file(self, filename):
        section = None
        with open(filename, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if line.startswith("["):
                    section = line[1:-1]
                elif section == "products":
                    name, price, category = line.split(";")
                    self.products[name] = Product(name, float(price), category)
                elif section == "customers":
                    name, mail = line.split(";")
                    self.customers.append(Customer(name, mail))
                elif section == "stock":
                    name, quantity = line.split(";")
                    self.warehouse.change_quantity(self.products[name], int(quantity))
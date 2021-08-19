# Write a class Product that has three attributes:
# type
# name
# price
# Then create a class ProductStore, which will have some Products and will operate with all products in the store. All
# methods, in case they can’t perform its action, should raise ValueError with appropriate error information.
# Tips: Use aggregation/composition concepts while implementing the ProductStore class. You can also implement additional
# classes to operate on a certain type of product, etc.
# Also, the ProductStore class must have the following methods:
# add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your store(30 percent)
#set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by input identifiers
# (type or name). The discount must be specified in percentage
# sell_product(product_name, amount) - removes a particular amount of products from the store if available, in other case raises an error. It also increments income if the sell_product method succeeds.
# get_income() - returns amount of many earned by ProductStore instance.
# get_all_products() - returns information about all available products in the store.
# get_product_info(product_name) - returns a tuple with product name and amount of items in the store.


class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price

    def __repr__(self):
        return (f"{self.type}, {self.name}, {self.price}")


class ProductStore:

    def __init__(self):
        self.products = {}
        self.summary_income = 0

    def add(self, obj, amount):
        if isinstance(obj, Product):
            self.products[obj.name] = {'product': obj, 'amount': amount}
        else:
            raise TypeError('ProductError')

    def get_product_info(self, product_name):
        if product_name in self.products:
           print((product_name, self.products[product_name]['amount']))
        else:
            raise TypeError('ProductError')

    def get_all_products(self):
        print(self.products)

    def set_discount(self, identifiers, percent: int, identifier_type = 'name'):
        if not identifiers or len(identifiers) == 0:
            print('Wrong identifier')
            return

        if percent <= 0:
            print('Wrong percent')
            return

        if identifier_type != 'name' and identifier_type != 'type':
            print('Wrong identifier type')
            return

        if identifier_type == 'name':
            for identifier in identifiers:
                if identifier not in self.products:
                    print('Identifier not found')
                    return

                self.products[identifier]['discount'] = percent
                print(self.products)

        else:
            for identifier in identifiers:
                for product in self.products:
                    if self.products[product]['product'].type == identifier:
                        self.products[product]['discount'] = percent
                        print(self.products)

    def sell(self, name, amount1):
        product = self.products[name]
        a = product['amount']
        b = self.products[name]['product'].price
        if  0 < amount1 < a:
            product['amount'] -= amount1
            self.get_all_products()
            if 'discount' not in product:
                self.summary_income += amount1 * b
                print(f'Income is {amount1 * b}')
            else:
                self.summary_income += amount1 * b * 0.01 * product['discount']
                print(f'Income with discount is {amount1 * b * 0.01 * product["discount"]}')
        else:
            raise TypeError('AmountError')

    def get_income(self):
        print(f'Summary income is {self.summary_income}')


s = ProductStore()

#p = Product()
p = Product('Sport', 'Jack', 100)
#p2 = {'type': 'Food', 'name': 'Ramen', 'price': 1.5}
p2 = Product('Food', 'Ramen', 20)
p3 = Product('Food', 'Cheese', 50)

s.add(p, 40)
s.add(p2, 20)
s.add(p3, 500)
s.get_all_products()

s.get_product_info('Jack')
s.set_discount(['Food'], 50, 'type')
s.sell('Ramen', 10)
s.sell('Jack', 20)
s.get_income()

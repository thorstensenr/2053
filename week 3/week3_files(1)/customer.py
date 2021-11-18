from person import Person


class Customer(Person):
    def __init__(self, first_name, last_name, orders):
        # use super() to call the initializer of the super class Person
        # use super() to call any class method in the super class
        super().__init__(first_name, last_name)
        self.orders = orders

    def __str__(self):
        super().__str__()

    def add_order(self, order_num):
        self.orders.append(order_num)

    def get_orders(self):
        return self.orders

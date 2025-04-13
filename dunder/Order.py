


class Order:
    def  __init__(self,cart, customer):
        self.cart = cart
        self.customer = customer

    def __len__(self):
        return len(self.cart)

    def __str__(self):
        return f"{self.customer} bought {self.cart}"

    def __bool__(self):
        return len(self.cart) > 0

    def add_item(self,other):
        self.cart.append(other)

order = Order(['Mouse','Screen','Keyboard'], 'John')
print(bool(order))

order.add_item('usb cable')
print(order.cart)




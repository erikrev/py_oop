class Kettle(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

print("Models: {0.make} {0.price} {1.make} {1.price}".format(kenwood, hamilton))
print(hamilton.on)
# hamilton.switch_on()
print(hamilton.on)

Kettle.switch_on(kenwood)
print(kenwood.on)

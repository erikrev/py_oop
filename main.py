class Kettle(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.price)

kenwood.price = 13
print(kenwood.price)

class Kettle(object):
    power_source = "electricity"

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

print("*" * 80)
kenwood.power = 1.5
print(kenwood.power)
# print(hamilton.power) ERROR
print("Switch to atomic power")
Kettle.power_source = "atomic"
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)
print("Switch kenwood to gas")
kenwood.power_source = "gas"
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
Kettle.power_source = "atomic"

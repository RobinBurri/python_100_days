# *args (positional arguments)
def add(*args):
    t = 0
    for arg in args:
        t += arg
    return t


# args = (1, 2, 3, 4, 5)

total = add(1, 2, 3, 4, 5)
print(total)


# kwargs (keyword arguments)
def addkwargs(**kwargs):
    t = 0
    for _, value in kwargs.items():
        t += value
    return t


# kwargs = {"one": 1, "two": 2, "three": 3}

print(addkwargs(one=1, two=2, three=3))


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.color = kw.get("color")
        self.model = kw.get("model")


my_car = Car(make="Ford", color="blue", model="Mustang")
print(my_car.make)
print(my_car.color)
print(my_car.model)

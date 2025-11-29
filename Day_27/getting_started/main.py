def add (*args):
    summation = 0
    for n in args:
       summation += n
    return summation

print(add(2, 4, 7, 6, 7, 3, 2))


def calculate (n , **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=4, multiply=5)


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.speed = kwargs.get("speed")

my_car = Car(make="Nissan", model="Gtr R35")
print(my_car.make, my_car.model, my_car.speed)
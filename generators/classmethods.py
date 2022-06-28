class Car:
    def __init__(self, brand, color, available=False):
        self.brand = brand
        self.color = color
        self.availableproperty = available

    @classmethod
    def available(cls, brand, color, available):
        return cls(brand, color, available)

    @staticmethod
    def is_available(check):
        return check


first_car = Car('Mustang', 'red')
second_car = Car.available('Camaro', 'black', True)
print(first_car.brand, first_car.color)
print(second_car.brand, second_car.color)
ls = [first_car, second_car]
for i in range(2):
    print('{} is available: {}'.format(ls[i].brand, ls[i].is_available(ls[i].availableproperty)))

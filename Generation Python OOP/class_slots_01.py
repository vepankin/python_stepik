class Car:
    def __init__(self, color, owner):
        self.color = color
        self.owner = owner

class ElectricCar(Car):
    __slots__ = ('power_reserve',)

    def __init__(self, color, owner, power_reserve):
        super().__init__(color, owner)
        self.power_reserve = power_reserve
        self.torque = 350


car = ElectricCar('yellow', 'Gvido', 400)

car.hp = 238

print(car.__slots__)
print(car.__dict__)
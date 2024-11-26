class Distance(float):
    def __new__(cls, value, unit):
        instance = super().__new__(cls, value)
        instance.unit = unit
        return instance


distance = Distance(1, 'Meters')
distance = 33.5
print(distance)
print(distance, distance.unit)

distance.unit = 'Kilometers'
print(distance, distance.unit)
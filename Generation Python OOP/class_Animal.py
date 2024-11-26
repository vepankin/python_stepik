class Animal:
    pass

class Cat(Animal):
    def __new__(cls, *args, **kwargs):
        print('1. Вызова метода __new__()')
        return Animal()

    def __init__(self, name):
        print('2. Вызова метода __init__()')
        self.name = name


cat = Cat('Кемаль')
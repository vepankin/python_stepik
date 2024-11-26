class Cat:
    def __new__(cls, *args, **kwargs):
        print('calling __new__ :')
        print(super())
        #return object.__new__(cls)
        #return super(Cat, cls).__new__(cls)
        #return super().__new__(cls)
        return super(Cat, cls).__new__(cls)
    
    def __init__(self):
        print('calling __init__ :')
        print(super(Cat, Cat))
        print(super(Cat, self))
        #super().__init__()
        #super(Cat, Cat).__init__(self)
        super(Cat, self).__init__()
        
    def talk(self):
        print('Meow...')
    
c = Cat()    
c.talk()
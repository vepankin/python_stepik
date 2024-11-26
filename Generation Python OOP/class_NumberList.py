from collections import UserList

class NumberList(UserList):
    @staticmethod
    def isproperitem(item):
        if not isinstance(item, (int,float)):
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
        return True
        
    def __init__(self, iterable=()):
        print('init')
        super().__init__(x for x in iterable if self.isproperitem(x))
        
        
    def __setitem__(self, index, item):
        print('setitem')
        if self.isproperitem(item):
            super().__setitem__(index,item)

    def insert(self, index, item):
        print('insert')
        if self.isproperitem(item):
            super().insert(index,item)

    def append(self, item):
        print('append')
        if self.isproperitem(item):
            super().append(item)

    def extend(self, other):
        print('extend')
        
        if isinstance(other, type(self)):
            self.data.extend(other)
        else:
            self.data.extend(item for item in other if self.isproperitem(item))

    def __iadd__(self, other):
        print('iadd')
        self.extend(other)
        return self


nl = NumberList([2,3])

nl2 = nl + [4,5]
print(nl2, type(nl2))

nl3 = [0,1] + nl
print(nl3, type(nl3))

ul = UserList(['a','b'])
print(type(ul + [1,2]))

class MyList(list):
    
    print('-----------------------')
      
    @staticmethod
    def isproperitem(item):
        return True
        
    def __init__(self, iterable=()):
        print('init')
        super().__init__(x for x in iterable if self.isproperitem(x))
        
        
    def __setitem__(self, index, item):
        print('setitem')
        if self.isproperitem(item):
            super().__setitem__(index,item)

    def insert(self, index, item):
        print('insert')
        if self.isproperitem(item):
            super().insert(index,item)

    def append(self, item):
        print('append')
        if self.isproperitem(item):
            super().append(item)

    def extend(self, other):
        print('extend')
        super().extend(other)

    def __iadd__(self, other):
        print('iadd')
        self.extend(other)
        return self

ml = MyList([1,2,3,4,5])
ml += [123,788]
print(type(ml))
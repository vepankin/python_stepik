class AdvancedTuple(tuple):
    
    def __add__(self, other):
        if hasattr(other, '__iter__'):
            return __class__([*self, *iter(other)])
        return NotImplemented
    
    def __radd__(self, other):
        if hasattr(other, '__iter__'):
            return __class__([*iter(other), *self])
        return NotImplemented
    
    def call_add(self, other):
        return self.__add__(other)
    
    def get_class(self):
        return __class__
    
at1 = AdvancedTuple([1,2,3,4])
t = ( 5,6,7,8 )
at2 = at1.call_add(t)

print(at2)
print(at2.get_class())
print('callable =', callable(at2.get_class()))
from math import sqrt

class Vector:
    
    def __init__(self, *args):
        self._data = args
        
    def __repr__(self):
        return f'{self._data}'
    
    def __len__(self):
        return len(self._data)
    
    def __add__(self, other):
        if isinstance(other, Vector):
            if len(self) == len(other):
                return Vector(*map(sum, zip(self._data, other._data)))
            raise ValueError('Векторы должны иметь равную длину')    
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, Vector):
            if len(self) == len(other):
                return Vector(*map(lambda p: p[0]-p[1], zip(self._data, other._data)))
            raise ValueError('Векторы должны иметь равную длину')    
        return NotImplemented    

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self) == len(other):
                return sum(map(lambda p: p[0]*p[1], zip(self._data, other._data)))
            raise ValueError('Векторы должны иметь равную длину')    
        return NotImplemented    
    
    def norm(self):
        return sqrt(sum(map(lambda p: p**2, self._data)))

    def __eq__(self, other):
        if isinstance(other, Vector):
            if len(self) == len(other):
                return all(map(lambda p: p[0]==p[1], zip(self._data, other._data)))
            raise ValueError('Векторы должны иметь равную длину')    
        return NotImplemented     
    
a = Vector(1, 2, 3)
b = Vector(3, 4, 5)
c = Vector(5, 6, 7, 8)

print(a)                       # (1, 2, 3)
print(b)                       # (3, 4, 5)
print(c)                       # (5, 6, 7, 8)

print(a + b)                   # (4, 6, 8)
print(a - b)                   # (-2, -2, -2)
print(a * b)                   # 1*3 + 2*4 + 3*5 = 26
print(c.norm())                # sqrt(5**2 + 6**2 + 7**2 + 8**2) = sqrt(174) = 13.19090595827292

print(a == Vector(1, 2, 3))    # True
print(a == Vector(4, 5, 6))    # False
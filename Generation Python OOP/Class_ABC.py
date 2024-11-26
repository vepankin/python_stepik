class A:
    a = 1
class B(A):
    b = 2

class C(B):
    c = 3
    
    
c = C()

print(c.a, c.b, c.c)

A.a = 100

print(c.a, c.b, c.c)
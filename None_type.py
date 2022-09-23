#n = 2
#d = None

#if n == 1:
    #d = 23

#if d is None:
    #print('<None>')
    
def foo(x: int = 33) -> None:
    l.append(3)
    print('x = ', x)
    return 23

l = list()
y = foo(l)

print(foo.__annotations__)
print(*l)

def bar():
    i = 10
    print('id inside:', id(i))
    return i

i = 20
print('id outside:', id(i))
i = bar()
print('id after bar:', id(i))
def foo():
    global i
    i = 100


i = 0
foo()
print(i)
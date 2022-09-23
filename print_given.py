def print_given(*arg, **kwd):
    for a in arg:
        print(a, type(a))
    for k, v in sorted(kwd.items()):
        print(k, v, type(v))
        
print_given(b=2, d=4, a=1, c=3)
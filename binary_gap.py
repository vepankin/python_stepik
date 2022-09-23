n = 0b100000001001000
s = '{:b}'.format(n)
print(s)
l = s.split('1')[1:-1]
print(l)
result = 0
if len(l):
    result = len(max(l))
print(result)
'''
n, k = int(input()), int(input())
l = [x for x in range(1, n + 1)]

while len(l) >= k and k > 1:
    print(*l)
    l = l[k:] + l[:k - 1]

print(*l)
print('-' * 10)

while len(l) > 1:
    print(*l)
    for j in range(k - 1):
        l = l[1:] + l[:1]
    l = l[1:]

print(l)
'''

print('-' * 10)

z = 0b100

print(f'{z:d}')
z >>= 1
print(f'{z:d}')
print('this is decimal format: {:d}'.format(z))
print(bin(z))
n, x, y, a, b = 5, 1, 3, 4, 5

z = list(range(n + 1))
print(z)

for r in ((x, y), (a, b)):
    print(z[:r[0]], z[r[1]:r[0] - 1:-1], z[r[1] + 1:])

    z = z[:r[0]] + z[r[1]:r[0] - 1:-1] + z[r[1] + 1:]
    
print(*z[1:])
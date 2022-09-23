n = 100
d = {}
result = 0
for x in range(1, n+1):
    k = sum(map(int, str(x)))
    d.setdefault(k, []).append(x)
    result = max(result, len(d[k]))

print(result)
s = input()
r = len(s) % 3

print(s[:3 if r == 0 else r], end='')

if len(s) > 3:
    k = (len(s) - r) // 3
    for i in range(1 if r == 0 else 0, k):
        print(',', s[r + 3 * i: r + 3 * i + 3], sep='', end='')

def sieve(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    i = 2
    while (i * i <= n):
        print('i =', i)
        if sieve[i]:
            k = i * i
            while (k <= n):
                print('...k =', k)
                sieve[k] = False
                k += i
        i += 1
    return sieve

n = 25
s = sieve(n)
print('s =', s)
d = dict([(i, s[i]) for i in range(n + 1) if s[i] == True])
print(list(d.keys()))
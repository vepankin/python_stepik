def arrayF(n):
    F = [0] * (n + 1)
    i = 2
    while (i * i <= n):
        if (F[i] == 0):
            k = i * i
            while (k <= n):
                if (F[k] == 0):
                    F[k] = i
                k += i
        i += 1
    return F

def factorization(x, F):
    primeFactors = []
    while (F[x] > 0):
        primeFactors += [F[x]]
        x /= F[x]
        x = int(x)
    primeFactors += [x]
    return primeFactors

x = 1000000000
F = arrayF(x)
print(F)
fz = factorization(x, F)
print(fz)
N = 36
l = [1]
N1 = N
while N1 > 1:
    for i in range(2, N1 + 1):
        if N1 % i == 0:
            N1 = N1 // i
            l += [N1, i]
            break

l = list(set(l))

while True:

    print(sorted(l))
    l2 = l.copy()
    
    f = True
    for x in l:
        for y in l:
            r = x * y
            if r not in l and r not in l2 and r <= N and N % r == 0:
                l2.append(r)
                f = False
    if f:
        break
    else:
        l = l2
                

print(len(l2))

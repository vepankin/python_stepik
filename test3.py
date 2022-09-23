S = 'aabbcc'
C = [1, 2, 1, 2, 1, 2]

def get_min_cost(l, C):

    cost = C[l[0]:l[-1] + 1]
    print('cost =', cost)
    sorted_cost = sorted(cost)
    print(' sc =', sorted_cost)

    return sum(sorted_cost[:len(cost) - 1])
    

ch = S[0]
l = [0]

for i in range(1, len(S)):
    if ch == S[i]:
        l.append(i)
    else:
        if len(l) > 1:
            # calc the cost
            min_cost = get_min_cost(l, C)
            print(min_cost)
        l = [i]
        ch = S[i]

if len(l) > 1:
    # calc the cost
    min_cost = get_min_cost(l, C)
    print(min_cost)
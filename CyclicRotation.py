def solution(A, K):
    # write your code in Python 3.6
    if len(set(A)) > 1 or (len(A) and K % len(A) == 0):
        for _ in range(K % len(A)):
            A = [A[-1]] + A[:-1]
    return(A)

A = []
K = 3
print("A =", A)
print("R =", solution(A, K))
print("A =", A)
import array
import time

def g1(string):
    return map(ord, string)

def g2(string):
    arr = array.array('b')
    arr.frombytes(string.encode())
    return arr.tolist()

t1 = time.perf_counter_ns()
l = g1('1234567890123456789012345678901234567890')
t2 = time.perf_counter_ns()

print(f'Время работы g1 = {t2-t1}')

t1 = time.perf_counter_ns()
l = g2('1234567890123456789012345678901234567890')
t2 = time.perf_counter_ns()

print(f'Время работы g2 = {t2-t1}')

t1, t11 = time.monotonic(), time.perf_counter()
for _ in range(3):
    time.sleep(1)
t2, t22 = time.monotonic(), time.perf_counter()
print(f'Время работы (monotonic) = {t2-t1}')
print(f'Время работы (perf_counter) = {t22-t11}')
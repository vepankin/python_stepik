import time
from math import factorial                   # функция из модуля math
import calendar
from datetime import date

def factorial_recurrent(n):                  # рекурсивная функция
    if n == 0:
        return 1
    return n * factorial_recurrent(n - 1)    

def factorial_classic(n):                    # итеративная функция
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

def calculate_it(func, *args):
    t1 = time.perf_counter_ns()
    res = func(*args)
    t2 = time.perf_counter_ns()
    return res, t2-t1

def get_the_fastest_func(funcs, *arg):
    fastest_func = None
    fastest_time = -1
    for func in funcs:
        r, t = calculate_it(func, *arg)
        # show time
        print(func.__name__, t)
        
        if fastest_time < 0 or fastest_time > t:
            fastest_func = func
            fastest_time = t
    return fastest_func

def for_and_append():                            # с использованием цикла for и метода append()
    iterations = 10_000_000
    result = []
    for i in range(iterations):
        result.append(i + 1)
    return result

# с использованием списочного выражения
def list_comprehension():
    iterations = 10_000_000
    return [i + 1 for i in range(iterations)]

# с использованием цикла for и метода append()
def for_and_append_i(iterable):
    result = []
    for elem in iterable:
        result.append(elem)
    return result
        
# с использованием списочного выражения
def list_comprehension_i(iterable):
    return [elem for elem in iterable]    

# с использованием встроенной функции list()
def list_function_i(iterable):
    return list(iterable) 

def get_all_mondays(year):
    return [date(year, m, w[0]) for m in range(1, 13) for w in calendar.monthcalendar(year, m) if w[0]]

def get_all_mondays_append(year):
    mondays = []
    for month in range(1, 13):
        for week in calendar.monthcalendar(year, month):
            monday = week[0]
            if monday:
                mondays.append(date(year, month, monday))
    return mondays


"""
funcs = (factorial, factorial_recurrent, factorial_classic)
fastest_func = get_the_fastest_func(funcs, 10)
print('The fastest is \'{}\''.format(fastest_func.__name__))

funcs = (for_and_append, list_comprehension)
fastest_func = get_the_fastest_func(funcs)
print('The fastest is \'{}\''.format(fastest_func.__name__))

funcs = (for_and_append_i, list_comprehension_i, list_function_i)
fastest_func = get_the_fastest_func(funcs, range(1_000_000))
print('The fastest is \'{}\''.format(fastest_func.__name__))
"""

funcs = (get_all_mondays_append, get_all_mondays)
fastest_func = get_the_fastest_func(funcs, 3030)
print('The fastest is \'{}\''.format(fastest_func.__name__))
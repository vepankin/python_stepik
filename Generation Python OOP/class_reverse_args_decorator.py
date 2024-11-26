import functools

class MaxCallsException(Exception):
    pass

class limited_calls:
    def __init__(self, n):
        self.n = n
        
    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if self.n:
                value = func(*args, **kwargs)
                self.n -= 1
                return value
            raise MaxCallsException('Превышено допустимое количество вызовов')    
        return wrapper
    
class reverse_args:
    def __init__(self, func):
        functools.update_wrapper(self, func)        # сохранение информации о декорируемой функции
        self.func = func
        
    def __call__(self, *args, **kwargs):
        args = reversed(args)
        return self.func(*args, **kwargs)
    
    
class reverse_args_v2:
        
    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            args = reversed(args)
            return func(*args, **kwargs)
        return wrapper    

@reverse_args_v2()
def concat(a, b, c):
    return a + b + c
        
print(concat('apple', 'cherry', 'melon'))
# Decorator pattern

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('*****')
        func(*args, **kwargs)
        print('*****')
    return wrap_func

@my_decorator
def hello(a, b):
    print(a, b)

hello('hi',':)')

from time import time
from unittest import result

def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper

@performance
def long_time():
    for i in range(1000000):
        i*5

long_time()


import time
from functools import wraps

def fn_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print("Time usage of function '{}' is {:.5f}s".format(function.__name__, t1 - t0))
        return result
    return function_timer


@fn_timer
def say_hello(name):
    print('Hello {}'.format(name))


if __name__ == '__main__':
    say_hello('Vincent')


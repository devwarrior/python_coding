''' timing with decorator '''
from functools import wraps
import time


def time_fun(method):
    '''
    @brief decorator to compute execution time of a function.
    '''
    @wraps(method)
    def wrap_timed(*args, **kw):
        '''
            @brief compute time elapsed while executing
            @param *args arguments for called method
            @param **kw arguments for called method
        '''
        start_time = time.time()
        result = method(*args, **kw)
        elapsed_time = time.time() - start_time
        print(method.__name__ + " " + str(elapsed_time*1000))
        return result
    return wrap_timed


@time_fun
def do_things():
    '''
    @brief a function that prints hello world
    '''
    print('Hello World')

if __name__ == '__main__':
    do_things()

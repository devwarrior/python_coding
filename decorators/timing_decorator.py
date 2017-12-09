from functools import wraps
import time


def time_fun(method):
    '''
    @brief decorator to compute execution time of a function.
    '''
    @wraps(method)
    def wrap_timed(*args, **kw):
        start_time = time.time()
        result = method(*args, **kw)
        elapsed_time = time.time() - start_time
        print(method.__name__ + " " + str(elapsed_time*1000))
        return result
    return wrap_timed


@time_fun
def simulate_do_things():
    print('here')

def main():
    simulate_do_things()
if __name__ == '__main__':
    main()
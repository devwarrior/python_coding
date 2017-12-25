''' check for map list '''
import time
from functools import wraps

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
        print(elapsed_time*1000, end='')
        # print(method.__name__ + " " + str(elapsed_time*1000))
        return result
    return wrap_timed

@time_fun
def create_list_for(num):
    the_list = []
    for i in range(num):
        the_list.append(i)
    return the_list

@time_fun
def create_list_comp(num):
    the_list = [x for x in range(num)]
    return the_list

@time_fun
def create_list_map(num):
    the_list = list(map(lambda f: f, range(num)))
    return the_list

def process(val):
    return val / 2

@time_fun
def process_entries_for(num):
    tot = 0
    for idx in range(num):
        tot = tot + process(idx)
    return tot

@time_fun
def process_entries_comp(num):
    return sum([process(x) for x in range(num)])

@time_fun
def process_entries_map(num):
    return sum(map(lambda f: f/2, range(num)))

if __name__ == '__main__':
    test_data = [1000, 10000, 100000, 1000000, 10000000, 100000000]
    for item in test_data:
        print(" "+str(len(create_list_for(item))))

    for item in test_data:
        print(" "+str(len(create_list_comp(item))))

    for item in test_data:
        print(" "+str(len(create_list_map(item))))

    for item in test_data:
        print(" "+str(process_entries_for(item))+" "+str(item))

    for item in test_data:
        print(" "+str(process_entries_comp(item))+" "+str(item))

    for item in test_data:
        print(" "+str(process_entries_map(item))+" "+str(item))


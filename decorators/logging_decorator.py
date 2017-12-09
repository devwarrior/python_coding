'''
decorator to log functions executions
'''
from functools import wraps
import logging
import time

def log(logger, level='info'):
    '''
    @brief decorator implementing the logging of a function.
    '''
    def log_decorator(method):
        '''
        @brief decorator implementing the logging of a function.
        '''
        @wraps(method)
        def wrapper(*args, **kw):
            '''
                @brief compute time elapsed while executing
                @param *args arguments for called method
                @param **kw arguments for called method
            '''
            getattr(logger, level)(method.__name__)
            return method(*args, **kw)
        return wrapper
    return log_decorator

LOGGER = logging.getLogger('__main__')
LOGGER.setLevel(logging.DEBUG)
F_HANDLER = logging.FileHandler('log_file.log')
F_HANDLER.setLevel(logging.DEBUG)
LOGGER.addHandler(F_HANDLER)
FORMATTER = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
F_HANDLER.setFormatter(FORMATTER)

@log(LOGGER, level='debug')
def simulate_do_things(tvalue):
    '''
    @brief a function that simulates work
    '''
    time.sleep(tvalue)

@log(LOGGER, level='warning')
@log(LOGGER, level='warning')
def simulate_do_things1(tvalue):
    '''
    @brief a function that simulates work
    '''
    time.sleep(tvalue)


if __name__ == '__main__':
    simulate_do_things1(1)
    simulate_do_things(0.8)

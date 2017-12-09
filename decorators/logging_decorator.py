'''
decorator to log functions executions
'''
from functools import wraps
import logging
import time

def log(logger, level='info'):
    def log_decorator(fn):
        @wraps(fn)
        def wrapper(*a, **kwa):
            getattr(logger, level)(fn.__name__)
            return fn(*a, **kwa)
        return wrapper
    return log_decorator

logger = logging.getLogger('__main__')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

@log(logger, level='debug')
def simulate_do_things(tvalue):
    print("simulate_do_things")
    time.sleep(tvalue)

@log(logger, level='warning')
@log(logger, level='warning')
def simulate_do_things1(tvalue):
    time.sleep(tvalue)


if __name__ == '__main__':
    simulate_do_things1(1)
    simulate_do_things(0.8)

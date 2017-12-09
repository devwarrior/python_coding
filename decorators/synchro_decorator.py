'''
decorator to synchronize threads
'''
import threading
import time

lock = threading.Lock()

def synchro(lock_id):
    '''
    @brief implements a decorator to synchronize threads.
    '''
    def wrap(f):
        def newFunction(*args, **kw):
            with lock_id:
                return f(*args, **kw)
        return newFunction
    return wrap


def worker(name, timing):
    '''
    @brief implements a worker thread
    '''
    for i in range(10):
        time.sleep(timing)
        print(name)

@synchro(lock)
def worker1(name, timing):
    '''
    @brief implements a worker thread
    '''
    for i in range(10):
        time.sleep(timing)
        print(name)


if __name__ == '__main__':
    print('Not synchronized threads')
    TH1 = threading.Thread(target=worker, args=('TH1', 0.1,))
    TH2 = threading.Thread(target=worker, args=('TH2', 0.2,))
    TH1.start()
    TH2.start()
    TH1.join()
    TH2.join()
    print('Synchronized threads')
    STH1 = threading.Thread(target=worker1, args=('STH1', 0.1,))
    STH2 = threading.Thread(target=worker1, args=('STH2', 0.5,))
    STH1.start()
    STH2.start()

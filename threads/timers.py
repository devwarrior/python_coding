# ''' sample code for timer in python '''
# import threading

# def timed_worker():
#     '''
#     @brief a function that does something
#     '''
#     print('timed_worker')

# if __name__ == '__main__':
#     TH1 = threading.Timer(5, timed_worker)
#     TH1.start()


import threading
import time

def timed_worker(timed_worker_name):
    print('timed_worker'+timed_worker_name)

if __name__ == '__main__':
    TW1 = threading.Timer(5, timed_worker, args=('TW1',))
    TW2 = threading.Timer(2, timed_worker, args=('TW2',))
    TW1.start()
    TW2.start()


# ''' sample code for timer in python '''
# import threading

# def timed_worker(iterations=5, name='name'):
#     '''
#     @brief a function that does something
#     '''
#     for _ in range(iterations):
#         print('timed_worker')

# if __name__ == '__main__':
#     TH1 = threading.Timer(5, timed_worker, args)
#     TH1 = threading.Timer(5, timed_worker)
#     TH1.start()

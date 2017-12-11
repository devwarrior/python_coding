''' sample code for timer in python '''
import threading

def timed_worker():
    '''
    @brief a function that does something
    '''
    print('timed_worker')

if __name__ == '__main__':
    TH1 = threading.Timer(5, timed_worker)
    TH1.start()

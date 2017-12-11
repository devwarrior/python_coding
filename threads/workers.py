''' Worker threads sample code '''
import threading
import time


def worker(worker_name, timing):
    '''
    @brief a function that does something
    '''
    for _ in range(10):
        print(worker_name)
        time.sleep(timing)

if __name__ == '__main__':
    TH1 = threading.Thread(target=worker, args=('TH1', 0.1,))
    TH2 = threading.Thread(target=worker, args=('TH2', 0.2,))
    TH1.start()
    TH2.start()
    TH1.join()
    TH2.join()

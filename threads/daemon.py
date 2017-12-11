''' working threads vs daemon thread '''
import threading
import time

# Daemons are only useful when the main program is running,
# and it's okay to kill them off once the other non-daemon
# threads have exited. Without daemon threads, we have to
# keep track of them, and tell them to exit, before our
# program can completely quit. By setting them as daemon
# threads, we can let them run and forget about them, and
# when our program quits, any daemon threads are killed
# automatically.

def daemon():
    '''
    @brief simulates a ripetitive job
    '''
    while True:
        time.sleep(1)
        print('daemon')

def worker(worker_name, timing):
    '''
    @brief a function that does something
    '''
    for _ in range(100):
        print(worker_name)
        time.sleep(timing)

if __name__ == '__main__':
    DAE = threading.Thread(target=daemon)
    DAE.setDaemon(True)
    DAE.start()
    TH1 = threading.Thread(target=worker, args=('TH1', 0.1,))
    TH2 = threading.Thread(target=worker, args=('TH2', 0.2,))
    TH1.start()
    TH2.start()

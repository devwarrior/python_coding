''' sample code to handle the list of running threads. '''
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

def worker(timing):
    '''
    @brief a function that does something
    '''
    for _ in range(4):
        time.sleep(timing)

def list_threads():
    '''
    @brief prints the list of running threads.
    '''
    for thread in threading.enumerate():
        print(thread.getName())

if __name__ == '__main__':
    DAE = threading.Thread(target=daemon, name='daemon')
    DAE.setDaemon(True)
    DAE.start()
    TH1 = threading.Thread(target=worker, args=(5,), name='pippo')
    TH2 = threading.Thread(target=worker, args=(5,), name='pluto')
    TH1.start()
    TH2.start()
    list_threads()

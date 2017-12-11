''' sample code for signaling between threads '''
import threading
import time

class ConsumerThread(threading.Thread):
    '''
    Implements a consumer thread subclassing threading.Thread
    '''
    def __init__(self, name, Evt):
        threading.Thread.__init__(self)
        self.name = name
        self.evt = Evt

    def run(self):
        print(self.name)
        self.main()

    def wait_for_event(self):
        '''
        @brief this method waits for an event
        @param self the class
        '''
        print(self.name + ' Waiting for event')
        event_is_set = self.evt.wait()
        print(self.name + ' event set: %s', event_is_set)

    def main(self):
        '''
        @brief this the main function of the thread class.
        @param self the class
        '''
        while True:
            self.wait_for_event()
            print(self.name + ' dooing some job')

def do_something():
    ''' @brief a function that does something '''
    while True:
        print('doing_something')
        time.sleep(3)
        EVT.set()
        EVT.clear()

if __name__ == '__main__':
    EVT = threading.Event()
    CONSUMER = ConsumerThread('consumer thread', EVT)
    CONSUMER.start()
    TH1 = threading.Thread(target=do_something)
    TH1.start()
    print('Event is set')

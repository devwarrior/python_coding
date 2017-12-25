'''
simple module implements a circular queue. Full info and description on www.xappsoftware.com
'''
import time
import threading
LOCK = threading.Lock()


def synchro(lock_id):
    '''
    @brief a decorator to synchronize threads.
    '''
    def wrap(method):
        def wrapped_function(*args, **kw):
            with lock_id:
                return method(*args, **kw)
        return wrapped_function
    return wrap

class CQueue():
    ''' implements a circular queue '''
    def __init__(self, q_size=32):
        self.queue = list()
        self.head = 0
        self.tail = 0
        self.q_size = q_size

    @synchro(LOCK)
    def enqueue(self, data):
        '''
        @brief append an element at
        @param data the item to be appended to the list
        @return True if there is enough space to append the element, False otherwise.
        '''
        if self.size() == self.q_size-1:
            print("Queue Full!")
            return False
        self.queue.append(data)
        self.tail = (self.tail + 1) % self.q_size
        return True

    @synchro(LOCK)
    def dequeue(self):
        '''
        @brief append an element at
        @return the item retrieved from the list, or False if the queue is empty
        '''
        if self.size() == 0:
            print("Queue Empty!")
            return False
        data = self.queue[self.head]
        self.head = (self.head + 1) % self.q_size
        return data

    def size(self):
        '''
        @brief compute the number of valid elements in the queue
        @return the number of valid elements in the queue
        '''
        if self.tail >= self.head:
            return self.tail-self.head
        return self.q_size - (self.head-self.tail)

    @synchro(LOCK)
    def print_queue(self):
        '''
        @brief Prints on the standard output the content of the queue
        @return the number of valid elements in the queue
        '''
        appo = list()
        for i in range(self.head, self.size()):
            appo.append(self.queue[i%self.q_size])
        print(appo)


def producer(the_queue, timing):
    '''
    @brief produce and insert new data into the_queue
    @param the_queue the queue used to store data
    @param timing the interval of time between two insert
    '''
    for counter in range(50):
        the_queue.enqueue(counter)
        time.sleep(timing)

def consumer(the_queue, timing):
    '''
    @brief consume dataof the queue.
    @param the_queue the queue where t retrieve data.
    @param timing the interval of time between two retrieve.
    '''
    for _ in range(20):
        time.sleep(timing)
        print('consumer - get() - ' + str(the_queue.dequeue()))
        print('consumer - list() -')
        the_queue.print_queue()



if __name__ == '__main__':
    C_QUEUE = CQueue(q_size=32)

    CONSUMER_C_QUEUE = threading.Thread(group=None, target=consumer,
                                        name='consumer_queue', args=(C_QUEUE, 0.8))
    CONSUMER_C_QUEUE.start()
    PRODUCER_C_QUEUE = threading.Thread(group=None, target=producer,
                                        name='producer_queue', args=(C_QUEUE, 0.2))
    PRODUCER_C_QUEUE.start()
    PRODUCER_C_QUEUE.join()
    CONSUMER_C_QUEUE.join()

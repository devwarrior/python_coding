'''
simple module implements a circular queue. Full info and description on www.xappsoftware.com
'''
import time
import threading
class CQueue():
    def __init__(self, q_size=32):
        self.queue = list()
        self.head = 0
        self.tail = 0
        self.q_size = q_size

    def enqueue(self, data):
        if self.size() == self.q_size-1:
            print("Queue Full!")
            return "Queue Full!"
        self.queue.append(data)
        self.tail = (self.tail + 1) % self.q_size
        return True

    def dequeue(self):
        if self.size() == 0:
            return "Queue Empty!"
        data = self.queue[self.head]
        self.head = (self.head + 1) % self.q_size
        return data

    def size(self):
        if self.tail >= self.head:
            return self.tail-self.head
        return self.q_size - (self.head-self.tail)

    def print_queue(self):
        print(self.queue)


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

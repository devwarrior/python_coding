'''
This simple module implements a producer-consumer using a FIFO and a LIFO Queue
'''

import Queue
import threading
import time

def producer(the_queue, timing):
    '''
    @brief produce and insert new data into the_queue
    @param the_queue the queue used to store data
    @param timing the interval of time between two insert
    '''
    for counter in range(20):
        the_queue.put(counter)
        time.sleep(timing)

def consumer(the_queue, timing):
    '''
    @brief consume dataof the queue.
    @param the_queue the queue where t retrieve data.
    @param timing the interval of time between two retrieve.
    '''
    for _ in range(20):
        time.sleep(timing)
        print('consumer - get() - ' + str(the_queue.get()))
        print('consumer - list() -')
        for elem in list(the_queue.queue):
            print(elem)
        print('-------------------')


if __name__ == '__main__':
    FIFO_QUEUE = Queue.Queue()
    LIFO_QUEUE = Queue.LifoQueue()

    CONSUMER_FIFO = threading.Thread(group=None, target=consumer,
                                     name='consumer_fifo', args=(FIFO_QUEUE, 0.4))
    CONSUMER_FIFO.start()
    PRODUCER_FIFO = threading.Thread(group=None, target=producer,
                                     name='producer_fifo', args=(FIFO_QUEUE, 0.2))
    PRODUCER_FIFO.start()
    PRODUCER_FIFO.join()
    CONSUMER_FIFO.join()

    CONSUMER_LIFO = threading.Thread(group=None, target=consumer,
                                     name='consumer_fifo', args=(LIFO_QUEUE, 0.4))
    CONSUMER_LIFO.start()
    PRODUCER_LIFO = threading.Thread(group=None, target=producer,
                                     name='producer_fifo', args=(LIFO_QUEUE, 0.2))
    PRODUCER_LIFO.start()
    PRODUCER_LIFO.join()
    CONSUMER_LIFO.join()

"""simple module showing priority queue usage. Full info and description on www.xappsoftware.com
"""
import time
import threading
from random import randint
# python 2.x import Queue
import queue

def producer(the_queue, timing):
    """[Produces and inserts new data into the_queue]

    Arguments:
        the_queue {[CQueue]} -- [the queue used to store data]
        timing {[Integer]} -- [the interval of time between the production of two items]
    """
    while True:
        the_queue.put((0, 'high priority insertion'))
        time.sleep(timing)

def consumer(the_queue, timing):
    """[Consumes data from the queue]

    Arguments:
        the_queue {queue item} -- [the queue used to get data.]
        timing {Integer}} -- [the interval of time between two retrieves.]
    """
    while True:
        time.sleep(timing)
        print('consumer - get() - ' + str(the_queue.get()))


if __name__ == '__main__':
    # python2 Queue.Queue() and Queue.LifoQueue()
    PRIO_QUEUE = queue.PriorityQueue()
    print('Populating the priority queue')
    for counter in range(10):
        time.sleep(0.4)
        prio = randint(0, 3)
        strn = "data - "+ str(prio) + " " + str(time.asctime())
        PRIO_QUEUE.put((prio, strn))
        print((prio, strn))

    time.sleep(1)

    CONSUMER_PRIO_QUEUE = threading.Thread(group=None, target=consumer,
                                           name='consumer_queue', args=(PRIO_QUEUE, 1))
    CONSUMER_PRIO_QUEUE.start()
    PRODUCER_PRIO_QUEUE = threading.Thread(group=None, target=producer,
                                           name='producer_queue', args=(PRIO_QUEUE, 1))
    PRODUCER_PRIO_QUEUE.start()
    PRODUCER_PRIO_QUEUE.join()
    CONSUMER_PRIO_QUEUE.join()

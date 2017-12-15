'''
simple module showing priority queue usage. Full info and description on www.xappsoftware.com
'''
import time
from random import randint
# python 2.x import Queue
import queue


if __name__ == '__main__':
    # python2 Queue.Queue() and Queue.LifoQueue()
    PRIO_QUEUE = queue.PriorityQueue()
    print('Populating the priority queue')
    for counter in range(10):
        time.sleep(0.4)
        prio = randint(0, 9)
        strn = "data - "+ str(prio) + " " + str(time.asctime())
        PRIO_QUEUE.put((prio, strn))
        print((prio, strn))

    print('Getting data from the priority queue')
    print('=========================')
    for counter in range(10):
        prio, strn = PRIO_QUEUE.get()
        print((prio, strn))

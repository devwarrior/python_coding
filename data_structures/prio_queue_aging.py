'''
simple module implementing a starvless priority queue with aging.
Full info and description on www.xappsoftware.com
'''
import threading
import time
from pprint import pprint
LOCK = threading.Lock()

def synchro(lock_id):
    """ Decorator to synchronize threads.

    Arguments:
        lock_id {Lock Object} -- The lock object used to synchronize threads

    Returns:
        method -- The wrapped method
    """
    def wrap(method):
        def wrapped_function(*args, **kw):
            with lock_id:
                return method(*args, **kw)
        return wrapped_function
    return wrap


class AgingPriorityQueue(object):
    """ Class implementing a priority queue with aging.
    """
    def __init__(self, qsize=32, max_aging=10):
        """[summary]

        Keyword Arguments:
            qsize {Integer} -- he max size for the queue (default: {32})
            max_aging {Integer} -- The maximum value for the aging (default: {10})
        """
        self.max_aging = max_aging
        self.queue = list()
        self.queue_len = 0
        self.q_size = qsize

    @synchro(LOCK)
    def enqueue(self, data, item_prio=0, aging=10):
        """ Enqueues a new item into the queue

        Decorators:
            synchro Synchronizes the access to the queue

        Arguments:
            data {data} -- the item to be added to the queue

        Keyword Arguments:
            item_prio {Integer} -- The priority of the item (default: {0})
            aging {Integer} -- The initial aging of the item (default: {10})

        Returns:
             Boolean -- False if the queue is full, True if the item has been inserted.
        """
        res = False
        if len(self.queue) == self.q_size:
            print("Queue Full!")
        else:
            self.queue.append((data, item_prio, aging))
            self.queue = sorted(self.queue, key=lambda element: (element[1], element[2]))
            self.queue_len = self.queue_len + 1
            self.__update_aging()
            res = True
        return res

    def __update_aging(self):
        """ Updates the aging of the items in the list
        """
        for i in range(self.queue_len):
            elem = list(self.queue[i])
            elem[2] = (elem[2] - 1)%self.max_aging
            if elem[2] == 0:
                elem[1] -= 1
            item = tuple(elem)
            self.queue[i] = item
        return

    @synchro(LOCK)
    def dequeue(self):
        """ Extracts an item from the queue.

        Decorators:
            synchro Synchronizes the access to the queue

        Returns:
            [type] -- a tuple representing an item or False.
        """
        if self.queue_len == 0:
            print("Queue is Empty!")
            return False
        else:
            the_tuple = self.queue[0]
            del self.queue[0]
            self.queue_len -= 1
            self.__update_aging()
            return the_tuple[0]

    def print_queue(self):
        """ Prints out the queue content
        """
        print("====")
        pprint(self.queue)
        print("----")


if __name__ == '__main__':
    AG_Q = AgingPriorityQueue()
    AG_Q.enqueue("1111111111111111", 1)
    AG_Q.print_queue()
    time.sleep(0.5)
    AG_Q.enqueue("7777777777777777", 2)
    AG_Q.print_queue()
    time.sleep(0.5)

    for idx in range(32):
        AG_Q.enqueue("n"+str(idx), 0)
        AG_Q.print_queue()
        time.sleep(0.5)

    for idx in range(32):
        AG_Q.print_queue()
        print(AG_Q.dequeue())
        time.sleep(0.5)

""" Simple module implementing a starveless priority queue with round robin.
Full info and description on www.xappsoftware.com
"""
import threading
from operator import itemgetter

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


class PriorityQueueRR(object):
    """ Class implementing a priority queue with round robin.
    """
    def __init__(self, rr_list=[0, 0, 1], qsize=32):
        """ Initializes the Priority Queue with Round Robin

        Arguments:
            rr_list {List} -- The list of priorities for round robin

        Keyword Arguments:
            qsize {Integer} -- The max size for the queue (default: {32})
        """

        self.rr_list = rr_list
        self.rr_len = len(rr_list)
        self.rr_index = 0
        self.queue = []
        self.queue_len = 0
        self.q_size = qsize

    @synchro(LOCK)
    def enqueue(self, data, item_prio=0):
        """ Enqueues a new item into the queue

        Decorators:
            synchro Synchronizes the access to the queue

        Arguments:
            data {data} -- the item to be added to the queue

        Keyword Arguments:
            item_prio {Integer} -- The priority of the item (default: {0})

        Returns:
            Boolean -- False if the queue is full, True if the item has been inserted.
        """
        res = False
        if len(self.queue) == self.q_size:
            print("Queue Full!")
        else:
            self.queue.append((data, item_prio))
            self.queue = sorted(self.queue, key=itemgetter(1))
            self.queue_len = self.queue_len + 1
            res = True
        return res

    @synchro(LOCK)
    def dequeue(self):
        """Retrieves an item from the queue

        Decorators:
            synchro Synchronizes the access to the queue

        Returns:
            type -- The item retrieved from the list, or False if the queue is empty.
        """
        if self.queue_len == 0:
            print("Queue is Empty!")
            return False
        else:
            pos, the_tuple = self.__get_next_item()
            del self.queue[pos]
            self.rr_index = (self.rr_index + 1) % self.rr_len
            self.queue_len = self.queue_len - 1
            return the_tuple[0]

    def __get_next_item(self):
        """Finds the next item to be dequeued

        Returns:
            tuple -- A tuple containing the item and the position of the item inside the queue
        """
        for pos, the_tuple, in enumerate(self.queue):
            if the_tuple[1] == self.rr_list[self.rr_index]:
                return pos, the_tuple
        return 0, self.queue[0]

    @synchro(LOCK)
    def print_queue(self):
        """ Prints on the standard output the content of the queue

        Decorators:
            synchro synchronizes threads
        """
        if self.queue_len == 0:
            print("Queue is empty")
        else:
            print(self.queue)

if __name__ == '__main__':
    RR_Q = PriorityQueueRR()
    RR_Q.print_queue()
    RR_Q.enqueue("gigi", 0)
    RR_Q.enqueue("gigi1", 0)
    RR_Q.enqueue("gigi2", 1)
    RR_Q.enqueue("gigi3", 0)

    RR_Q.print_queue()
    print(RR_Q.dequeue())
    RR_Q.print_queue()
    print(RR_Q.dequeue())
    RR_Q.print_queue()
    print(RR_Q.dequeue())
    RR_Q.print_queue()
    print(RR_Q.dequeue())

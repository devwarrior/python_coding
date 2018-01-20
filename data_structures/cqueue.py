"""[simple module that implements a circular queue.
    Full info and description on www.xappsoftware.com]
"""

import time
import threading
LOCK = threading.Lock()


def synchro(lock_id):
    """[Decorator to synchronize threads.]

    Arguments:
        lock_id {[Lock Object]} -- [The lock object used to synchronize threads]

    Returns:
        [method] -- [The wrapped method]
    """
    def wrap(method):
        def wrapped_function(*args, **kw):
            with lock_id:
                return method(*args, **kw)
        return wrapped_function
    return wrap


class CQueue():
    """[implements a circular queue]
    """

    def __init__(self, q_size=32):
        """[Initializes the queue structure]

        Keyword Arguments:
            q_size {[Integer]} -- [the maximum size of the queue] (default: {32})
        """
        self.queue = [None] * q_size
        self.head = 0
        self.tail = 0
        self.q_size = q_size

    @synchro(LOCK)
    def enqueue(self, data):
        """[Insert an element into the queue.]

        Decorators:
            synchro synchronizes threads

        Arguments:
            data {[data]} -- [the item to be appended to the list]

        Returns:
            [Boolean] -- [True if there is enough space to append the element, False otherwise.]
        """
        res = False
        if self.__size() == self.q_size - 1:
            print("Queue Full!")
        else:
            self.queue[self.tail] = data
            self.tail = (self.tail + 1) % self.q_size
            res = True
        return res

    @synchro(LOCK)
    def dequeue(self):
        """[Retrieve an element from the queue]

        Decorators:
            synchro synchronizes threads

        Returns:
            [type] -- [The item retrieved from the list, or False if the queue is empty.]
        """
        data = False
        if self.__size() == 0:
            print("Queue Empty!")
        else:
            data = self.queue[self.head]
            self.head = (self.head + 1) % self.q_size
        return data

    def __size(self):
        """[Computes the number of valid elements in the queue]

        Returns:
            [Integer] -- [the number of valid elements in the queue]
        """
        if self.tail >= self.head:
            return self.tail - self.head
        else:
            return self.q_size - (self.head - self.tail)

    @synchro(LOCK)
    def print_queue(self):
        """[Prints on the standard output the content of the queue]

        Decorators:
            synchro synchronizes threads
        """
        to_be_printed = list()
        for i in range(self.head, self.__size()):
            to_be_printed.append(self.queue[i % self.q_size])
        print(to_be_printed)


def producer(the_queue, timing):
    """[Produces and inserts new data into the_queue]

    Arguments:
        the_queue {[CQueue]} -- [the queue used to store data]
        timing {[Integer]} -- [the interval of time between the production of two items]
    """
    for counter in range(50):
        the_queue.enqueue(str(counter))
        time.sleep(timing)


def consumer(the_queue, timing):
    """[Consumes data from the queue]

    Arguments:
        the_queue {[type]} -- [the queue used to get data.]
        timing {[type]} -- [the interval of time between two retrieves.]
    """
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

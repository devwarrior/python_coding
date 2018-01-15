'''
simple module implementing a starveless priority queue with round robin.
Full info and description on www.xappsoftware.com
'''
import threading
from operator import itemgetter

LOCK = threading.Lock()

def synchro(lock_id):
    '''
    @brief implements a decorator to synchronize threads.
    '''
    def wrap(method):
        def wrapped_function(*args, **kw):
            with lock_id:
                return method(*args, **kw)
        return wrapped_function
    return wrap


class PriorityQueueRR(object):
    '''
    @brief Class implementing a priority queue with round robin.
    '''
    def __init__(self, rr_list=[0, 0, 1], qsize=32):
        self.rr_list = [0, 0, 1]
        self.rr_len = len(rr_list)
        self.rr_index = 0
        self.queue = list()
        self.queue_len = 0
        self.q_size = qsize

    @synchro(LOCK)
    def enqueue(self, data, item_prio=0):
        '''
        @brief put a new item into the queue
        @param data the item to be enqueued
        @param item_prio the priority of the item, defaulted to zero.
        @return Falso if the queue is full, True if the item has been inserted.
        '''
        if len(self.queue) == self.q_size:
            print("Queue Full!")
            return False
        self.queue.append((data, item_prio))
        self.queue = sorted(self.queue, key=itemgetter(1))
        self.queue_len = self.queue_len + 1
        return True

    @synchro(LOCK)
    def dequeue(self):
        '''
        @brief extract an item from the queue
        @return an item 
        '''
        if self.queue_len == 0:
            print("Queue is Empty!")
            return False
        else:
            pos, the_tuple = self.get_next_item()
            del self.queue[pos]
            self.rr_index = (self.rr_index + 1) % self.rr_len
            self.queue_len = self.queue_len - 1
            return the_tuple[0]

    def get_next_item(self):
        '''
        @brief find the next item to be dequeued
        @return a tuple containing the item and the position of the item inside the queue
        '''
        for pos, the_tuple, in enumerate(self.queue):
            if the_tuple[1] == self.rr_list[self.rr_index]:
                return pos, the_tuple
        return 0, self.queue[0]

    def print_queue(self):
        '''
        @brief print out the queue content
        '''
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

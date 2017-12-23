'''
simple module showing priority queue usage. Full info and description on www.xappsoftware.com
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
    def __init__(self, rr_list=[0, 0, 1], qsize=32):
        self.rr_list = [0, 0, 1]
        self.rr_len = len(rr_list)
        self.rr_index = 0
        self.queue = list()
        self.queue_len = 0
        self.q_size = qsize

    @synchro(LOCK)
    def enqueue(self, data, item_prio=0):
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
        @brief print out the queue
        '''
        print(self.queue)

if __name__ == '__main__':
    rr_q = PriorityQueueRR()
    rr_q.enqueue("gigi", 0)
    rr_q.enqueue("gigi1", 0)
    rr_q.enqueue("gigi2", 1)
    rr_q.enqueue("gigi3", 0)

    rr_q.print_queue()
    print(rr_q.dequeue())
    rr_q.print_queue()
    print(rr_q.dequeue())
    rr_q.print_queue()
    print(rr_q.dequeue())
    rr_q.print_queue()
    print(rr_q.dequeue())

''' simple scheduled timer '''
import sched
import time
def do_something(mysched):
    ''' @brief a function that does something '''
    print('do_something')
    SCHEDULER.enter(1, 1, do_something, (mysched,))


if __name__ == '__main__':
    SCHEDULER = sched.scheduler(time.time, time.sleep)
    SCHEDULER.enter(1, 1, do_something, (SCHEDULER,))
    SCHEDULER.run()

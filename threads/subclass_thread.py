''' subclassing threads '''
import threading

class SubThread(threading.Thread):
    ''' SubClass of Thread '''
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print(self.name)

if __name__ == '__main__':
    for i in range(5):
        t = SubThread('thread-'+str(i))
        t.run()

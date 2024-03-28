from threading import Thread
import time

def watch_tv(n):
    print('watch_tv time is start %s' % time.strftime('%Y-%m-%d %X', time.localtime()))
    time.sleep(n)
    print('watch_tv time is over %s' % time.strftime('%Y-%m-%d %X', time.localtime()))
    return 'watch_tv'

def eat_food(n):
    print('eat_food time is start %s' %time.strftime('%Y-%m-%d %X',time.localtime()))
    time.sleep(n)
    print('eat_food time is over %s' % time.strftime('%Y-%m-%d %X', time.localtime()))
    return 'eat_food'

class CustomThread(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}):
        Thread.__init__(self, group, target, name, args, kwargs)
    def run(self):
        if self._target != None:
            self._return = self._target(*self._args, **self._kwargs)
    def join(self, *args):
        Thread.join(self, *args)
        return self._return

if __name__ == "__main__":
    thread_list = []
    thread_1 = CustomThread(target=watch_tv, args=(10,))
    thread_2 = CustomThread(target=eat_food, args=(2,))
    thread_list.append(thread_1)
    thread_list.append(thread_2)

    for t in thread_list:
        t.start()

    for t in thread_list:
        t.join()
        


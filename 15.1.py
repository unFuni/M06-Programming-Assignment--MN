#Mang Nung 15.1
#15.1 Use multiprocessing to create three separate processes. Make each one wait a 
# random number of seconds between zero and one, print the current time, and then exit.

import multiprocessing
from datetime import datetime
import random
import time


def print_time():
    now = datetime.now()
    print("Today's date and time {}".format(now))
    time.sleep(random.random())

if __name__ == '__main__':
    proc1 = multiprocessing.Process(target=print_time())
    proc2 = multiprocessing.Process(target=print_time())
    proc3 = multiprocessing.Process(target=print_time())
    proc1.start()
    proc2.start()
    proc3.start()
    proc1.join()
    proc2.join()
    proc3.join()

    print('Exit')
import threading as th
import time
def lw1():
    while True:
        print("a")
        time.sleep(1)

def lw2():
    while True:
        print("b")
        time.sleep(1)
thread1=th.Thread(target=lw1)
thread2=th.Thread(target=lw2)

thread1.start()
thread2.start()

thread1.join()

thread2.join()

import threading
import time

class CustomThread(threading.Thread):
    def run(self):
        for i in range(1,5):
            time.sleep(2)
            print("custom thread\n")
       

t=CustomThread()
t.start()

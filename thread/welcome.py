import threading
import time


def f():
    print('Thread function\n')
    time.sleep(5)
    return
def f1():
    print('Thread function1\n')
    time.sleep(5)
    return

def main():
    t = threading.Thread(target=f)
    t.start()
    
    t1 = threading.Thread(target=f)
    t1.start()
    
if __name__=="__main__":
    main()

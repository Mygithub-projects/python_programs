import threading
import time

def repeat(n):
    print(threading.current_thread().getName())
    for i in range(1,n):
        print(i)
       # time.sleep(2)

def main():
    print(threading.current_thread().getName())
    print("main function starts")    
    t1 = threading.Thread(target=repeat, args=(10,), daemon=False)
    #dt1.setDaemon(True)
    t1.setName("mythread")
    t1.start()
    print(t1.isDaemon())
    
if __name__=="__main__":
    main()
    

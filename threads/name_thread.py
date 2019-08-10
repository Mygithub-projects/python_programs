import threading

def f(a,b):
    print(threading.current_thread().getName()+"\n")
    if(a>b):
        return a
    else:
        return b

def main():
    print(threading.current_thread().getName()+"\n")
    t1 = threading.Thread(target=f,args=(5,3))
    t2 = threading.Thread(target=f,args=(10,20))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__=="__main__":
    main()
    
          

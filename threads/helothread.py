
import threading
import time
class HelloThread(threading.Thread):

    def __init__(self,name,id):
        threading.Thread.__init__(self)
        self.name=name
        self.id=id
        
    def run(self):
        time.sleep(10)
        print( "Hello {}, I am Thread - {} \n".format(self.name,self.id))


def main():
    hello = HelloThread("John ",1)
    hello.start()

    print("\n")

    hello1 = HelloThread("Joy ",2)
    hello1.start()

    print("waiting for threads to complete ...\n")

    #hello.join()
    #hello1.join()

    print("exit\n")

if __name__=="__main__":
    main()
    

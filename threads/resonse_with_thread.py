import os
import threading 
import time
from queue import Queue

print("this is with thread\n")
queue = Queue()
threads = []

start = time.time()



dirs=["c:\\PythonPrograms\\classes","c:\\PythonPrograms\\exception",
      "c:\\PythonPrograms\\files","c:\\PythonPrograms\\functions",
      "c:\\PythonPrograms\\datastructures","c:\\PythonPrograms\\gui",
      "c:\\PythonPrograms"]

def getfilescount(dir):
    cnt = 0
    for filename in os.listdir(dir):
        if filename.endswith("py"):
            cnt+=1
    queue.put((dir,cnt))

for dir in dirs:
    t = threading.Thread(target=getfilescount,args=(dir,))
    threads.append(t)
    t.start()
 


for t in threads:
    t.join()

while not queue.empty():
    dirname,count = queue.get()
    print("{} has {} files".format(dirname,count))


    
end = time.time()
time_taken = end-start

print("time taken = {}".format(time_taken))

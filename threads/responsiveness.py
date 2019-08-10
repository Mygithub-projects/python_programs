import os
import time

print("this is without thread\n")
start = time.time()


dirs=["c:\\PythonPrograms\\classes","c:\\PythonPrograms\\exception",
      "c:\\PythonPrograms\\files","c:\\PythonPrograms\\functions",
      "c:\\PythonPrograms\\datastructures","c:\\PythonPrograms\\gui",
      "c:\\PythonPrograms"]
for dir in dirs:
    cnt=0
    for filename in os.listdir(dir):
        if filename.endswith("py"):
            cnt+=1
    print("directory {} has {} python files".format(dir,cnt))
end = time.time()
time_taken = end-start

print("time taken = {}".format(time_taken))

'''
print("this is without thread\n")
start = time.time()
cnt=0
subdir=0
alldirs=[]
for dir in os.listdir("c:\\PythonPrograms\\"):
  subdir+=1
  alldirs.append(dir)
print("number of subdirectories are {}".format(subdir))

for i in alldirs:
    print(i)
print("-------------------")

for file in os.walk("c:\\PythonPrograms\\"):
    cnt+=1
    print(file)
     
print(cnt)
end = time.time()
time_taken = end-start

print("time taken = {}".format(time_taken))
'''

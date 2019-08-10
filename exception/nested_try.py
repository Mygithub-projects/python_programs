import sys
try:
     f = open("c:\\PythonPrograms\\forloop2.py")
     try:
         f.write("Hello");
     finally:
         print("clean up\n")
         f.close()
         print("file closed\n")
except PermissionError as io:
     print("handling exception\n")
     print(io)   
finally:
    print("done\n")
    

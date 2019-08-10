try:
    try:
        
        with open("C:\\PythonPrograms\\functions\\dirprog111.py") as f:
            f.read()
    finally:
            print("inner finally")

except FileNotFoundError as fn:
    print("File Not found error \n")
finally:
    print("outer finally\n")
          
'''with open("C:\\PythonPrograms\\car.jpg","rb") as f:
    print(f.read())'''

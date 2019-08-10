try:
    with open("c:\\pythonprograms\\abcd.py") as f: # open a file
        f.read()
    
    multiples_of_ten=[10,20,30]
    print(multiples_of_ten[2])     # 3 is an invalid index

except IndexError as ie_error:
    print("invalid index")

except FileNotFoundError as fn_error:
    print("file does not exist")
finally:
    print('all the operations are over')

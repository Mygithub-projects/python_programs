'''
import sys
a = int(input("enter first number"))
b = int(input("enter second number"))
c = a+b
print(a>b)

print(a is not b)
print(~a)
print("size = ",sys.getsizeof(int))
print(~-2) 
'''
'''
a = 450
b = 2
c = a >> b
print(c)
'''
'''
try:
     raise Exception('spam', 'eggs')
except Exception as inst:
     print(type(inst))     # the exception instance
     print(inst.args)      # arguments stored in .args
     print(inst)           # __str__ allows args to be printed directly)
     x, y = inst.args
     print('x =', x)
     print('y =', y)
'''
'''
fruits_list = ['apple','orange','kiwi']

def changefruits(lst):
    lst[1]="strawberry"

def main():
    print('before function call list of fruits = ',fruits_list)
    changefruits(fruits_list)
    print('after function call list of fruits = ',fruits_list)
    
if __name__=="__main__":
    main()
'''

x = [1,2]

def changelist(a):
    a = [10,20]
    print(" a = ",a)

def main():
    print("before function call x = ",x)
    changelist(x)
    print("after function call x = ",x)
    
if __name__=="__main__":
    main() 


'''
import math 
def factorial(num):
    factorial1 = math.factorial(num)
    print(factorial1)
factorial(4)
'''
'''
def fact(num):
    i=1
    k=1
    for i in range(num):
        k = i*k
    return k
print(fact(5))
    
'''
'''
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

n=int(input("enter the  number\n"))
print(factorial(5))
'''
'''
str1="madam"
lst=list(reversed(str1))
print(''.join(lst))
'''
'''
import os

print(os.listdir("c:\\xyz"))
'''

'''
import os

print(os.listdir("C:\\PythonPrograms\\fibs.py"))

'''
'''
number = -1
Range = int(input("how many layers do you want the tree?"))
for x in range(0,Range):
    number = number + 2
    print(" " * (Range - x), "*" * number)
    '''

k=10
for i in range(1,10):
    print("\n")
    print(k*' ',end="\t")
    k=k-1
    for j in range(1,i):
        print("*",end="")























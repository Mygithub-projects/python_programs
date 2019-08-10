'''
fib = [0,1,1,2,3,5,8,13,21,34,55]
result = list(filter(lambda x: x % 2==0, fib))
print(result)
'''
'''
num_list= [45,23,67,98,34,23,38] 
final_list = list(filter(lambda x: (x>50) , num_list)) 
print(final_list) 
'''
'''
from functools import reduce
num_list= [1000,2,4,5] 
answer = reduce((lambda a,b: a//b) , num_list)
print(answer) 
'''
'''
import random



s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^"

passlen = 8

p =  "".join(random.sample(s,passlen ))

print(p)
'''
'''
def f():
    a=1
    b=2


print(f.__code__.co_nlocals)
'''

actor=['salman','sharukh']
movie=['ekta tiger','ddlj']

li = list(map(lambda x,y:(x,y), actor,movie))
print(li)



'''
str='jothi'
print(str.upper())
'''
'''
a, b = 10, 2.5
print(a//b)
'''

'''
a,b=True,False
print(True if a or b else False)
'''

count=10
def outer():
    count = 0
    for val in range(4):
        count+=1
        print("count=",count)

outer()

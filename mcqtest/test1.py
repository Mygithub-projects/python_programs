'''
for i in range(5):
    print(i)

'''

'''
myList = [lambda x: x ** 2, lambda x: pow(x, 3), lambda x: x **4]
for func in myList:
    print(func(3), end='')


    '''

'''
num = 1
def func():
    global num
    print("first", num)
    num = num + 1
    print(num)

func()
print("last=",num)

'''
'''
myList = [lambda x: x ** 2, lambda x: pow(x, 3), lambda x: x **4]
for func in myList:
    print(func(4), end=' ')

    '''
'''
lst1 = [1, 2, 3]
print(lst1*2)
'''
'''
set1 = {1, 2, 1, 3, 4}
print(set1[3])
'''
'''
lst = [1, 2, 3, 4, 5, 6, 7, 8]
print(lst[:6:2])
'''
'''
try:
    print(5 * 2)
finally:
    print(10)

'''

'''
str1 = "Hello"
print(str1.replace("l", "x"))

'''

'''
try:
    x = 10
    y = 0

    ans = x/y

except ZeroDivisionError as err:
    print(err)

else:
        print(ans)

'''

'''
print(x)
'''
'''
str1 = 'Hello world'
str1[0] = 'h'
print(str1)
'''
'''
def main():
    dict = {}
    dict['id'] = 10
    dict['name'] = 'test'
    dict['age'] = 30
    print(len(dict))

main()
#print(dict['age'])
'''


'''
myList = [lambda x: x ** 2, lambda x: pow(x, 3), lambda x: x **4]
for func in myList:
    print(func(2), end=' ')
'''
'''
num = 1
def func():
    global num
    num = num + 1
    print(num)

func()
print(num)
'''
'''
x = 1
while True:
    if x % 5 ==0:
         break
    print(x)
    x+=1
'''
'''
def func(x = 1, y = 2):
              x = x + y
              y += 1
              print(x, y)
func(y = 2, x = 1)
'''
str1 = "Hello World"
print(str1[1::5])

















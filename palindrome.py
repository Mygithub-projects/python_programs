'''
str1=str(input("enter input string\n"))
rev_str=str1[::-1]
print("reverse =",reverse(str1))
print(str2)
if(str1==rev_str):
    print("string is palindrome",str1)
else:
    print("string is not palindrome",str1)
print(end="")

'''

def factorial(n):
    fact=1
    while n>=1:
        fact = fact * n
        i-=1
    return fact
print(factorial(4))

'''
lst1 =[464,347,674,863,579]#Getting the input
lst2=[]#Creating an empty list
for i in lst1:#for looping every element in lst1
    for j in i:# for looping element in element
        i=int((j) for j  in str(i))#accessing independent elements of list1
        lst2.append(sum(i))#sum opeation of individual elements
print(lst2)
'''
'''
#Input is quantity of each item
#storing item name and amount in another dictionary

name_item=['bag','glass','phone']#items from input
price_item=[2000,5000,12000]#price of items
no_qty=[2,5,3]#quantity assigned to each item

d={}#creating empty dictionary
lst1=(map(lambda name_item,no_qty:name_item*no_qty)price_item,no_qty))#finding qty*price
dictionary=d.lst1 #storing in a new dictionary
'''
'''
#Checking given number is prime or not

n=int(input("Enter the number"))#Getting input from user
try:#forming a try block
    if n<0:#checking for input less than 0
        print("Number cannot be prime")#printing number can't be prime
except:#except block
    ValueError
if n>1:#forming loop for n value greater than1
    for i in range (2,n):#for checking range between 2 and n
        if n%i==0:#checking condition for prime
            print("Not a prime")#printing for not prime number
        else:#else block
            print("Prime")#printing for prime number
'''
'''
#Function to generate fibonecci series
def fib():#Defining a function
    n=int(input("Enter the number"))#input data from user
    a=0 #assigning values
    b=1 #assigning values
    c=[]#creating empty list
    for i in range(2,n+1):#looping through 2 to 5
        if n>=1:#checking for initial input
            c=n #updating in list c
        else:
            c=a+b #addition of first two values
            a=b   #swapping of values
            b=c   #swapping of values
            print(c)#printing the output
fib()
'''
'''
class Account:#Creating Class
    def__init__(self,customer_name,balance=1000)#Creating Constructors
    self.customer_name=customer_name
    self.balance=balance
def deposit(self,amount):#Creating Deposit function
    Max_amount=10,000
    if amount>10000:
        return("Amount exceeds per day limit")
    elif amount%100==0:
        return(self.balance+amount)
def withdraw(self,amount):#Creating Withdraw function
    Min_balance=500
    if balance<500:
        return ("Insufficient Amount in Account")
    elif amount % 100 == 0:
        return (self.balance - amount)
'''
'''
import re

lst1="01-APR-2019"
pattern=(r'^[0-9]{2}-[A-Z]{3)-[0-9]{4}')
result=re.search[pattern,lst1]
print(result)
'''
'''
lst= [464,347,674,863,579]

#create an empty list 
lst1 = []

#loop for getting the string values in list
for j in lst:
    x = (int(i) for i in str(j))

#appending the list with the sum of elements 
    lst1.append(sum(x))

#Display the output
print(lst1)
'''
'''
price_of_items = {bag:2000,glass:5000,phone:12000}
#Create empty list for quantity, price and items 
quantity = []
item = []
price = []
for i in len(price_of_items):
#Get the quantity values as input
    input ("Enter Quantity:", qty)
#Add the quantity of items in the list quantity
quantity.append(qty)
#In the below for loop the price is collected.
for j,k in price_of_items.items():
    item.append(j)
    price.append(k)
# the amount = quantity * price is calculated
    amount = list(map(lambda x,y : x*y (quantity,price)) 
    new_lst = dict(zip(item,amount))
    print(new_lst)
#The sum of all the items are calculated
print("The total amount:", sum(amount))
'''
'''
#created custom exception
try:
 class NegativeError(Exception):
    pass

 def primenumber(n):
    #checks whether the number is 0 or 1
    if (n==0) or (n==1):
        print("neither prime nor composite")
    #Checks whether the number is 2    
    elif n==2:
        print("prime")
     #checks for negative input values   
    elif n<0:
        raise ValueError
    #checks for a prime number 
    else:
        for i in range (2,n+1):
            
            if (n%i==0):
               print ("notprime")#output is not prime
            else:
               print("prime")#output is prime

                
#Exception is handled if the number is negative
except ValueError:
     
    print("Entered number is negative please enter positive number")
               
primenumber(23)
'''
'''
def fibonacci(n,a=0,b=1):
   c=0 #initialise c value to be zero 
   for i in range(0,n+1):  #checks for input values from 0 to 1
        c = a+b  #compute C
        a=b # assign a value to b
        b=c  #assign b value to c
        print(c) # prints the value of c
fibonacci(8)
'''
'''
n = input("Enter the string")
#includes the pattern of 01-APR-2019
pattern = (r'^[0-9]{2}+\-[A-Z]{3}+\-[0-9]{4}')
#checks for the valid format
if (n == pattern):
    print("valid format")
else:
    print("invalid format")
'''
'''
a = input("Enter the string:").split(',')
print(' '.join(sorted(set(a))))
'''
'''
    class bankaccount():
        def __init__(self, customer_name):
            self.balance = balance
            self.customer_name = customer_name
            self.balance = 1000

            
            def deposit(self, amount):
                 #gets the input amount deposited
                deposit_amount = ("Enter the amount deposited:")
                 #Deposit amount should be multiples of 100
                if (deposit_amount % 100) == 0:
                    #Deposit amount should not exceed 10000
                    if deposit_amount > 0 and deposit_amount < 10000:
                        #calculates the amount
                        self.deposit_amount = deposit_amount + self.balance
                        print(("The balance is:"),format(deposit_amount))
                    else:
                         print("The amount should not exceed Rs.10000:")
                else:
                                            print("The amount should be multiples of 100:")
                        #checks for negative values and moves to exception
                        if deposit_amount < 0:
                           raise ValueError

            def withdraw(self, amount):
                #gets the input of the withdrawal amount
                withdraw_amount = ("Enter the amount to be withdrawn:")
                Withdrawal amount should be multiples of 100
                if (withdraw_amount % 100) == 0:
                    if withdraw_amount < self.balance:
                        self.withdraw_amount = self.balance - withdraw_amount
                        print("The balance is:",format(withdraw_amount))
                    else:
                        print("Insufficient balance")
                else:
                        print("The withdrawal amount should be multiples of 100:")
                        #checks for negative values and mo0ves to exception
                        if (withdraw_amount) < 0:
                             raise ValueError

#handles exception
except ValueError:
        print("Enter positive values of amount")

obj = print(bankaccount("Harshini"))
obj.deposit():
obj.withdraw():
'''
'''
class bankaccount():
        def __init__(self, customer_name):
            self.balance = balance
            self.customer_name = customer_name
            self.balance = 1000

            
            def deposit(self, amount):
                 #gets the input amount deposited
                deposit_amount = ("Enter the amount deposited:")
                 #Deposit amount should be multiples of 100
                if (deposit_amount % 100) == 0:
                    #Deposit amount should not exceed 10000
                    if deposit_amount > 0 and deposit_amount < 10000:
                        #calculates the amount
                        self.deposit_amount = deposit_amount + self.balance
                        print(("The balance is:"),format(deposit_amount))
                    else:
                         print("The amount should not exceed Rs.10000:")
                else:
                                            print("The amount should be multiples of 100:")
                        #checks for negative values and moves to exception
                        if deposit_amount < 0:
                           raise ValueError

            def withdraw(self, amount):
                #gets the input of the withdrawal amount
                withdraw_amount = ("Enter the amount to be withdrawn:")
                Withdrawal amount should be multiples of 100
                if (withdraw_amount % 100) == 0:
                    if withdraw_amount < self.balance:
                        self.withdraw_amount = self.balance - withdraw_amount
                        print("The balance is:",format(withdraw_amount))
                    else:
                        print("Insufficient balance")
                else:
                        print("The withdrawal amount should be multiples of 100:")
                        #checks for negative values and mo0ves to exception
                        if (withdraw_amount) < 0:
                             raise ValueError

#handles exception
except ValueError:
        print("Enter positive values of amount")

obj = print(bankaccount("Harshini"))
obj.deposit():
obj.withdraw():
'''
a = input("Enter the string:").split(',')
print(' '.join(sorted(set(a))))



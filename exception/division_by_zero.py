try:
    
    x = int(input("enter dividend"))
    y = int(input("enter divisor"))

except ZeroDivisionError as err:
    print(err)
else:
    
    ans = x / y
    print("quotient = ",ans)

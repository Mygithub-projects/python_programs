try:
    x=20
    print(" value of x = ",x)

except NameError as error:
    print(error)

else:

    try:
        x=int(input("enter any integer\n"))
        assert(x>0),"x value must be > 0"
    except AssertionError as checkx:
        print(checkx)

finally:
    print("execution is over")
    
    
    
    

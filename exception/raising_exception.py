try:
    a = int(input("enter integer\n"))
    if(a>10):
        raise Exception("HighValue for {}. please enter below 10".format(a))
finally:
    print("done")
    
    
    

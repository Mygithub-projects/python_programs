a = 5
def func(b):
    global c
    c = a + b
    return c

    
print(func(4))        # gives 4+5=9
print(c)             # now it's defined (9)‏

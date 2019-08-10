length = 0
breadth = 0

def area(l,b):
    length = l      # creates a local variable length
    breadth = b     # creates a local variable breadth
    return l * b


print("area= {} ".format(area(10,5)))
print("length = {} and breadth = {} ".format(length,breadth))

length = 0
breadth = 0

def area(l,b):
    global length       
    global breadth

    length = l         # refers global length
    breadth = b        # refers global breadth
    return length * breadth

print("length ={} and breadth = {} ".format(length,breadth))

print("area= ",area(10,5))

print("length ={} and breadth = {} ".format(length,breadth))

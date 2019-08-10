odd_or_even = lambda x: " {} is even".format(x) if(x%2==0) else " {} is odd".format(x)

map_obj = map(odd_or_even,[2,4,5,6,7,8,10,11])


# print(list(map_obj)) # list output.

print(set(map_obj))  # set output.

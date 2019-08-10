def square_cube(n):
    square = n*n
    cube = square *n
    return square,cube

#s,c = square_cube(5)
#print("square of 5 = ",s)
#print("cube of 5 = ",c)

ans = square_cube(4)
s = ans[0]    # using index value can be retrieved.
c = ans[1]

print("square of 4 = ",s,"and cube of 4 =",c)





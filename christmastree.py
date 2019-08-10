n = int(input("enter the range of stars\n"))
x = 20
for i in range(1,n+1):
    print(" "*x+"* "*i)
    x=x-1
    print("\n")

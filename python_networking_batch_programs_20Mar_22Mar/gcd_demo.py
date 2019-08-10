x=int(input("enter x\n"))
y=int(input("enter y\n"))


if(x>y):
    small=y
else:
    small=x
for i in range(1,small+1):
    if(x%i==0) and (y%i==0):
        gcd=i

print("gcd of {} and {} = {}".format(x,y,gcd))

n=int(input("enter the number\n"))
l=n//2
f=0
for i in range(2,l+1):
    if(n%i==0):
        f=1
        break
    else:
        continue
if(f==0):
    print("{} is a prime number".format(n))
else:
    print("{} is not a prime number".format(n))


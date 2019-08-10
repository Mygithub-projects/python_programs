n=int(input("enter the number\n"))
lst=[]
f=0
for j in range (2,n+1):
    l=j//2
    for i in range(2,l+1):
        if(j%i==0):
            f=1
            break
        else:
            continue
    if(f==0):
        lst.append(j)
   
print(lst)

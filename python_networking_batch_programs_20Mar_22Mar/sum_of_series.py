sum=0
lst=[]
n=int(input("enter the number\n"))
for i in range(1,n+1):
    sum=sum+(i/(i+1))
    lst.append(sum)
    

print("cumulative sum=",lst)
print("sum=",sum)

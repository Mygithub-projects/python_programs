lst_of_numbers=[]
lst_first=[]
lst_second=[]

n1=int(input("enter the first number\n"))
n2=int(input("enter the second number\n"))

for i in range(2,n1//2+1):
    if(n1%i==0):
        lst_first.append(i)
    else:
        continue

for i in range(2,n2//2+1):
    if(n2%i==0):
        lst_second.append(i)
    else:
        continue

print(lst_first)
print(lst_second)
gcd=0
for i in range(0,len(lst_first)):
    max=lst_first[i]
    for j in range(0,len(lst_second)):
        if(lst_first[i]==lst_second[j]):
           if(gcd<max):
               gcd=max

print(gcd)
           
               

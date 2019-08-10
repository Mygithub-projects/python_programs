l=['a','e','i','o','u']
s=list(input('enter string '))
l1=[i for i in s if i in l]
print('no of vowels present is ',l1,len(l1))
l2=[l1.count(i) for i in l1]
print(dict(zip(l1,l2)))

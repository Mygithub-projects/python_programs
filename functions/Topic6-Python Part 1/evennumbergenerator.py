def EvenGenerator(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1


n=int(input('Enter the value for n\n'))
values = []
for i in EvenGenerator(n):
    values.append(str(i))

print (",".join(values))

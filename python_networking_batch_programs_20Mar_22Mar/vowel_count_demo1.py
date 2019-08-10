string="beautiful"
d={}
vowels=['a','e','i','o','u']
for el in string:
    if(el in vowels):
        print(el,end="")
        d[el]=string.count(el)
print("\n",d) 

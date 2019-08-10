'''
odd_number = []

for i in range(50):
    if(i%2==0):
        odd_number.append(i)


print(odd_number)
'''
'''
odd_number = [x for x in range(50) if x%2 == 0]

print(odd_number)
'''
'''
product_list = [a*b for a in [1,2,3] for b in [10,20,30]]
print(product_list)
'''
'''
num_list = [1,2,3,4,5]

power_dict = {k:k**k for k in num_list}

print(power_dict)
'''
'''
multiples_gen = (i for i in range(30) if i % 3 == 0)

for x in multiples_gen:
  print(x)
'''
str  = "Hi abcd 1233"

number_set = {x for x in str if x.isdigit()}
print(number_set)
              


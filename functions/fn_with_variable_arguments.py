def add(*num):  # single star for non-keyword variable length arguments.
    sum = 0
    for n in num:
        sum += n;
    return sum

print(add())  # 0 argument
print(add(1)) # 1 argument
print(add(1,2))  # 2 arguments
print(add(1,2,3))  # 3 arguments
print(add(1,2,3,4))  # 4 arguments

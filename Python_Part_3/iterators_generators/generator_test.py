'''
def evennumber_generator():
    print("Hello")
    for i in range(5):
        yield i*2

x = evennumber_generator()


'''
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

print(fact(6))

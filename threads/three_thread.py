import threading


def sum_of_even_series(n):
    i=1
    next = 2
    sumeven=0
    while( i <= n):
        sumeven +=next
        next+=2
        i+=1
    print("sum of even numbers = {} \n".format(sumeven))

def checknumber(n):
    if (n%2==0):
        print("{} is even number\n".format(n))
    else:
       print("{} is odd number\n".format(n))

def main():
    t1 = threading.Thread(target=sum_of_even_series,args=(5,))
    t2 = threading.Thread(target=checknumber,args=(7,))

    t1.
    t1.start()
    t2.start()

   

if __name__=="__main__":
    main()
    
    


class HundredMultiples():
    def __init__(self,start=1,max=1000,value=0):
        self.max = max
        self.start = start
        self.value=0
        
    def __iter__(self):
        return self

    def __next__(self):
        self.value = self.start*100
        if self.value > 1000:
            raise StopIteration
        else:
            self.start +=1
        return self.value
       


def main():
    obj = HundredMultiples()
    #for i in obj:
    #   print(i)

    iterator = iter(obj)
    
    while True:
        try:
            item = iterator.__next__()
            print(item,end=' ')
        except StopIteration as s:
            break
    
        

if __name__=="__main__":
    main()



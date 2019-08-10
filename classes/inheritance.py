from abc import abstractmethod
class Shape:
    @abstractmethod
    def area(self,a,b):
        pass
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def print(self):
        print("measurement = {} and {}".format(self.a,self.b),"and area = {}".format(self.area(self.a,self.b)))
   
class Rectangle(Shape):
    def area(self,a,b):
        return self.a * self.b

class Triangle(Shape):
    def area(self,a,b):
        return 0.5 * self.a * self.b



def main():
    r = Rectangle(20,8)
    r.print()

    t = Triangle(10,5)
    t.print()

   

if __name__=="__main__":
    main()


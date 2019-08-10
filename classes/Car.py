'''
def f1(self):
    print("method outside class")

    
class Car:
    def __init__(self):
        self.__updateSoftware()

    def __updateSoftware(self):
        print("updating software...")

    def drive(self):
        print("driving")

    f = f1


    
redcar = Car()
redcar._Car__updateSoftware()
redcar.price = 2000
print(redcar.price)
redcar.f()

print(redcar.price)
'''

class Car:
    
    def __init__(self):
        self.__startEngine()

    def __startEngine(self):
        print("starting engine")


c = Car()
print("dict = ",Car.__dict__)
print("base  = ",Car.__bases__)
print("module = ",Car.__module__)
print("Name = ",Car.__name__)

#c.Car.__startEngine()












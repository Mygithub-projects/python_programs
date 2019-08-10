'''
import vehicle_test
import sys
class Person(object):
  def __init__(self):
    self.name = 'Nelson'
    self.phone = '9834567335'
    
def main():
    obj = Person()
    c = vehicle_test.Car("tn-55-4444","Honda","eid-76543345")

    #dictionary contains the attributes of instance.
    print("attributes of obj are ",obj.__dict__,"\n")

    # Car is imported from vehicle_test module
    print("Module name of car is = ",vehicle_test.Car.__module__,"\n") 

    #name of base class
    print("Base class of Car class is = ",vehicle_test.Car.__bases__,"\n")

    #name of a class
    print("Class to which c belongs to ",c.__class__,"\n")

    print(vehicle_test.__loader__)
          
if __name__=="__main__":
    main()
'''
import vehicle_test
import sys

print(vehicle_test.__loader__)
print(sys.__loader__)
print(vehicle_test.__package__)

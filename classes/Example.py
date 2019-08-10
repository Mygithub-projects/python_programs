'''
class Car():
    company="Honda"
    

    def __init__(self,vid_number,registration_number):
        self._vid_number = vid_number
        self.registration_number = registration_number

    def displayInformation(self):
        return ("The car\'s VIN is {0} and Registration Number is {1}"
                .format(self._vid_number,self.registration_number))
 
    
c1 = Car("HNTN0001","TN-22-5555")
print(c1.displayInformation()," manufactured by ", c1.company)

print("Vehicle Identification Number = ",c1._vid_number)

'''
'''
class Voter:

    def __init__(self,adharid,name):
        self.__adharid = adharid
        self.name = name

v = Voter(23456,"archana")
print("Adhar Id = ",v.__adharid)

'''


class Voter:
    

    def __init__(self,adharid,name):
        self.__adharid = adharid
        self.name = name

    def set_adharid(self,adharid):
        self.__adharid = adharid

    def get_adharid(self):
        return self.__adharid


    
    
v = Voter(23456,"archana")
print("using get method",v.get_adharid())

#using set method
v.set_adharid(54321)
print("using get method",v.get_adharid())

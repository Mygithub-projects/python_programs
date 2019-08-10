class Person:
    def displayPersonDetail(self,adharid,first_name,last_name):
        print(self.adharid, self.first_name,self.last_name)

'''

class Employee(Person):

    def __init__(self):
        self.id=201
        self.desg='Software Engineer'
        self.company_name= 'HCL'
        super().__init__()


    def displayEmployeeDetail(self):
        return self.displayPersonDetail() + self.id,self.desg,self.company_name
    

'''
    
    
            

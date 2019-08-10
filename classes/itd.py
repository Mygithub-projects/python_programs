class Person():

    def __init__(self,adharid,first_name,last_name):
        self.adharid=adharid
        self.first_name=first_name
        self.last_name=last_name
    
    def displayPersonDetail(self):
        return "Adhar id ={} ".format(self.adharid), "Name = {} {} ".format(self.first_name, self.last_name)


class Employee(Person):

    def __init__(self,adharid,first_name,last_name,id,desg,company_name):
        self.id=id
        self.desg=desg
        self.company_name= company_name
        Person.__init__(self,adharid,first_name,last_name)
       


    def displayEmployeeDetail(self):
        return self.displayPersonDetail(),self.id,self.desg,self.company_name
    

        
    
    
            

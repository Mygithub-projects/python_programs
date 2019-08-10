class Employee:
    empCount=0

    def __init__(self,name,salary):
        self.name= name
        self.salary = salary
        Employee.empCount +=1

    def displayCount(self):
        print("total Employee %d:" %Employee.empCount)

    def displayEmployee(self):
        print("Name :", self.name, ", Salary ", self.salary)

   
              

emp1 = Employee('jothi',500000)
emp1.displayEmployee()
emp1.displayCount()
setattr(emp1,salary,600000)
emp1.displayEmployee()

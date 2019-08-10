class Account:

    name_of_bank = "ICICI"
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        self.balance -= amount


    def display(self):
        print("Name = {} and balance = {} ".format(self.name,self.balance))


def main():

  
    print(Account("abcd",2000).name_of_bank)
    
    
    a = Account("jothi",2000)
     
    a.display()
    a.deposit(5000)
    a.display()
    a.withdraw(3000)
    a.display()
    print(a.name_of_bank)
    

if __name__=="__main__":
    main()

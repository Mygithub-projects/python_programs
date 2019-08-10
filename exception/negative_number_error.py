class NegativeNumberError(Exception):
    def __init__(self,arg):
        self.strerror=arg
      

try:
    a = -10;
    if(a<0):
        raise NegativeNumberError("-ve value not allowed")
except NegativeNumberError as ne:
    print(ne.strerror)
    

        

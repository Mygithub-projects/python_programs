from datetime import date 
  
def calculateAge(birthDate): 
    today = date.today()
    print(today.year,today.month,today.day)
    age = today.year - birthDate.year - ((today.month, today.day) < 
         (birthDate.month, birthDate.day)) 
  
    return age 
# Driver code  
print(calculateAge(date(1973, 1, 5)), "years") 

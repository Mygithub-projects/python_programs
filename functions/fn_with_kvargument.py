# **kwargs method
def display_emp(**data):
    for k,v in data.items():
        print("{} \t : {}".format(k,v))

#calling **kwargs function
display_emp(id=1001, name="hillary",age=30)

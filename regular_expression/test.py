import re
xx = "Hello 123 how are you?"
r1 = re.findall(r"^\w",xx)
r2 = re.split(r's',"this is example of split")
print(r2)
print(r1)

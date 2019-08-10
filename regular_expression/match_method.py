'''
import re

x = "Hello, Hi How are you?"
p = re.match(r"Hi",x)
print(p)
'''
'''
import re

x = "Hello Hi How are you?"
p = re.search(r"\w+",x)
print(p)
'''
import re

x = "Hello Hi How are you?\nI am good."
p = re.split(r"\n+",x)
print(p)

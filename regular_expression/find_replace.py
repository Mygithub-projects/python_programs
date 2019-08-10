'''
import re 

with open("C:\\PythonPrograms\\regular_expression\\ganga.txt") as infile:
    lines = infile.readlines()

#replace all Ganga with Yamuna
matchstr = re.compile(r'Ganga', re.IGNORECASE)‏
for line in lines:
  line = matchstr.sub(r'Yamuna', line)‏
  print(line)
'''

import re

with open("C:\\PythonPrograms\\regular_expression\\ganga.txt","r") as f:
   lines  = f.readlines()
   

for line in lines:
    if(re.findall(r"river",line)):
       print(line)
       

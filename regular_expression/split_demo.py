
'''
import re
sentence="This year summer is very hot.  Winter is very cold"
answer = re.split(r"i",sentence,maxsplit=1)
print(answer)
'''
'''
line = "Upgrade the PSI3 program to PSI4.  PSI3 was an excellent program."
matchstr = re.split("PSI3", line)
for i in matchstr:
    print(i)


'''
'''
import re
sentence = "Ganga is the longest river"
res = re.sub("Ganga","Nile",sentence)
print(res)

'''
'''
import re
p=re.compile('function')
res1=p.findall('This function is very helpful')
print(res1)
res2=p.findall('function is very powerful')
print(res2)
'''
'''
import re
x = "Uses of Python Script"
res = re.findall(r"\w",x)

'''
'''
import re
x = " Now we are testing many programs "
p = re.search(r"\w+",x)
print(p)
print(p.start())
print(p.end)
#print("Before match: ", line[0:p.start()])
#sprint("After match:", line[p.end():])
'''
import re

















import re
with open("c:\\PythonPrograms\\regular_expression\\ganga.txt") as f:
    lines = f.readlines()
cnt=0
for line in lines:
    p = re.search(r"Ganga",line)
    cnt+=1


print(cnt)

import json
'''
lst = [10,20,30]
with open("c:\\PythonPrograms\\files\\numfile.txt","w")as f:
    json.dump(lst,f)
    print("list is written into file\n")

print(json.dumps([1,'example','list']))
'''



with open("c:\\PythonPrograms\\files\\numfile.txt","r")as f:
    print(json.load(f))

'''
dict = {"name":"jothi", "batch":"networkTesting"}
with open("c:\\PythonPrograms\\files\\numfile.txt","w")as f:
    json.dump(dict,f)

with open("c:\\PythonPrograms\\files\\numfile.txt","r")as f:
    print(json.load(f))
'''

'''
file = open("c:\\PythonPrograms\\file3.txt","w")
file.write("first line\n")
file.write("second line\n")
file.write("third line\n")
file.write("fourth line\n")
file.close()
'''
f= open("c:\\PythonPrograms\\file6.txt","rb+")
#f.write(b"Hello are you?")
f.seek(7,0)
print(f.read())
print(f.tell())
f.seek(-9,2)
print(f.read())
f.close()
    #print(f.seek(11,0))
    #print(f.write("\n"))
   ## print(f.readline())
   # print(f.tell())





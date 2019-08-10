'''
cast = ["Tom Cruise", "Will Smith", "Dwayne Johnson", "Jackie Chan",
        "Arnold Schwarzenegger"]

def display_actors():
    for actors in cast:
        print(actors,end="")


'''


with open("c:\\PythonPrograms\\files\\tuplecontent.txt","w") as f:
    no_name=(100,'ram',200,'raj',300,'ragu')
    content = str(no_name)
    print(f.write(content))


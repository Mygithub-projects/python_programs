
def actors():
    cast=['ajith','salman']
    print(cast)
actors()

'''
def movieyear():
    movie=["The Holly Grail","The Life of Brain","The Meaning of Life"]
    years=[1975,1979,1983]
    out=list(zip(movie,years))      #list(),zip() function used to merge the data
    print(out)
movieyear()
'''
'''
movies=["The Holy Grail","The Life of Brain","The Meaning ofLife"]
year=[1975,1979,1983]
#Using lambda function to map both the lists
lst3=list(map(lambda x,y:(x,y),movies,year))
print(lst3)
'''
def movies_list():
    lst1=["The Holy Grail","The Life of Brain","The Meaning of Life"]#assigning movies list to lst1
    lst2=[1975,1979,1983]#assigning year's to lst2
    d={}#declare an empty dict
    n=0
    for i in lst1: #for each element in list1
        d[i]=lst2[n] #assign values as year in list
        n=n+1
    print(list(d.items())) #print dict
movies_list()#calling the function


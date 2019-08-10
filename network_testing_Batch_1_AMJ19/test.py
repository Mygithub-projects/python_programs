'''
#DECLARING TWO VALUED LISTS AND ONE EMPTY LIST:
movies = ["The Holy Grail", "The Life of Brain", "The Meaning of Life"]
years = [1975, 1979, 1983]
movies_list = []
#INSERTING MOVIES AND YEARS IN THE LIST USING ZIP IN A TUPLE FORMAT
list1 = list(zip(movies,years))
print("list1 = ",list1)
#USING FOR LOOP TO ARRANGE TUPLE INTO NORMAL LIST
for element in list1:
    if type(element) == tuple:
        for el in element:
#NORMAL LIST IS APPENDED TO ANOTHER LIST CALLED MOVIELIST
            movies_list.append(el)
#FINALLY MOVIE LIST IS DISPLAYED IN OUTPUT
print("GIVEN BELOW MOVIE LIST:")
print(movies_list)
'''
'''
import re
# MOBILE NUMBERS GIVEN AS INPUT:
mobile_1='91-9962512345'
mobile_2='919962512345'

# REGULAR EXPRESSION PATTERN TO FIND ISD CODES OF MOBILE NUMBERS GIVEN:
result1=re.search(r'(\d{2})-\d{10}', mobile_1)
result2=re.search(r'(\d{2})\d{10}', mobile_2)

# PRINTING ISD CODE OF MOBILE NUMBERS
if result1:
    print(result1)
    print('ISD code of mobile number1 is {}'.format(result1.group(1)))
else:
    print('Invalid mobile number')

if result2:
    print('ISD code of mobile number2 is {}'.format(result2.group(1)))
else:
    print('Invalid mobile number')
    '''
'''
movies=["The Holy Grail","The life of Brain","The meaning of life"]
years=[1975,1979,1983]
movies_years=[] #initialising the empty list for movies and years in one list
print("The givenlist of movies:",movies)  #getting the given list of movies
print("The givenlist of years:",years)    #getting the given list of years
for i in range(len(years)):
    movies_years.append(movies[i])#appending the movies to movies_years list
    movies_years.append(years[i]) #appending the years to movies_years list
print("The movies list and years in one list")
print(movies_years)
'''
'''
bk=[(12354,'Computer Programming',5,449),(12355,'Programming for beginners',8,649),(12356,'Computer Basics',3,179)]
tot=list(map(lambda a:(a[1],a[2]*a[3]),bk))
print("The required list is :",list(tot))
'''
'''
import re
isd1='91-9962512345'
isd2='919962512345'
m1=re.search(r'(\d{2})-(\d+)',isd1) #matching the pattern with the help of regular expression
print("The ISD1 number is ",m1.group(1))

m2=re.search(r'(\d{2})-(\d+)',isd2)
print("The ISD2 number is ",m2.group(1))
'''
'''
movies=['The Holy Grail','The Life of Brain','The Meaning of Life']

years= [1975, 1979, 1983]




#Inserting years into movies using 'zip()'

elem_years=-1


for elem_movies in range(1,len(movies)+3,2):


    movies.insert(elem_movies,years[elem_years+1])


    elem_years+=1
print('\nYears inserted to movies list: ',movies)
'''
def bookshop():
    try:
        lst = ((12354, "Computer Programming", 5 , 449 ),(12355,"Programming for beginners",8 ,649),(12356,"Computer Basics",3 ,179 ))
        amount= (list(map(lambda x:x[2]* x[3],lst)))#by using lambda function total is found
        index_value=lst[0][1],lst[1][1],lst[2][1]#using index value title is found
        book_list = list(zip(index_value,amount))#appending both list
        print("The books and amount:{}".format(book_list))

    except Exception as err:
        print(err)


bookshop()




























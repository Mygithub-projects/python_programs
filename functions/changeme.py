def changeme( mylist ):
   "This changes a passed list into this function"
   # call by reference 
   # mylist.append([1,2,3,4]);

   #local variable
   mylist = [5,6,7]
   print ("Values inside the function: ", mylist)
   return 

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print ("Values outside the function: ", mylist)
print ("after function call")
print (mylist)


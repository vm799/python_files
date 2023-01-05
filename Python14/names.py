# Ask the user to enter the names of pupils in class
# If user enters 'stop' this should indicate all the names in class have been entered
# print out the number of names the users entered once loop has finished


from unicodedata import name

count=0
names_of_pupils = (str(input(
    """
    Please type in the names of the students in your class -one at a time please:    """
    )).lower())

print(names_of_pupils)

while names_of_pupils != "stop":
    names_of_pupils = (str(input("Keep going! When all of your class has been typed in type 'stop':  ")).lower())
    #print(names_of_pupils)
    count += 1
    
    if names_of_pupils == "stop":
        print(f"The total number of names you entered is: {count}" )
    
    
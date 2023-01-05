# ask for the user's input as a string
# initialise a list and add all incorrect entries to the list
# until John is entered, then print out all incorrect names

incorrect_names_list = []
incorrect_name = " "

incorrect_name = (input("Enter your name:  ")).lower()

while incorrect_name != "john":
    incorrect_names_list.append(incorrect_name) #add to initialised list
    incorrect_name = (input("Enter your name:  ")).lower() # all lower to make input value case insensitive
   
    
    if incorrect_name == "john":
        print(incorrect_names_list)
  
      
    
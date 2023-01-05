# ask user to type in a sentence
# create a magic trick and ask which letters the user would like to see disappear
# could be vowels or consonents or every a or any random letter
# initialise 2 variables with the user inputs 
# strip the user sentence of the user's chosen letters

user_sentence = (input("""
    Let's do a magic trick.
    Type in a sentence, any sentence you like! :  
    """
    ))

magic_letters_to_remove = (input("""
    Okay dokey.
    Now type in any letter/ or letters you'd like to magically disappear:    
    """
    ))

magic_letters_list = (" ".join(magic_letters_to_remove)).split()
#print(magic_letters_list) sanity check
# need to create individual strings from user input
# split the characters inputted into individual list items

#intitialise string variable
magical_new_sentence = " "

#now it is possible to create a new string from matching characters in the original sentence 
#as long as NOT in the list created
magical_new_sentence = [char for char in user_sentence if char not in magic_letters_list]


print("".join(magical_new_sentence))



#this only works for single characters but not a string of more than 1 char
#magical_new_sentence = user_sentence.replace(magic_letters_to_remove, "")
#print(magical_new_sentence)

#needed some guidance and found some help here https://stackoverflow.com/questions/65662795/return-string-without-vowels-in-python
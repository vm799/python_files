# write a program to give meaning to an abbreviation
# create a dictionary with key is the  meaning and value the  abbreviations
# at least 4 pairs
# add 2 more pairs 

abbreviation_dictionary = {
    "API": "Apllication programming interface",
    "IDE": "Integrated development environment",
    "OOP": "Object-Orientated Programming",
    "SSH": "Secure Shell"
}
'''
("UX": "User Experience")
("SDK": "Software development kit")
'''
abbreviation_dictionary["UX"] = "User Experience"
abbreviation_dictionary["SDK"] = "Secure Development Kit"



user_request = input("""
    Please type in the abbreviation 
    you would like to search for it's full meaning: """).upper()

if user_request in abbreviation_dictionary: #if the abbreviation typed in by user is in the preformatted dictionary
        print(f"""
    Here is the full meaning: {abbreviation_dictionary[user_request]}
    """)
        
elif user_request not  in abbreviation_dictionary: # if the user request is not in the abbreviation
         print("""
    ---- Sorry that abbreviation not found ----
    """)


'''  # created loop for same program
while True:
    user_request = input("""
    Please type in the abbreviation 
    you would like to search for it's full meaning: 
    """).upper()

    if user_request in abbreviation_dictionary:
        print(f"""
    Here is the full meaning: {abbreviation_dictionary[user_request]}
    """)
        
    elif user_request not  in abbreviation_dictionary:
         print("""
    ---- Abbreviation not found ----
    """)  
'''
        
        
#https://www.w3schools.com/python/python_dictionaries_add.asp
# https://blog.hyperiondev.com/index.php/2022/04/26/6-coding-acronyms-you-need-to-know/
#create a simple calculator program
#ask for 2 inputs
#the operation that user would like to perform
#show answer
#every equation written by user should be written to a text file


from encodings import utf_8, utf_8_sig

#defining the functions to use within the main calculator function
def subtract(num1, num2):
    return (f"{num1 - num2}")

def multiply(num1, num2):
    return (f"{num1 * num2}")

def add(num1, num2):
    return (f"{num1 + num2}")

#to account for user entering 0 and resulting in an ZeroDivisionError
def divide(num1, num2):
    return (f"{round((num1 / num2), 2)}")

#initial user menu
print(""""
          
        Please type which option you would like:
        _________________________________________________________________________
        
        1. To create an equation and print to a file 
        
        or
        
        2. To print out all the equations already on the file called equations.txt
        __________________________________________________________________________
        """)

#loop to ensure program keeps running if user inputs incorrectly
while True:
    menu_option = input("""
        Enter your menu option please (1 or 2): """)
    
    if menu_option == "1":
        try:
            input_num_1 = int(input("""
        Please type in a whole number: """))
            input_num_2 = int(input("""
        Please type in another whole number: """))
            
            operation = str(input("""
        Please type in the sign of what you would like to do with the 2 numbers: 
        i.e please type in  * for mulitply
                            / for divide
                            + for addition
                            - for subtraction : """))
        except ValueError:
            print("""
        *** Sorry that wasn't a number, please try again. Menu options again:  """)    
            continue
        
        if operation in ("*","-","/","+"):
            
                if operation == "+":
                    equation = (f"{input_num_1} + {input_num_2} = {add(input_num_1, input_num_2)}")
                    
                elif operation == "*":
                    equation =(f"{input_num_1} * {input_num_2} = {multiply(input_num_1, input_num_2)}")
                    
                elif operation == "/":
                    
                    if input_num_2 == 0:   
                        while True: 
                            input_num_2 = int(input("""
        *** Sorry! We can't divide by 0, please could you type in a number bigger than 0:  """))
                            if input_num_2 !=0:
                                break
                    if input_num_2 != 0:       
                                equation = (f"{input_num_1} / {input_num_2} = {divide(input_num_1, input_num_2)}")
                        
                elif operation == "-":
                    equation = (f"{input_num_1} - {input_num_2} = {subtract(input_num_1, input_num_2)}")
            
                print(f"""
        Thank you, this equation: {equation} has been written to the text file. 
        
        Here is your menu again:  """)
            
                with open("Python29/equations.txt", "a", encoding="utf_8_sig") as user_equation_log:   
                    user_equation_log.writelines(equation + "\n")
                    continue
        else:
            print("""
        *** Uh Oh! That was not a valid operation. Menu options again:""")
            continue
    
    if menu_option == "2":
        while True:       
            file_name = input("""
        Please type in the name of the file you would like to review, in the form (e.g equations):  """)
        
            
            try:
                    with open(f"Python29/{file_name}.txt", "r", encoding="utf_8_sig") as file_request:   
                        file_equations = file_request.read() 
                        print(f""" 
Here are the equations from the file you requested:  

{file_equations}""")
                    
            except FileNotFoundError:
                    print("""
        *** Sorry that's an invalid filename please try again, you may need to check the spelling.""")
                    
            
            else:
                ("""
        ***Sorry could you check spelling and type in the name of file again without the .txt at the end: 
            """)
    
    else:
        print("""
        *** Sorry, that was not a valid option. Please try again out of 1 or 2.""")       

    #https://www.w3schools.com/python/ref_func_round.asp
    #https://stackoverflow.com/questions/54634571/create-new-files-dont-overwrite-existing-files-in-python
    #https://melaniewalsh.github.io/Intro-Cultural-Analytics/02-Python/07-Files-Character-Encoding.html
    #https://realpython.com/python-exceptions/
    #https://www.w3schools.com/python/python_try_except.asp
    #https://www.geeksforgeeks.org/check-multiple-conditions-in-if-statement-python/
    #https://practicaldatascience.co.uk/data-science/how-to-try-except-for-python-exception-handling#:~:text=A%20try%2Fexcept%20block%20wraps,prints%20File%20does%20not%20exist%20.
    #https://www.programiz.com/python-programming/examples/calculator
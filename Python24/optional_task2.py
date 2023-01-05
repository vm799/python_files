#create a program to act as a calculator
#create functions for each of the mathematical functions
#print out menu

def add_num():
    num1 = int(input("""
Please enter your first number:  """))
    num2 = int(input("""
Please enter your second number:  """))
    sum_answer = num1 + num2
    print(f"""
          \033[1;32mYour answer to {num1} + {num2} = {sum_answer}\033[0m
          """) #change colour and bold the statement
    calculator()
    
def subtract_num():
    num1 = int(input("""
Please enter your first number:  """))
    num2 = int(input("""
Please enter your second number:  """))
    subtracted_answer = num1 - num2
    print(f"""
          \033[1;33mYour answer to {num1} - {num2} = {subtracted_answer}\033[0m
          """)
    calculator()

def multiply_num():
    num1 = int(input("""
Please enter your first number:  """))
    num2 = int(input("""
Please enter your second number:  """))
    multiplied_answer = num1 * num2
    print(f"""
          \033[1;34mYour answer to {num1} * {num2} = {multiplied_answer}\033[0m
          """)
    calculator()

def divide_num():
    num1 = int(input("""
Please enter your first number:  """))
    num2 = int(input("""
Please enter your second number: """))
    divided_answer = num1 / num2
    print(f"""
          \033[1;31mYour answer to {num1} ⁒ {num2} = {divided_answer}\033[0m
          """)
    calculator()

def calculator():
    menu_choice = int(input("""
Here's your calculator menu:

Option 1: add
Option 2: subtract
Option 3: mulitply
Option 4: divide

Please choose the number of the option you would like:  """))

    if menu_choice == 1:
        add_num()
    elif menu_choice == 2:
        subtract_num()
    elif menu_choice == 3:
         multiply_num()
    elif menu_choice == 4:
        divide_num()

calculator()
# Create a program to allow access to 2 different calculators
# A homeloan calculator 
# An investment calculator

# enable the user to access the correct calculator of their choice 
# bond or investment
# make sure that the method of entry makes no difference- case insensitive

#    IF INVESTMENT: 
# 1. Ask for amount of money to deposit
# 2. Ask for the interest rate in terms of a percentage - only enter the number
# 3. Ask for the no. of years the user would like to invest 
# 4. Ask the user to choice between simple or compound
# 5. Use all the above to plug into the formula to work out the return on investment
# for given time and at interest rate


import math
import re

# reminder how to print on multiple lines
# https://pythonprogramming.net/multi-line-printing-python-3/
# learn how to accept an input that is case insensitive
#  https://stackoverflow.com/questions/50192965/how-to-make-user-input-not-case-sensitive
# learn how to check inputs are correct strings before proceeding o/w asking for valid input again
# https://stackoverflow.com/questions/53531966/in-python-how-do-i-repeat-a-prompt-for-input-if-the-input-does-not-equal-1-4

investment_choice = ""
investment_choice = str(input(
"""
Choose either 'investment' or 'bond' from the menu below to proceed:

investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan
"""
)).lower()
#print(investment_choice)

# learned to use while loop to keep asking if input not either of two given options
while investment_choice not in ["bond", "investment"]:
    print("Sorry that was not one of the options we have available")
    investment_choice = (input("please can you type in 'bond' or 'investment':  ")).lower()

#print(investment_choice)

if investment_choice == "investment":
    amount_to_deposit = float(input("Please type in the amount of money you want to deposit:  "))
    
    interest_rate = input("Please type in the interest rate, by inputting the number without the % sign: (type in 8 for 8%) ")
    #when my son tested it he still put 8%(despite all the instructions!!!) so I learned how to accept this input and extract the integer
    #https://stackoverflow.com/questions/11339210/how-to-get-integer-values-from-a-string-in-python
    interest_rate_number = int(re.search(r'\d+', interest_rate).group())
    #print(interest_rate_number)
    
    number_of_years = float(input("Please type in the number of years you would like to invest for: "))
    interest = (input("What type of interest would you like? Choose 'simple' or 'compound': ")).lower()
    print(
    f"""
    Thank you for this information.
    To confirm you would like to deposit £{amount_to_deposit}
    At the interest rate of {interest_rate_number}%
    For {number_of_years} years
    With {interest} interest.
    Your total amount will now follow:
    """
    )
    
    if interest == "simple":
        roi = amount_to_deposit*(1 + (interest_rate_number/100)*number_of_years)
        print(f"The total amount when {interest} interest is applied is £{roi}")

    if interest =="compound":
        roi = round(amount_to_deposit* math.pow((1 +(interest_rate_number/100)), number_of_years),2)
        print(f"The total amount when {interest} interest is applied is £{roi}")
     


   
if investment_choice == "bond":
    present_house_value = float(input("Please type in the present value of your house:  £"))
    interest_rate = (input("Please type in your interest rate, by inputting the number without the % sign: (type in 8 for 8%) "))
    interest_rate_number = int(re.search(r'\d+', interest_rate).group())
    number_of_months = float(input("Please type in the number of months you plan to repay the bond: "))
    monthly_interest = (interest_rate_number / 12)
    print(
    f"""
    Thank you for this information.
    To confirm your house is valued at £{present_house_value}
    The interest rate of your bond is {interest_rate_number}%
    Your would like to pay this off in {number_of_months} months.
   
    Your total amount to repay each month will now follow:
    """
    )
   
    monthly_repayment = (round((monthly_interest*present_house_value)/((1  - math.pow((1+ monthly_interest), (-1*number_of_months)))),2))
    
                                               
                                               
    print(f"The total amount to repay each month is £{monthly_repayment}")


# learning about math.pow
# https://www.w3schools.com/python/ref_math_pow.asp
# math.pow(x,y) is x to the power of y
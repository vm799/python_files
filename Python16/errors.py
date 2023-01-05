# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

print("Welcome to the error program")#SYNTAX ERROR placed brackets around print statement- string
print ("\n")#SYNTAX ERROR incorrect indentation and missing brackets

ageStr = 0 # variable was not defined
ageStr = 24 # I'm 24 years old. 
#syntax error -incorrect indentation. 
# Also changed str to int
# changed double == to =

age = int(ageStr) #runtime error as cannot cast a string to integer
#print(age) -checking variable 
print(f"I'm {age} years old.") 
#syntax error concantenate with format statement
# removed extra """"
# removed spaces and + signs

#three = 3 
# removed " to make sure 3 is an integer not string"
# logical error for calculation to work for 3 years and 6 months three should equal 3.5

three = 3.5 # in number or years and months time, did not account for 6months
answerYears = age  + three  
#needs to be in 3 years and 6 months after user is 24, added extra 6 months to variable
# better name for variable would be added_years_after_age
#print(answerYears) --checking variable works

print(f"The total number of years in 3 years and 6 months will be: {answerYears}") 
# added "in 3 years and 6 months will be:"
#synatx error missing brackets
#changed into format statement
# removed + sign
# removed ""
# changed answerYears to a variable from string

answerMonths = answerYears * 12
# wrong variable given changed to answerYears
# LOGICAL ERROR as three needs to be answerYears to get correct answer
print(f"In 3 years and 6 months, I'll be {answerMonths} months old") 
# missing brackets syntax error
# remove +
# change to format statement
# remove extra """"
# logical error as print statement did not account for extra 6 months
# either add 6 to print statement but that would hard code it
# three should = 3.5 

#HINT, 330 months is the correct answer
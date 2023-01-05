# ask user to type in their full name
# check that 2 names have been entered
#  give the appropriate message to the various outputs
#     if nothing typed
#     if too many letters typed
#     if too few
#     if name correct

user_name = input("Please enter your full name:  ")
print(len(user_name))

if len(user_name) == 0:
    print("You haven't entered anything. Please enter your full name.")

elif len(user_name) < 4:
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")

elif len(user_name) > 25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")

# not sure how to find a space in a string
# discovered the "in" operator
# http://net-informations.com/python/basics/contains.htm


elif len(user_name) > 4 and len(user_name) < 25 and (" " in user_name):  
    print("Thank you for entering your full name.")

# learned how to use "not in" operator

# https://www.geeksforgeeks.org/how-to-check-if-a-set-contains-an-element-in-python/
elif (" " not in user_name):
    print("Sorry that didn't work. I couldn't detect your first name and surname. ")
  
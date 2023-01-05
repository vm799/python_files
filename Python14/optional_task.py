# ask the user for a number less than or equal to 100
# if they make an error and type in a number above 100 then
# ask them to try again until a number less than or equal to 100 is entered
# once this is  entered check it is even
# if even then multiply this number by 2 abd print
# if odd then multiply by 3 and print

user_num = int(input("Please type in a number that is equal to or less than 100:  "))


while user_num > 100:
    user_num = int(input("Uh oh! Please try again and type in a number that is equal to or less than 100:  "))

if user_num <= 100 and user_num % 2 == 0:
   user_num_even = user_num*2 
   print(f"This number, multiplied by 2 is {user_num_even}, is even.")
   
else:
   user_num_odd = user_num*3
   print(f"This number, multiplied by 3 is  {user_num_odd}, is odd.")
   
    
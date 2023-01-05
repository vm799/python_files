#request 2 inputs from user

#put the data obtained into variables num1 and num2

#swap the data in num1 to num2 and num2 to num1

#print out the values of the variable before and after swap


num1 = input("Please type in a number of your choice: ")
num2 = input("Thank you for that number. Please can you type in another number of your choice: ")

print(num1)
print(num2)

#num1 = num2
# unsure how to swap values without losing the value in one variable
# unless I assign the swapped values to another variable

#num1_swap = num2
#num2_swap = num1

#print(num1_swap)
#print(num2_swap)

# going to research into trying to swap both varibales at the same time
#https://stackoverflow.com/questions/14836228/is-there-a-standardized-method-to-swap-two-variables-in-python

# I'll try again now with this and comment out code lines 20 - 24

num1, num2 = num2, num1

print(num1)
print(num2)

#Hurray it worked!
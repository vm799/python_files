# ask for a number to be entered
# check if this number is odd or even
# print out a statement with the number and if it is even or odd

number = int(input("Please enter a number:  "))
print(number)

# needed help with % syntax 
# https://www.freecodecamp.org/news/the-python-modulo-operator-what-does-the-symbol-mean-in-python-solved/#:~:text=The%20%25%20symbol%20in%20Python%20is,%2C%20*%20%2C%20**%20%2C%20%2F%2F%20.

if(number % 2) == 0 :
    print(f"{number} is even!")
else:
    print(f"{number} is odd!")
    
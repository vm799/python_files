# ask user to input number and make sure it is converted to an integer data value
# store as variable num
# if the number is bigger than 10 output using a for loop output as many times as the value
# if user input is less than or equal to 10 program print "Sorry, too small"

num = int(input("Please type in a number:  "))

if num > 10: 
    for i in range(1, num):
        print(num)
else: 
    print("Sorry, too small.")
    
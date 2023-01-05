# Ask the user to type in a number
# Using the while loop create a repeating structure that prints out
# all even numbers from 1 upto the number inputted by user

count = 1
num = int(input("Please type in a number:  "))
#print(num)

while num >= count:
    if count % 2 == 0:
        print(count)
    count += 1
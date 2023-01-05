# write a program that asks user to enter a number
# when the user enters -1 the program should stop
# then calculate the average of all the numbers entered excl -1

count = 0
total = 0

num = int(input("Please type in a number:  "))


while num != -1:
    total += num
    count += 1
    num = int(input("Please type in a number:  "))
    
    
    if num == -1:
        
        print(f"The average of the numbers you entered is:  {total/count}")
        break
   
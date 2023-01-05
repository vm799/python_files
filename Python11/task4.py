# allow user to type in a number
# find out if this number can be divided by 2 and 5, if it is even and ends in 5 or 0
#  find out if this number can be divided by 2 OR 5, if it is even and ends in 5 or 0
# find out if this number CANNOT be divided by 2 OR 5

num = int(input("Please type in a number:  "))
#print(num)

if (num % 2 == 0) and (num % 5== 0):
    print("This number can be divided by 2 AND by 5!")
elif (num % 2==0) or (num % 5 == 0):
    print("This number can be divided by 2 OR 5")
elif num % 2 or 5 != 0:
    print("This number CANNOT be divided by 2 or 5")
    

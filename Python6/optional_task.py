# request user to enter 3 different measurements for triange lengths
# calculate area of triangle =>
# s = side1 + side2 +side3 / 2
# area = sqrt(s(s-a)*(s-b)*(s-c))

side1 = input("Please type in the length of the first side of your triangle: ")
side2 = input("Please type in the length of the second side of your triangle: ")
side3 = input("Please type in the length of the third side of your triangle: ")

a = int(side1)
b = int(side2)
c = int(side3)

s = (a + b + c)/2
print(s)

import math

print(math.sqrt(s*(s - a)*(s-b)*(s-c)))

#https://www.w3schools.com/python/ref_func_round.asp
print(round(math.sqrt(s*(s - a)*(s-b)*(s-c)), 2))

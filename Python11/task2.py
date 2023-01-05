# Calculate the area of a building foundation
# check what shape the building is : round/rectangular/ square
# ask for the relevant dimensions depending on the shape of building
# calculate area of foundation

from cmath import pi

shape = input("What is the shape of the building?: (round/square/rectangular)  ")

if shape == "round":
    radius = float(input("Please give the radius of the building dimensions(m): "))
    area = round(pi*(radius*radius),2)
elif shape == "rectangular":
    length= float(input("Please give the length of the building dimensions(m): "))
    width= float(input("Please give the width of the building dimensions(m): "))
    area = length * width 

else:
    square_length = float(input("Please give the length of one side of the building dimensions(m): "))
    area = square_length*square_length 

print(f"The area that will be taken up by the foundation is: {area}m2")

"""
if shape == "round":
    area = pi*(radius*radius) 
elif shape == "rectangular":
"""    


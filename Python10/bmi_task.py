# calculate a person's BMI
# ask for the weight in kg and height in m
# formula for BMI : weight kg / height m all multiplied by height
# if BMI 30 or more - obese
# if BMI 25 or more - overweight
# if BMI 18.5 or more - normal
# if BMI less than 18.5  - underweight

# state the actual BMI and the anaylsis

weight = float(input("What is your weight in Kgs please: "))
height = float(input("What is your height in Metres please: "))

#print(weight)
#print(height)

# had to remind myself how to round to 2dp 
# https://www.tutorialspoint.com/How-to-round-down-to-2-decimals-a-float-using-Python
bmi = round((weight) / (height * height), 2)
# bmi = bmi_1/ height

if bmi > 30:
    category = "obese"
elif bmi > 25:
    category = "overweight"
elif bmi > 18.5:
    category = "normal"
else: 
    category = "underweight"

print(f"Your BMI is {bmi} which indicates that you may be {category}.")
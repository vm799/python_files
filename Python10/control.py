# ask for the user's age
# if age is over 18 state You are old enough
# if below 18 state too young or almost there


age = int(input("I need to know how old you are please:  "))

print(f"Thank you, you are {age} years old.")

if age >= 18:
    print("You are old enough.")

elif age > 16 and age < 18: 
    print("Almost there.")

else:
    print("You're just too young!")
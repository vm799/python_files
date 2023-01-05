# check if person is 18 or over to allow them access to party
# ask the person year of birth and from that work out how old they are
# if the person is old enough then let them in!

year_of_birth = input("Hello there, before I let you in, I need to know the year of your birth please:  ")
age = 2022 - int(year_of_birth)
print(f"Thank you, you are {age} years old.")

if age >= 18:
    print("Congrats, you are old enough.")

else:
    print("Sorry buddy, you can't come in!")
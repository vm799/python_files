#ask the usee to input a year and no. of years
#using a loop determine and print out which of those years were or are going to be leap


start_year = int(input("Please type in the year you want to start from:  "))
num_of_years = int(input(f"Please type in how many years you would like to check from {start_year} onwards:  "))


for i in range(start_year, (start_year+num_of_years)):
    if (i) % 4 == 0:
        print("")  #adding space to delineate which year is a leap lear
        print(f"{i} is a leap year!!")
        print("")
    else:
        print(f"Hmm, {i} doesn't seem to be a leap year")

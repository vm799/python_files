# use for loops to generate and print out any times tables
# ask user which times table they would like to see
# use tis number in the loop to generate the printout


times_table = int(input("""
    Welcome to the times table generator. 
    Which times table would you like to see today?
    Please type in a number:  """))

for x in range(1,13):
    print(f" {times_table} * {x} = {x*times_table}")
    print("")
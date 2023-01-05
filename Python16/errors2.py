# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

animal = "lion" #change to string with  "" syntax error
animal_type = "cub"
number_of_teeth = 16

full_spec = (f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth.")
# runtime error
# missing f in format statement 
# missing brackets syntax error
print (full_spec) # missing brackets syntax error

#logical error. changes around variables, in the wrong place
#full stop added at end of sentance
# changed capital letter of Lion
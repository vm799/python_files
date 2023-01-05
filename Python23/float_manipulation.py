# import the math module
# write a program to ask the user to type in 10 numbers that can be decimals
# store these numbers in a list
# find the total of all the numbers and print
# find index of max number and print
# find index of min munber and print
# calc the average of numbers and round to 2 dp and print
# find median of the number and print

import math
import statistics


user_inputs = input("""
                    
Please type in 10 numbers (with a space after each number):  """)
input_list = user_inputs.strip() #store numbers in a list
new_list_no_spaces = (input_list.split(" "))
int_list = [float(x) for x in new_list_no_spaces] #caste the list to floats

total = sum(int_list) 
min_value = min(int_list) 
max_value = max(int_list)

min_index = int_list.index(min_value) #finding the index of the min value in the list of numbers
max_index = int_list.index(max_value)

list_average =  round(sum([float(i) for i in int_list])/len(input_list),2)
#iterating over numbers to caste to float
#adding together all numbers and dividing by the number in list, rounded to 2 dp

median_number_list = statistics.median(int_list) #using the statistics module to access median method

print(f"""
The total of all numbers is: {total} """)
print(f"The index of the maximum value is: {max_index} ")
print(f"The index of the minimum value is: {min_index} ")
print(f"The average of all numbers is: {list_average} ")
print(f"""The median of all numbers is: {median_number_list} 
""")



# https://www.google.com/search?q=how+to+count+number+of+items+in+list+python&oq=how+do+i+count+number+of+items+in+list+&aqs=chrome.1.69i57j0i22i30j0i390l3.217248j0j4&sourceid=chrome&ie=UTF-8
# https://java2blog.com/find-index-of-max-value-in-list-python/
#https://stackoverflow.com/questions/64151040/how-to-add-all-string-type-numbers-in-list-in-python-3
#https://realpython.com/python-sort/
# https://www.geeksforgeeks.org/find-median-of-list-in-python/
#
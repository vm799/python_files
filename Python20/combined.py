# create a new file called numbers1.txt
# this file will contain numbers that will be sorted in ascending order

# create a new file called numbers2.txt
# this file will contain numbers that will be sorted in ascending order

# create a new file called all_numbers.txt
# this file will contain all the numbers from both files sorted in ascending order

from datetime import date


data =  ""
data2 = "" #both data sets initialised as strings

with open("numbers1.txt", "w") as num_data1: 
    for num in range (10,51):
      data =  num_data1.write(str(num) + "\n" ) #add numbers to first file

    
with open("numbers2.txt", "w") as num_data2:
    for num in range (1,20):
      data2 = num_data2.write(str(num) + "\n") # populate numbers to second file


with open("numbers1.txt") as num_data1:
    data = num_data1.read()
with open("numbers2.txt") as num_data2:   
    data2 = num_data2.read() 

data += data2 # amalgamate the data to store in one variable

with open("all_numbers.txt", "w") as all_numbers:
    nums_list = data.split() #create a list 
    nums_list_arranged = sorted(nums_list, key=int) # sort the list
    nums_sorted = (" ".join(nums_list_arranged) ) #return to strings with space between them
    all_numbers.write(nums_sorted) # write newly arranged data to file

    
# struggled with sorting a string of numbers https://www.geeksforgeeks.org/python-sort-numeric-strings-in-a-list/
# https://www.w3schools.com/python/ref_file_readlines.asp#:~:text=The%20readlines()%20method%20returns,no%20more%20lines%20are%20returned.
# https://www.geeksforgeeks.org/python-program-to-merge-two-files-into-a-third-file/
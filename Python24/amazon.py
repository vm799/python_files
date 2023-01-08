#read the content of text file
#read each line
#recognise keywords min, max, avg and execute code for each keyword to find min/max/avg of the numbers in string

from statistics import mean

def find_minimum_number(int_list):
    min_value = min(int_list) #using the min() function to return lowest value
    
    with open("output.txt", "w", encoding="utf-8-sig") as output_file: #writing to file
        output_file.write(f"The min of {int_list} is {min_value}\n")
        
def find_maximum_number(int_list):
    max_value = max(int_list)     
    
    with open("output.txt", "a", encoding="utf-8-sig") as output_file:
        output_file.write(f"The max of {int_list} is {max_value}\n")
        
def find_average_number(int_list):
    avg_value = round(mean(int_list),2)  #round the result to 2dp
    
    with open("output.txt", "a", encoding="utf-8-sig") as output_file:
        output_file.write(f"The avg of {int_list} is {avg_value}\n")

with open("input.txt", "r", encoding="utf-8-sig") as input_file:
    single_line_input = input_file.readlines()  # read file and return list of the lines in file
    
    for line in single_line_input: # iterate through the list
        single_line_nums = (line[4:]) # removing the letters and symbols i.e "min:" to then work with the numbers and maths functions
        print(single_line_nums)

        single_line_numlist = single_line_nums.split(",")
        print(single_line_numlist)

        int_list = ([(int(x)) for x in single_line_numlist]) # return a list of the individual numbers and caste them to integers
        print(int_list)
        
        if "max" in line: #if the keyword max,min,avg found in the original line output of readlines() then the relevant function can be actioned
            max_line = find_maximum_number(int_list)

        if "min" in line:
            min_line = find_minimum_number(int_list)
            
        if "avg" in line:
            avg_line = find_average_number(int_list)


#research
#https://bobbyhadz.com/blog/python-write-string-to-file-on-new-line-every-time        
#https://www.quora.com/How-do-I-write-the-output-of-a-function-to-a-text-file-in-python
#https://cmdlinetips.com/2012/09/three-ways-to-write-text-to-a-file-in-python/#:~:text=To%20create%20and%20write%20to,a%20new%20file%20to%20write.&text=If%20you%20want%20to%20append,if%20it%20does%20not%20exist.
#https://blog.finxter.com/how-to-convert-a-string-list-to-an-integer-list-in-python/
#https://www.simplilearn.com/tutorials/python-tutorial/find-average-of-list-in-python#:~:text=To%20find%20the%20average%20of%20the%20numbers%20in%20a%20list,function%20from%20the%20statistics%20module.
#https://www.codingem.com/python-how-to-find-the-largest-number-in-a-list/#:~:text=In%20Python%2C%20there%20is%20a,greatest%20number%20in%20that%20list.   
#https://www.programiz.com/python-programming/methods/built-in/sum        
#https://bobbyhadz.com/blog/python-remove-first-two-characters-from-string 
#https://www.edureka.co/blog/python-list-remove/#:~:text=The%20remove()%20method%20removes,or%20slice%20from%20a%20list.
#https://www.w3schools.com/python/ref_string_split.asp
#https://www.pythontutorial.net/python-basics/python-read-text-file/ 
#add to the amazon.py task with a percentile function
from statistics import mean

def find_minimum_number(int_list):
    min_value = min(int_list)
    with open("output2.txt", "w") as output_file:
        output_file.write(f"The min of {int_list} is {min_value}\n")
        
        
def find_maximum_number(int_list):
    max_value = max(int_list)
    with open("output2.txt", "a") as output_file:
        output_file.write(f"The max of {int_list} is {max_value}\n")
        
def find_average_number(int_list):
    avg_value = mean(int_list)
    with open("output2.txt", "a") as output_file:
        output_file.write(f"The avg of {int_list} is {avg_value}\n")

def find_percentile(x, int_list): 
    ordered_list = sorted(int_list) #sort numbers into ascending values
    percentile_value = round(x/100*(len(int_list))) #find the index that equates to percentile value of x
    percentile = ordered_list[percentile_value] #find the value that corresponds to the index in an ordered_list
    with open("output2.txt", "a") as output_file:
        output_file.write(f"The {x}th percentile of {ordered_list} is {percentile}\n")

with open("input2.txt", "r") as input_file:
    single_line_input = input_file.readlines()  
   
    for line in single_line_input:
        single_line_nums = (line[4:])
        ordered_list = ([int(x) for x in single_line_nums.split(",")])
        
        if "max" in line:
           max_line = find_maximum_number(ordered_list)
        if "min" in line:
            min_line = find_minimum_number(ordered_list)
        if "avg" in line:
            avg_line = find_average_number(ordered_list)
        if "p70" in line:
            p70 =  find_percentile(70, ordered_list)
        if "p90" in line:
            p90 = find_percentile(90, ordered_list)
               

            
        
        
            
        
        
                      
      
            
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
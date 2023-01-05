# Create a string
# Locate every alternative character and make it uppercase
# Locate every other alternative character and make it lowercase
# need to use upper()  and lower() while looping through the string and creating new one

# intitialise starting point

print("""
      CHALLENGE 1:     
"""
)

original_string= "I am A badass Ninja warrior princess"  

#for comparison start with printing the original string


print(f"This is the original string:  {original_string}")

# intialise a new string for the resulting changed string
new_string =""


for i in range (len(original_string)):  # the loop runs the same no. of times as letters in string
  if i % 2 != 0:
    new_string = new_string + original_string[i].lower()
  else:
    new_string = new_string + original_string[i].upper()

print(f"This is the new fun string with alternating letters in each word:  {new_string}")

 
     


#Part 2: 
#start with same string
# Alternate with each word going from lower to upper case

print("""
      CHALLENGE 2:     
"""
)

print(f"This is the original string we are working with:  {original_string}")

original_string= "I am A badass Ninja warrior princess"  

new_string_list =[ ]

# convert the sentence into a list of individual strings
original_string_list = original_string.split()

#print(original_string_list)  #checking it worked! we have a list

for i in range (len(original_string_list)): #each time the loop goes through the list each item is changed according to algorithm
    if i % 2 != 0:
      new_string_list = new_string_list + [original_string_list[i].upper()]
      #print(new_string_list)
    else:
      new_string_list = new_string_list + [original_string_list[i].lower()]
      #print(new_string_list) neew to revert back to a string by combining items between spaces
new_string = (" ".join(new_string_list))

print(f"This is the resultant string with alternating upper and lower case words:  {new_string}")







""" TRIED A DIFFERENT SOLUTION, not happy with result but left here for learning purposes
for i in range (0, len(original_string_list), 2): # the loop runs the same no. of times as letters in string, skipping alt list items
    
    new_string_reversed_words = new_string_reversed_words + (original_string_list[i].upper()).split()
    print(new_string_reversed_words)
    
for i in range (1, len(original_string_list), 2): # the loop runs the same no. of times as letters in string, skipping alt list items
    
    new_string_reversed_words = new_string_reversed_words + (original_string_list[i].lower()).split()
    print(new_string_reversed_words)
   
    #new_string_reversed_words = new_string_reversed_words + original_string_list[i].upper()

#print(f"This is the new fun string with alternating words in the sentence:  ")
"""

# got a bit stuck, advice found here https://www.geeksforgeeks.org/python-alternate-cases-in-string/#:~:text=Method%20%231%20%3A%20Using%20upper(),()%20and%20lower()%20respectively.
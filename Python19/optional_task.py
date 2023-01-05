# create another text file with some random text (randomtextgenerator.com)
# Part 1:  write a program that will count the no. of characters, words and lines in the file
# Part 2:  write a program that will count the no.of vowels (a,e,i,o,u)

characters = 0
words = 0
lines = 0
vowel = 0
vowel_list = ["a","e","i","o","u"]

with open("input.txt", "r+") as random_word_file:
    for line in random_word_file:
        words += (len((line.split("."))[0].split(" "))) # break each line of text before full stop and select first index
        characters += (len((line.replace(" ", "")).strip('\n'))) # remove spaces and line break and count letters in the string
        lines += 1 # counter for each time looped over each line
        vowel += len([char for char in line if char in vowel_list]) # create a new list with  each character in each line of text       
# that matches a character in the vowel list and calculating the length of this newly formed list

print(f"""
      The number of characters are {characters}, there are {vowel} vowels, {words} words and {lines} lines.
      """)

#https://blog.finxter.com/python-count-characters-except-empty-spaces/ 


         

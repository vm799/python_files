# aim is to create a program to count character frequency in a string
# record the no. of times a letter occurs in a dictionary
# print out result

print("""
      SOLUTION ONE:  
      """)
from collections import Counter

counting_string = "I'm an astronaut"

dictionary_character_frequency = Counter(counting_string) # using the Counter to store object as key and count it's values
print(dict(dictionary_character_frequency)) # used dict to print out the dictionary

#https://docs.python.org/3/library/collections.html#module-collections
#https://www.geeksforgeeks.org/python-frequency-of-each-character-in-string/
#https://stackoverflow.com/questions/69336164/is-there-a-way-of-only-printing-the-dictionary-in-a-counter-output

print("""
      SOLUTION TWO:  
      """)
second_counting_string = "I'm an astronaut"
letter_frequency = {}

for letter in second_counting_string:  #looping over the string checking for letter frequency in string
    if letter in letter_frequency:
        letter_frequency[letter] += 1 
    else:
        letter_frequency[letter] = 1

print(letter_frequency)

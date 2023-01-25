# ask user to input a sentence and store in str_manip
# find the last letter in this sentence and replace every time it occurs with @
# print the last 3 characters in the sentence backwards
# make a 5 letter word to be constructed from first 3 of the sentence and last 2 of the sentence


str_manip = str(input("Please could you enter a sentence? : "))
print(str_manip)

#print(str_manip.len()) didnt work
#https://www.w3schools.com/python/gloss_python_string_length.asp#:~:text=To%20get%20the%20length%20of,use%20the%20len()%20function.
#as a reminder of use of function

print(len(str_manip))
#https://flexiple.com/python/python-replace-character-in-string/
# needed help to remember what the replace method takes as parameters
print(str_manip.replace(str_manip[-1],"@"))


print(str_manip[len(str_manip): -4 :-1])

print(str_manip[0:3] + str_manip[-2: ])
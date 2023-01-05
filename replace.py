# with string given remove the ! and replace with space
# print this new string
# change this string to capital letters
# print the same string backwards

sentence = '"The!quick!brown!fox!jumps!over!the!lazy!dog!."' #realised that the answer required " " either end of sentence 
#so worked out a way of using a string with speech marks

print(sentence.replace("!", " ")) # but this has a space at the end too
# and the answer didn't have a space between dog and !
# researched how to apply replace function to all "!"" expect last one

#print(sentence.replace("!", " ")).deleteCharAt(-3)
#print(sentence.deleteCharAt(-3))

print(sentence.replace("!", " ",8))
""" Researching led me to learn how to count the number of times I want the function 
 t0 work
 https://www.folkstalk.com/tech/how-to-replace-the-last-character-of-a-string-in-python-with-code-examples/#:~:text=To%20replace%20the%20last%20N,back%20to%20the%20original%20variable.
 """
# works hurrrrayyy!!
# but still leaves the ! at the end
# research how to remove remaining "!"

print(sentence.replace("!", " ",8).replace("!", "")) #maybe try chaining another replace function?

# print(sentence.upper()) #this returned back to original sentence

print(sentence.replace("!", " ",8).upper()) #tried putting 2 functions togther and it worked!!


# wasn't sure if it was the orginal sentence you needed reverse, done both

print(sentence[ : :-1]) # original sentence reversed

print(sentence.replace("!", " ",8).upper()[ : :-1]) # last sentence reversed by
# trying to combine all functions
# it worked!!

print("Task 2 ")
print(" ANSWERS: ")
sentence = '"The!quick!brown!fox!jumps!over!the!lazy!dog!."'
print(sentence.replace("!", " ",8).replace("!", ""))
print(sentence.replace("!", " ",8).replace("!", "").upper())
print(sentence.replace("!", " ",8).replace("!", "").upper()[ : :-1])


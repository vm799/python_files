# create a random joke generator 
# use the random module 
# create a list of jokes and display a random code every time the program runs

import random

jokes = []

#credit: https://www.rd.com/list/short-jokes/ jokes taken from this site.
joke1 =("Did you hear about the mathematician who’s afraid of negative numbers?   Answer: He’ll stop at nothing to avoid them.")
joke2 =("Helvetica and Times New Roman walk into a bar. Answer: Get out of here!” shouts the bartender. We don’t serve your type")
joke3 = ("Hear about the new restaurant called Karma? Answer: There’s no menu: You get what you deserve.")
joke4 =("Why don’t scientists trust atoms?  Answer: Because they make up everything")
joke5 = ("What kind of exercise do lazy people do?  Answer: Diddly-squats.")

jokes = [joke1, joke2, joke3, joke4, joke5] #found this a neater way to add the jokes to a list and manipulate as individual items

joke = random.choice(jokes) #use the random module to pick a random item for the list

#adding some colour and fun to the resulting print output
print( 
      f"""
       \033[1;35m  
    Hey there\033[0m!  
\033[1;35m
I have a joke for you\033[0m:
        
\033[1;32m{joke} \033[0m
        """)

#https://www.studytonight.com/python-howtos/how-to-print-colored-text-in-python
#https://pynative.com/python/random/
#https://note.nkmk.me/en/python-string-concat/
#https://www.geeksforgeeks.org/python-append-string-to-list/
#https://stackoverflow.com/questions/20196159/how-to-append-multiple-values-to-a-list-in-python
#https://www.askpython.com/python/string/append-multiple-strings-in-python
#https://www.askpython.com/python/string/convert-string-to-list-in-python
#https://pynative.com/python/random/
#https://www.geeksforgeeks.org/python-script-to-create-random-jokes-using-pyjokes/
#https://pythonprinciples.com/blog/lists-of-strings-in-python/#:~:text=Create%20list%20of%20strings,must%20be%20surrounded%20by%20quotes.
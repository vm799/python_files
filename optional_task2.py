# ask for the name of the user's fav restaurant
# store in fav_rest
# find the users fav no
# store in int_fav
# print out both

fav_rest = input("Hey there, please tell me the name of your favourite restaurant:  ")
int_fav = int(input("Awesome! now tell me your favourite number:  "))


print(fav_rest)
print(int_fav)

print(int(fav_rest))
# invalid literal for int() with base 10: 'nandos'
# this indicates that the data value in the variable fav_rest 
# is not a data type that can be converted in numbers/ integers
# letters cannot be converted to integers perhaps?

#print(int(str(fav_rest)))

#https://www.google.com/search?q=can+you+convert+a+string+of+letters+to+an+integer+in+python&oq=can+you+convert+a+string+of+letters+to+an+integer+in+python&aqs=chrome..69i57j0i546l4.14443j0j4&sourceid=chrome&ie=UTF-8
# reserached if letters could be coded to integers and only if "converted to unicode code point for a given character"

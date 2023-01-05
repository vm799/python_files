def print_values_of(keys, dictionary):
    for key in keys:
# print(dictionary[k]) error- "k" should be key
        print(dictionary[key])
        
#simpson_catch_phrases = {"lisa": "BAAAAAART!", "bart": "Eat My Shorts!", "marge": "Mmm~mmmmm", "homer": 'd'oh', "maggie": " (Pacifier Suck)"} 
#  d'oh error need to deliniate the apostrophe used in the word d'oh to be "d'oh" and initialised as a string
#  "maggie": " (Pacifier Suck) inappropriate brackets, removed brackets

simpson_catch_phrases = {
    "lisa": "BAAAAAART!", 
    "bart": "Eat My Shorts!", 
    "marge": "Mmm~mmmmm", 
    "homer": "d'oh!", 
    "maggie": "Pacifier Suck"
    }

#print_values_of(simpson_catch_phrases, 'lisa', 'bart', 'homer')
#  the "keys" and "dictionary" values are in the wrong order
#  in the example the dictionary is first and then keys
#  but 'def print_values_of(keys, dictionary)' passes keys first then dictionary as arguments

#print_values_of('lisa', 'bart', 'homer', simpson_catch_phrases)
#  this shows  as 4 arguments, needs to be 2
#  lisa, bart and homer are all keys and need to be contained by square brackets ["lisa", "bart", "homer"]

print_values_of(['lisa', 'bart', 'homer'], simpson_catch_phrases)

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''
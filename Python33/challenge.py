#exercism challenges

#----Challenge 1----#
#Add a prefix to a word

#adding "un" to string
def add_prefix_un(word):
    print(f" Your word is: un{word}")
    
add_prefix_un("happy")
add_prefix_un("manageable")

#----Challenge 2----#
# Add a prefix to word groups

#loop through the list of words and add prefix which is the first index of list
def make_word_groups(vocab_words):
    word_list=[]
    set_prefix =  vocab_words[0]
    for i in vocab_words:
        word_list.append(f"{set_prefix}{i}")

    #remove the first index of list before joining list items to create the required string output
    word_list.remove(word_list[0])
    new_ouput = " : : ".join(word_list)
    print(f"""
          '{new_ouput}' 
          """)

make_word_groups(['en', 'close', 'joy', 'lighten'])
make_word_groups(['pre', 'serve', 'dispose', 'position'])
make_word_groups(['auto', 'didactic', 'graph', 'mate'])
make_word_groups(['inter', 'twine', 'connected', 'dependent'])


#----Challenge 3----#
# Remove a suffix from a word

#remove suffix and if the last letter is i then replace with y
def remove_suffix_ness(word):
    new_word_without_suffix = word.replace("ness", "")
    
    #if end of word is "i"
    if new_word_without_suffix[len(new_word_without_suffix)-1] == "i":
        print(new_word_without_suffix.replace("i","y"))
    else:
        print(new_word_without_suffix)
    
        
remove_suffix_ness("heaviness")
remove_suffix_ness("sadness")


#----Challenge 4----#
# Extract and transform a word

#remove the full stop at end of sentence before splitting into list and using required index
#to find word-adjective in question and print with required "en" at end to from verb
def adjective_to_verb(sentence, index):
    adjective = (sentence.strip(".").split(" "))[index]
    print(f"{adjective}en")
    

adjective_to_verb('I need to make that bright.', -1 )

adjective_to_verb('It got dark as the sun set.', 2)


# Part 1:  create a function that prints days of week
# Part 2: create a function that replaces every second word with "Hello"

def days_of_week():
    print(f"The days of the week are Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday")

days_of_week()


def replace_every_second_word():
    replaced_sent =" "
    i=0 #index to iterate through the sentence
    
    sentence = input("""

    Please type in a sentence of your choice: """)
    new_sent= sentence.split() #create an iterable list from string
   
    for word in new_sent:
        if i%2==1:  # as index starts at 0, every second word will be odd
           replaced_sent += "hello " 
        else:
            replaced_sent += word + " "
        i += 1
    print(replaced_sent) 
    
replace_every_second_word()
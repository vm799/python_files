# take in user inputs for name, age, hair colour, eye colour
# create an adult class with attributes from user inputs
# create a method can_drive() that prints name and old enough to drive

#user inputs
name = input("""
            Please type in your name:  """)
while True: 
    age = input("""
            Please type in your age:  """)
    if age.isnumeric():
        age = int(age)
        print("""
            Thank you!""")
        break
    else:
        print("""
            Oops! Is that your age? please try again!""")
        
hair_colour = input("""
            Please type in your hair colour:  """)
eye_colour = input("""
            Please type in your eye colour:  """)


class Adult:
    
    #constructor of class object Adult with 4 attributes
    def __init__(self, name, age, hair_colour, eye_colour):
        self.name = name
        self.age = age
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour
    
    # method of class object Adult   
    def can_drive(self):
        print(f"""
    _______________________________________________________________________

    Hi there {self.name}, you are old enough to drive! 
    _______________________________________________________________________
""")
        
# subclass of Adult class with same attributes
class Child(Adult):
    
    def __init__(self):
        self.name = name
    
    #subclass method to override the Adult method if user too young
    def can_drive(self):
        print(f"""
    _______________________________________________________________________
    
    Hi there {self.name}, I'm so sorry but you are NOT old enough to drive! 
    _______________________________________________________________________
""") 
    
# function to determine age of user and call relevant class or subclass therefore if can drive
def determine_object_class():
    if age >= 18:
        person = Adult(name, age, hair_colour, eye_colour)
        person.can_drive()
    
    elif age < 18:
        person = Child()
        person.can_drive()
        
determine_object_class()
        
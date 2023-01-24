# take in user inputs for name, age, hair colour, eye colour
# create an adult class with attributes from user inputs
# create a method can_drive() that prints name and old enough to drive



name = input("""
            Please type in your name:  """)
age = int(input("""
            Please type in your age:  """))
hair_colour = input("""
            Please type in your hair colour:  """)
eye_colour = input("""
            Please type in your eye colour:  """)


class Adult:
    
    def __init__(self):
        self.name = name
        self.age = age
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour
        
    def can_drive(self):
        print(f"""
    _______________________________________________________________________

    Hi there {self.name}, you are old enough to drive! 
    _______________________________________________________________________
""")
        

class Child(Adult):
    def can_drive(self):
        print(f"""
    _______________________________________________________________________
    
    Hi there {self.name}, I'm so sorry but you are NOT old enough to drive! 
    _______________________________________________________________________
""") 
    

def determine_object_class():
    if age >= 18:
        person = Adult()
        person.can_drive()
    
    elif age < 18:
        person = Child()
        person.can_drive()
      
        
determine_object_class()
        
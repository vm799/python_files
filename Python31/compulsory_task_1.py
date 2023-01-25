"""
Course management program
- Create a class object Course and subclass OOPCourse
- with added functionality to manage trainers, course content and contact details
"""
class Course:
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"
    
    #methods to print out coontact and head office details
    def contact_details(self):
        print("Please contact us by visiting: ", self.contact_website)
    
    def head_office_location(self):
        print("The head office is based in Cape Town")

#subclass of the course object
class OOPCourse(Course):
    
    #constructor for the subclass
    def __init__(self, description =  "OOP Fundamentals", trainer = "Mr Anon A. Mouse"):
        self.description  = description
        self.trainer = trainer
    
    #methods to rpint out trainer and ocurse details
    def trainer_details(self):
        print(f"The course is about {self.description} and the trainer is {self.trainer}")
        
    def show_course_id(self):
        print("The course ID is: #12345")
        
#course 1 is an object of the subclass OOPCourse
course_1 = OOPCourse()

#calling the subclass methods on the newly created object course 1
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()

#An Email Simulation program using OOP

#class definition for Email with 4 variables
from unicodedata import name


class Email:
    """ Email inbox handling with filter for spam""" 
    
    #constructor method with 4 data attributes 
    def __init__(self, email_contents, from_address, has_been_read = False, is_spam = False):
        self.email_contents = email_contents
        self.has_been_read = has_been_read
        self.is_spam = is_spam
        self.from_address = from_address
    
    #string representation of object
    def __str__(self):
        return f"""
    
        #---------------------Email-----------------------------#
        
        Email contents:  {self.email_contents}.
        Email has {"not been read" if self.has_been_read == False else "been read"}.
        This email is from {self.from_address} and {"is not spam." if self.is_spam == False else "is spam!"}
        
        """
    
    #class method getter to access 'has_been_read' attribute
    def get_has_been_read(self):
        return self.has_been_read
    
    #class method setter to access and change the value of attribute has_been_read
    def set_has_been_read(self, new_value):
        self.has_been_read = new_value
    
    def get_is_spam(self):
        return self.is_spam
        
    #method to mark email read with self passed as argument   
    def mark_as_read(self):
        self.has_been_read = True
        print(f"""      
        #--------|  This email is now marked as read  |---------#
         
        """)
        
    #method to mark email as spam with self passed as argument   
    def mark_as_spam(self):
        self.is_spam = True


#initialise a list of objects
inbox = []

#functions to manage the email inbox
def add_email():
    email_contents = input("""
    What is the email about?  """)
    from_address = input("""
    Who is the email from?  """)
    has_been_read = False
    is_spam = False
    inbox.append(Email(email_contents, from_address, has_been_read, is_spam))
    print(f"""
    Thankyou, your email from {from_address},
    about {email_contents} has been sent and stored.""")
    

def get_count():
    print(f"""
          
        You have {len(inbox)} emails in your inbox
        
        """)

def get_email():
    for index, email in enumerate(inbox, 1):
        print(f"""
        {index}: {email.email_contents}""")
        
        #error handling in case of a number out of range of the length of the list of emails
    while True:
            user_input = input("""
        Enter the number of the email you want to read e.g 1
        (Type 'quit' to go back to main menu) :__ """)
            
            if user_input != "quit" and user_input.isnumeric():
                choice = int(user_input) -1 
            
                if choice in range(0, len(inbox)):
                    email = inbox[choice]
                    print(email)
                    email.mark_as_read()
                
            
            elif user_input in "quit":
                break
            
            else:
                print("""
        Uh oh! 
        Please try again and enter a valid number from the options""")
        

#function to return a list of emails not yet read
def get_unread_emails(my_inbox):
    unread_inbox=[]
    for i in my_inbox:
        if not i.get_has_been_read():
            unread_inbox.append(i)
            print(i)
    return unread_inbox
    

#function to return spam emails 
def get_spam_emails(my_inbox):
    spam_inbox=[]
    for i in my_inbox:
        if i.get_is_spam():
            spam_inbox.append(i)
            print(f"""                  
        The email from {i.from_address} is spam

        """)
    delete()
    
    if len(spam_inbox) == 0:
        print(f"""
                  
        There are no spam emails left.
        You have a nice clean inbox!
        
        """)
        
    return spam_inbox
   

#function to delete all emails marked as spam
def delete():
    for i in inbox:
        if i.get_is_spam():
            inbox.remove(i)
            print(f"""
        This email has now been deleted
        """)




#creation of an object variable/instance
inbox.append(Email("birthday", "dav@david.com", True, False))
inbox.append(Email("invitation", "dave@david.com", True, False))
inbox.append(Email("buyapanda", "rob@robin.com", False, True))
inbox.append(Email("jobspec", "pinda@linda.com", False, False))
inbox.append(Email("buythemoon", "jim@james.com", False, True))


user_choice = ""

while user_choice != "quit":
    user_choice = input("""
        #------------------EMAIL MANAGEMENT--------------#               
        
        Welcome.
        
        What would you like to do today? 
        
        --read all
        --get unread
        --mark spam
        --send
        --get number
        --quit 
            
        (please type in the option as it is seen here e.g read all) :   """)
    
    if user_choice == "read all":  
        get_email()
    
    elif user_choice == "get number":
        get_count()
                
    elif user_choice == "mark spam":
        get_spam_emails(inbox)
        
    elif user_choice == "send":
        add_email()

    elif user_choice == "get unread":
        get_unread_emails(inbox)
    
    
    elif user_choice == "quit":
        print("""
              
        Goodbye, see you again soon!
        
        """)
    
    else:
        print("""
        Oops - that's not a valid option. 
        Please try again!
        Here is the original menu again:
        """)
        

#https://realpython.com/python3-object-oriented-programming/
#https://www.listendata.com/2019/08/python-object-oriented-programming.html
#udemy.com/course/python-the-complete-python-developer-course/learn/lecture/5117034#overview
#https://www.askpython.com/python/oops/python-class-constructor-init-function
#https://realpython.com/python-class-constructor/#:~:text=__new__()%20%2C%20you%20call,use%20the%20super()%20function.
#https://data-flair.training/blogs/python-object/
#https://stackoverflow.com/questions/17534345/typeerror-missing-1-required-positional-argument-self
#
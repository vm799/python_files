#An Email Simulation

#class definition for Email with 4 variables
from unicodedata import name


class Email:
    """ Email inbox handling with filter for spam""" 
    email_count =0

    #constructor method with 4 data attributes 
    def __init__(self, email_contents, from_address, has_been_read, is_spam):
        self.email_contents = email_contents
        self.has_been_read = False
        self.is_spam = False
        self.from_address = from_address
        self.inbox = inbox.append(self)
        
        Email.email_count +=1
        print("Email added from" + from_address)
    
    #string representation of object
    def __str__(self):
        return f'This email contains {self.email_contents}, has {"not been read" if self.has_been_read == False else "been read"} and is from {self.from_address} and {"not spam" if self.is_spam == False else "is spam!"}'
    
    #method to mark email read with self passed as argument   
    def mark_as_read(self):
        self.has_been_read = True
        print(f"This email is now marked as read!")
        
    #method to mark email as spam with self passed as argument   
    def mark_as_spam(self):
        self.is_spam = True

    #function to take in email content and sender
    def add_email(self):
        email_contents = input("What is the email about?  ")
        from_address = input("Who is the email from?  ")
        has_been_read = False
        is_spam = False
        print(f"Thankyou, your email from {from_address} about {email_contents} has been sent and stored.")
        new_email = Email(email_contents, from_address, has_been_read, is_spam)
        inbox.append(new_email.from_address)
    
    #function to return no. of emails from length of inbox 
    def get_count(self, email_count):
        print(f"You have {email_count} messages")
    
    #function to return what is in email and mark email as read
    def get_email(self):
        
        self.from_address
        print(self.from_address)
        print(self.email_contents)

    #function to return a list of emails not yet read
    def get_unread_emails(self):
        unread_emails = [i for i in inbox]
        for i in unread_emails:
            print(i.has_been_read)
            
    #function to return spam emails 
    def get_spam_emails(self):
        if self.is_spam == True:
            print(f"The emails from {self.from_address} is spam, it's about {self.email_contents}")
        else:
            print(f"This email  from {self.from_address}is not spam")


    #function to delete all emails marked as spam
    def delete(self):
        print(len(inbox))
        if self.is_spam == True:
            inbox.remove(self)
            print(f"This email has now been deleted")
        print(len(inbox))

#initialise a list of objects
inbox = []

#creation of an object variable/instance
emailOne = Email("invitation", "dave@david.com", True, False)
firstemail = Email("invitation", "dave@david.com", True, False)
secondemail = Email("buyapanda", "rob@robin.com", False, True)
thirdemail = Email("jobspec", "pinda@linda.com", False, False)
fouremail = Email("buythemoon", "jim@james.com", False, True)

print()
user_choice = ""

while user_choice != "quit":
    user_choice = input("What would you like to do - read/mark spam/send/quit?:  ")
    
    if user_choice == "read":  
        for i in inbox:
            print(i.from_address, i.has_been_read)            
            Email.mark_as_read(i)
            
    elif user_choice == "mark spam":
        for i in inbox:
            Email.mark_as_spam(i)
            Email.delete(i)
            
    
    elif user_choice == "send":
        new_email = Email("invitation", "dave@david.com", False, False)
        
        Email.add_email(new_email)
    
    elif user_choice == "quit":
        print("Goodbye")
    
    else:
        print("Oops - incorrect input")
        

#https://realpython.com/python3-object-oriented-programming/
#https://www.listendata.com/2019/08/python-object-oriented-programming.html
#udemy.com/course/python-the-complete-python-developer-course/learn/lecture/5117034#overview
#https://www.askpython.com/python/oops/python-class-constructor-init-function
#https://realpython.com/python-class-constructor/#:~:text=__new__()%20%2C%20you%20call,use%20the%20super()%20function.
#https://data-flair.training/blogs/python-object/
#https://stackoverflow.com/questions/17534345/typeerror-missing-1-required-positional-argument-self
#
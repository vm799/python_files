# use existing project capstone `nd create functions to replace menu options
# check duplicate user names cannot be entered
# on selection of 'vm' each task should have a number which can be selected
# if '-1' is selected the main menu returns
#when the task is selected, the user can EDIT or MARK COMPLETE 
#add option to generate reports 

#=====importing libraries===========

from datetime import date, datetime
from collections import defaultdict

#====Login Section====
'''write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''

def reg_user(users):
    
    print("""
        You have selected the option to register a new user.
        Please follow the instructions below:
                   """)
    
    # nested while loop to allow the registration process to loop if username already in file    
    while True:
        new_username = input("Create username:  ")  
        if new_username  in users:
            print("""
        oh no! this username already exists, please try again.
                """)
                
        if new_username not in users:
            print(f"""
        Brilliant, the username {new_username} has been created. 
        Now for your password please.
                 """)
            password = input ("Create password:  ")

            print("""
        Thank you for the password. 
        One more time please.
                 """)
            password1 = input("Confirm password:  ")

            # if passwords don't match user is sent to beginning of registration process for security
            if password != password1:      
                print("""
        Passwords don't match. Please try again.
        I'm afraid you have to start again for security. 
        
        Please enter your new username and password again.
                         """)
            
            #if both passwords match, the new username and password added to file
            if password == password1:  
                with open("Python26/user.txt", "a") as all_users_file:
                    all_users_file.write(new_username + ", " + password + "\n")
                
                print(f"""
        Success, you have registered as a new user! 
        Welcome {new_username}.
                         """)
                break

def add_task():
    print("""
        You have selected the option to add a new task.
        Please follow the instructions below:
    """)
        
    user_name = input("""
        Who is this task assigned to?    """)
    task_title = input ("""
        What is the title of the task?   """)
    task_description = input ("""
        Please describe this task:    """)
    task_due_date = input ("""
        When is this task due to be completed by? (dd/mm/yy):    """)
    task_assigned = str(date.today())  #date set to the day the task was inputted
    
    # set as default not completed, to be changed at a later date 
    task_completed = str("No") 
    print("""
              
        Thank you for all those details. 
        We will save them to the task file for your reference.
        
              """)
    # write new task to file separated by commas to make creation of list easier   
    with open("Python26/tasks.txt", "a") as task_file: 
        task_file.write(user_name + ", " + task_title + ", " + task_description + ", " + task_due_date + ", " + task_assigned + ", " + task_completed + "\n")
     
def view_all():
    with open("Python26/tasks.txt", "r") as  task_file:
        for line in task_file.readlines():  
            tasks = line.split(",") 
            print(f"""
___________________________________________________
        
Task:                 {tasks[1]}
        
Assigned to:           {tasks[0]}
Date assigned:        {tasks[4]}
Due date:             {tasks[3]}
Task Completed:       {tasks[5]}
        
Task description:     
{tasks[2]}
              

                        """)
            
def view_mine():
    with open("Python26/tasks.txt", "r") as task_file:
        data = task_file.readlines()
        
        # assign a counter/number called 'index' to each line and start at 1 not 0, split to return a list and find first item in list
        for index, line in enumerate(data, start=1):  
            split_line = line.split(", ") 
            if username == split_line[0]:
                print(f"""
                      
__________________[ Task {index} ]___________________

Task:                 {split_line[1]}        
Assigned to:          {split_line[0]}
Date assigned:        {split_line[4]}
Due date:             {split_line[3]}
Is task Completed?:   {split_line[5]}        
Task description:   
{split_line[2]}  
                            """)                      
    
    while True:
        task_choice_input = input("""
Please select a task number to amend (Type in -1 to exit to menu): """)
        task_choice = int(task_choice_input)
        user_task_choice = task_choice -1     #to align with 0 being the first item in list
        
        #leave the loop as user has typed -1 to exit
        if user_task_choice == -2:
            break 
        
        if user_task_choice == 0 or user_task_choice < len(data):       
            edit_data = data[user_task_choice]  #finding the task the user wants to amend
            list_edit_data =  edit_data.split(", ")
            if_task_completed = list_edit_data[5] #finding the last item once a list has been created
            if_task_completed_lowercase = if_task_completed.lower()
            
            #if task is already recorded as completed then it cannot be amended
            if "yes" in if_task_completed_lowercase : 
                print(f"""   
Sorry! This task has been completed and cannot be amended.
Try a different task or create another.""")    
                break
        
            else:   
                print(f"""   
Fabulous.
You now have 2 options:

1. Mark this task complete
2. Edit the task
""")
                user_choice_input = input("Please type in the number of the option you require: (1 or 2)  ")
                user_choice_1 = int(user_choice_input)
                
                if user_choice_1 == 1:
                    is_task_complete = "Yes\n"
                    split_line = edit_data.split(", ") #original line from data file is matched up with the line of data from user choice of task converted to list
                    split_line[-1] = is_task_complete #first item is selected from the line of data selected above and changed to the new name

                    amended_line = ", ".join(split_line) #the list is now joined back to a string to create the amended line of data
                    data[user_task_choice] = amended_line #the fully formed amended line is then shown to be the new line in the original data in the user's choice of task

                    print(f"""
Thank you, you have now changed Task {user_task_choice +1} to: Completed.
        """) 
                with open("Python26/tasks.txt", "w") as tasks_amend:
                    for line in data:
                        tasks_amend.writelines(line)

                if user_choice_1 == 2:
                    print(f"""

OK, great.

Now what would you like to change within the task?
Here are your options:

  1.  Change who the task is assigned to
  2.  Change when the task is due
        """)
        
                    choice = int(input("Please select the number of the option you would like to amend within the task: "))   

                    if choice ==1:
                        print(f"""
    You have chosen to change the name.
        """)
                        new_name = str(input("Please tell me who you would like to assign this task to:  "))
                        split_line = edit_data.split(", ") #original line from data file is matched up with the line of data from user choice of task converted to list
                        split_line[0] = new_name #first item is selected from the line of data selected above and changed to the new name
                        amended_line = ", ".join(split_line) #the list is now joined back to a string to create the amended line of data
                        data[user_task_choice] = amended_line #the fully formed amended line is then shown to be the new line in the original data in the user's choice of task
                        print(f"""
    Thank you, you have now changed the name assigned on Task {user_task_choice + 1} to {new_name}.
        """)
                        with open("Python26/tasks.txt", "w") as tasks_amend:
                            for line in data:
                                print(line)                    
                                tasks_amend.writelines(line)     
           
                    elif choice == 2:
                        print(f"""
    You have chosen to change when this task is due.
        """)
                        new_task_date = str(input("Please tell me when this task is now due (DD/MM/YY):  "))
                        split_line = edit_data.split(", ") 
                        split_line[3] = new_task_date 
                        amended_line = ", ".join(split_line) 
                        data[user_task_choice] = amended_line                          
                        print(f"""
    Thank you, you have now changed the due date of Task {user_task_choice + 1} to {new_task_date}.
        """)
                        with open("Python26/tasks.txt", "w") as tasks_amend:
                            for line in data:
                                tasks_amend.writelines(line) #write new data to the file
    
def gen_reports():
    
    print(f"""
    ____________________________________________________________________
    
    Thank you for choosing to generate reports on  user and task data.
    
    Two new files have now been generated:
        
        task_manager.txt for reports on all the tasks
        user_overview.txt for reports on all the users
        
    ____________________________________________________________________
          """)
    with open("Python26/user.txt", "r") as user_overview, open("Python26/tasks.txt", "r") as task_overview:
     
        tasks = task_overview.readlines()
        
        users_assigned_tasks =[] #intialising lists 
        user_task_due_date = []
        user_task_is_complete = []
        user_task_due = []
    
        for task in tasks:
            task_count = (len(tasks)) #no.of tasks
            task_list = task.split(", ")
            
            task_list_user = (task_list[0])
            task_list_due = (task_list[-3])
            due_date_format = datetime.strptime(task_list_due, "%d/%m/%y") #formatting the due date for each task with datetime module
            is_task_completed = (task_list[-1])
            today = datetime.now()  #returning the date as of today when the user is accessing program
            
            
            users_assigned_tasks.append(task_list_user) # 
            user_task_due_date.append(task_list_due)  
            user_task_is_complete.append(is_task_completed.strip("\n"))  

            # checking if the task has NOT been completed and if task is overdue by comparing two formatted dates
            #if incomplete and due date in past then keyword "overdue" added to list
            if is_task_completed == "No\n" and today.date() > due_date_format.date(): 
                user_task_due.append("Overdue") 
            
            elif is_task_completed == "No\n" and today.date() < due_date_format.date():
                user_task_due.append("Due soon")
                
            elif is_task_completed == "Yes\n":
                user_task_due.append("Completed!")
                
        # joining 2 lists together with zip function
        user_task_dictionary = zip(users_assigned_tasks ,user_task_due_date) 
        user_task_if_complete_dictionary = zip(users_assigned_tasks, user_task_due)
        
        combined_dictionary_list= list(user_task_dictionary)
        combined_task_due_dictionary = list(user_task_if_complete_dictionary)
        
        #creating a dictionary with mulitple values for each key using defaultdict module
        task_due_dates_by_user = defaultdict(list) 
        task_if_due_and_complete = defaultdict(list)
        
        #creating a dictionary with the required key and value
        for due_date, user in combined_dictionary_list:
            task_due_dates_by_user[due_date].append(user) 
               
        for is_task_complete_overdue_due_soon, user in combined_task_due_dictionary:
           task_if_due_and_complete[is_task_complete_overdue_due_soon].append(user)
     
        users = user_overview.readlines()
        
        for user in users:
            user_count =(len(users))  #no. of users
    
    task_overdue = (user_task_due.count("Overdue")) 
    percent_task_overdue = round((task_overdue / task_count) * 100)
   
    with open("task_overview.txt", "w") as task_overview: 
        
        task_overview.writelines(f"""
                
    _________________________TASK OVERVIEW _____________________________
                                 
    Number of total tasks generated: {task_count}                            
    Number of completed jobs:  {user_task_due.count("Completed!")}
    Number of incomplete jobs:  {task_count - user_task_due.count("Completed!")}    
    Number of incomplete and overdue jobs: {user_task_due.count("Overdue")}       
    Number of incomplete jobs due soon:  {user_task_due.count("Due soon")}
    
    Percentage of tasks incomplete: {round(((task_count - user_task_due.count("Completed!")) / task_count) * 100)} % 
    Percentage of tasks overdue: {percent_task_overdue} % 
    ____________________________________________________________________
          
              """)
            
    with open("user_overview.txt", "w") as user_overview:
        
        user_overview.writelines(f""" 
                               

                  _________________________USER OVERVIEW _____________________________
                                 
                  Number of total number users registered: {user_count}   
                  
                  Number of total number tasks generated: {task_count}  
        
        """) 
            
    with open("Python26/user_overview.txt", "a+") as user_overview:
        for user, due_date in task_due_dates_by_user.items():  #iterating over dictionary
            user_overview.writelines(f"""  
                  ________________________________________________________________
        
                  The registered user called: {user} has {len(due_date)} tasks assigned to them.
        
                  {user} has been assigned {round((len(due_date)/ (task_count)) * 100)}% of the total number of tasks
    
                 """)   
       
    with open("Python26/user_overview.txt", "a+") as user_overview: 
        for i in task_if_due_and_complete: #iterating over dictionary for each user (i)
            user_overview.writelines(f"""
                                         
                                         
                                         
                  _________________________________USER NAME: {i}___________________________________________________
                  
                  For user {i} there are {task_if_due_and_complete[i].count("Completed!")} task(s) COMPLETED
                  this represents {round((task_if_due_and_complete[i].count("Completed!"))/ len(task_if_due_and_complete[i])*100)} % of all the tasks assigned to this user. 
                
                  There are also {task_if_due_and_complete[i].count("Due soon")} task(s) DUE SOON
                  this represents {round(((task_if_due_and_complete[i].count("Due soon"))/ len(task_if_due_and_complete[i]))*100)} % of all the tasks assigned to this user. 
             
                  And finally {task_if_due_and_complete[i].count("Overdue")} task(s) OVERDUE
                  this represents {round(((task_if_due_and_complete[i].count("Overdue"))/ len(task_if_due_and_complete[i]))*100)} % of all the tasks assigned to this user. 
                  
                    """)
def view_stats():
    
    
    with open("Python26/tasks.txt", "r") as task_file:
        task_count = len(task_file.readlines())
            
    with open("Python26/user.txt", "r") as  user_file:
        user_count = len(user_file.readlines())
           
    print(f"""
Thank you for selecting the statistics option. 
Just compiling here for you now.
____________________________________________________

Total number of tasks: {task_count}
Total number of users: {user_count}
____________________________________________________
              
                """)
    gen_reports()
    
    #printing out stats from 2 files generated
    with open("Python26/user_overview.txt", "r") as  user_overview:
        content = user_overview.read()
        print(content)
    with open("Python26/task_overview.txt", "r") as  task_overview:
        content = task_overview.read()
        print(content)
        
        

usernames = []
passwords = []

print("""  
LOGIN HERE:  
      """)

with open("Python26/user.txt", "r")  as all_users_file:
        
    for line in all_users_file:  #read each line of file
        line_without_commas = line.replace(",", " ") #replace commas with space
        line_list = (line_without_commas.split()) #split data into a list 
        usernames.append(line_list[0]) # take the first in the list and add to list
        passwords.append(line_list[1]) #add second item in line of file to passwords list
               
while True: 
    username = input("Enter your username:  ").lower() # case insensitive
    password = input("Please type in your password:  ") #asking to input both again each time for security purposes
    
    if username not in usernames: #check for username entered in list compiled from file
        print("""
        Sorry username not found, please try again.
              """)
        
    if username in usernames:
        print("""
        Thank you, your username has been found.
        Just checking the password.
              """)
        
        if password != passwords[usernames.index(username)]:  #if password is not found at the same index position as the username in the corresponding list
            print("""
        Sorry, that password doesn't match with what we have. 
        Please try again.
              """)
             
        else:
            print("""
        That's fabulous! 
        Username and password both checked out.
        You may continue.""")
            break

while True:  #while loop to allow the loop to run and present the same menu after each option is completed

    if username == "admin":
        menu = input('''
    Select one of the following options below:

    a  - Adding a task 
    r  - Registering a user
    va - View all tasks
    vm - view my tasks
    gr - generate reports
    st - View statistics
    e  - Exit

    : ''').lower()  
    
    elif username != "admin":    # non-admin user menu without full options
        menu = input('''
    Select one of the following options below:

    a  - Adding a task
    va - View all tasks
    vm - view my task
    e  - Exit

    : ''').lower() 
    
    if menu == "r":
        reg_user(usernames)
                         
    elif menu == 'a':
        add_task()
        
    elif menu == 'va':
        view_all()
        
    elif menu == 'vm':
        view_mine()
        
    elif menu == 'gr':
        gen_reports()
        
    elif menu == 'st':
        view_stats()
              
    elif menu == 'e':
        print("""
        Thanks for dropping by.
        Goodbye for now!
              """)
        exit()

    else:
        print("""
        Oops, that is not one of the options here.
        Please Try again.
              """)     





#new research for this capstone:
#https://www.accelebrate.com/blog/using-defaultdict-python
#https://docs.python.org/3/library/collections.html#collections.defaultdict
#https://www.digitalocean.com/community/tutorials/concatenate-lists-python
#https://stackoverflow.com/questions/466345/convert-string-jun-1-2005-133pm-into-datetime
#https://stackoverflow.com/questions/46915426/how-to-check-if-a-date-is-earlier-than-todays-date  
#https://myprogrammingtutorial.com/python-count-occurrences-of-element-in-list/
#https://www.guru99.com/python-list-count.html
#https://realpython.com/python-counter/
#https://stackabuse.com/python-check-if-string-contains-substring/
#https://www.geeksforgeeks.org/how-to-convert-datetime-to-date-in-python/
#https://pynative.com/python-compare-dates/#:~:text=If%20you%20want%20to%20compare,part%20from%20the%20datetime%20object.&text=To%20compare%20only%20the%20time,part%20from%20the%20datetime%20object.    
#https://pynative.com/python-datetime-format-strftime/#:~:text=Use%20datetime.,hh%3Amm%3Ass%20format. 
#https://java2blog.com/remove-time-from-datetime-python/#:~:text=Using%20the%20datetime.-,strftime()%20function%20to%20remove%20time%20from%20datetime%20in%20Python,based%20on%20a%20datetime%20object.     
#https://stackoverflow.com/questions/60294481/checking-if-date-is-overdue-from-text-file  
#https://www.geeksforgeeks.org/how-to-open-two-files-together-in-python/  
#https://realpython.com/python-enumerate/          
#https://www.freecodecamp.org/news/python-convert-string-to-int-how-to-cast-a-string-in-python/#:~:text=To%20convert%2C%20or%20cast%2C%20a,int(%22str%22)%20.


    
         
    












      
    





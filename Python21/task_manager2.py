# alter the existing program so that only user with name "admin" is allowed to register new users
# create a new menu for the admin user
# this menu should have an extra option to display statistics
# statistics should include total number of tasks and total number of users

from datetime import date

usernames = []
passwords = []


print("""  
LOGIN HERE:  
      """)
complete = False

all_users_file = open("Python21/user.txt", "r")
        
for line in all_users_file:
            line_without_commas = line.replace(",", " ")
            line_list = (line_without_commas.split())
            usernames.append(line_list[0])
            
            passwords.append(line_list[1])
            

while not complete: 
    username = input("Enter your username:  ").lower()
  
    if username not in usernames:
        print("Sorry username not found, please try again")
        continue
    
    if username in usernames:
        print("Thank you, your username has been found")
        break
            
while not complete: 
    password = input("Please type in your password:  ")
        
    if password != passwords[usernames.index(username)]:
        print("Sorry, that doesn't match with what we have. Try again.")
             
    if password == passwords[usernames.index(username)]:
            print(f"""
                  That's fabulous {username.capitalize()}! 
                  All checked out, you may continue on your journey.""")
            
            break
    all_users_file.close()

while True:
    #presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    if username == "admin":
        menu = input('''
    Select one of the following Options below:

    a - Adding a task
    r - Registering a user
    va - View all tasks
    vm - view my task
    st - View statistics
    e - Exit

    : ''').lower()
        
    else: 
        menu = input('''
    Select one of the following Options below:

    a - Adding a task
    va - View all tasks
    vm - view my task
    e - Exit

    : ''').lower()


    if menu == "r":
        print("""
    You have selected the option to register a new user.
    Please follow the instructions below:
    """)
        username = input("Create username:  ")
        print("Thank you for the username.")
        password = input ("Create password:  ")
        print(f"Thank you {username} for the password. One more time please.")
        password1 = input("Confirm password:  ")

        if password != password1:
                print("Passwords don't match. Please try again.")
                continue
    
        elif username in usernames:
                print("username exists")
            
    
        else: 
            all_users_file = open("Python21/user.txt", "a")
            all_users_file.write(user_name + ", " + password + "\n")
            print("""
                  Success, you have registered as a new user! 
                  Welcome.
                  """)
        all_users_file.close()
    
    elif menu == 'a':
        print("""
    You have selected the option to add a new task.
    Please follow the instructions below:
    """)
        
        user_name = input("Who is this task assigned to?    ")
        task_title = input ("What is the title of the task?   ")
        task_description = input ("Please describe this task:    ")
        task_due_date = input ("When is this task due to be completed by?:    ")
        task_assigned = str(date.today())
        task_completed = str("No")
        print("""
              Thank you for all those details. 
              We will save them to the task file for your reference.
              """)
        
        task_file = open("Python21/tasks.txt", "a")
        task_file.write(user_name)
        task_file.write(user_name + ", " + task_title + task_description + ", " + task_due_date + ", " + task_assigned + ", " + task_completed + "\n")
    #task_file.close()
       
         
    elif menu == 'va':
        task_file = open("Python21/tasks.txt", "r")
        for line in task_file.readlines():
        
            tasks = line.split(",")
       
       
            print(f"""
_______________________________________
        
Task:                 {tasks[1]}
        
Assigned to:           {tasks[0]}
Date assigned:        {tasks[4]}
Due date:             {tasks[3]}
Task Completed:       {tasks[5]}
        
 Task description:     
{tasks[2]}
        
        
_______________________________________
        """)
         
            #task_file.close()
            
    

    elif menu == 'vm':
        task_file = open("Python21/tasks.txt", "r")
        for line in task_file.readlines():  
            split_line = [ele for x in line.split(",") for ele in x.split()]
           
            if username == split_line[0]:
            
                 print(f"""
____________________________________________________
        
Task:                 {split_line[1]}
        
Assigned to:           {split_line[0]}
Date assigned:        {split_line[4]}
Due date:             {split_line[3]}
Task Completed:       {split_line[5]}
        
Task description:   
{split_line[2]}
        
____________________________________________________
""")
           

            #task_file.close()
    
    elif menu == 'st':
       
        task_file = open("Python21/tasks.txt", "r")
        task_count = len(task_file.readlines())
            
       
        
        user_file = open("Python21/user.txt", "r")
        user_count = len(user_file.readlines())
           
       

        print(f"""
              Thank you for selecting the statistics option. 
              Just compiling here for you now.
____________________________________________________

Total number of tasks: {task_count}
Total number of users: {user_count}
____________________________________________________
              
              """)
        task_file.close()
        user_file.close()
        

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")     

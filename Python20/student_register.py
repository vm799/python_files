# request user for the number of students that are registering
# run the program for that number
# ask for ID number each time program runs
# add the ID data to a new file reg_form.txt

with open("reg_form.txt", "w+") as student_register:
    no_of_students = int(input("""
Please input number of students 
registering:   """))
    
    for i in range (0, no_of_students): #run the registration for the no. of students registering
        student_id = input("""
Please input id of student 
registering:   """)
        
        student_register.write(student_id + "\n")  #write the student ID to the file for future record
        print("""
Please sign on the dotted line.......................
          """)

print("""
      Thank you for registering.
      """)
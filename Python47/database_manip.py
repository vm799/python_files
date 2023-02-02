import sqlite3

db = sqlite3.connect('Python47/student_db')
cursor = db.cursor()  # Get a cursor object


cursor.execute('''
    CREATE TABLE python_programming(id INTEGER PRIMARY KEY, name VARCHAR(35),
                   	grade INTEGER)
''')

db.commit()


#add indiviudal student data to the variable rows to add in table
rows = [(55, 'Carl Davis', 61),
        (66, 'Dennis Fredrickson', 88),
        (77, 'Jane Richards', 78),
        (12, 'Peyton Sawyer', 45),
        (2, 'Lucas Brooke', 99 ) ]



# Insert rows of the students data into the table
cursor.executemany('''INSERT OR REPLACE INTO python_programming(id, name, grade)
                  VALUES(?,?,?)''', rows)
print(f' {len(rows)} users inserted')

db.commit()

# select all records with a grade between 60 and 80 inclusive and print them
cursor.execute('''SELECT * FROM python_programming WHERE grade > 59 AND grade < 81''')
student_rows = cursor.fetchall()
print(student_rows)


# Change Carl Davis's grade to 65
id = 55
cursor.execute('''UPDATE python_programming SET grade = ? WHERE id= ? ''',(65, id))

# Delete Dennis Fredrickson's row
cursor.execute('''DELETE from python_programming WHERE name = "Dennis Fredrickson" ''')

# Change the grade of all people with id BELOW 55
id = 55
cursor.execute('''UPDATE python_programming SET grade = ? WHERE id < ? ''',(100 , 55))

db.commit()

db.close()
print('Connection to database closed')


# https://stackoverflow.com/questions/11853167/parameter-unsupported-when-inserting-int
# https://sqlite.org/forum/info/3f4ec53a5c3f19f8
# https://stackoverflow.com/questions/36518628/sqlite3-integrityerror-unique-constraint-failed-when-inserting-a-value
#https://likegeeks.com/python-sqlite3-tutorial/
# https://stackoverflow.com/questions/5331894/i-cant-get-pythons-executemany-for-sqlite3-to-work-properly
# https://www.google.com/search?q=what+does+atomicity+mean+in+sql&oq=what+does+atomicity+mean+in+sql&aqs=chrome..69i57j33i160l3j33i22i29i30l2.11700j1j7&sourceid=chrome&ie=UTF-8
# https://www.sqlitetutorial.net/sqlite-update/
# https://www.google.com/search?sxsrf=AJOqlzVx3x0_4Apcy4dD-HMAgZwM8TDo-A:1675246312295&q=Python+sqlite3+update+specific+columns&sa=X&ved=2ahUKEwip9OvqivT8AhWaaMAKHfZwCy8Q1QJ6BAhEEAE&biw=666&bih=637&dpr=1
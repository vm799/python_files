# create a program to be used by a bookstore clerk
import sqlite3
from pprint import pprint

db = sqlite3.connect('Python48/books_db')
cursor = db.cursor()  # Get a cursor object

#===============DATABASE================#

cursor.execute('''
    CREATE TABLE books1(id INTEGER PRIMARY KEY, Title VARCHAR(35), Author VARCHAR(15), quantity INTEGER)
''')

db.commit()

#add indiviudal student data to the variable rows to add in table
rows = [(3001, 'A Tale of Two Cities ', 'Charles Dickens', 30),
        (3002, 'Harry Potter and the Philospher's Stone', 'J.K Rowling', 40),
        (3003, 'The Lion, The Witch and the Wardrobe', 'C.S.Lewis', 25),
        (3004, 'The Lord of the Rings', 'J.R.R. Tolkein' 37),
        (3005, 'Alice in Wonderland', 'Lewis Carroll', 12) ]

# pprint()

# Insert rows of the books data into the table
cursor.executemany('''INSERT OR REPLACE INTO python_programming(id, name, grade)
                  VALUES(?,?,?)''', rows)
print(f' {len(rows)} books added to the database')
db.commit()


#===============FUNCTIONS================#
def add_book():
    pass

def update_book():
    pass

def delete_book():
    pass

def search_book():
    pass




# menu for bookstore clerk
#while loop to allow the loop to run and present the same menu after each option is completed

while True:  

    menu = input('''
    *______________________BOOK MANAGEMENT MENU______________________________*
        
        Welcome! 
        Please select one of the following options below:
         
                1. Add new books to the database
                2. Update existing book information in the database
                3. Delete a book(s) from the database
                4. Search the database for a specific book
                5. Exit
    *__________________________________________________________*
    
    :__ ''').lower() 
        

    if menu == '1':
        add_book()
    elif menu == '2':
        update_book()
    elif menu == '3':
        delete_book()
    elif menu == '4':
        search_book()
    elif menu == '5':
        break
    else:
        print('''
    
        Please try again, that was not a valid option
        ''')
                
                
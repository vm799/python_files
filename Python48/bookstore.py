# create a program to be used by a bookstore clerk
import sqlite3

db = sqlite3.connect('Python48/books_db')
cursor = db.cursor()  # Get a cursor object

#===============DATABASE================#

cursor.execute('''
    CREATE TABLE books(id INTEGER PRIMARY KEY, Title VARCHAR(35), Author VARCHAR(15), quantity INTEGER)
''')

db.commit()

#add indiviudal student data to the variable rows to add in table
rows = [(3001, 'A Tale of Two Cities ', 'Charles Dickens', 30),
        (3002, 'Harry Potter and the Philospher\'s Stone', 'J.K Rowling', 40),
        (3003, 'The Lion, The Witch and the Wardrobe', 'C.S.Lewis', 25),
        (3004, 'The Lord of the Rings', 'J.R.R. Tolkein', 37),
        (3005, 'Alice in Wonderland', 'Lewis Carroll', 12) 
        ]



# Insert rows of the books data into the table
cursor.executemany('''INSERT OR REPLACE INTO books(id, title, author, quantity)
                  VALUES(?,?,?,?)''', rows)
print(f"""
    =================================================  
    {len(rows)} books added to the bookshelf database
    =================================================  
      """)
db.commit()

cursor.execute('''SELECT * FROM books''')
book_rows = cursor.fetchall()

for i in book_rows:
        print(f""" 
    Title: {i[1]}  
    by Author: {i[2]}  
    -------------------------------------------------""")
        
for i in book_rows:
        print(f"""
*---------New table created with following user row added:
      
{i}
      """)


#===============FUNCTIONS================#
def add_book():
    
    while True:
        id = input("""
                   
        -*-* Please type in the ID of the book you would like to add:  
        (numbers only please)__ """)
        
        if id.isnumeric():
            print(f"""
        Thank you, ID is {id}
        """)
            break
        
        else:
            print("""
        Sorry, try again! Just numbers please.
        """)
        
    while True:
        quantity = input("""
        -*-*Please type in the quantity of this book you would like to add:  
        (numbers only please)__ """)
        
        if quantity.isnumeric():
            print(f"""
        Thank you, quantity is {quantity}
        """)
            break
        
        else:
            print("""
        Sorry, try again! Just numbers please.
        """)   
    
    title = input("""
        -*-*Please type in the title of the book you would like to add:  """)
    
    author = input("""
        -*-*Please type in the author of the book you would like to add:  """)
    
    
    
    cursor.execute('''INSERT OR REPLACE INTO books(id, title, author, quantity)
                  VALUES(?,?,?,?)''', (id, title, author, quantity))
    db.commit()
    
    print(f"""
          
        #--- New book added to the database: {quantity} books of {title} by {author} ---#""")
    
    cursor.execute('''SELECT * FROM books''')
    book_rows = cursor.fetchall()

    for i in book_rows:
        print(f""" 
    Title: {i[1]}  
    by Author: {i[2]}  
    """)

    

def update_book():
    while True:
        id = input("""
        -*-*Please type in the ID of the book you would like to update:  (numbers only please)
        type exit to go back to main menu___:  """)
        
        if id.isnumeric():
            print(f"""
        Thank you, ID is {id}
        """)

        if cursor.execute('''SELECT title, author FROM books WHERE id =?''', ([id])).fetchone():                  
            print(f"""
        *---------Thank you ID found----------*
        """)
            while True:
                new_quantity = input("""
        -*-*Please type in the new quantity of this book:  (numbers only please):  """)  
        
                if new_quantity.isnumeric():
                    print(f"""
        Thank you, updated quantity is {new_quantity}
        """)
                    cursor.execute('''UPDATE books SET quantity = ? WHERE id= ? ''',(new_quantity, id))
                    db.commit()

                    cursor.execute('''SELECT * FROM books''')
                    book_rows = cursor.fetchall()

                    for i in book_rows:
                        print(f""" 
        Title: {i[1]}  
        by Author: {i[2]}  
        Stock levels: {i[3]}""")
    
        
                    break     
                        
                else:
                    print("""
        Sorry, try again! Just numbers please.
        """)
                    
        elif id in "exit":
            print("""
                  
        --Taking you back to the main menu now--
        
        """)
            break   
               
        else:
            cursor.execute('''SELECT * FROM books''')
            book_rows = cursor.fetchall()
            print(f"""                          
        *** Sorry that ID doesn't exist- please try another from these: ***
        """)
            for i in book_rows:
                print(f"""
        ID: {i[0]}  TITLE: {i[1]}
        """)
  
  
def delete_book():
    while True:
        
        id = input("""
        -*-*Please type in the ID of the book you would like to delete:  (numbers only please)
        type exit to go back to main menu___:  """)
        
        if id.isnumeric():
            print(f"""
        Thank you, ID is {id}
        """)
                
                
        if cursor.execute('''SELECT title, author FROM books WHERE id =?''', ([id])).fetchone():                  
            print(f"""
        *---------Thank you ID found----------*""")
        
            cursor.execute('''DELETE from books WHERE id = ? ''', ([id]))
            db.commit()
            
            cursor.execute('''SELECT * FROM books''')
            book_rows = cursor.fetchall()
            print(f"""
        *---Your book is now deleted
        *---Your updated bookshelf database:
           """) 
            
            for i in book_rows:
                print(f""" 
        Title: {i[1]}  
        by Author: {i[2]}  """)   
            break
        
        else:
            cursor.execute('''SELECT * FROM books''')
            book_rows = cursor.fetchall()
            print(f"""
                          
        *** Sorry that ID doesn't exist- please try another from these: ***""")
            for i in book_rows:
                print(f""" 
        ID: {i[0]}  
        TITLE: {i[1]}  """)
                
            
            

def search_book():
    while True:
        id = input("""
        -*-*Please type in the ID of the book you would like to look for:  
        (numbers only please)__ """)
        
        if id.isnumeric():
            print(f"""
        Thank you, ID is {id}""")
        
        if cursor.execute('''SELECT title, author FROM books WHERE id =?''', ([id])).fetchone():                  
            print(f"""
        *---------Thank you ID found----------*""")   
            cursor.execute('''SELECT * FROM books WHERE id =?''', ([id]))
            book_update = cursor.fetchone()
            
            print(f"""
                  
        *--*Here is your book*--*
        
        ID:               {book_update[0]}
        TITLE:            {book_update[1]}
        AUTHOR:           {book_update[2]}
        STOCK LEVELS:     {book_update[3]}
        
        """)
            db.commit()
            break
        
        else:
            cursor.execute('''SELECT * FROM books''')
            book_shelf = cursor.fetchall()
            print(f"""
                          
        *** Sorry that ID doesn't exist- please try another from these: ***

        """)
            
            for i in book_shelf:
                print(f""" 
        ID:    {i[0]}  
        Title: {i[1]}  """)
        

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
    *________________________________________________________________________*
    
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
                
                
#To build a program to take in stock data for shoes and return various dat points that can be used
#in a presentation to managers to discuss financial metrics

#========The beginning of the class==========
from encodings import utf_8_sig
import fileinput

class Shoe:
    """Stock-taking program to manage stock of various branded running shoes"""
    
    #constructor for class Shoe with attributes
    def __init__(self, country, code, product, cost, quantity):
        
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    #returns the cost of the shoes
    def get_cost(self):
        print(f"""
        The cost of this shoe is {self.cost}""")
    
    #returns the quantity of the shoes
    def get_quantity(self):
        print(f"""
        The quantity of this shoe is: {self.quantity}""")

    #special method to return a string representation of Shoe object
    def __str__(self):
        
        return(f"""
        * Product name: {self.product}
        * Manufactured in: {self.country}
        * Shoe code:  {self.code} 
        * Stock levels are: {self.quantity}
        == Each shoe costs:  £{(int(self.cost)/100)} ==
        """)

#=============Shoe list===========
shoe_list = []
#==========Functions outside the class==============

#reading stock data from file, removing top line, creating a list of string items 
# and adding it to intialised list above
#intialised global variable to make sure function doesn't run more than once 
#duplicating stock in shoe list

def read_shoes_data():
    #try-catch block for error handling if file not present
    try:
        with open("inventory.txt", "r") as inventory_file:
            
            #return a list of data from file
            stockroom_file = inventory_file.readlines()
            
            #remove top line
            altered_stockroom_file = (stockroom_file[1:len(stockroom_file)])
            for individual_shoe_list in altered_stockroom_file:
                individual_shoe_string = individual_shoe_list.split("'")
                
                #split at the comma, each individual string in the list of shoe strings
                for i in individual_shoe_string:
                    list_shoe_strings = i.split(",")

                    #create the new Shoe object  and add to the initialised shoe_list
                    shoe_list.append(Shoe(list_shoe_strings[0], list_shoe_strings[1], list_shoe_strings[2], list_shoe_strings[3], list_shoe_strings[4]))
                    print(f"""
        Shoe no. {len(shoe_list)} added and on the stock list
        
        """)
            
    #catch any errors in case file doesn't exist
    except FileNotFoundError:
        print("""
              
              
        #====================================================================#
                
                ******ERROR! Inventory File does not exist******
                
                Please add the inventory file 
                This is needed for this stock management program to run.
                
                Or call 24hr IT helpdesk: 01234 567 890 for advice.
                
        #====================================================================#
        
        """)
        
#function to allow user to add a shoe with their own spec and generate a shoe object
#and add the new shoe object to the shoe list created above
def capture_shoes():
    print("""
        #===========================================================#
        This option will allow you to add another shoe item to stock
        #===========================================================#
        """)
    new_item_country = input("""
        Please type in the country of origin of the shoe:  """)
    new_item_code = input("""
        Please type in the code of the shoe starting with SKU.
                Please type uppercase SKU 
                and then 6 numbers after (e.g SKU123456):  """)
    new_item_product = input("""
        Please type in the name of the shoe product - the name and brand (e.g Air Force 1):  """)
    
    #to catch any errors in user typing letters instead of numbers
    while True:
        new_item_cost = input("""
        Please type in the cost of the shoe in pence (e.g 2300):  """)
        if new_item_cost.isnumeric():
            print("""
        Thankyou for that!""")
            break
        elif new_item_cost.isnumeric() != True:
            print("""
        Sorry, that didn't seem like a valid numberical input, please try again""")

#to catch any errors in user typing letters instead of numbers
    while True:    
        new_item_quantity = input("""
        Please type in the quantity of the shoe stock:  """)
        if new_item_quantity.isnumeric():
            print("""
        Thankyou for that!""")
            break
        else:
            print("""
        Sorry, that didn't seem like  a valid numberical input, please try again""")
    
    #managing user inputs to create the shoe object with attributes set in the class
    shoe_list.append(Shoe(new_item_country, new_item_code, new_item_product, new_item_cost, new_item_quantity))
    print(Shoe(new_item_country, new_item_code, new_item_product, new_item_cost, new_item_quantity))

#Allow all the shoes to be printed using the str method to 
#structure the print output
def view_all():
    print("""
        #===========================================================#
        This option will allow you to view all the shoes in stock
        #===========================================================#
        """)
    
    for item in shoe_list:
        print(item)

# Find shoe of lowest stock and give option to increase stock levels
# update new quantity on the file
def re_stock():      
        print("""
        #==============================================================#
        This option will allow you to check low stock and top up numbers
        #==============================================================#
            """)
        
        quantity_data =[]
        
        # to loop through the shoes and add all the quantity data to a list, then find smallest
        # number, equate this to low_stock variable
        for shoe in shoe_list:
            quantity_data += [shoe.quantity] 
            new_list =[int(item.strip()) for item in quantity_data]
            low_stock = int(min(new_list))
        
        # match the shoe that has the same stock levels as the low_stock variable
        for shoe in shoe_list:
            if int(shoe.quantity) == low_stock:
                print(f"""
            ===============*****-LOW STOCK WARNING-****=====================
            
            Shoe product called: {shoe.product} is running on low stock volume.  
            Please restock now!
            """)
                
                restock_choice = input("""
            Do you want to add more stock to this product?  """)
                
                # while loop to catch  any errors in user input of restock amount
                if restock_choice in "yes":
                    
                    while True:
                        restock_amount = input("""
            How much stock would you like to add?:  """)
                        if restock_amount.isnumeric():
                            print("""
            Thank you for that, we will now update the stocks.""")
                            break
                        else:
                            print("""
            Oops that didn't seem like a valid numerical input, please try again""")   

                    current_stock = int(shoe.quantity)
                    new_stock = str((current_stock + int(restock_amount)))
                    print(f"""
            -******************************************************-
            
                The quantity of this shoe {shoe.product} was: {shoe.quantity} 
                Now updated by: {restock_amount} to {new_stock}
            
            -******************************************************-
            """)

                # add new stock to file with fileinput method
                    with open("inventory.txt", "r+") as inventory_file:
                        for l in fileinput.input(files = "inventory.txt"):
                            l = l.replace(shoe.quantity, (f"{new_stock}\n"))
                            inventory_file.writelines(l)
                        print("""
                              
        ****--Stock now updated to shoe inventory file--****
            """)
                        break
                    
                elif restock_choice != "yes" or restock_choice == "no":
                    print("""
            OK, no problem, you can always try again if you wish.
            Back to the Main menu here for you: """)
                    break

# enable user to search and output all data for a shoe with the shoe SKU code
def search_shoe():
    print("""
        #=============================================================#
        This option will allow you to search for a shoe by its SKU code
        #=============================================================#
        """)
    
    user_shoe_choice = input("""
        Which shoe would you like me to find for you? 
        Please type in the full shoe code including SKU in Uppercase (e.g SKU66734):  
        
        (Please note if incorrect code, you will be taken back  to main menu)
                                    
                                    :___""")
    
    for shoe in shoe_list:
        if shoe.code == user_shoe_choice:
            print(f"""
        -******************************************************-
        
        Here's your shoe!:  
        {shoe}
        
        -******************************************************-
        """) 

# Allow user to find the TOTAL value of each stock of a particular shoe
# dividing by 100 to give result in £
def value_per_item():
    print("""
        Individual shoe stock values are being calculated.""")
    
    for shoe in shoe_list:
        print(f"""
    -**************************************************-
    
    The shoe stock of : 
    {shoe.product} is valued at £{(int(shoe.quantity) * int(shoe.cost))/100}
    
    -**************************************************-
    """)

# Allow the user to search the shoe list and find shoe that has highest stock 
# and put it it on sale
def highest_qty():
    print("""
        #===============================================================#
        This option will allow you to check surplus stock and put on sale
        #===============================================================#
        """)
    
    quantity_data =[]
    
    # find the quantity attribute for each shoe, add to list and find max value
    for shoe in shoe_list:
        quantity_data += [shoe.quantity] 
        new_list =[int(item.strip()) for item in quantity_data]
        highest_stock = int(max(new_list))

    # with knowledge of max value, search for shoe with this attribute and output the shoe
    # to put on sale
    for shoe in shoe_list:    
        if int(shoe.quantity) == highest_stock:
            print(shoe)
            print(f"""
        -******************************************************-
    
        This shoe: {shoe.product} has the highest stock at {shoe.quantity}
        
                ******This shoe is now on SALE ******
    
        -******************************************************-
        """)

# #==========Main Menu=============

# start program by adding shoes to list from external txt file
read_shoes_data()

while True:
    user_choice = input(f"""
        #=================================================#
         Hello there, welcome to the SuperShoes stockroom.
        #=================================================#
        
        --Here are your options today.
        
        --Please type in the number of the option you would like: 
        
        1. Add a shoe product to stock
        
        2. View all shoes data in stock 
        
        3. Re-stock shoes on low stock
        
        4. Search for a shoe using shoe code
        
        5. Check shoe stock value 
        
        6. Put shoe on sale
                            (please type 1,2,3,4,5 or 6):__""")
    
    if user_choice in ('1','2','3','4','5','6',123456):
        
        #allow function to generate data from inventory file ready for managing through menu below
        print(f"""
        Thank you, you chose option: {user_choice}, 
        just processing stock data now...
    """)

    if user_choice == '1':
        capture_shoes()
    
    elif user_choice == '2':       
        view_all()
            
    elif user_choice == '3':       
        re_stock()

    elif user_choice == '4':
        search_shoe()
    
    elif user_choice == '5':
        value_per_item()
    
    elif user_choice == '6':
       highest_qty()
            
    else:
        print("""
              
        ################################
        
        Oh no! 
        That wasn't one of the options. 
        Please try again.
        
        
        Try 1 2,3,4,5 or 6 please.
        
        ################################
        
        """)
    
#==============RESEARCH==========#  
#https://www.udemy.com/course/python-the-complete-python-developer-course/learn/lecture/5058970#overview   
#https://data-flair.training/courses/python-course/lessons/7-4-i-inheritance-in-python-practical/
#https://www.freecodecamp.org/news/object-oriented-programming-in-python/
#https://www.w3schools.com/python/python_strings_slicing.asp
#https://stackoverflow.com/questions/23078756/python-get-the-last-element-of-each-list-in-a-list-of-lists
#https://stackoverflow.com/questions/155609/whats-the-difference-between-a-method-and-a-function
#https://www.youtube.com/watch?v=Ej_02ICOIgs
#https://www.w3schools.com/python/python_file_open.asp
#https://www.programiz.com/python-programming/file-operation
#https://docs.python.org/3/howto/unicode.html
#https://www.tutorialsteacher.com/python/slice-method#:~:text=Python%20slice()%20function,and%20__len__()%20methods.
#https://www.w3schools.com/python/trypython.asp?filename=demo_string2
#https://stackoverflow.com/questions/43301841/remove-n-from-a-list
#https://stackoverflow.com/questions/29950493/get-last-element-of-type-string-in-a-list
#https://www.geeksforgeeks.org/python-how-to-get-the-last-element-of-list/
#https://stackoverflow.com/questions/44085616/how-to-split-strings-inside-a-list-by-whitespace-characters
#https://www.geeksforgeeks.org/python-append-string-to-list/
#https://bobbyhadz.com/blog/python-remove-newline-from-list
#https://docs.python.org/2/library/functions.html#getattr
#https://stackoverflow.com/questions/39086/search-and-replace-a-line-in-a-file-in-python
#https://blog.finxter.com/how-to-search-and-replace-a-line-in-a-file-in-python/
#https://www.askpython.com/python/examples/add-a-newline-character-in-python
#https://bobbyhadz.com/blog/python-run-function-only-once
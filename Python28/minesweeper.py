# create a function that takes in a grid of #, which are mines and -, which are mine-free spots
# return a grid in which each square is replaced by a digit
# each digit represents the no. of mines adj to each spot

from operator import concat
from random import random
from time import clock_getres
from tkinter import Grid
import random

random_game_symbols=["-", "#"]
values =[]

def create_random_grid():

#defensive loop to catch any other inputs other than numbers
    while True:
        try:
            no_of_rows = int(input("How many rows would you like in your grid?  "))
            no_of_cols = int(input("How many columns would you like in your grid? "))
            
        except ValueError:
            print("""
                  Sorry that is not a valid number - try again please
                  """)
            continue
        else:
            #randomly populate a list with 2 symbols given for no of ros and cols given by user
            game_list = [random.choices(random_game_symbols, k = no_of_cols) for _ in range(no_of_rows)]
           
            #create a 2D grid from the game 
            game_grid = "\n".join([str(i) for i in game_list])
            
            print(f"""
Your randomly generated game grid:  
          
{game_grid}            
""")
            break
        
    # generated another grid replacing first str ("-") with int (0) to make it easier to increment values to each index
    new_random_game_symbols=[0, "#"]
    game_grid_nested_lists = [random.choices(new_random_game_symbols, k = no_of_cols) for _ in range(no_of_rows)]
    
    #to print a less cluttered grid for print purposes only
    game_grid = "\n".join([str(i) for i in game_list])     

    #enumerate function used to give each index a numbered row and column
    #commented out for end print out to represent task requirements
    
    # for row, list in enumerate(game_grid_nested_lists, start=1):
    #     for column, value in enumerate(list):
            
    #         print(f" Row {row} Column {column} contains {value}")
    
    #looping though all the indices      
    for row in range(no_of_rows):
        for column in range(no_of_cols):
          
            #ignoring the mines at ("#") 
            if game_grid_nested_lists[row][column] == "#":
                continue
            
            #counting mines above
            if row > 0 and game_grid_nested_lists[row-1][column] == "#":
                game_grid_nested_lists[row][column] = game_grid_nested_lists[row][column] + 1
            #counting mines below
            if row < no_of_rows-1 and game_grid_nested_lists[row+1][column] == "#":
                game_grid_nested_lists[row][column] = game_grid_nested_lists[row][column] + 1
            #counting mines left
            if column > 0 and game_grid_nested_lists[row][column-1] == "#":
                game_grid_nested_lists[row][column] = game_grid_nested_lists[row][column] + 1
            #counting mines right
            if column < no_of_cols-1 and game_grid_nested_lists[row][column+1] == "#":
                game_grid_nested_lists[row][column] = game_grid_nested_lists[row][column] + 1
            #counting mines top-right
            if row > 0 and column < no_of_cols-1 and  game_grid_nested_lists[row-1][column+1] == "#":
                game_grid_nested_lists[row][column] = game_grid_nested_lists[row][column] + 1
            #counting mines top-left
            if row > 0 and column > 0 and  game_grid_nested_lists[row-1][column-1] == "#":
                game_grid_nested_lists[row][column] = game_grid_nested_lists[row][column] + 1
            #counting mines bottom-left
            if row < no_of_rows-1 and column>0  and game_grid_nested_lists[row+1][column-1] == "#":
                game_grid_nested_lists[row][column] = game_grid_nested_lists[row][column] + 1
            #counting mines bottom-right
            if row < no_of_rows -1 and column< no_of_cols-1 and  game_grid_nested_lists[row+1][column+1] == "#":
                game_grid_nested_lists[row][column] = game_grid_nested_lists[row][column] + 1

    #replacing int with string to have an equally formatted and spaced grid
    for row, list in enumerate(game_grid_nested_lists, start=1):
        for column, value in enumerate(list):
            new_list = [[str(x) for x in list] for list in game_grid_nested_lists]
    
    #recreating grid for output display            
    new_game_grid = "\n".join([str(i) for i in new_list])
    
    print(f"""
Your new game grid with no. of adjacent mines shown:  
          
{new_game_grid}            
""")
create_random_grid()


#https://www.freecodecamp.org/news/python-find-in-list-how-to-find-the-index-of-an-item-or-element-in-a-list/
#https://www.101computing.net/number-only/
#https://snakify.org/en/lessons/two_dimensional_lists_arrays/
#https://snakify.org/en/lessons/two_dimensional_lists_arrays/
#https://www.w3resource.com/python-exercises/list/python-data-type-list-exercise-86.php
#https://stackoverflow.com/questions/44731844/how-to-create-and-display-a-3x3-grid-in-python-displaying-numbers-1-9
#https://www.w3schools.com/python/ref_random_choices.asp
#https://realpython.com/python-enumerate/
#https://www.digitalocean.com/community/tutorials/concatenate-lists-python
#https://www.tutorialspoint.com/How-to-join-list-of-lists-in-python
#https://www.askpython.com/python/examples/create-minesweeper-using-python
#https://medium.com/swlh/this-is-how-to-create-a-simple-minesweeper-game-in-python-af02077a8de#:~:text=Simple%20Steps&text=Display%20empty%20grid,Levels%20of%20difficulty
#https://stackoverflow.com/questions/1923054/convert-string-character-to-integer-in-python
#https://www.google.com/search?q=how+do+i+add+a+space+at+the+end+of+each+list+in+a+nested+list+python&oq=how+do+i+add+a+space+at+the+end+of+each+list+in+a+nested+list+python&aqs=chrome..69i57.13092j0j4&sourceid=chrome&ie=UTF-8